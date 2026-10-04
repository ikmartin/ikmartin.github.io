/* Hover preview for links into the corpus.
 *
 * Any link carrying data-note points at a note; the build puts that attribute on prose links, backlinks, the notes table and the index pages, and deliberately never on a link to an unpublished note -- there is nothing there to reveal.
 *
 * notes-preview.json is fetched once, on the first hover rather than at page load, so a reader who never hovers pays nothing. It is ~100 KB and covers every published note, which is what makes every subsequent preview instant.
 *
 * The card stays while the pointer is inside it, so links in the excerpt are clickable. Excerpt hrefs are stored root-relative, so they are re-prefixed with the page's own base.
 */
(function () {
  "use strict";

  var SHOW_MS = 300;   // long enough that crossing a paragraph of links does not flicker
  var HIDE_MS = 200;   // grace to travel from the link into the card

  var links = document.querySelectorAll("a[data-note]");
  if (!links.length) return;

  var base = document.body.getAttribute("data-base") || "";
  var card = null, showTimer = null, hideTimer = null, current = null, data = null;

  function load() {
    if (data) return data;
    data = fetch(base + "notes-preview.json")
      .then(function (r) { return r.ok ? r.json() : {}; })
      .catch(function () { return {}; });   // no previews rather than a broken page
    return data;
  }

  function build() {
    if (card) return card;
    card = document.createElement("div");
    card.className = "note-preview";
    card.setAttribute("role", "tooltip");
    card.hidden = true;
    card.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
    card.addEventListener("mouseleave", hideSoon);
    document.body.appendChild(card);
    return card;
  }

  function place(link) {
    var r = link.getBoundingClientRect();
    var w = card.offsetWidth, h = card.offsetHeight;
    var pad = 8;
    var left = r.left;
    var top = r.bottom + pad;
    if (left + w > window.innerWidth - pad) left = window.innerWidth - w - pad;
    if (left < pad) left = pad;
    // Flip above the link when there is no room below.
    if (top + h > window.innerHeight - pad && r.top - h - pad > pad) top = r.top - h - pad;
    card.style.left = (left + window.pageXOffset) + "px";
    card.style.top = (top + window.pageYOffset) + "px";
  }

  function show(link, note) {
    build();
    card.innerHTML =
      '<p class="note-preview-title">' + escapeHtml(note.title) +
      (note.taxon ? '<span class="note-preview-taxon">' + escapeHtml(note.taxon) + "</span>" : "") +
      '</p><div class="note-preview-body">' + rebase(note.html) + "</div>";
    card.hidden = false;
    place(link);
    typeset();
  }

  // Mirrors _unbase() in sitegen/pipelines/excerpt.py: it stores href and src bare,
  // this puts the viewing page's own base back. Both attributes, or an excerpt with an
  // inline image resolves only at the site root.
  function rebase(html) {
    return base ? html.replace(/\b(href|src)="(?!https?:|\/\/|\/|#|data:)/g, '$1="' + base) : html;
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.appendChild(document.createTextNode(s || ""));
    return d.innerHTML;
  }

  function typeset() {
    // MathJax arrives async, so it may not be here yet -- and `tags: 'ams'` keeps
    // equation numbering across calls, so reset before each card.
    if (!window.MathJax || !window.MathJax.typesetPromise) return;
    try {
      if (window.MathJax.texReset) window.MathJax.texReset();
      window.MathJax.typesetPromise([card]);
    } catch (e) {
      /* an un-typeset preview still reads as TeX; not worth breaking hover over */
    }
  }

  function hide() {
    if (card) card.hidden = true;
    current = null;
  }

  function hideSoon() {
    clearTimeout(showTimer);
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, HIDE_MS);
  }

  Array.prototype.forEach.call(links, function (link) {
    var slug = link.getAttribute("data-note");
    if (!slug) return;

    link.addEventListener("mouseenter", function () {
      clearTimeout(hideTimer);
      clearTimeout(showTimer);
      showTimer = setTimeout(function () {
        load().then(function (all) {
          var note = all[slug];
          // Also guards the case where the pointer left during the fetch.
          if (note && note.html && current === slug) show(link, note);
        });
        current = slug;
      }, SHOW_MS);
    });

    link.addEventListener("mouseleave", hideSoon);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { clearTimeout(showTimer); hide(); }
  });
  window.addEventListener("scroll", function () {
    if (current) hide();
  }, { passive: true });
})();
