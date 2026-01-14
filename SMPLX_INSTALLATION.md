# SMPL-X Motion Capture - Installation Guide

## 📋 Prerequisites

- ComfyUI 0.8.2+
- PyTorch 2.11.0+
- Python 3.12+
- 8GB+ VRAM (12GB+ recommended)

---

## 🚀 Quick Installation

### 1. Install Required ComfyUI Nodes

**Via ComfyUI Manager:**
- ComfyUI-VideoHelperSuite (VHS)
- ComfyUI-WHAM

**Or manually:**
```bash
cd /path/to/comfyui/custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
git clone https://github.com/YOUR_REPO/ComfyUI-WHAM.git
```

---

### 2. Install WHAM Dependencies

**Required Python packages:**
```bash
cd /path/to/comfyui
source venv/bin/activate

# Install WHAM requirements
pip install -r custom_nodes/ComfyUI-WHAM/requirements.txt

# Install additional dependencies
pip install progress mmengine mmcv-lite mmpose
```

**What gets installed:**
- `progress` - Progress bars
- `mmengine` - MMEngine framework
- `mmcv-lite` - Computer vision library (lightweight)
- `mmpose` - Pose estimation library
- `smplx` - Official SMPL-X library
- `loguru`, `yacs`, `joblib` - Utilities
- `ultralytics` - YOLO detection
- `gdown`, `huggingface_hub` - Model downloads

---

### 3. Install SMPL-X Library

```bash
pip install smplx
```

---

### 4. Download SMPL-X Models

**Get models from:** https://smpl-x.is.tue.mpg.de/

1. Register and download SMPL-X models
2. Extract to `/path/to/comfyui/models/smplx/`
3. Should have:
   - `SMPLX_NEUTRAL.pkl`
   - `SMPLX_MALE.pkl`
   - `SMPLX_FEMALE.pkl`

---

### 5. Install Custom SMPL-X Export Node

```bash
cp -r /path/to/my-comfy-stuff/custom_nodes/ComfyUI-SMPLX-Export /path/to/comfyui/custom_nodes/
```

---

### 6. Restart ComfyUI

```bash
pkill -f "python main.py"
cd /path/to/comfyui
./start_comfyui.sh
```

---

## ✅ Verify Installation

**Check that these nodes appear in ComfyUI:**
- LoadWHAMModels
- WHAMInference
- SaveSMPLXParams
- ExportSMPLXAnimation
- ExportSMPLXMeshSequence

---

## 🔧 Troubleshooting

### "No module named 'progress'"
```bash
pip install progress
```

### "No module named 'mmpose'"
```bash
pip install mmengine mmcv-lite
pip install --no-deps mmpose
```

### "Failed to import WHAM components"
```bash
cd /path/to/comfyui
source venv/bin/activate
pip install -r custom_nodes/ComfyUI-WHAM/requirements.txt
pip install progress mmengine mmcv-lite mmpose
```

### "SMPL-X models not found"
- Download from https://smpl-x.is.tue.mpg.de/
- Extract to `models/smplx/`
- Check paths in ExportSMPLXMeshSequence node

---

## 📦 Complete Installation Script

```bash
#!/bin/bash
# Complete SMPL-X installation script

cd /path/to/comfyui
source venv/bin/activate

# Install WHAM dependencies
pip install -r custom_nodes/ComfyUI-WHAM/requirements.txt

# Install additional requirements
pip install progress mmengine mmcv-lite
pip install --no-deps mmpose
pip install smplx

# Copy custom node
cp -r /path/to/my-comfy-stuff/custom_nodes/ComfyUI-SMPLX-Export custom_nodes/

# Copy workflows
cp /path/to/my-comfy-stuff/workflows/smplx_*.json user/default/workflows/

echo "Installation complete! Restart ComfyUI."
```

---

## 📊 Disk Space Requirements

- WHAM models: ~500MB (auto-downloaded on first use)
- SMPL-X models: ~200MB
- Python packages: ~1GB
- **Total:** ~1.7GB

---

## 🎯 Next Steps

After installation:
1. Restart ComfyUI
2. Load `smplx_motion_capture_complete_v2.json`
3. Select a video
4. Run workflow
5. Get BVH animation + mesh sequence!

---

**Version:** 1.0  
**Date:** January 14, 2026  
**Tested on:** NVIDIA Thor DevKit, Ubuntu Linux
