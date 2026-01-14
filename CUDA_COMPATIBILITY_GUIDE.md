# CUDA Compatibility Issue - NVIDIA Thor GPU

## ❌ The Problem

Your NVIDIA Thor GPU has CUDA capability **sm_110**, but the current PyTorch installation only supports:
- sm_50, sm_80, sm_86, sm_89, sm_90, sm_90a

This causes SAM2 and other models to fail with:
```
RuntimeError: CUDA error: no kernel image is available for execution on the device
```

---

## ✅ Solutions

### Solution 1: Use CPU Mode (Temporary Workaround)

**For SAM2 nodes, use CPU mode:**
- In the SAM2 node settings, look for "device" option
- Set it to "cpu" instead of "cuda"
- This will be slower but will work

### Solution 2: Upgrade PyTorch (Recommended)

**Your Thor GPU needs PyTorch with CUDA 13.0+ support.**

The current PyTorch (2.5.1) doesn't support sm_110. You need a newer nightly build.

**⚠️ Warning:** This might break other things. Backup first!

```bash
cd /home/john/comfyui
source venv/bin/activate

# Uninstall current PyTorch
pip uninstall -y torch torchvision torchaudio

# Install PyTorch nightly with CUDA 13.0 support
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu130
```

### Solution 3: Use Alternative Nodes

**Instead of SAM2, use:**
- **ComfyUI-RMBG** - Background removal (works on CPU)
- **ComfyUI-TBG-SAM3** - If you can get it working
- **DepthAnything** - Works fine on your GPU

---

## 🎯 Quick Fix for SAM2

### Option A: Force CPU in Workflow

1. Find the SAM2 node in your workflow
2. Look for "device" parameter
3. Change from "auto" or "cuda" to "cpu"
4. Execute

### Option B: Set Environment Variable

Add to your start script:

```bash
# Edit start_comfyui.sh
export CUDA_VISIBLE_DEVICES=""  # This forces CPU mode
```

---

## 🔍 Check Your PyTorch Version

```bash
cd /home/john/comfyui
source venv/bin/activate
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}'); print(f'Supports sm_110: {torch.cuda.get_device_capability(0) if torch.cuda.is_available() else \"N/A\"}')"
```

---

## 📊 What Works vs What Doesn't

### ✅ Works Fine on Thor:
- DepthAnythingV2/V3
- Image processing nodes
- Most custom nodes
- Video loading/saving
- Basic image generation

### ⚠️ May Have Issues:
- SAM2 (CUDA kernel incompatibility)
- SAM3 (missing dependencies + CUDA issues)
- Some advanced segmentation
- Models requiring specific CUDA ops

### 🔄 Workaround:
- Use CPU mode for problematic nodes
- Use alternative nodes
- Wait for PyTorch update

---

## 🚀 Recommended Approach

**For now:**

1. **Use CPU mode for SAM2**
   - Slower but works
   - Set device="cpu" in node

2. **Use RMBG for background removal**
   - Works better on Thor
   - Already installed

3. **Use DepthAnything for depth/normals**
   - Works perfectly
   - No CUDA issues

4. **Wait for PyTorch update**
   - NVIDIA will likely release compatible version
   - Or PyTorch will add sm_110 support

---

## 🛠️ If You Want to Try PyTorch Upgrade

**Backup first!**

```bash
# Backup current environment
cd /home/john/comfyui
cp -r venv venv_backup

# Try upgrade
source venv/bin/activate
pip install --upgrade --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu130

# Test
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

# If it breaks, restore:
# rm -rf venv
# mv venv_backup venv
```

---

## 💡 Alternative Workflows

**Instead of SAM2 segmentation:**

1. **Use RMBG** (Background Removal)
   - Already working
   - Good for simple masking

2. **Use DepthAnything + Depth to Mask**
   - Generate depth map
   - Convert to mask
   - Works great!

3. **Use Image Filters**
   - Edge detection
   - Color-based masking
   - Works on CPU

---

## 📝 Summary

**The Issue:**
- Thor GPU (sm_110) not supported by current PyTorch
- SAM2 CUDA kernels fail

**Quick Fix:**
- Use CPU mode for SAM2
- Or use alternative nodes (RMBG, DepthAnything)

**Long-term Fix:**
- Wait for PyTorch update
- Or try nightly build (risky)

---

**For now, use CPU mode or alternative nodes. Your Thor GPU works great for most other tasks!** 🎮
