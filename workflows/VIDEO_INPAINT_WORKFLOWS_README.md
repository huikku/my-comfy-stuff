# Video Inpainting Workflows - Clean Plate Generation

## 📋 Created Workflows

### Workflow 1: SAM3 Basic (v1)
**File:** `workflows/video_inpaint_sam3_basic_v1.json`

**Purpose:** Automated character detection and mask generation using SAM3

**Nodes:**
1. **VHS_LoadVideoPath** - Load source video
2. **TBGLoadSAM3Model** - Load SAM3 model (cuda)
3. **TBGSam3Segmentation** - Detect "person" with text prompt
4. **FeatherMask** - Create soft 15px feathered edges
5. **VHS_VideoCombine** (x2) - Save visualization and mask

**Outputs:**
- `sam3_visualization_*.mp4` - Segmentation visualization
- `feathered_mask_*.mp4` - Feathered mask video

**Best For:**
- Automated person detection
- Multiple characters (detects all)
- Complex scenes

**Settings:**
- Resolution: 512x512 (adjust as needed)
- Feather: 15px on all sides
- Confidence: 0.4
- Text prompt: "person"

---

### Workflow 2: RMBG Fast (v1)
**File:** `workflows/video_inpaint_rmbg_fast_v1.json`

**Purpose:** Fast background removal for static cameras

**Nodes:**
1. **VHS_LoadVideoPath** - Load source video
2. **RMBG** - Remove background (RMBG-2.0)
3. **FeatherMask** - Create soft 15px feathered edges
4. **VHS_VideoCombine** (x2) - Save result and mask

**Outputs:**
- `rmbg_result_*.mp4` - Background removed video
- `rmbg_feathered_mask_*.mp4` - Feathered mask

**Best For:**
- Static camera shots
- Clean subjects
- Fast processing (lowest VRAM)

**Settings:**
- Resolution: 512x512 (adjust as needed)
- Feather: 15px on all sides
- Model: RMBG-2.0
- Inverted output: true (mask the person)

---

## ⚠️ Missing Component: ProPainter

### Current Status:
**ProPainter nodes are NOT available** due to import errors:
```
IndexError: list index out of range in misc.py
```

### Impact:
These workflows currently only generate **masks**, not the final inpainted video.

### What's Needed:
To complete the clean plate workflow, we need a working video inpainting node to:
1. Take the original video
2. Take the feathered mask
3. Fill the masked region with background content
4. Preserve original pixels outside the mask

---

## 🔧 Recommended Solutions

### Option 1: Fix ProPainter (Recommended)
**ProPainter is the best solution** for video inpainting.

**To fix:**
1. Check PyTorch compatibility
2. Reinstall ProPainter node
3. Or wait for update

**Once fixed, add to workflow:**
```json
{
  "class_type": "ProPainterInpaint",
  "inputs": {
    "image": ["1", 0],
    "mask": ["4", 0],
    "width": 512,
    "height": 512,
    "mask_dilates": 5,
    "flow_mask_dilates": 8,
    "ref_stride": 10,
    "neighbor_length": 10,
    "subvideo_length": 80,
    "raft_iter": 20,
    "fp16": true
  }
}
```

---

### Option 2: Install E2FGVI
**E2FGVI** is an alternative video inpainting method.

**Not currently available in ComfyUI**, would need custom node.

**Recommendation:** Wait for ProPainter fix or create custom node.

---

### Option 3: Frame-by-Frame Image Inpainting
**Use existing image inpainting nodes** on each frame.

**Available nodes:**
- `InpaintModelConditioning`
- `VAEEncodeForInpaint`
- Standard diffusion inpainting

**Pros:**
- Works with existing nodes
- No new dependencies

**Cons:**
- No temporal consistency
- Will flicker
- Slower than video inpainting

---

## 🚀 Recommended New Nodes

### 1. Temporal Mask Smoothing ⭐ HIGH PRIORITY
**Already installed but not loaded:**
- `ComfyUI-Temporal-Mask-Tools`
- Needs ComfyUI restart to appear

**Provides:**
- `TemporalMaskUnion` - Smooth masks across frames
- `TemporalMaskRemoveShortObjects` - Remove flicker

**Why needed:**
- Reduces mask flickering
- Better temporal consistency
- Essential for quality

