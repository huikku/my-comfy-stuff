# ⚠️ IMPORTANT: Current Limitation

## What These Workflows Do (v1.0)

**These workflows generate MASKS ONLY - they do NOT perform the actual video inpainting.**

### Current Status:

**✅ Working:**
- Mask generation (SAM3 detects characters, RMBG removes background)
- Feathered mask edges (smooth blending)
- Temporal smoothing support

**❌ NOT Working:**
- **Video inpainting** (filling the masked region with background)
- ProPainter node has import errors
- No alternative inpainting solution currently integrated

---

## What You Get

### SAM3 Workflow Output:
1. **Visualization video** - Shows where SAM3 detected the character
2. **Feathered mask video** - Black/white mask with soft edges

### RMBG Workflow Output:
1. **Background removed video** - Character removed, transparent/alpha background
2. **Feathered mask video** - Black/white mask with soft edges

---

## What's Missing

**To complete the clean plate, you need:**
- Video inpainting to fill the masked region with plausible background content
- This requires ProPainter or similar video inpainting model
- ProPainter is installed but has import errors (needs fixing)

---

## Current Use Cases

**What you CAN do with v1.0:**
1. Generate masks for manual inpainting in other software
2. Use RMBG output with transparent background for compositing
3. Test character detection accuracy
4. Prepare masks for external video inpainting tools

**What you CANNOT do yet:**
1. Fully automated character removal
2. Generate complete clean plates
3. Fill masked regions with background content

---

## Workarounds

### Option 1: Use External Tools
1. Generate mask with these workflows
2. Export mask and original video
3. Use external video inpainting:
   - Adobe After Effects (Content-Aware Fill)
   - DaVinci Resolve (Object Removal)
   - RunwayML (Video Inpainting)
   - Kling AI

### Option 2: Manual Compositing
1. Use RMBG workflow to remove background
2. Create or use existing background plate
3. Composite in video editor

### Option 3: Wait for v2.0
- Fix ProPainter integration
- Complete automated workflow
- Full clean plate generation

---

## Why ProPainter Doesn't Work

**Error:** `IndexError: list index out of range` in `misc.py`

**Likely causes:**
- PyTorch version incompatibility
- Missing dependencies
- Thor GPU compatibility issue

**Status:** Needs debugging and fixing

---

## Future (v2.0)

**When ProPainter is fixed, the complete workflow will be:**

```
1. Load Video
   ↓
2. Generate Mask (SAM3 or RMBG)
   ↓
3. Temporal Smoothing
   ↓
4. Feather Edges
   ↓
5. VIDEO INPAINTING (ProPainter) ← Currently broken
   ↓
6. Preserve Original Pixels
   ↓
7. Save Clean Plate
```

**Then you'll get:**
- Complete clean plate video
- Character fully removed
- Background reconstructed
- Ready to use output

---

## Summary

**v1.0 = Mask Generation Only**
- Good for: Preparing masks, testing detection, external workflows
- Not good for: Automated clean plate generation

**v2.0 = Complete Pipeline** (pending ProPainter fix)
- Will do: Full automated character removal
- Will output: Complete clean plate videos

---

**These workflows are currently a foundation for video inpainting, not a complete solution.**

For actual inpainting, you'll need to either:
1. Fix ProPainter
2. Use external tools
3. Wait for v2.0 update
