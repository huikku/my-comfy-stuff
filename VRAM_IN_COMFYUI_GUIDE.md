# 🎮 VRAM Monitoring Inside ComfyUI - Setup Complete!

## ✅ Installed Components

I've installed two custom nodes that provide VRAM monitoring directly in ComfyUI:

### 1. **ComfyUI-Manager** ⭐ (Main Tool)
- Shows VRAM usage in the UI
- Provides system resource monitoring
- Manages custom nodes
- **Status:** Installed and Loaded ✓

### 2. **ComfyUI-Tooling-Nodes**
- Additional utility nodes
- System monitoring capabilities
- **Status:** Installed and Loaded ✓

---

## 🎯 How to See VRAM in ComfyUI

### Method 1: ComfyUI-Manager Button (Top Right)

1. **Open ComfyUI** in your browser: http://10.0.0.39:8188

2. **Look for the "Manager" button** in the top-right corner of the interface

3. **Click on "Manager"** - This opens the ComfyUI-Manager panel

4. **System Info Tab** - Shows:
   - GPU information
   - VRAM usage
   - System RAM
   - CPU usage

### Method 2: System Monitor (If Available)

Some versions show a small system monitor widget that displays:
- GPU utilization
- VRAM usage
- CPU usage

Look for it in the bottom-right or top-right corner.

---

## 📊 What You'll See

### In ComfyUI-Manager:

**GPU Information:**
- GPU Name: NVIDIA Thor
- Total VRAM: ~125GB
- Used VRAM: Updates in real-time
- Free VRAM: Available memory
- GPU Utilization: Percentage

**System Information:**
- CPU Usage
- System RAM
- Python version
- ComfyUI version

---

## 🔧 Additional Features

### ComfyUI-Manager Provides:

1. **Custom Node Management**
   - Install/uninstall custom nodes
   - Update custom nodes
   - Browse node registry

2. **Model Management**
   - Download models
   - Manage model files
   - Check missing models

3. **System Monitoring**
   - Real-time VRAM tracking
   - Performance metrics
   - Resource usage

4. **Workflow Management**
   - Install missing nodes for workflows
   - Check workflow compatibility

---

## 🚀 Quick Access

### To Open Manager:
1. Open ComfyUI: http://10.0.0.39:8188
2. Click **"Manager"** button (top-right)
3. Navigate to different tabs:
   - **Install Custom Nodes** - Browse and install nodes
   - **Install Models** - Download models
   - **System Info** - View VRAM and system stats

---

## 💡 Tips

### Monitor VRAM While Working:

1. **Keep Manager Open**
   - Open Manager panel
   - Go to System Info tab
   - Watch VRAM usage as you work

2. **Check Before Large Operations**
   - Before processing large images/videos
   - Check available VRAM
   - Adjust settings if needed

3. **Clear Cache When Needed**
   - If VRAM gets full
   - Use the terminal scripts:
     ```bash
     cd /home/john/comfyui
     source venv/bin/activate
     python clear_vram.py
     ```

---

## 🎨 Visual Indicators

### What to Look For:

**Green Zone (0-60% VRAM):**
- ✅ Plenty of memory
- Safe to run large workflows

**Yellow Zone (60-85% VRAM):**
- ⚠️ Getting full
- May want to clear cache soon

**Red Zone (85-100% VRAM):**
- 🔴 Nearly full
- Risk of OOM errors
- Clear cache or restart

---

## 🛠️ Troubleshooting

### Can't Find Manager Button?

1. **Refresh the page** (Ctrl+R or Cmd+R)
2. **Clear browser cache**
3. **Check if ComfyUI-Manager loaded:**
   - Look in terminal for "ComfyUI-Manager" in the startup logs
   - Should see: `0.1 seconds: /home/john/comfyui/custom_nodes/ComfyUI-Manager`

### Manager Not Showing VRAM?

Your NVIDIA Thor GPU might not report VRAM in the standard way. Use the terminal tools instead:
```bash
cd /home/john/comfyui
./check_vram.sh
```

---

## 📱 Alternative: Browser DevTools

You can also check VRAM via browser console:

1. Press **F12** to open DevTools
2. Go to **Console** tab
3. Type:
   ```javascript
   // This might show GPU info if available
   navigator.gpu
   ```

---

## 🎯 Best Workflow

### Recommended Setup:

1. **Main Monitor:** ComfyUI interface
2. **Second Monitor/Window:** Terminal with live VRAM:
   ```bash
   watch -n 1 nvidia-smi
   ```

Or use the interactive monitor:
```bash
cd /home/john/comfyui
./vram_monitor.sh
# Choose option 4 for live monitoring
```

---

## 📚 Summary

**In ComfyUI Interface:**
- ✅ ComfyUI-Manager button (top-right)
- ✅ System Info tab shows GPU stats
- ✅ Real-time monitoring

**In Terminal:**
- ✅ `./check_vram.sh` - Quick check
- ✅ `./vram_monitor.sh` - Interactive monitor
- ✅ `nvidia-smi` - Full GPU info
- ✅ `python clear_vram.py` - Clear cache

---

## 🚀 You're All Set!

**ComfyUI is now running with VRAM monitoring!**

Access it at: **http://10.0.0.39:8188**

Look for the **"Manager"** button in the top-right corner to see your GPU stats! 🎮✨