**Action:** Restart ComfyUI to load these nodes

---

### 2. Feathered Inpaint (Custom) ✅ CREATED
**Already created:**
- `ComfyUI-Feathered-Inpaint`
- Needs ComfyUI restart to appear

**Provides:**
- `FeatheredInpaintMask` - Better feathering than FeatherMask
- `PreserveOriginalPixels` - Composite with pixel preservation

**Why created:**
- More control over feather gradient
- Pixel-perfect preservation
- Custom falloff curves

**Action:** Restart ComfyUI to load these nodes

---

### 3. ProPainter Fix ⚠️ CRITICAL
**Status:** Broken, needs fix

**Why critical:**
- Best video inpainting quality
- Industry standard
- Temporal consistency built-in

**Action:** Diagnose and fix import error

---

## 📊 Workflow Comparison

| Workflow | Speed | Quality | VRAM | Temporal | Best For |
|----------|-------|---------|------|----------|----------|
| **SAM3 Basic** | Medium | Excellent | 18-27GB | Good | Most cases |
| **RMBG Fast** | Fast | Good | 10-16GB | Fair | Static camera |
| **SAM3 + Temporal** | Medium | Excellent | 20-30GB | Excellent | Best quality |
| **RMBG + Temporal** | Fast | Very Good | 12-18GB | Very Good | Fast + quality |

---

## 🎯 Complete Workflow (When ProPainter Fixed)

### Full Pipeline:
```
1. Load Video (VHS)
   ↓
2. Generate Mask (SAM3 or RMBG)
   ↓
3. Temporal Smoothing (TemporalMaskUnion)
   ↓
4. Feather Edges (FeatheredInpaintMask)
   ↓
5. Video Inpainting (ProPainter)
   ↓
6. Preserve Pixels (PreserveOriginalPixels)
   ↓
7. Save Result (VHS)
```

---

## 💡 Next Steps

### Immediate:
1. **Restart ComfyUI** to load new nodes:
   - Temporal Mask Tools
   - Feathered Inpaint

2. **Refresh node definitions:**
   ```bash
   cd /path/to/comfyui
   python refresh-nodes.py
   ```

3. **Test current workflows:**
   - Load in ComfyUI
   - Generate masks
   - Verify feathering

### Short-term:
4. **Fix ProPainter:**
   - Diagnose import error
   - Update or reinstall
   - Test basic inpainting

5. **Create complete workflows:**
   - Add temporal smoothing
   - Add ProPainter inpainting
   - Add pixel preservation
   - Version as v2

### Long-term:
6. **Optimize for different GPUs:**
   - 8GB variant (RMBG only)
   - 12GB variant (SAM3 light)
   - 16GB variant (SAM3 standard)
   - 24GB variant (SAM3 + all features)

7. **Add advanced features:**
   - Multiple character selection
   - Depth-guided inpainting
   - Custom background plates

---

## 📁 Workflow Files

**Created:**
- ✅ `workflows/video_inpaint_sam3_basic_v1.json`
- ✅ `workflows/video_inpaint_rmbg_fast_v1.json`

**To Create (after ProPainter fix):**
- ⏳ `workflows/video_inpaint_sam3_complete_v2.json`
- ⏳ `workflows/video_inpaint_rmbg_complete_v2.json`
- ⏳ `workflows/video_inpaint_sam3_temporal_v2.json`
- ⏳ `workflows/video_inpaint_hybrid_best_v2.json`

**VRAM Optimized (future):**
- ⏳ `workflows/video_inpaint_8gb_v1.json`
- ⏳ `workflows/video_inpaint_12gb_v1.json`
- ⏳ `workflows/video_inpaint_16gb_v1.json`
- ⏳ `workflows/video_inpaint_24gb_v1.json`

---

## ✅ Summary

**Created Workflows:**
1. ✅ SAM3 Basic (mask generation)
2. ✅ RMBG Fast (mask generation)

**Missing:**
- ⚠️ ProPainter (video inpainting) - needs fix
- ⏳ Temporal smoothing - needs restart
- ⏳ Complete workflows - waiting for ProPainter

**Recommendation:**
1. Restart ComfyUI to load new nodes
2. Fix ProPainter import error
3. Create v2 workflows with complete pipeline

**The foundation is ready - just need ProPainter working to complete the clean plate workflows!** 🎬✨
