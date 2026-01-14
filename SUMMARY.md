# ComfyUI Video Inpainting Workflows - Summary

## 🎯 Overview

Complete workflows for removing foreground characters from video scenes (creating "clean plates") using ComfyUI.

---

## 📦 What's Included

### Workflows (2)
- **SAM3 Basic v1** - Automated character detection using text prompts
- **RMBG Fast v1** - Fast background removal for static cameras

### Custom Node (1)
- **Feathered Inpaint** - Creates soft mask edges with pixel preservation

### Documentation (5)
- Technical research on state-of-the-art video inpainting
- Workflow variants with RMBG and Depth integration
- Temporal smoothing techniques to reduce flickering
- Complete installation and usage guides

---

## 🚀 Quick Start

### 1. Install Dependencies

**Required ComfyUI Nodes:**
```bash
# Core nodes
- ComfyUI-VideoHelperSuite (VHS)
- ComfyUI-TBG-SAM3 (for SAM3 workflow)
- ComfyUI-RMBG (for RMBG workflow)

# Optional (for advanced features)
- ComfyUI-Temporal-Mask-Tools
- ComfyUI-DepthAnythingV2/V3
```

**Install Feathered Inpaint:**
```bash
cp -r custom_nodes/ComfyUI-Feathered-Inpaint /path/to/comfyui/custom_nodes/
```

### 2. Load a Workflow

1. Open ComfyUI
2. Click "Load"
3. Select `video_inpaint_sam3_basic_v1.json` or `video_inpaint_rmbg_fast_v1.json`
4. Set video path in "VHS_LoadVideoPath" node
5. Click "Queue Prompt"

### 3. Check Output

Results saved to: `/path/to/comfyui/output/`

---

## 🎬 Workflow Details

### SAM3 Basic v1

**What it does:**
- Loads video
- Detects "person" using SAM3 text prompt
- Creates feathered mask (15px soft edges)
- Saves visualization and mask

**Best for:**
- Automated detection
- Multiple characters
- Complex scenes

**VRAM:** 18-27GB  
**Speed:** ~1-2 fps

**Outputs:**
- `sam3_visualization_*.mp4` - Shows detected masks
- `feathered_mask_*.mp4` - Mask with soft edges

---

### RMBG Fast v1

**What it does:**
- Loads video
- Removes background using RMBG
- Creates feathered mask (15px soft edges)
- Saves result and mask

**Best for:**
- Static camera shots
- Clean subjects
- Fast processing

**VRAM:** 10-16GB  
**Speed:** ~5-10 fps

**Outputs:**
- `rmbg_result_*.mp4` - Background removed
- `rmbg_feathered_mask_*.mp4` - Mask with soft edges

---

## ⚙️ Customization

### Adjust Resolution

In "VHS_LoadVideoPath" node:
```json
"custom_width": 512,   // or 720, 1080
"custom_height": 512   // or 720, 1080
```

### Change Detection Prompt (SAM3)

In "TBGSam3Segmentation" node:
```json
"text_prompt": "person"  // or "character", "man", "woman", etc.
```

### Adjust Feathering

In "FeatherMask" node:
```json
"left": 15,    // pixels to feather
"top": 15,
"right": 15,
"bottom": 15
```

---

## 🔧 VRAM Requirements

| GPU VRAM | Recommended Workflow | Max Resolution |
|----------|---------------------|----------------|
| **8GB** | RMBG Fast | 720p |
| **12GB** | RMBG Fast or SAM3 | 720p |
| **16GB** | SAM3 Basic | 1080p |
| **24GB+** | SAM3 Basic | 1080p-4K |

---

## 📚 Documentation

### Technical Details
- **VIDEO_INPAINTING_RESEARCH_REPORT.md** - State-of-the-art research, technical comparison
- **VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md** - Advanced options with RMBG and Depth

### Guides
- **TEMPORAL_SMOOTHING_GUIDE.md** - Reduce mask flickering (detailed)
- **TEMPORAL_SMOOTHING_QUICKSTART.md** - Quick start guide
- **workflows/VIDEO_INPAINT_WORKFLOWS_README.md** - Complete workflow guide

---

## ✅ Current Status

**Working:**
- ✅ Mask generation (SAM3, RMBG)
- ✅ Feathered edges
- ✅ Temporal smoothing nodes available

**Known Limitations:**
- ⚠️ These workflows generate **masks only**
- ⚠️ ProPainter (video inpainting) has import errors
- ⚠️ Complete inpainting pipeline pending ProPainter fix

**Future (v2):**
- Fix ProPainter integration
- Complete workflows with full inpainting
- Pixel preservation compositing
- VRAM-optimized variants

---

## 🎯 Use Cases

### Current (v1 - Mask Generation)
- Generate masks for manual inpainting
- Test character detection
- Prepare masks for external tools
- Temporal mask smoothing

### Future (v2 - Complete Pipeline)
- Fully automated character removal
- Clean plate generation
- Background reconstruction
- VFX-ready output

---

## 💡 Tips

**Best Quality:**
- Use SAM3 workflow
- Add temporal smoothing (after installing nodes)
- Use 1080p resolution
- Adjust feathering to 15-20px

**Fastest Processing:**
- Use RMBG workflow
- Reduce to 512x512 resolution
- Static camera scenes work best

**Lowest VRAM:**
- Use RMBG workflow
- 512x512 resolution
- Process in segments if needed

---

## 🆘 Troubleshooting

### Nodes Not Showing
```bash
# Restart ComfyUI
pkill -f "python main.py"
cd /path/to/comfyui
./start_comfyui.sh
```

### Out of Memory
- Reduce resolution to 512x512
- Use RMBG workflow instead of SAM3
- Process fewer frames at once

### Video Won't Load
```bash
# Install ffmpeg
sudo apt install -y ffmpeg
```

---

## 📖 Learn More

**Start with:**
1. `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow usage
2. `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical details
3. `TEMPORAL_SMOOTHING_QUICKSTART.md` - Reduce flickering

**Advanced:**
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - RMBG & Depth options
- `TEMPORAL_SMOOTHING_GUIDE.md` - Complete temporal guide

---

## 🔗 Resources

**ComfyUI:** https://github.com/comfyanonymous/ComfyUI  
**SAM3:** Meta AI (November 2025)  
**RMBG:** Background removal model  
**ProPainter:** CVPR 2023 (pending integration)

---

**Version:** 1.0  
**Date:** January 14, 2026  
**Status:** Mask generation workflows complete, full inpainting pending ProPainter fix

---

**Ready to generate clean plate masks!** 🎬✨
