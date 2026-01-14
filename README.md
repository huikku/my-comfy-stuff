# ComfyUI Video Inpainting Workflows

Clean plate generation workflows for removing foreground characters from video scenes.

## ⚠️ IMPORTANT: Read This First

**These workflows generate MASKS ONLY - they do NOT perform actual video inpainting.**

See `CURRENT_LIMITATION.md` for details.

**What you get:** Character detection masks with soft edges  
**What you DON'T get:** Complete clean plate videos (requires ProPainter fix)

---

## 📦 What's Included

### Workflows (2)
- `video_inpaint_sam3_basic_v1.json` - SAM3 automated character detection → **MASK OUTPUT**
- `video_inpaint_rmbg_fast_v1.json` - RMBG fast background removal → **MASK OUTPUT**

### Custom Node (1)
- `ComfyUI-Feathered-Inpaint` - Feathered mask edges with pixel preservation

### Documentation (7)
- `CURRENT_LIMITATION.md` - **READ THIS!** Explains what's missing
- `SUMMARY.md` - Complete overview and quick start
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research & state-of-the-art
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - Advanced workflow options
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce mask flickering (detailed)
- `TEMPORAL_SMOOTHING_QUICKSTART.md` - Quick start guide
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage guide

---

## 🚀 Quick Start

**Read:** `CURRENT_LIMITATION.md` first to understand what these workflows do

**TL;DR:**
1. Install required ComfyUI nodes (SAM3 or RMBG, VHS)
2. Copy `custom_nodes/ComfyUI-Feathered-Inpaint` to your ComfyUI
3. Load a workflow in ComfyUI
4. Set video path
5. Run!
6. **Get masks** (not complete clean plates)

---

## 🎯 Workflows

### SAM3 Basic v1
- **Output:** Character detection mask + visualization
- **VRAM:** 18-27GB
- **Best for:** Complex scenes, multiple characters
- **Does NOT:** Fill masked region with background

### RMBG Fast v1
- **Output:** Background removed video + mask
- **VRAM:** 10-16GB
- **Best for:** Static camera, clean subjects
- **Does NOT:** Reconstruct background content

---

## ✅ Current Status (v1.0)

**What Works:**
- ✅ Character detection (SAM3)
- ✅ Background removal (RMBG)
- ✅ Mask generation with feathered edges
- ✅ Temporal smoothing support

**What's Missing:**
- ❌ **Video inpainting** (ProPainter broken)
- ❌ Background reconstruction
- ❌ Complete clean plate generation
- ❌ Automated character removal

**Use Cases:**
- Generate masks for external tools
- Test character detection
- Prepare for manual inpainting
- Background removal for compositing

---

## 🔮 Future (v2.0)

**When ProPainter is fixed:**
- ✅ Complete video inpainting
- ✅ Automated clean plate generation
- ✅ Background reconstruction
- ✅ Full pipeline workflows

**Until then:**
- Use external tools for actual inpainting
- Or manually composite results
- Or wait for ProPainter fix

---

## 📚 Documentation

**Start here:** 
1. `CURRENT_LIMITATION.md` - Understand what's missing
2. `SUMMARY.md` - Complete overview

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
- **NOT required:** ProPainter (broken anyway)

---

**Version:** 1.0 (Mask Generation Only)  
**Date:** January 14, 2026  
**Author:** huikku

**Ready to generate masks - actual inpainting requires external tools or v2.0!** 🎬
