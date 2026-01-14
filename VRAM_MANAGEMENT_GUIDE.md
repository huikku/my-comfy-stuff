# VRAM Monitoring and Management Guide 🎮

## 📊 Available Tools

I've created several tools to help you monitor and manage VRAM on your NVIDIA Thor GPU:

### 1. Quick VRAM Check
```bash
cd /home/john/comfyui
./check_vram.sh
```
Shows current GPU status and utilization.

### 2. Clear VRAM Cache (Soft)
```bash
cd /home/john/comfyui
source venv/bin/activate
python clear_vram.py
```
Clears PyTorch cache without restarting ComfyUI. Good for freeing up unused memory.

### 3. Interactive VRAM Monitor
```bash
cd /home/john/comfyui
./vram_monitor.sh
```
Full interactive menu with options to:
- View VRAM status
- Clear PyTorch cache
- Restart ComfyUI
- Live monitoring
- View GPU processes

---

## 🚀 Quick Commands

### Check GPU Status
```bash
nvidia-smi
```

### Watch GPU in Real-Time
```bash
watch -n 1 nvidia-smi
```
Press `Ctrl+C` to exit

### Check ComfyUI Process
```bash
ps aux | grep "python main.py"
```

### Kill ComfyUI (Free All VRAM)
```bash
pkill -f "python main.py"
```

---

## 💡 VRAM Management Tips

### When to Clear VRAM:

1. **After Large Generations**
   - Run `python clear_vram.py` after processing large images/videos
   - Frees cached tensors

2. **Before Switching Workflows**
   - Clear cache before loading different models
   - Prevents memory fragmentation

3. **If You Get OOM Errors**
   - "Out of Memory" errors mean VRAM is full
   - Restart ComfyUI or clear cache

### VRAM Usage in ComfyUI:

Your NVIDIA Thor has **~125GB VRAM** which is massive! You should rarely run out, but:

- **Models**: 2-20GB each (depending on model)
- **Images**: Varies by resolution
- **Video**: Can use a lot for long sequences
- **Cached Data**: Accumulates over time

---

## 🔧 Troubleshooting

### "CUDA out of memory" Error

**Option 1: Clear Cache (Quick)**
```bash
cd /home/john/comfyui
source venv/bin/activate
python clear_vram.py
```

**Option 2: Restart ComfyUI (Full Clear)**
```bash
pkill -f "python main.py"
cd /home/john/comfyui
./start_comfyui.sh
```

**Option 3: Use ComfyUI's Built-in Options**
- In ComfyUI settings, enable "Low VRAM mode" (if available)
- Reduce batch sizes
- Process smaller images

### Check What's Using VRAM
```bash
nvidia-smi
```
Look at the "Processes" section at the bottom.

---

## 📈 Monitoring VRAM During Workflow

### Method 1: Terminal Window
Open a second terminal and run:
```bash
watch -n 1 nvidia-smi
```

### Method 2: Use the Interactive Monitor
```bash
cd /home/john/comfyui
./vram_monitor.sh
# Choose option 4 for live monitoring
```

---

## 🎯 Best Practices

### 1. Regular Cache Clearing
After processing large batches:
```bash
python /home/john/comfyui/clear_vram.py
```

### 2. Monitor During Heavy Workloads
Keep `nvidia-smi` running in a separate terminal when doing video processing or using multiple models.

### 3. Restart Periodically
If you're running ComfyUI for hours/days, restart it occasionally to fully clear memory:
```bash
pkill -f "python main.py" && cd /home/john/comfyui && ./start_comfyui.sh
```

### 4. Use Efficient Workflows
- Unload models when not needed
- Process in batches rather than all at once
- Use lower precision when possible (fp16 vs fp32)

---

## 📊 Understanding Your GPU

### NVIDIA Thor Specs:
- **VRAM**: ~125GB (shared with system RAM)
- **Architecture**: ARM-based
- **CUDA**: 13.0
- **Compute Capability**: sm_110

**Note**: Your Thor GPU shares memory with system RAM, so you have a massive pool available!

---

## 🛠️ Advanced: Python Script for Custom Monitoring

You can also use Python directly:

```python
import torch

# Check if CUDA is available
print(f"CUDA Available: {torch.cuda.is_available()}")

# Get device
device = torch.device('cuda:0')

# Check memory
allocated = torch.cuda.memory_allocated(device) / 1024**3
reserved = torch.cuda.memory_reserved(device) / 1024**3

print(f"Allocated: {allocated:.2f} GB")
print(f"Reserved: {reserved:.2f} GB")

# Clear cache
torch.cuda.empty_cache()
print("Cache cleared!")
```

---

## 📝 Quick Reference

| Command | Purpose |
|---------|---------|
| `./check_vram.sh` | Quick GPU status |
| `python clear_vram.py` | Clear PyTorch cache |
| `./vram_monitor.sh` | Interactive monitor |
| `nvidia-smi` | Full GPU info |
| `watch -n 1 nvidia-smi` | Live monitoring |
| `pkill -f "python main.py"` | Kill ComfyUI |

---

## 🆘 Emergency: System Frozen/Unresponsive

If your system becomes unresponsive due to VRAM issues:

1. **SSH from another computer** (if possible)
2. **Kill ComfyUI**: `pkill -f "python main.py"`
3. **Check processes**: `nvidia-smi`
4. **Reboot if needed**: `sudo reboot`

---

**Your VRAM management tools are ready!** 🚀

Start with `./check_vram.sh` for a quick check, or `./vram_monitor.sh` for full control.
