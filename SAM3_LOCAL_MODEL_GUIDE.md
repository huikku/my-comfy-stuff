# Using Local SAM3 Model - Quick Fix

## ✅ Your SAM3 Model is Already Installed!

**Location:** `/home/john/comfyui/models/sam3/sam3-002.pt` (3.3GB)

---

## 🎯 How to Use It (Avoid HuggingFace Error)

### Method 1: Use Simple Model Loader ⭐ Recommended

**In your workflow:**

1. **Add node:** "TBG SAM3 Model Loader" (NOT the "Advanced" one)
2. **Set model_source to:** "local" or browse to select `sam3-002.pt`
3. **The node should find** your model in `models/sam3/`

**Avoid:** "TBG SAM3 Model Loader and Downloader" - this tries to download from HuggingFace

---

### Method 2: Use Existing Workflow

**Try these workflows that should use local models:**

1. `SAM3_And_RMBG_Mask_Workflow.json`
2. `sam3_segment_everything_v02.json`

**If they error:**
- Open the workflow
- Find the SAM3 loader node
- Change `model_source` from "auto" to "local"
- Select your `sam3-002.pt` file

---

### Method 3: Manual Configuration

**If the node insists on downloading:**

1. **In the SAM3 loader node**, look for these settings:
   - `model_source`: Set to "local" or "custom"
   - `checkpoint_path`: Point to `/home/john/comfyui/models/sam3/sam3-002.pt`
   - `use_hf`: Set to False (if available)

---

## 🔧 Why the Error Happens

The "TBG SAM3 Model Loader and Downloader" node tries to:
1. Download from HuggingFace `facebook/sam3`
2. This repo is **gated** (requires approval)
3. You need to log in to HuggingFace

**But you don't need to!** You already have the model locally.

---

## 🚀 Quick Test

**Try this in ComfyUI:**

1. Add "TBG SAM3 Model Loader" node
2. Add "TBG SAM3 Segmentation" node
3. Connect them
4. In the loader, select your local model
5. Execute!

---

## 📝 If You Still Get Errors

**Option 1: Check Model Path**
```bash
ls -lh /home/john/comfyui/models/sam3/
```
Should show: `sam3-002.pt` (3.3GB)

**Option 2: Rename Model (if needed)**

Some nodes might expect specific names:
```bash
cd /home/john/comfyui/models/sam3/
# Create a symlink with different name if needed
ln -s sam3-002.pt sam3_model.pt
```

**Option 3: Use Different SAM3 Node**

If TBG-SAM3 doesn't work with local models, you can:
- Use SAM2 instead (also installed)
- Use RMBG for background removal
- Wait for TBG-SAM3 update

---

## 💡 Recommended Approach

**For now, use:**

1. ✅ **RMBG nodes** - Work great for background removal
2. ✅ **SAM2 nodes** - Should work after PyTorch upgrade
3. ✅ **DepthAnything** - Works perfectly

**SAM3 is installed but the node has HuggingFace dependency issues.**

---

## 🆘 Alternative: Get HuggingFace Access

**If you really want to use the downloader:**

1. Go to: https://huggingface.co/facebook/sam3
2. Request access (requires Meta account)
3. Wait for approval
4. Create HuggingFace token
5. Configure in ComfyUI

**But this is NOT needed** - you already have the model!

---

## ✅ Summary

**You have the SAM3 model!**
- Location: `/home/john/comfyui/models/sam3/sam3-002.pt`
- Size: 3.3GB ✓
- Config: Available ✓

**To use it:**
- Use "TBG SAM3 Model Loader" (simple version)
- Select "local" model source
- Point to your `sam3-002.pt` file

**Or use alternatives:**
- RMBG for background removal
- SAM2 for segmentation
- DepthAnything for depth/normals

---

**The model is ready - just tell the node to use the local file instead of downloading!** 🎯
