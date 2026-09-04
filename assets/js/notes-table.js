/* Sort the notes table by clicking a column header.
 *
 * The table is rendered newest-first, so it is already useful with JavaScript off; this only re-orders what is there. Tags has no button -- a list of tags has no order to sort by.
 *
 * Sort keys come from each cell's data-sort attribute rather than its text, so "Abelian Cone" sorts case-insensitively and a date sorts as YYYY-MM-DD rather than as whatever it happens to display.
 */
(function () {
  "use strict";

  var table = document.getElementById("notes-table");
  if (!table || !table.tBodies.length) return;

  var tbody = table.tBodies[0];
  var headers = Array.prototype.slice.call(table.querySelectorAll("thead th"));

  function key(row, i) {
    var cell = row.cells[i];
    return (cell && cell.getAttribute("data-sort")) || "";
  }

  function sortBy(index, ascending) {
    var rows = Array.prototype.slice.call(tbody.rows);
    rows.sort(function (a, b) {
      var x = key(a, index), y = key(b, index);
      // Blanks sort last in both directions: an undated note is not "earliest".
      if (x === y) return 0;
      if (x === "") return 1;
      if (y === "") return -1;
      return ascending ? (x < y ? -1 : 1) : (x < y ? 1 : -1);
    });
    var frag = document.createDocumentFragment();
    rows.forEach(function (r) { frag.appendChild(r); });
    tbody.appendChild(frag);
  }

  headers.forEach(function (th, index) {
    var button = th.querySelector("button");
    if (!button) return;
    button.addEventListener("click", function () {
      var ascending = th.getAttribute("aria-sort") !== "ascending";
      headers.forEach(function (other) {
        if (other.hasAttribute("aria-sort")) other.setAttribute("aria-sort", "none");
      });
      th.setAttribute("aria-sort", ascending ? "ascending" : "descending");
      sortBy(index, ascending);
    });
  });
})();
