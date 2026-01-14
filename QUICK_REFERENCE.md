# ComfyUI Video Inpainting - Quick Reference Card

## 🚀 Quick Commands

### Start ComfyUI
```bash
cd /home/john/comfyui && ./start_comfyui.sh
```
**Access:** http://10.0.0.39:8188

### Stop ComfyUI
```bash
pkill -f "python main.py"
```

### Refresh Nodes
```bash
cd /home/john/comfyui && python refresh-nodes.py
```

---

## 📁 Key Locations

| Item | Location |
|------|----------|
| **ComfyUI** | `/home/john/comfyui` |
| **Input Videos** | `/home/john/comfyui/input/` |
| **Output Files** | `/home/john/comfyui/output/` |
| **Workflows** | `/home/john/comfyui/workflows/` |
| **Models** | `/home/john/comfyui/models/` |
| **SAM3 Model** | `/home/john/comfyui/models/sam3/sam3-002.pt` |
| **Logs** | `/home/john/comfyui/user/comfyui.log` |

---

## 🎬 Available Workflows

| Workflow | File | Purpose | VRAM |
|----------|------|---------|------|
| **SAM3 Basic** | `video_inpaint_sam3_basic_v1.json` | Auto detect person | 18-27GB |
| **RMBG Fast** | `video_inpaint_rmbg_fast_v1.json` | Fast BG removal | 10-16GB |

---

## 🔧 Installed Nodes

### Segmentation
- ✅ SAM3 (text-prompted)
- ✅ SAM2 (interactive)
- ✅ RMBG (background removal)

### Video
- ✅ VideoHelperSuite (VHS)
- ⚠️ ProPainter (needs fix)

### Temporal
- ✅ Temporal Mask Tools (NEW)
- ✅ Feathered Inpaint (NEW)

### Depth
- ✅ DepthAnythingV2
- ✅ DepthAnythingV3

### Utilities
- ✅ VRAM Monitor
- ✅ LLM Bridge
- ✅ ComfyUI Manager
- ✅ rgthree-comfy (48 nodes)

---

## ⚡ Workflow Quick Start

### 1. Load Workflow
- Open ComfyUI: http://10.0.0.39:8188
- Click "Load"
- Select workflow from `/home/john/comfyui/workflows/`

### 2. Set Video Path
- Find "VHS_LoadVideoPath" node
- Enter video path
- Adjust resolution (512, 720, or 1080)

### 3. Run
- Click "Queue Prompt"
- Check output in `/home/john/comfyui/output/`

---

## 📊 Resolution Guide

| GPU VRAM | Recommended | Max |
|----------|-------------|-----|
| **8GB** | 512x512 | 720x720 |
| **12GB** | 720x720 | 1080x1080 |
| **16GB** | 1080x1080 | 1080x1080 |
| **24GB+** | 1080x1080 | 4K |
| **Thor 125GB** | Any | 4K+ |

---

## 🔍 Common Issues

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
- Reduce resolution
- Use RMBG workflow
- Process fewer frames

### Video Won't Load
```bash
sudo apt install -y ffmpeg
```

---

## 📚 Documentation

| Guide | File |
|-------|------|
| **Complete Guide** | `COMPLETE_INSTALLATION_GUIDE.md` |
| **Workflow Guide** | `workflows/VIDEO_INPAINT_WORKFLOWS_README.md` |
| **Research Report** | `VIDEO_INPAINTING_RESEARCH_REPORT.md` |
| **Temporal Smoothing** | `TEMPORAL_SMOOTHING_GUIDE.md` |
| **LLM Bridge** | `LLM_BRIDGE_SETUP.md` |
| **VRAM Management** | `VRAM_MANAGEMENT_GUIDE.md` |

---

## ⚠️ Known Issues

| Issue | Status | Workaround |
|-------|--------|------------|
| **ProPainter** | Import error | Use v1 workflows (mask only) |
| **MotionCapture** | Missing deps | Use WHAM alternative |
| **Temporal nodes** | Need restart | Restart ComfyUI |

---

## 🎯 Next Steps

1. ✅ Restart ComfyUI (load new nodes)
2. ✅ Test workflows (mask generation)
3. ⚠️ Fix ProPainter (complete inpainting)
4. ⏳ Create v2 workflows (full pipeline)

---

## 💡 Tips

### Best Quality
- Use SAM3 workflow
- Add temporal smoothing (after restart)
- Use feathered inpaint (after restart)
- 1080p resolution

### Fastest Processing
- Use RMBG workflow
- 512x512 resolution
- Static camera scenes

### Lowest VRAM
- Use RMBG workflow
- 512x512 resolution
- Limit frame count

---

## 📞 Quick Help

**Check logs:**
```bash
tail -f /home/john/comfyui/user/comfyui.log
```

**Check running processes:**
```bash
ps aux | grep "python main.py"
```

**Check VRAM usage:**
```bash
nvidia-smi
```

**Check disk space:**
```bash
df -h /home/john/comfyui
```

---

**Version:** 1.0 | **Updated:** Jan 14, 2026 | **Status:** ✅ Operational (masks) | ⚠️ Pending (inpainting)
