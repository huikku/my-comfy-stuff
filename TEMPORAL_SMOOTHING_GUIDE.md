# Temporal Smoothing & Feathered Inpaint - Installation Guide

## ✅ Installed Components

### 1. Temporal Mask Tools
**Location:** `/path/to/comfyui/custom_nodes/ComfyUI-Temporal-Mask-Tools`

**Nodes Available:**
- **Temporal Mask Union** - Combines nearby frames to reduce flicker
- **Temporal Mask Remove Short Objects** - Removes one-frame glitches
- **Temporal smoothing algorithms** - For consistent masks across frames

**Usage:**
```
SAM3 Mask → Temporal Mask Union → Feathered Mask → Inpaint
```

---

### 2. Feathered Inpaint Mask (Custom)
**Location:** `/path/to/comfyui/custom_nodes/ComfyUI-Feathered-Inpaint`

**Nodes:**

#### **Feathered Inpaint Mask 🎨**
Creates a mask with soft edges for smooth blending

**Inputs:**
- `mask`: Original mask from SAM3/RMBG
- `feather_pixels`: Edge softness (0-100 pixels)
- `feather_falloff`: Gradient curve (linear/smooth/smoother)

**Outputs:**
- `feathered_mask`: Mask with soft edges for inpainting
- `inpaint_zone`: Binary mask of inpaint region
- `preserve_zone`: Binary mask of preserved pixels

**How it works:**
```
Zone 1 (Center): mask = 1.0 → Full inpaint
Zone 2 (Edge): mask = 0.0-1.0 → Feathered blend
Zone 3 (Outside): mask = 0.0 → Original pixels preserved
```

#### **Preserve Original Pixels 🔒**
Composites inpainted result with original, preserving untouched pixels

**Inputs:**
- `original_image`: Source video frame
- `inpainted_image`: ProPainter output
- `feathered_mask`: Feathered mask from above

**Output:**
- `result`: Final frame with perfect pixel preservation

**How it works:**
```
result = original * (1 - mask) + inpainted * mask

Where mask = 0: 100% original (untouched)
Where mask = 1: 100% inpainted
Where mask = 0.5: 50/50 blend
```

---

## 🎬 Complete Workflow

### Workflow: Temporal Smoothing + Feathered Inpaint

```
1. VHS Load Video
   ↓
2. SAM3 Segment (text: "person")
   ↓
3. Temporal Mask Union (smooth across frames)
   - window_size: 3-5 frames
   - mode: "majority"
   ↓
4. Feathered Inpaint Mask 🎨
   - feather_pixels: 10-20
   - feather_falloff: "smooth"
   ↓
5. ProPainter Inpaint
   - Use feathered_mask
   ↓
6. Preserve Original Pixels 🔒
   - original_image: from step 1
   - inpainted_image: from step 5
   - feathered_mask: from step 4
   ↓
7. VHS Save Video
```

---

## 🎯 Benefits

### Temporal Smoothing:
- ✅ Reduces mask flickering between frames
- ✅ Removes one-frame glitches
- ✅ Smoother mask transitions
- ✅ More consistent inpainting

### Feathered Edges:
- ✅ Soft blend at mask boundary
- ✅ No hard edges visible
- ✅ Natural-looking transitions
- ✅ Customizable falloff curves

### Pixel Preservation:
- ✅ **100% original pixels** outside feather zone
- ✅ No compression artifacts
- ✅ Perfect quality preservation
- ✅ Only inpaint what's needed

---

## 📊 Parameter Guide

### Temporal Mask Union

**window_size:**
- `1`: No smoothing
- `3`: Light smoothing (recommended start)
- `5`: Medium smoothing
- `7+`: Heavy smoothing (may blur motion)

**mode:**
- `"or"`: Include pixel if in mask in ANY frame (expands mask)
- `"majority"`: Include if in mask in MOST frames (balanced)

### Feathered Inpaint Mask

**feather_pixels:**
- `0`: No feathering (hard edge)
- `5-10`: Light feather (subtle blend)
- `10-20`: Medium feather (recommended)
- `20-50`: Heavy feather (very soft)
- `50+`: Extreme feather (large blend zone)

**feather_falloff:**
- `"linear"`: Straight gradient
- `"smooth"`: Smoothstep (recommended)
- `"smoother"`: Smootherstep (most natural)

---

## 🔧 Troubleshooting

### Mask Still Flickers
**Solution:**
- Increase temporal window_size (try 5 or 7)
- Use "majority" mode
- Add Temporal Mask Remove Short Objects

### Visible Edge Line
**Solution:**
- Increase feather_pixels (try 15-20)
- Use "smoother" falloff
- Check ProPainter mask_dilates parameter

### Inpaint Bleeding Outside Mask
**Solution:**
- Reduce feather_pixels
- Use "linear" falloff for tighter control
- Check mask dilation in ProPainter

### Original Pixels Not Preserved
**Solution:**
- Verify using Preserve Original Pixels node
- Check feathered_mask is correct
- Ensure original_image is from source, not processed

---

## 💡 Advanced Tips

### For Static Cameras:
```
Use larger feather (20-30px)
Temporal smoothing: window 5-7
Result: Very smooth, natural blend
```

### For Moving Cameras:
```
Use smaller feather (10-15px)
Temporal smoothing: window 3-5
Result: Tighter control, less blur
```

### For Fast Motion:
```
Use minimal feather (5-10px)
Temporal smoothing: window 3
Result: Preserve motion sharpness
```

### For Best Quality:
```
1. Temporal smooth the mask first
2. Apply feathering
3. Inpaint with ProPainter
4. Preserve original pixels
5. Result: Perfect blend, no artifacts
```

---

## 🎨 Workflow Variants

### Variant 1: Maximum Quality
```
SAM3 → Temporal Union (5) → Feather (20, smooth) → ProPainter → Preserve
```

### Variant 2: Fast Processing
```
RMBG → Temporal Union (3) → Feather (10, linear) → ProPainter → Preserve
```

### Variant 3: Complex Scene
```
SAM3 → Remove Short Objects → Temporal Union (7) → Feather (15, smoother) → ProPainter → Preserve
```

---

## ✅ Restart ComfyUI

**To load the new nodes:**
```bash
pkill -f "python main.py"
cd /path/to/comfyui
./start_comfyui.sh
```

**Then look for:**
- Temporal Mask Union
- Temporal Mask Remove Short Objects
- Feathered Inpaint Mask 🎨
- Preserve Original Pixels 🔒

---

## 🎯 Summary

**You now have:**
1. ✅ Temporal smoothing (reduce flicker)
2. ✅ Feathered mask edges (smooth blend)
3. ✅ Pixel preservation (untouched outside mask)

**This gives you:**
- Professional-quality inpainting
- No visible seams
- Perfect pixel preservation
- Temporal consistency

**Exactly what you asked for!** 🎬✨
