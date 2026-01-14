# ComfyUI Video Inpainting Workflows

Clean plate generation workflows for removing foreground characters from video scenes.

## 📦 What's Included

### Workflows (2)
- `video_inpaint_sam3_basic_v1.json` - SAM3 automated character detection
- `video_inpaint_rmbg_fast_v1.json` - RMBG fast background removal

### Custom Node (1)
- `ComfyUI-Feathered-Inpaint` - Feathered mask edges with pixel preservation

### Documentation (6)
- `SUMMARY.md` - **Start here!** Complete overview and quick start
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research & state-of-the-art
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - Advanced workflow options
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce mask flickering (detailed)
- `TEMPORAL_SMOOTHING_QUICKSTART.md` - Quick start guide
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage guide

---

## 🚀 Quick Start

**Read:** `SUMMARY.md` for complete overview

**TL;DR:**
1. Install required ComfyUI nodes (SAM3 or RMBG, VHS)
2. Copy `custom_nodes/ComfyUI-Feathered-Inpaint` to your ComfyUI
3. Load a workflow in ComfyUI
4. Set video path
5. Run!

---

## 🎯 Workflows

### SAM3 Basic v1
- **Purpose:** Automated person detection
- **VRAM:** 18-27GB
- **Best for:** Complex scenes, multiple characters

### RMBG Fast v1
- **Purpose:** Fast background removal
- **VRAM:** 10-16GB
- **Best for:** Static camera, clean subjects

---

## ⚠️ Current Status

**v1.0 - Mask Generation:**
- ✅ SAM3 and RMBG mask generation
- ✅ Feathered edges
- ✅ Temporal smoothing support

**Future v2.0 - Complete Inpainting:**
- ⏳ ProPainter integration (pending fix)
- ⏳ Full clean plate generation
- ⏳ Pixel preservation compositing

---

## 📚 Documentation

**Start here:** `SUMMARY.md`

**For details:**
- Technical research → `VIDEO_INPAINTING_RESEARCH_REPORT.md`
- Advanced options → `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md`
- Reduce flickering → `TEMPORAL_SMOOTHING_QUICKSTART.md`
- Workflow guide → `workflows/VIDEO_INPAINT_WORKFLOWS_README.md`

---

## 🔧 Requirements

- ComfyUI 0.8.2+
- PyTorch 2.11.0+
- 8GB+ VRAM (16GB+ recommended)
- Required nodes: VHS, SAM3 or RMBG

---

**Version:** 1.0  
**Date:** January 14, 2026  
**Author:** huikku

**Ready to generate clean plate masks!** 🎬✨
