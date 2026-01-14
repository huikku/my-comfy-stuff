# ComfyUI Video Inpainting System

**NVIDIA Thor DevKit - Complete Video Inpainting Solution**

---

## 🎯 Quick Start

### Start ComfyUI
```bash
cd /home/john/comfyui && ./start_comfyui.sh
```
**Access:** http://10.0.0.39:8188

### Documentation
- **Quick Reference:** `QUICK_REFERENCE.md` ⭐ START HERE
- **Complete Guide:** `COMPLETE_INSTALLATION_GUIDE.md`
- **All Docs:** `DOCUMENTATION_INDEX.md`

---

## 📦 What's Installed

### Core System
- ✅ ComfyUI 0.8.2
- ✅ PyTorch 2.11.0 (CUDA 13.0 - Thor optimized)
- ✅ Python 3.12.3
- ✅ 23 Custom Node Packages
- ✅ 792 Nodes Indexed

### Key Features
- ✅ **SAM3** - Text-prompted segmentation
- ✅ **RMBG** - Fast background removal
- ✅ **Temporal Smoothing** - Reduce flicker
- ✅ **Feathered Masks** - Smooth blending
- ✅ **LLM Bridge** - AI workflow generation
- ⚠️ **ProPainter** - Video inpainting (needs fix)

---

## 🎬 Available Workflows

| Workflow | Purpose | VRAM |
|----------|---------|------|
| **SAM3 Basic v1** | Auto detect person | 18-27GB |
| **RMBG Fast v1** | Fast BG removal | 10-16GB |

**Location:** `/home/john/comfyui/workflows/`

---

## 📚 Documentation (30+ Files)

### Essential
- `QUICK_REFERENCE.md` - One-page reference
- `COMPLETE_INSTALLATION_GUIDE.md` - Main guide
- `DOCUMENTATION_INDEX.md` - All documentation

### Video Inpainting
- `VIDEO_INPAINTING_RESEARCH_REPORT.md` - Technical research
- `VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md` - Advanced workflows
- `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` - Workflow guide

### System
- `TEMPORAL_SMOOTHING_GUIDE.md` - Reduce flickering
- `VRAM_MANAGEMENT_GUIDE.md` - Memory management
- `LLM_BRIDGE_SETUP.md` - AI integration

**See `DOCUMENTATION_INDEX.md` for complete list**

---

## 🚀 Usage

### 1. Load Workflow
- Open ComfyUI: http://10.0.0.39:8188
- Click "Load"
- Select workflow from `workflows/`

### 2. Set Video Path
- Find "VHS_LoadVideoPath" node
- Enter video path
- Adjust resolution

### 3. Run
- Click "Queue Prompt"
- Check `output/` for results

---

## 📁 Directory Structure

```
/home/john/comfyui/
├── .agent/              # AI rules & workflows
├── custom_nodes/        # 23 node packages
├── input/               # Input videos
├── models/              # AI models
├── nodes/               # Node definitions
├── output/              # Generated files
├── workflows/           # Workflow JSONs
├── *.md                 # 30+ documentation files
└── refresh-nodes.py     # Refresh node defs
```

---

## ⚡ Common Commands

```bash
# Start ComfyUI
cd /home/john/comfyui && ./start_comfyui.sh

# Stop ComfyUI
pkill -f "python main.py"

# Refresh nodes
cd /home/john/comfyui && python refresh-nodes.py

# Check logs
tail -f /home/john/comfyui/user/comfyui.log
```

---

## 🔧 Troubleshooting

### Nodes Not Showing
```bash
pkill -f "python main.py"
cd /home/john/comfyui && ./start_comfyui.sh
```

### SAM3 Model Error
```bash
cd /home/john/comfyui/models/sam3
ln -sf sam3-002.pt sam3.pt
```

### Out of Memory
- Reduce resolution (512x512)
- Use RMBG workflow
- See `VRAM_MANAGEMENT_GUIDE.md`

**More:** See `QUICK_REFERENCE.md` or `COMPLETE_INSTALLATION_GUIDE.md`

---

## ⚠️ Known Issues

| Issue | Status | Workaround |
|-------|--------|------------|
| **ProPainter** | Import error | Use v1 workflows (mask only) |
| **Temporal nodes** | Need restart | Restart ComfyUI |
| **MotionCapture** | Missing deps | Use WHAM alternative |

---

## 🎯 Next Steps

1. ✅ Test workflows (mask generation)
2. ⚠️ Fix ProPainter (complete inpainting)
3. ⏳ Create v2 workflows (full pipeline)
4. ⏳ VRAM-optimized variants

---

## 📊 System Status

**Version:** 1.0  
**Date:** January 14, 2026  
**Status:** ✅ Operational (mask generation) | ⚠️ Pending (video inpainting)

**Installed:**
- ✅ ComfyUI + 23 custom nodes
- ✅ SAM3, RMBG, VHS, Temporal, Feathered
- ✅ LLM Bridge + 792 nodes indexed
- ✅ 2 workflows + 30+ docs

**Pending:**
- ⚠️ ProPainter fix
- ⏳ Complete workflows (v2)
- ⏳ VRAM variants

---

## 📖 Learn More

**Start Here:**
1. Read `QUICK_REFERENCE.md`
2. Review `COMPLETE_INSTALLATION_GUIDE.md`
3. Try workflows in `workflows/`

**Explore:**
- Browse `DOCUMENTATION_INDEX.md`
- Check component-specific guides
- Review research reports

---

## 🆘 Support

**Documentation:** 30+ comprehensive guides  
**Workflows:** 2 working workflows (v1)  
**Logs:** `/home/john/comfyui/user/comfyui.log`  
**Help:** See troubleshooting sections in guides

---

**🎬 Ready to create clean plates! Start with `QUICK_REFERENCE.md` →**
