# ComfyUI Video Workflows

Complete workflows for video inpainting and human motion capture.

## 📦 What's Included

### Video Inpainting Workflows ✅
Clean plate generation for removing foreground characters.

**Complete Workflows (v2 - WITH Inpainting):**
- `video_inpaint_sam3_complete_v2.json` - SAM3 + ProPainter
- `video_inpaint_rmbg_complete_v2.json` - RMBG + ProPainter

### SMPL-X Motion Capture Workflow ⭐ NEW
Human motion tracking for match move and animation.

**Workflow:**
- `smplx_motion_capture_v1.json` - WHAM + SMPL-X parameter export

### Custom Nodes
- `ComfyUI-Feathered-Inpaint` - Feathered mask edges
- `ComfyUI-SMPLX-Export` - SMPL-X parameter and mesh export

### Documentation
- `README.md` - This file
- `SMPLX_MOTION_CAPTURE_GUIDE.md` - Motion capture guide
- `SUMMARY.md` - Video inpainting overview
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - Advanced options
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce flickering
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage

---

## 🎬 Video Inpainting

**Purpose:** Remove characters from video, generate clean plates

**Quick Start:**
1. Install: VHS, SAM3/RMBG, ProPainter
2. Load v2 workflow
3. Set video path
4. Get complete clean plate!

**See:** `SUMMARY.md` for details

---

## 🎯 SMPL-X Motion Capture

**Purpose:** Track human motion for match move, animation reference

**Quick Start:**
1. Install: VHS, WHAM, smplx library
2. Load `smplx_motion_capture_v1.json`
3. Set video path
4. Get SMPL-X parameters + visualization!

**Outputs:**
- SMPL-X parameters (.npz, .json, .pkl)
- Visualization video
- Compatible with Blender, Maya, Houdini

**See:** `SMPLX_MOTION_CAPTURE_GUIDE.md` for details

---

## 🚀 Installation

### Video Inpainting
```bash
# Required nodes (install via ComfyUI Manager):
- ComfyUI-VideoHelperSuite (VHS)
- ComfyUI-TBG-SAM3 or ComfyUI-RMBG
- ComfyUI_ProPainter_Nodes

# Copy custom node:
cp -r custom_nodes/ComfyUI-Feathered-Inpaint /path/to/comfyui/custom_nodes/
```

### SMPL-X Motion Capture
```bash
# Required nodes:
- ComfyUI-VideoHelperSuite (VHS)
- ComfyUI-WHAM

# Install SMPL-X library:
pip install smplx

# Copy custom node:
cp -r custom_nodes/ComfyUI-SMPLX-Export /path/to/comfyui/custom_nodes/

# Download SMPL-X models:
# https://smpl-x.is.tue.mpg.de/
# Extract to: models/smplx/
```

---

## 📊 Workflows Summary

| Workflow | Purpose | Output | VRAM |
|----------|---------|--------|------|
| **SAM3 Complete v2** | Clean plates | Video (character removed) | 20-30GB |
| **RMBG Complete v2** | Clean plates (fast) | Video (character removed) | 12-18GB |
| **SMPL-X Capture v1** | Motion tracking | SMPL-X params + viz | 4-8GB |

---

## 🔧 Requirements

- ComfyUI 0.8.2+
- PyTorch 2.11.0+
- 8GB+ VRAM (12GB+ recommended)
- FFmpeg (for video processing)

---

**Version:** 2.0 (Video Inpainting) + 1.0 (Motion Capture)  
**Date:** January 14, 2026  
**Author:** huikku

**Ready for video inpainting and motion capture!** 🎬✨
