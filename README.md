# ComfyUI Video Inpainting Workflows

**Complete clean plate generation workflows for removing foreground characters from video scenes.**

## ✅ WORKING: Full Video Inpainting!

**ProPainter is now fixed and working!** These workflows generate complete clean plates, not just masks.

---

## 📦 What's Included

### Complete Workflows (v2 - WITH Inpainting)
- `video_inpaint_sam3_complete_v2.json` - SAM3 + ProPainter → **COMPLETE CLEAN PLATE**
- `video_inpaint_rmbg_complete_v2.json` - RMBG + ProPainter → **COMPLETE CLEAN PLATE**

### Mask-Only Workflows (v1 - Legacy)
- `video_inpaint_sam3_basic_v1.json` - SAM3 mask generation only
- `video_inpaint_rmbg_fast_v1.json` - RMBG mask generation only

### Custom Node
- `ComfyUI-Feathered-Inpaint` - Feathered mask edges with pixel preservation

### Documentation
- `SUMMARY.md` - Complete overview and quick start
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - Advanced options
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce flickering (detailed)
- `TEMPORAL_SMOOTHING_QUICKSTART.md` - Quick start guide
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage guide

---

## 🚀 Quick Start

**Use v2 workflows for complete clean plates!**

1. **Install required ComfyUI nodes:**
   - ComfyUI-VideoHelperSuite (VHS)
   - ComfyUI-TBG-SAM3 (for SAM3 workflow)
   - ComfyUI-RMBG (for RMBG workflow)
   - ComfyUI_ProPainter_Nodes (for inpainting)

2. **Copy custom node:**
   ```bash
   cp -r custom_nodes/ComfyUI-Feathered-Inpaint /path/to/comfyui/custom_nodes/
   ```

3. **Load a v2 workflow:**
   - Open ComfyUI
   - Load `video_inpaint_sam3_complete_v2.json` or `video_inpaint_rmbg_complete_v2.json`
   - Set video path in "VHS_LoadVideoPath" node
   - Click "Queue Prompt"

4. **Get your clean plate:**
   - Output saved to `/path/to/comfyui/output/`
   - Complete video with character removed!

---

## 🎯 Workflows

### SAM3 Complete v2 ⭐ NEW
- **Output:** Complete clean plate video (character removed, background filled)
- **VRAM:** 20-30GB
- **Best for:** Complex scenes, multiple characters, automated detection
- **Includes:** SAM3 detection + feathered mask + ProPainter inpainting

### RMBG Complete v2 ⭐ NEW
- **Output:** Complete clean plate video (character removed, background filled)
- **VRAM:** 12-18GB
- **Best for:** Static camera, clean subjects, faster processing
- **Includes:** RMBG removal + feathered mask + ProPainter inpainting

### v1 Workflows (Legacy - Mask Only)
- Use v2 instead for complete results
- v1 only generates masks without inpainting

---

## ✅ What's Fixed

**ProPainter Integration:**
- ✅ Fixed PyTorch version parsing for dev versions
- ✅ ProPainter nodes now load successfully
- ✅ Full video inpainting working
- ✅ Complete clean plate generation

**Complete Pipeline:**
```
1. Load Video
   ↓
2. Generate Mask (SAM3 or RMBG)
   ↓
3. Feather Edges
   ↓
4. VIDEO INPAINTING (ProPainter) ✅ NOW WORKING
   ↓
5. Save Clean Plate
```

---

## 📊 VRAM Requirements

| GPU VRAM | Recommended Workflow | Resolution |
|----------|---------------------|------------|
| **12GB** | RMBG Complete v2 | 512p |
| **16GB** | RMBG Complete v2 | 720p |
| **20GB** | SAM3 Complete v2 | 512p |
| **24GB+** | SAM3 Complete v2 | 720p-1080p |

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
- PyTorch 2.11.0+ (dev versions supported)
- 12GB+ VRAM (20GB+ recommended)
- Required nodes: VHS, SAM3 or RMBG, ProPainter

---

**Version:** 2.0 (Complete Video Inpainting)  
**Date:** January 14, 2026  
**Author:** huikku

**Ready to generate complete clean plates!** 🎬✨
