/* "Visited": a PATH through the corpus, plus a cursor marking where you are on it.
 *
 * Not a log of every note seen -- a path, which is why moving along it never reorders it. Two cases on each note page load and nothing else: a note already on the path just moves the cursor, and a note that is not truncates everything ahead of the cursor and appends. So a back-link click, a Visited-list click, the browser back button, a prose link and a reload are all the same operation, and repeatedly clicking back walks C -> B -> A instead of oscillating between two notes.
 *
 * sessionStorage, so it is per-tab and clears when the tab closes -- no server, no cookie, nothing to consent to. Only zettelkasten notes are recorded: the template leaves data-note-url empty on every other kind of page, which is what keeps academic and project pages out of it.
 *
 * The rail renders the path REVERSED, newest at the top, so array index and screen row run in opposite directions. Everything here indexes the array; only the render loop thinks in rows.
 */
(function () {
  "use strict";

  var KEY = "visited.v2";   // v1 was a bare array with no cursor, and would be misread
  var body = document.body;
  var block = document.getElementById("visited");
  var list = document.getElementById("visited-list");

  var base = body.getAttribute("data-base") || "";
  var url = body.getAttribute("data-note-url") || "";
  var title = body.getAttribute("data-note-title") || "";

  /* The state transition, kept pure and total so it can be exercised outside a browser.
   *
   * `items.length = i + 1` is the truncation, and it does the right thing at i === -1 (empty path) without a special case. The path can never hold a duplicate: the retained prefix had none and the appended note was not in it.
   */
  function advance(items, i, url, title) {
    for (var k = 0; k < items.length; k++) {
      if (items[k].u === url) return { items: items, i: k };  // already on the path
    }
    items.length = i + 1;                                     // drop everything ahead
    items.push({ u: url, t: title });
    return { items: items, i: items.length - 1 };
  }

  /* A cursor outside the array would point the back link at nothing, so it is clamped rather than trusted. Anything else malformed degrades to an empty path. */
  function load() {
    try {
      var raw = JSON.parse(sessionStorage.getItem(KEY) || "null");
      if (!raw || !Array.isArray(raw.items)) return { items: [], i: -1 };
      var items = raw.items.filter(function (it) { return it && typeof it.u === "string"; });
      var i = Math.floor(raw.i);
      if (!isFinite(i) || i < -1) i = -1;
      if (i > items.length - 1) i = items.length - 1;
      return { items: items, i: i };
    } catch (e) {
      return { items: [], i: -1 };  // private mode, quota, or a corrupt value
    }
  }

  /* The link above the page title, pointing one step back along the path.
   *
   * data-note is what gives it its hover preview and its green colour, both for free: preview.js binds every a[data-note] at load and runs after this script. It keys on slug, so recover it from the URL -- notes are the only thing recorded here and their URL is always notes/<slug>/. No match means no preview, not a broken link.
   */
  function fillBackLink(prev) {
    var back = document.getElementById("back-link");
    if (!back || !prev) return;
    var slug = /^notes\/(.+)\/$/.exec(prev.u);
    back.href = base + prev.u;
    if (slug) back.setAttribute("data-note", slug[1]);
    // aria-label, not title: a native tooltip would race the hover card.
    back.setAttribute("aria-label", "Back to " + (prev.t || "the last note"));
    back.hidden = false;
  }

  var state = load();

  if (url) {
    state = advance(state.items, state.i, url, title);
    try {
      sessionStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {
      /* storage unavailable: the path is still rendered for this page */
    }
    fillBackLink(state.items[state.i - 1]);
  }

  if (!block || !list || !state.items.length) return; // block stays hidden

  // Reversed: newest at the top, so screen row 0 is the LAST array element.
  var frag = document.createDocumentFragment();
  var cursorRow = null;
  for (var k = state.items.length - 1; k >= 0; k--) {
    var item = state.items[k];
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = base + item.u;
    a.textContent = item.t || item.u;
    if (k === state.i) {
      li.className = "current";
      cursorRow = li;
      // The cursor is where back resumes from, worth marking even on a page that
      // is not a note -- but only an actual note page IS the page.
      if (item.u === url) a.setAttribute("aria-current", "page");
    }
    li.appendChild(a);
    frag.appendChild(li);
  }
  list.appendChild(frag);
  block.hidden = false;

  /* Centre the cursor in the ~10-row window. It used to be pinned at row 0 and so always visible; now it can sit anywhere, including well outside the window.
   *
   * Measured with rects rather than offsetTop: .visited-list is not positioned, so its offsetParent is the sticky .rail and offsetTop would be against the wrong box. Must run AFTER the block is unhidden -- a hidden element has no layout and every rect reads zero.
   */
  if (cursorRow && list.scrollHeight > list.clientHeight) {
    list.scrollTop += cursorRow.getBoundingClientRect().top
                    - list.getBoundingClientRect().top
                    - (list.clientHeight - cursorRow.offsetHeight) / 2;
  }
})();
