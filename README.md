# ComfyUI Video Inpainting Workflows

Clean plate generation workflows for removing foreground characters from video scenes.

## 📦 Contents

### Workflows
- `video_inpaint_sam3_basic_v1.json` - SAM3 automated character detection
- `video_inpaint_rmbg_fast_v1.json` - RMBG fast background removal

### Custom Nodes
- `ComfyUI-Feathered-Inpaint` - Feathered mask edges with pixel preservation

### Documentation
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research & state-of-the-art
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - RMBG & Depth integration options
- `VIDEO_INPAINTING_MISSING_PIECES.md` - Missing features & roadmap
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce mask flickering
- `TEMPORAL_SMOOTHING_QUICKSTART.md` - Quick start guide
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage guide
- `COMPLETE_INSTALLATION_GUIDE.md` - Full installation instructions

## 🚀 Quick Start

1. **Install Required Nodes:**
   - ComfyUI-TBG-SAM3 (for SAM3 workflow)
   - ComfyUI-RMBG (for RMBG workflow)
   - ComfyUI-VideoHelperSuite (VHS)
   - ComfyUI-Temporal-Mask-Tools
   - Copy `custom_nodes/ComfyUI-Feathered-Inpaint` to your ComfyUI

2. **Load a Workflow:**
   - Open ComfyUI
   - Load `video_inpaint_sam3_basic_v1.json` or `video_inpaint_rmbg_fast_v1.json`
   - Set video path
   - Run!

3. **Read the Docs:**
   - Start with `workflows/VIDEO_INPAINT_WORKFLOWS_README.md`
   - See `VIDEO_INPAINTING_RESEARCH_REPORT.md` for technical details

## 🎯 Workflow Overview

### SAM3 Basic (v1)
- **Purpose:** Automated person detection and mask generation
- **VRAM:** 18-27GB
- **Best for:** Complex scenes, multiple characters
- **Output:** Segmentation visualization + feathered mask

### RMBG Fast (v1)
- **Purpose:** Fast background removal
- **VRAM:** 10-16GB
- **Best for:** Static camera, clean subjects
- **Output:** Background removed video + feathered mask

## ⚠️ Current Status

**Working:**
- ✅ Mask generation (SAM3, RMBG)
- ✅ Temporal smoothing
- ✅ Feathered edges

**Pending:**
- ⚠️ ProPainter video inpainting (import error - needs fix)
- ⏳ Complete v2 workflows with full inpainting pipeline

## 📚 Documentation

See the markdown files for:
- Technical research on video inpainting
- Workflow variants and options
- Installation instructions
- Temporal smoothing techniques
- Missing features and roadmap

## 🔧 System Requirements

- ComfyUI 0.8.2+
- PyTorch 2.11.0+ (CUDA 13.0 for Thor GPU)
- 8GB+ VRAM (16GB+ recommended)

---

**Version:** 1.0  
**Date:** January 14, 2026  
**Author:** huikku
