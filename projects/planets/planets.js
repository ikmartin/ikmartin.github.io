/* The gallery renderer. Knows nothing about Dash, so the preview page and the exported site run identical code over identical data.
 *
 * Two things are computed here rather than shipped. The synthetic drift is a closed formula over each cell's own gamut ellipsoid, so exporting statistics instead of frames is both smaller and leaves spread and contrast genuinely live. And `annual` runs one clock in Earth years against which every body plays at its own period, so nothing needs a shared frame count and the grid never repeats.
 */
(function (global) {
  "use strict";

  /* ---------------------------------------------------------------- colour */

  /* Ported from color.py. The piecewise transfer function matters: a 2.2 gamma approximation looks fine and puts the deployed site subtly off the portal. */
  var XYZ_TO_RGB = [
    [3.2404542, -1.5371385, -0.4985314],
    [-0.969266, 1.8760108, 0.041556],
    [0.0556434, -0.2040259, 1.0572252],
  ];
  var WHITE = [0.95047, 1.0, 1.08883];
  var DELTA = 6.0 / 29.0;
  var THREE_DELTA_SQ = 3.0 * DELTA * DELTA;

  function labToRgb(L, a, b, out, at) {
    var fy = (L + 16.0) / 116.0;
    var fx = fy + a / 500.0;
    var fz = fy - b / 200.0;
    var xyz = [fx, fy, fz];
    for (var i = 0; i < 3; i++) {
      var f = xyz[i];
      xyz[i] = (f > DELTA ? f * f * f : THREE_DELTA_SQ * (f - 4.0 / 29.0)) * WHITE[i];
    }
    for (var c = 0; c < 3; c++) {
      var m = XYZ_TO_RGB[c];
      var v = m[0] * xyz[0] + m[1] * xyz[1] + m[2] * xyz[2];
      v = v < 0 ? 0 : v > 1 ? 1 : v;
      v = v <= 0.0031308 ? v * 12.92 : 1.055 * Math.pow(v, 1.0 / 2.4) - 0.055;
      out[at + c] = Math.round(v * 255);
    }
  }

  /* ---------------------------------------------------------------- decode */

  function decode(entry) {
    if (!entry) return null;
    var raw = global.atob(entry.b64);
    var bytes = new Uint8Array(raw.length);
    for (var i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);
    if (entry.dtype === "f32") return new Float32Array(bytes.buffer);
    if (entry.dtype === "i16") return new Int16Array(bytes.buffer);
    if (entry.dtype === "i8") return new Int8Array(bytes.buffer);
    return bytes;
  }

  /* Two int8 axes back to the full orthonormal basis the drift needs.
     Gram-Schmidt first: quantisation leaves the pair neither quite unit length nor quite perpendicular, and re-orthonormalising throws most of that error away instead of carrying it into every frame. The third axis is then the cross product, exactly - which is why only two are shipped. */
  function unpackAxes(body) {
    var cells = body.cells, packed = body.axes;
    var axes = new Float32Array(cells * 9);
    for (var i = 0; i < cells; i++) {
      var p = i * 6, o = i * 9;
      var x0 = packed[p] / 127, y0 = packed[p + 1] / 127, z0 = packed[p + 2] / 127;
      var x1 = packed[p + 3] / 127, y1 = packed[p + 4] / 127, z1 = packed[p + 5] / 127;
      var len = Math.hypot(x0, y0, z0) || 1;
      x0 /= len; y0 /= len; z0 /= len;
      var dot = x1 * x0 + y1 * y0 + z1 * z0;
      x1 -= dot * x0; y1 -= dot * y0; z1 -= dot * z0;
      len = Math.hypot(x1, y1, z1) || 1;
      x1 /= len; y1 /= len; z1 /= len;
      axes[o] = x0; axes[o + 1] = y0; axes[o + 2] = z0;
      axes[o + 3] = x1; axes[o + 4] = y1; axes[o + 5] = z1;
      axes[o + 6] = y0 * z1 - z0 * y1;
      axes[o + 7] = z0 * x1 - x0 * z1;
      axes[o + 8] = x0 * y1 - y0 * x1;
    }
    return axes;
  }

  var ARRAYS = ["mean", "axes", "extents", "phases", "mask"];
  var SERIES_ARRAYS = ["rgb", "masks"];

  /* Every array arrives base64-encoded and has to be turned into a typed array before anything indexes it. Skipping this does not throw: `entry[0]` on the wrapper object is simply undefined, the colour maths yields NaN, a Uint8ClampedArray clamps that to 0, and the mask lookup is undefined so the alpha is 0 too. The result is a perfectly transparent canvas and no error anywhere. */
  function prepare(data) {
    if (data.__prepared) return data;
    Object.keys(data.bodies).forEach(function (key) {
      var body = data.bodies[key];
      ARRAYS.forEach(function (name) {
        if (body[name] && body[name].b64) body[name] = decode(body[name]);
      });
      if (body.axes && body.axes.length === body.cells * 6) body.axes = unpackAxes(body);
      if (body.phases && body.phases.BYTES_PER_ELEMENT === 1) {
        var turns = new Float32Array(body.cells * 3);
        for (var q = 0; q < turns.length; q++) turns[q] = body.phases[q] / 255;
        body.phases = turns;
      }
      Object.keys(body.series || {}).forEach(function (view) {
        var series = body.series[view];
        SERIES_ARRAYS.forEach(function (name) {
          if (series[name] && series[name].b64) series[name] = decode(series[name]);
        });
      });
    });
    data.__prepared = true;
    return data;
  }

  /* ------------------------------------------------------------------ drift */

  /* animate.scaled_extents: one scalar per cell over all three axes, so the ellipsoid changes size but never shape, normalised against the liveliest cell so its travel is fixed whatever the contrast. */
  function contrastFactors(extents, cells, contrast) {
    var factors = new Float32Array(cells);
    var reference = 0.0;
    var i;
    for (i = 0; i < cells; i++) {
      var e0 = extents[i * 3], e1 = extents[i * 3 + 1], e2 = extents[i * 3 + 2];
      var mag = Math.sqrt(e0 * e0 + e1 * e1 + e2 * e2);
      factors[i] = mag;
      if (mag > reference) reference = mag;
    }
    for (i = 0; i < cells; i++) {
      if (factors[i] <= 0 || reference <= 0) factors[i] = 0;
      else if (contrast === 1.0) factors[i] = 1.0;
      else factors[i] = Math.pow(factors[i] / reference, contrast - 1.0);
    }
    return factors;
  }

  var FREQ = [1, 2, 3];

  /* animate.lab_frames, per cell rather than per stack. Phases are baked at export so the browser and the portal shimmer identically. */
  function driftColours(body, t, spread, contrast, out) {
    var cells = body.cells;
    var mean = body.mean, axes = body.axes, ext = body.extents, phases = body.phases;
    var factors = contrastFactors(ext, cells, contrast);
    for (var i = 0; i < cells; i++) {
      var L = mean[i * 3], A = mean[i * 3 + 1], B = mean[i * 3 + 2];
      var f = factors[i];
      if (f > 0) {
        for (var k = 0; k < 3; k++) {
          var amp = spread * ext[i * 3 + k] * f;
          if (amp === 0) continue;
          var wave = Math.cos(2 * Math.PI * (FREQ[k] * t + phases[i * 3 + k]));
          var base = (i * 3 + k) * 3;
          L += amp * wave * axes[base];
          A += amp * wave * axes[base + 1];
          B += amp * wave * axes[base + 2];
        }
      }
      labToRgb(L, A, B, out, i * 4);
      out[i * 4 + 3] = body.mask[i] ? 255 : 0;
    }
  }

  /* ------------------------------------------------------------------ series */

  /* Sample a baked series at a fractional phase, blending the two frames either side. Masks are taken from the nearer frame rather than blended: a half-observed cell was never observed. */
  function seriesColours(series, phase, out) {
    var n = series.frames;
    var cells = series.cells;
    /* A loop closes, so its last frame is followed by its first and phase spans n intervals. A timeline is open: it spans n-1 intervals and ends ON its last frame. Spanning n and wrapping instead put a cross-dissolve from 540 Ma into the present day at the far end of every deep-time sweep. */
    var exact = phase * (series.wraps ? n : n - 1);
    var i0 = Math.floor(exact);
    var i1;
    if (series.wraps) {
      i0 = i0 % n;
      i1 = (i0 + 1) % n;
    } else {
      i0 = Math.min(i0, n - 1);
      i1 = Math.min(i0 + 1, n - 1);
    }
    /* `blend: false` where the pattern moves between observations rather than changing in place. Blending Jupiter dissolves the Great Red Spot out of one longitude and into another instead of carrying it there. */
    var w = series.blend === false ? 0 : exact - Math.floor(exact);
    var rgb = series.rgb;
    var near = w < 0.5 ? i0 : i1;
    var masks = series.masks;
    /* One mask for the whole series unless its footprint moves, in which case there is one per frame. Same lookup either way. */
    var maskAt = masks ? (near % (series.maskFrames || 1)) * cells : 0;
    for (var c = 0; c < cells; c++) {
      var a = (i0 * cells + c) * 3;
      var b = (i1 * cells + c) * 3;
      out[c * 4] = rgb[a] + (rgb[b] - rgb[a]) * w;
      out[c * 4 + 1] = rgb[a + 1] + (rgb[b + 1] - rgb[a + 1]) * w;
      out[c * 4 + 2] = rgb[a + 2] + (rgb[b + 2] - rgb[a + 2]) * w;
      out[c * 4 + 3] = masks ? (masks[maskAt + c] ? 255 : 0) : 255;
    }
  }

  function meanColours(body, out) {
    for (var i = 0; i < body.cells; i++) {
      labToRgb(body.mean[i * 3], body.mean[i * 3 + 1], body.mean[i * 3 + 2], out, i * 4);
      out[i * 4 + 3] = body.mask[i] ? 255 : 0;
    }
  }

  /* -------------------------------------------------------------------- draw */

  function paint(tile, colours, data) {
    var ctx = tile.ctx;
    var image = tile.image;
    var px = image.data;
    if (data.indexMap) {
      var map = tile.indexMap;
      for (var p = 0; p < map.length; p++) {
        var cell = map[p];
        if (cell < 0) {
          px[p * 4 + 3] = 0;
          continue;
        }
        px[p * 4] = colours[cell * 4];
        px[p * 4 + 1] = colours[cell * 4 + 1];
        px[p * 4 + 2] = colours[cell * 4 + 2];
        px[p * 4 + 3] = colours[cell * 4 + 3];
      }
    } else {
      px.set(colours);
    }
    ctx.putImageData(image, 0, 0);
  }

  /* -------------------------------------------------------------------- main */

  function renderGallery(container, data, options) {
    options = options || {};
    data = prepare(data);
    var state = {
      view: options.view || data.defaults.view,
      spread: options.spread !== undefined ? options.spread : data.defaults.spread,
      contrast: options.contrast !== undefined ? options.contrast : data.defaults.contrast,
      /* A multiplier rather than an absolute rate: the modes count in different
         units - loops per second, Earth years per second, millions of years per
         second - so one number can only scale them, not set them. */
      speedScale: options.speedScale !== undefined ? options.speedScale : 1,
      clock: 0,
      venus: 0,
    };

    container.innerHTML = "";
    container.classList.add("gallery-grid");
    var wide = data.indexMap ? data.indexMap.width : data.cols;
    var high = data.indexMap ? data.indexMap.height : data.rows;
    container.style.setProperty("--tile-aspect", wide / high);

    var indexMap = data.indexMap ? decode(data.indexMap) : null;
    var tiles = [];

    data.grid.forEach(function (row) {
      row.forEach(function (key) {
        var cellEl = document.createElement("div");
        cellEl.className = "tile";
        var canvas = document.createElement("canvas");
        canvas.width = wide;
        canvas.height = high;
        if (!data.indexMap) canvas.classList.add("pixelated");
        cellEl.appendChild(canvas);
        if (data.labels) {
          var label = document.createElement("span");
          label.className = "tile-label";
          cellEl.appendChild(label);
        }
        container.appendChild(cellEl);
        var ctx = canvas.getContext("2d");
        var tile = {
          key: key,
          el: cellEl,
          ctx: ctx,
          image: ctx.createImageData(wide, high),
          indexMap: indexMap,
          label: cellEl.querySelector(".tile-label"),
        };
        if (key === "venus") {
          cellEl.classList.add("clickable");
          cellEl.addEventListener("click", function () {
            state.venus = (state.venus + 1) % data.venus.length;
          });
        }
        tiles.push(tile);
      });
    });

    function bodyFor(tile) {
      var key = tile.key === "venus" ? data.venus[state.venus] : tile.key;
      return data.bodies[key];
    }

    var scratch = null;

    function draw() {
      var body, series;
      for (var i = 0; i < tiles.length; i++) {
        var tile = tiles[i];
        body = bodyFor(tile);
        if (!body) continue;
        if (!scratch || scratch.length !== body.cells * 4) {
          scratch = new Uint8ClampedArray(body.cells * 4);
        }
        series = body.series && body.series[state.view];

        if (state.view === "animated") {
          driftColours(body, state.clock, state.spread, state.contrast, scratch);
        } else if (series) {
          /* One clock, each body over its own span: this is where the drift comes from. Earth's year costs 1 unit of the annual clock, Mars' 1.88, Jupiter's 10.05, so they pull apart and only Earth and Mars ever re-align. */
          var turns = series.span > 0 ? state.clock / series.span : 0;
          var phase;
          if (series.wraps) {
            phase = turns - Math.floor(turns);
          } else {
            var swing = turns % 2;
            phase = swing <= 1 ? swing : 2 - swing;
          }
          seriesColours(series, phase, scratch);
        } else {
          /* No series for this mode. Freeze rather than blank: absence of data is not absence of planet. */
          meanColours(body, scratch);
        }
        paint(tile, scratch, data);
        if (tile.label) tile.label.textContent = body.label;
      }
    }

    /* One loop for the whole grid. Redraw rate and playback rate are separate: the browser offers frames at its own cadence, RENDER_FPS decides how many to use, and SPEED decides how much clock each second of wall time buys. Clamping dt keeps a backgrounded tab from lurching years forward when it returns. */
    var last = null;
    var since = 0;
    var interval = 1 / (data.renderFps || 30);
    function loop(now) {
      if (last === null) last = now;
      var dt = Math.min((now - last) / 1000, 0.25);
      last = now;
      state.clock += dt * (data.speed[state.view] || 0) * state.speedScale;
      since += dt;
      if (since >= interval) {
        since = 0;
        draw();
      }
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);

    return {
      set: function (patch) {
        Object.keys(patch).forEach(function (k) {
          if (patch[k] !== undefined && patch[k] !== null) state[k] = patch[k];
        });
        if (patch.view !== undefined) state.clock = 0;
      },
      state: state,
    };
  }

  /* `drift` and `sample` are exported so the build can check them against the Python they were ported from. Two implementations of the same maths only stay equal if something says so. */
  global.PlanetsGallery = {
    render: renderGallery,
    prepare: prepare,
    labToRgb: labToRgb,
    drift: driftColours,
    sample: seriesColours,
    decode: decode,
  };
})(window);
