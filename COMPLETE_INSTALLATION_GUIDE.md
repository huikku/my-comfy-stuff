# ComfyUI Video Inpainting System - Complete Installation & Usage Guide

**Version:** 1.0  
**Date:** January 14, 2026  
**System:** NVIDIA Thor DevKit (125GB Unified Memory)

---

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [What's Installed](#whats-installed)
3. [Installation Guide](#installation-guide)
4. [Quick Start](#quick-start)
5. [Workflow Usage](#workflow-usage)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Configuration](#advanced-configuration)

---

## 🎯 System Overview

### Purpose
Complete video inpainting system for removing foreground characters from video scenes (creating "clean plates").

### Key Features
- ✅ Automated character detection (SAM3)
- ✅ Fast background removal (RMBG)
- ✅ Temporal mask smoothing (reduce flickering)
- ✅ Feathered mask edges (smooth blending)
- ✅ Pixel-perfect preservation outside mask
- ⚠️ Video inpainting (ProPainter - needs fix)

### Workflow Pipeline
```
Video Input
    ↓
Mask Generation (SAM3 or RMBG)
    ↓
Temporal Smoothing (reduce flicker)
    ↓
Feather Edges (smooth blend)
    ↓
Video Inpainting (ProPainter - when fixed)
    ↓
Preserve Original Pixels
    ↓
Clean Plate Output
```

---

## 📦 What's Installed

### Core ComfyUI
- **Location:** `/home/john/comfyui`
- **Version:** 0.8.2
- **PyTorch:** 2.11.0.dev (CUDA 13.0 - Thor GPU optimized)
- **Python:** 3.12.3

### Custom Nodes (23 packages)

#### Segmentation & Masking
1. **ComfyUI-TBG-SAM3** ⭐
   - SAM3 (Segment Anything Model 3)
   - Text-prompted segmentation
   - Multi-instance detection
   - Video tracking
   - Model: `/home/john/comfyui/models/sam3/sam3-002.pt`

2. **ComfyUI-SAM2**
   - SAM2 (Segment Anything Model 2)
   - Interactive segmentation
   - Video tracking

3. **ComfyUI-RMBG** ⭐
   - Background removal (RMBG-2.0)
   - Fast processing
   - Low VRAM usage

#### Video Processing
4. **ComfyUI-VideoHelperSuite (VHS)** ⭐
   - Video loading/saving
   - Frame manipulation
   - Format conversion

5. **ComfyUI_ProPainter_Nodes** ⚠️
   - Video inpainting
   - **Status:** Import error (needs fix)

#### Temporal Processing
6. **ComfyUI-Temporal-Mask-Tools** ⭐ NEW
   - Temporal mask smoothing
   - Flicker reduction
   - Short object removal

7. **ComfyUI-Feathered-Inpaint** ⭐ NEW (Custom)
   - Feathered mask edges
   - Pixel preservation
   - Custom falloff curves

#### Depth & Normals
8. **ComfyUI-DepthAnythingV2**
   - Depth estimation
   - Depth-guided processing

9. **ComfyUI-DepthAnythingV3**
   - Enhanced depth estimation
   - Better accuracy

#### Utilities
10. **ComfyUI-Manager**
    - Node management
    - Updates

11. **ComfyUI-VRAM-Monitor**
    - Memory monitoring
    - System stats

12. **rgthree-comfy**
    - 48 utility nodes
    - Workflow helpers

13. **comfyui-llm-bridge** ⭐ NEW
    - AI workflow generation
    - Node definitions
    - Automated workflow creation

14. **comfyui-workspace-manager**
    - Workspace organization

15. **comfyui-tooling-nodes**
    - Development tools

16. **comfyui-utils**
    - Utility functions

17. **comfyui-sharp**
    - Image sharpening

18. **websocket_image_save**
    - Real-time saving

19. **ComfyUI-Image-Filters**
    - Image processing

20. **ComfyUI-WHAM**
    - Motion capture alternative

21. **ComfyUI-MotionCapture** ⚠️
    - Motion capture
    - **Status:** Missing dependencies

22. **ComfyUI-SAM2-CPU-Fix** (Custom)
    - SAM2 CPU fallback

23. **ComfyUI-DepthAnythingV2** (Duplicate entry)

---

## 🚀 Installation Guide

### Prerequisites
- ✅ NVIDIA Thor DevKit (or compatible GPU)
- ✅ Ubuntu Linux
- ✅ Python 3.12+
- ✅ CUDA 13.0+
- ✅ 125GB RAM (or 24GB+ for other systems)

### Step 1: ComfyUI Base Installation
**Already installed at:** `/home/john/comfyui`

If starting fresh:
```bash
cd /home/john
git clone https://github.com/comfyanonymous/ComfyUI.git comfyui
cd comfyui
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: PyTorch Upgrade (Thor GPU)
**Already done** - PyTorch 2.11.0 with CUDA 13.0

If needed:
```bash
cd /home/john/comfyui
./upgrade_pytorch_for_thor.sh
```

### Step 3: Install Custom Nodes

#### Essential Nodes (Already Installed)

**SAM3 (Segmentation):**
```bash
cd /home/john/comfyui/custom_nodes
git clone https://github.com/YOUR_REPO/ComfyUI-TBG-SAM3.git
```

**RMBG (Background Removal):**
```bash
cd /home/john/comfyui/custom_nodes
# Install via ComfyUI Manager or:
git clone https://github.com/YOUR_REPO/ComfyUI-RMBG.git
```

**VideoHelperSuite:**
```bash
cd /home/john/comfyui/custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
```

**Temporal Mask Tools:** ⭐ NEW
```bash
cd /home/john/comfyui/custom_nodes
git clone https://github.com/nomadoor/ComfyUI-Temporal-Mask-Tools.git
```

**Feathered Inpaint:** ⭐ NEW (Custom)
```bash
# Already created at:
/home/john/comfyui/custom_nodes/ComfyUI-Feathered-Inpaint/
```

**LLM Bridge:** ⭐ NEW
```bash
cd /home/john/comfyui/custom_nodes
git clone https://github.com/huikku/comfyui-llm-bridge.git

# Copy to top level:
cp -r comfyui-llm-bridge/.agent /home/john/comfyui/
cp comfyui-llm-bridge/refresh-nodes.py /home/john/comfyui/
ln -s /home/john/comfyui/custom_nodes/comfyui-llm-bridge/nodes /home/john/comfyui/nodes
```

### Step 4: Install System Dependencies

**FFmpeg (for video processing):**
```bash
sudo apt update
sudo apt install -y ffmpeg
```

**Python packages:**
```bash
cd /home/john/comfyui
source venv/bin/activate

# For SAM3
pip install ftfy

# For MotionCapture (if using)
pip install pytorch-lightning colorlog

# For Feathered Inpaint
pip install scipy
```

### Step 5: Download Models

**SAM3 Model:**
```bash
# Already at: /home/john/comfyui/models/sam3/sam3-002.pt
# If needed, download from HuggingFace (requires access)
```

**RMBG Models:**
```bash
# Auto-downloaded on first use
# Stored in: /home/john/comfyui/models/rmbg/
```

**DepthAnything Models:**
```bash
# Auto-downloaded on first use
# Stored in: /home/john/comfyui/models/depth_anything/
```

### Step 6: Restart ComfyUI

```bash
pkill -f "python main.py"
cd /home/john/comfyui
./start_comfyui.sh
```

### Step 7: Refresh Node Definitions (for LLM Bridge)

```bash
cd /home/john/comfyui
python refresh-nodes.py
```

---

## ⚡ Quick Start

### 1. Start ComfyUI

```bash
cd /home/john/comfyui
./start_comfyui.sh
```

**Access:**
- Local: http://localhost:8188
- Network: http://10.0.0.39:8188

### 2. Load a Workflow

**In ComfyUI:**
1. Click "Load" button
2. Navigate to `/home/john/comfyui/workflows/`
3. Select a workflow:
   - `video_inpaint_sam3_basic_v1.json` - Automated detection
   - `video_inpaint_rmbg_fast_v1.json` - Fast processing

### 3. Configure Input

**Set video path:**
1. Find "VHS_LoadVideoPath" node
2. Enter video path in "video" field
3. Adjust resolution if needed (default: 512x512)

### 4. Run Workflow

1. Click "Queue Prompt" button
2. Wait for processing
3. Check output in `/home/john/comfyui/output/`

---

## 🎬 Workflow Usage

### Workflow 1: SAM3 Basic (v1)

**File:** `workflows/video_inpaint_sam3_basic_v1.json`

**What it does:**
- Loads video
- Detects "person" using SAM3
- Creates feathered mask (15px edges)
- Saves visualization and mask

**Parameters to adjust:**

**VHS_LoadVideoPath:**
- `video`: Path to your video file
- `custom_width`: 512 (or 720, 1080)
- `custom_height`: 512 (or 720, 1080)
- `frame_load_cap`: 0 (all frames) or limit

**TBGSam3Segmentation:**
- `text_prompt`: "person" (or "character", "man", "woman")
- `confidence_threshold`: 0.4 (lower = more detections)
- `detect_all`: true (detect all instances)
- `min_size`: 100 (minimum object size in pixels)

**FeatherMask:**
- `left/top/right/bottom`: 15 (feather distance in pixels)

**Outputs:**
- `sam3_visualization_*.mp4` - Shows detected masks
- `feathered_mask_*.mp4` - Feathered mask video

**VRAM Usage:** 18-27GB

---

### Workflow 2: RMBG Fast (v1)

**File:** `workflows/video_inpaint_rmbg_fast_v1.json`

**What it does:**
- Loads video
- Removes background using RMBG
- Creates feathered mask (15px edges)
- Saves result and mask

**Parameters to adjust:**

**VHS_LoadVideoPath:**
- `video`: Path to your video file
- `custom_width`: 512 (or 720, 1080)
- `custom_height`: 512 (or 720, 1080)

**RMBG:**
- `model`: "RMBG-2.0" (best quality)
- `sensitivity`: 0.5 (0.0-1.0, higher = more aggressive)
- `process_res`: 1024 (processing resolution)
- `invert_output`: true (mask the person, not background)

**FeatherMask:**
- `left/top/right/bottom`: 15 (feather distance)

**Outputs:**
- `rmbg_result_*.mp4` - Background removed
- `rmbg_feathered_mask_*.mp4` - Feathered mask

**VRAM Usage:** 10-16GB

---

## 🔧 Troubleshooting

### ComfyUI Won't Start

**Check if already running:**
```bash
ps aux | grep "python main.py"
```

**Kill existing process:**
```bash
pkill -f "python main.py"
```

**Check logs:**
```bash
tail -f /home/john/comfyui/user/comfyui.log
```

---

### Nodes Not Appearing

**Restart ComfyUI:**
```bash
pkill -f "python main.py"
cd /home/john/comfyui
./start_comfyui.sh
```

**Refresh browser:**
- Press F5 or Ctrl+R

**Check node installation:**
```bash
ls -la /home/john/comfyui/custom_nodes/
```

---

### SAM3 Model Not Found

**Check model location:**
```bash
ls -la /home/john/comfyui/models/sam3/
```

**Should see:**
- `sam3-002.pt` (3.3GB)
- `sam3.pt` (symlink)
- `config.json`

**If missing, create symlink:**
```bash
cd /home/john/comfyui/models/sam3
ln -sf sam3-002.pt sam3.pt
```

---

### ProPainter Import Error

**Status:** Known issue - IndexError in misc.py

**Temporary workaround:**
- Use workflows v1 (mask generation only)
- Wait for fix or use alternative inpainting

**To diagnose:**
```bash
cd /home/john/comfyui
source venv/bin/activate
python -c "from custom_nodes.ComfyUI_ProPainter_Nodes import propainter_nodes"
```

---

### Out of Memory (VRAM)

**For 8GB GPUs:**
- Use RMBG workflow (10-16GB)
- Reduce resolution to 512x512 or lower
- Process fewer frames at once

**For 12GB GPUs:**
- Use RMBG or SAM3 with reduced batch
- Resolution: 720p max

**For 16GB+ GPUs:**
- Use any workflow
- Resolution: 1080p

**For Thor (125GB):**
- Use any workflow
- Resolution: 4K if needed
- No limitations

---

### Video Won't Load

**Check video format:**
- Supported: MP4, AVI, MOV, MKV
- Codec: H.264, H.265

**Check ffmpeg:**
```bash
ffmpeg -version
```

**If missing:**
```bash
sudo apt install -y ffmpeg
```

**Check video path:**
- Use absolute path: `/home/john/Videos/myvideo.mp4`
- Or relative to ComfyUI: `input/myvideo.mp4`

---

### Temporal Nodes Not Available

**These nodes need ComfyUI restart to load:**
- TemporalMaskUnion
- TemporalMaskRemoveShortObjects
- FeatheredInpaintMask
- PreserveOriginalPixels

**Solution:**
```bash
pkill -f "python main.py"
cd /home/john/comfyui
./start_comfyui.sh
```

**Verify installation:**
```bash
ls -la /home/john/comfyui/custom_nodes/ComfyUI-Temporal-Mask-Tools/
ls -la /home/john/comfyui/custom_nodes/ComfyUI-Feathered-Inpaint/
```

---

## 🎯 Advanced Configuration

### VRAM Optimization

**Edit workflow parameters:**

**For 8GB VRAM:**
```json
{
  "custom_width": 512,
  "custom_height": 512,
  "process_res": 512,
  "frame_load_cap": 100
}
```

**For 12GB VRAM:**
```json
{
  "custom_width": 720,
  "custom_height": 720,
  "process_res": 1024,
  "frame_load_cap": 200
}
```

**For 16GB+ VRAM:**
```json
{
  "custom_width": 1080,
  "custom_height": 1080,
  "process_res": 1024,
  "frame_load_cap": 0
}
```

---

### Temporal Smoothing (After Restart)

**Add to workflow after mask generation:**

**TemporalMaskUnion node:**
```json
{
  "class_type": "TemporalMaskUnion",
  "inputs": {
    "masks": ["previous_node", 0],
    "window_size": 5,
    "mode": "majority"
  }
}
```

**Parameters:**
- `window_size`: 3-7 (frames to average)
- `mode`: "majority" or "or"

---

### Custom Feathering (After Restart)

**Replace FeatherMask with FeatheredInpaintMask:**

```json
{
  "class_type": "FeatheredInpaintMask",
  "inputs": {
    "mask": ["previous_node", 0],
    "feather_pixels": 15,
    "feather_falloff": "smooth"
  }
}
```

**Parameters:**
- `feather_pixels`: 0-100 (edge softness)
- `feather_falloff`: "linear", "smooth", "smoother"

---

### Batch Processing

**Process multiple videos:**

1. Create a list of video paths
2. Use VHS_LoadVideoPath with different paths
3. Queue each workflow separately

**Or use Python script:**
```python
import os
import json

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]
workflow_template = "workflows/video_inpaint_sam3_basic_v1.json"

for video in videos:
    with open(workflow_template) as f:
        workflow = json.load(f)
    
    # Update video path
    workflow["1"]["inputs"]["video"] = f"/path/to/{video}"
    
    # Save modified workflow
    output_path = f"workflows/batch_{video}.json"
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    print(f"Created: {output_path}")
```

---

## 📊 Performance Benchmarks

### Processing Speed (Estimated)

**Thor DevKit (125GB):**
- SAM3: ~1-2 fps
- RMBG: ~5-10 fps
- Total: ~10-30 min for 1 min 1080p video

**RTX 4090 (24GB):**
- SAM3: ~1-2 fps
- RMBG: ~5-10 fps
- Total: ~10-30 min for 1 min 1080p video

**RTX 3080 (12GB):**
- SAM3: ~0.5-1 fps (720p)
- RMBG: ~3-5 fps
- Total: ~20-40 min for 1 min 720p video

**RTX 3070 (8GB):**
- RMBG only: ~2-4 fps (720p)
- Total: ~30-60 min for 1 min 720p video

---

## 📁 File Locations

### Important Directories

```
/home/john/comfyui/
├── .agent/                    # AI rules & workflows
├── custom_nodes/              # All custom nodes
├── input/                     # Input videos/images
├── models/                    # AI models
│   ├── sam3/                 # SAM3 models
│   ├── rmbg/                 # RMBG models
│   └── depth_anything/       # Depth models
├── nodes/                     # Node definitions (symlink)
├── output/                    # Generated outputs
├── user/                      # User data & logs
├── venv/                      # Python virtual environment
├── workflows/                 # Workflow JSON files
├── refresh-nodes.py          # Refresh node definitions
└── start_comfyui.sh          # Startup script
```

### Configuration Files

```
/home/john/comfyui/
├── .gitignore
├── category-map.json         # LLM Bridge config
├── requirements.txt          # Python dependencies
└── user/
    ├── comfyui.log          # Application logs
    └── __manager/
        └── config.ini       # ComfyUI Manager config
```

---

## 📚 Documentation Files

### Guides Created

```
/home/john/comfyui/
├── INSTALLATION_INFO.md                    # ComfyUI installation
├── CUSTOM_NODES_INSTALLATION_SUMMARY.md   # Custom nodes summary
├── VIDEO_INPAINTING_RESEARCH_REPORT.md    # Technical research
├── VIDEO_INPAINTING_ENHANCED_WORKFLOWS.md # Workflow variants
├── VIDEO_INPAINTING_MISSING_PIECES.md     # Missing features
├── TEMPORAL_SMOOTHING_GUIDE.md            # Temporal smoothing
├── TEMPORAL_SMOOTHING_QUICKSTART.md       # Quick start
├── LLM_BRIDGE_SETUP.md                    # LLM Bridge setup
├── LLM_BRIDGE_QUICKREF.md                 # Quick reference
├── OUTPUT_FILES_GUIDE.md                  # Output file access
├── VRAM_MANAGEMENT_GUIDE.md               # VRAM monitoring
├── VRAM_IN_COMFYUI_GUIDE.md              # In-app VRAM
├── VHS_TROUBLESHOOTING.md                 # Video Helper Suite
├── VIDEO_SYNC_GUIDE.md                    # Video sync playback
├── SLACK_GUIDE.md                         # Slack alternatives
├── CUDA_COMPATIBILITY_GUIDE.md            # CUDA/Thor GPU
├── SAM3_LOCAL_MODEL_GUIDE.md             # SAM3 local model
└── workflows/
    └── VIDEO_INPAINT_WORKFLOWS_README.md  # Workflow guide
```

---

## ✅ Installation Checklist

### Base System
- [ ] ComfyUI installed
- [ ] PyTorch 2.11.0 (CUDA 13.0)
- [ ] Python 3.12.3
- [ ] FFmpeg installed

### Custom Nodes
- [ ] ComfyUI-TBG-SAM3
- [ ] ComfyUI-SAM2
- [ ] ComfyUI-RMBG
- [ ] ComfyUI-VideoHelperSuite
- [ ] ComfyUI-Temporal-Mask-Tools
- [ ] ComfyUI-Feathered-Inpaint
- [ ] comfyui-llm-bridge
- [ ] ComfyUI-DepthAnythingV2/V3
- [ ] ComfyUI-Manager

### Models
- [ ] SAM3 model (sam3-002.pt)
- [ ] RMBG models (auto-download)
- [ ] DepthAnything models (auto-download)

### Configuration
- [ ] .agent folder copied
- [ ] refresh-nodes.py in top level
- [ ] nodes symlink created
- [ ] ComfyUI restarted
- [ ] Node definitions refreshed

### Workflows
- [ ] video_inpaint_sam3_basic_v1.json
- [ ] video_inpaint_rmbg_fast_v1.json
- [ ] Workflows tested

---

## 🎓 Learning Resources

### ComfyUI Basics
- Official Wiki: https://github.com/comfyanonymous/ComfyUI/wiki
- Video Tutorials: YouTube "ComfyUI tutorials"
- Community: ComfyUI Discord

### Video Inpainting
- ProPainter Paper: CVPR 2023
- SAM3 Documentation: Meta AI
- E2FGVI Paper: CVPR 2022

### Custom Nodes
- Node Development Guide: ComfyUI wiki
- Example Nodes: Browse custom_nodes/
- LLM Bridge: /home/john/comfyui/.agent/

---

## 🆘 Support

### Issues
- Check `/home/john/comfyui/user/comfyui.log`
- Review troubleshooting section above
- Check documentation files

### Updates
```bash
cd /home/john/comfyui
git pull
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

### Node Updates
```bash
cd /home/john/comfyui/custom_nodes/<node_name>
git pull
```

---

## 📝 Version History

### v1.0 (January 14, 2026)
- Initial system setup
- SAM3 + RMBG workflows
- Temporal smoothing nodes
- Feathered inpaint nodes
- LLM Bridge integration
- Complete documentation

### Future (v2.0)
- ProPainter integration
- Complete inpainting workflows
- VRAM-optimized variants
- Batch processing tools

---

**System Status:** ✅ Ready for mask generation | ⚠️ Waiting for ProPainter fix for complete inpainting

**Last Updated:** January 14, 2026
