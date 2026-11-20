# Strata Paint

An open-source painting and brand-mockup studio built for iPhone. It runs in Safari and can be added to your Home Screen, where it opens full screen like a normal app and works offline.

No App Store, no account, no subscription. It's one HTML file.

## What it does

**Drawing and painting**
- 48 brushes in 10 sets: Sketching, Inking, Calligraphy, Painting, Airbrushing, Spray paint, Texture, Luminance, Nature, Technical
- Paper grain textures (paper, canvas, charcoal, sponge, noise) that stay fixed to the page like real paper
- Tapered starts and ends, size/opacity jitter, scatter, colour jitter
- Wet painting brushes (Oil Blend, Round Brush, Wet Wash, Soft Blender) that pick up and mix the colours already on the layer
- Glow brushes that add light (Neon Glow, Light Pen, Sparkles, Bokeh)
- **Brush Studio**: tweak any brush's spacing, streamline, tapers, tip shape, grain, pressure, jitter, wet mix and glow, with a live preview. Duplicate brushes into "My brushes".
- **QuickShape**: draw a line, circle, ellipse, rectangle, triangle, arc or polyline and hold still at the end to snap it perfect
- Smudge and eraser, each using any brush from the library
- Pressure support for a stylus; simulated pressure from finger speed
- Symmetry (mirrors left ↔ right) and a grid guide
- Size and opacity sliders on the left edge, with a one-tap eyedropper button between them
- Drag the colour dot onto the canvas to fill an area

**Layers**
- Up to 60 layers, depending on canvas size
- Opacity, 16 blend modes, alpha lock, rename, reorder, duplicate, merge down, clear, delete
- A background colour you can hide to export a transparent PNG

**Tools**
- Paint bucket with threshold, finding edges from the current layer or from all layers
- Shapes: rectangle, rounded, ellipse, line, triangle, star, hexagon (filled or outline, 1:1 lock)
- Text with 12 fonts, weight, size, tracking, line height and alignment. It stays editable until you paint on it.
- Move & transform: drag, pinch to scale and rotate, flip, rotate 90°, fit, centre
- Eyedropper (or hold your finger still while using the brush)
- Insert photos from your library or camera

**Adjustments:** hue, saturation, brightness, contrast, blur, recolour layer, greyscale, invert, flip

**Brand kit**
- A brand palette saved with each canvas, plus recent colours and hex input
- Canvas presets: logo, square/portrait post, story, business card, 18×24 poster, banner, A4 print, or a custom size
- **Mockups:** business cards, T-shirt, tote bag, framed poster, social post on a phone, die-cut sticker. Apparel comes in several colours.
- Export PNG, transparent PNG or JPEG, then save to Photos or share

**Gestures:** pinch to zoom, two-finger tap to undo, three-finger tap to redo, hold at the end of a stroke to snap a shape, drag the colour dot to fill. History keeps 40 steps.

Canvases autosave in the browser (IndexedDB) and are listed in the gallery.

## Put it on your iPhone

1. Host the `strata/` folder anywhere that serves HTTPS. GitHub Pages is free: open the repo **Settings → Pages**, choose this branch, and save.
2. Open the page in **Safari** on your iPhone.
3. Tap **Share → Add to Home Screen**.

To try it on a computer instead, run `python3 -m http.server` inside `strata/` and open `http://localhost:8000`.

## Editing the code

All of the app is in `src/app.html`. After changing it, run:

```sh
python3 build.py
```

That rebuilds `index.html` with the Home Screen and offline settings. If you change files the offline cache stores, bump `VERSION` in `sw.js`.

## Limits

- Canvas size tops out at 4096 px per side and 12 megapixels, to stay within iPhone memory.
- No selection/lasso tool, animation or PSD export yet.
- Saved canvases live in that one browser. Export your finished work so it's safe.

## Licence

MIT. Use it, change it, share it.
