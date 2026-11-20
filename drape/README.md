# Drape 3D

An open-source 3D clothing mockup app for iPhone. Put your logos on T-shirts, hoodies, caps and more, spin them around in 3D, and export product shots for your brand.

It runs in Safari and can be added to your Home Screen. No App Store, no account, no 3D model files: every garment is built in code with Three.js.

## Two ways to mock up

**3D mode:** 16 garments built in code that you can spin, zoom and light.

**Photo mode:** load any photo of a blank garment, such as a flat lay, a ghost-mannequin render or a model wearing it, and place your logo on it. The logo bends into the folds (a displacement map from the photo), takes on the fabric's shading and texture, and can be perspective-warped by dragging its corners. Move with one finger, and pinch to resize and rotate.

## 3D garments

**Tops:** T-shirt, oversized tee, long sleeve (dropped shoulder), tank top, sweatshirt, hoodie, boxy cropped hoodie, zip-up hoodie (zipper, split pockets)
**Bottoms:** sweatpants, joggers (cuffed), shorts, all with waistband, drawcord, pocket openings and side seams
**Accessories:** cap (6 panels), trucker hat (mesh back), bucket hat, beanie (optional pom-pom), socks (pair), tote bag

Details include twin-needle stitching at hems, cuffs and collars, rib bands, hood edges and eyelets.

## Logos

- Add any image from Photos. A transparent PNG works best, such as one exported from Strata Paint.
- Or make a **text logo** with 10 fonts, weights, letter spacing and colour.
- Place it with one tap: centre chest, left chest, full back, back neck, sleeves, hood, pocket, cap front/sides/back, beanie cuff, tote front/back.
- Or **drag the logo** across the fabric, or use **Tap to place**.
- Size, rotate, opacity, and show/hide.
- **Finish:** screen print (fabric texture shows through), embroidery (stitched, raised sheen), vinyl (glossy), or puff print.
- **One-colour ink:** turn any logo into a single colour, such as white on a black hoodie.
- Several logos per garment. Logos follow you when you switch garments.

## Studio

- 14 garment colours plus any custom colour
- Fabric: standard, heather, brushed fleece, smooth
- Backgrounds and lighting presets (Studio, Soft, Dramatic, Golden)
- Front, ¾, side and back views, plus a turntable spin
- Pinch to zoom, drag to turn

## Export

3D: this view, front + back side by side, or a 4-angle sheet, with a background or a transparent one. Photo: the finished photo at full resolution. On iPhone, press and hold the image to save it to Photos, or tap Share.

## Put it on your iPhone

1. Host the `drape/` folder anywhere with HTTPS. GitHub Pages works: repo **Settings → Pages**.
2. Open it in **Safari**.
3. Tap **Share → Add to Home Screen**.

## Editing

The app is all in `src/app.html`. Run `python3 build.py` to rebuild `index.html`. Three.js 0.160.0 loads from jsDelivr, and the service worker caches it for offline use after the first visit.

## Licence

MIT
