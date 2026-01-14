# VideoHelperSuite (VHS) Troubleshooting Guide

## ✅ Fixed: FFmpeg Installed

FFmpeg has been installed on your system. This should resolve most VHS errors.

---

## 🔍 Common VHS Errors and Solutions

### Error: "FFmpeg not found"
**Solution:** ✅ FIXED - FFmpeg is now installed

### Error: "Cannot load video"
**Possible causes:**
1. **Unsupported video codec**
   - Try converting video to H.264/MP4
   - Use: `ffmpeg -i input.mov -c:v libx264 output.mp4`

2. **File path issues**
   - Make sure video is in ComfyUI input folder
   - Path: `/home/john/comfyui/input/`

3. **Permissions**
   - Check file permissions: `ls -la /home/john/comfyui/input/`

### Error: "Cannot save video"
**Solutions:**
1. Check output folder exists
2. Ensure write permissions
3. Try different codec settings

---

## 🎬 How to Use VHS Nodes

### Load Video:
1. Add "VHS Video Combine" or "Load Video" node
2. Place video in `/home/john/comfyui/input/`
3. Select the video file
4. Execute

### Save Video:
1. Add "VHS Video Combine" node
2. Connect your image sequence
3. Set FPS and codec
4. Execute
5. Find output in `/home/john/comfyui/output/`

---

## 🛠️ Verify Installation

### Check FFmpeg:
```bash
ffmpeg -version
```

### Check Python Package:
```bash
cd /home/john/comfyui
source venv/bin/activate
python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

---

## 📁 File Locations

**Input videos:** `/home/john/comfyui/input/`
**Output videos:** `/home/john/comfyui/output/`
**Temp files:** `/home/john/comfyui/temp/`

---

## 🎯 Supported Formats

**Input:**
- MP4 (H.264)
- MOV
- AVI
- MKV
- WebM

**Output:**
- MP4 (H.264) - Recommended
- WebM
- GIF
- Image sequences

---

## 🔧 If Error Persists

### 1. Check the exact error message in ComfyUI
Look at the error details in the UI

### 2. Check ComfyUI terminal output
The terminal where ComfyUI is running will show detailed errors

### 3. Restart ComfyUI
```bash
pkill -f "python main.py"
cd /home/john/comfyui
./start_comfyui.sh
```

### 4. Reinstall VHS dependencies
```bash
cd /home/john/comfyui
source venv/bin/activate
pip install --upgrade imageio-ffmpeg opencv-python
```

---

## 📝 What to Tell Me

If VHS still errors, please provide:
1. **Exact error message** from ComfyUI
2. **What you're trying to do** (load/save video?)
3. **Video file format** (MP4, MOV, etc.)
4. **Any terminal output** showing the error

---

## ✅ Quick Fix Checklist

- [x] FFmpeg installed
- [x] imageio-ffmpeg installed
- [x] opencv-python installed
- [ ] Video file in correct folder?
- [ ] Video format supported?
- [ ] ComfyUI restarted after installing ffmpeg?

---

**FFmpeg is now installed. Try your VHS workflow again!**

If you still get an error, let me know the exact error message and I'll help you fix it.
