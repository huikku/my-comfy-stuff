# SMPL-X Motion Capture - Alternatives to WHAM

## ⚠️ Current Situation

**WHAM crashes on Thor GPU** with segmentation fault when loading models.

**You asked for:** SMPL-X format output for motion capture  
**WHAM was:** Just one way to get motion data  
**SMPL-X is:** The output format (not tied to WHAM)

---

## 🎯 What is SMPL-X?

**SMPL-X** is a 3D body model format from https://smpl-x.is.tue.mpg.de/

**It contains:**
- Body pose (21 joints)
- Hand pose (optional)
- Face expression (optional)
- Body shape parameters
- Global position/rotation

**It's used for:**
- Character animation
- Motion retargeting
- VFX match move
- Game animation

---

## 🔄 Alternative Motion Capture Methods

### Option 1: Use External Motion Capture

**Capture motion elsewhere, import to SMPL-X:**

1. **Rokoko Studio** (free)
   - Webcam-based mocap
   - Exports FBX/BVH
   - Convert to SMPL-X with Python

2. **DeepMotion** (web-based)
   - Upload video
   - Get FBX animation
   - Convert to SMPL-X

3. **Plask.ai** (AI mocap)
   - Video → 3D motion
   - Export FBX
   - Convert to SMPL-X

4. **Blender + Pose Estimation**
   - Use Blender addons
   - Manual cleanup
   - Export SMPL-X directly

---

### Option 2: Use Different ComfyUI Nodes

**Other pose estimation in ComfyUI:**

1. **OpenPose** (if available)
   - 2D pose detection
   - Convert to 3D with lifting
   - Export to SMPL-X

2. **MediaPipe** (lightweight)
   - Fast pose detection
   - Works on CPU
   - Can convert to SMPL-X

3. **Manual Keyframing**
   - Use Blender
   - Keyframe animation
   - Export SMPL-X parameters

---

### Option 3: Fix WHAM

**Debug the crash:**

```bash
# Check WHAM models
ls -la ~/.cache/wham/

# Try downloading models manually
# (WHAM may crash during auto-download)

# Check for DPVO (depth/pose/velocity optimization)
pip install dpvo

# Monitor memory during load
watch -n 1 nvidia-smi
```

**Possible issues:**
- Model download timeout
- Out of memory during init
- Thor GPU compatibility
- Missing DPVO library

---

### Option 4: Use SMPL-X Library Directly

**Create SMPL-X data from scratch:**

```python
import smplx
import torch

# Create SMPL-X model
model = smplx.create(
    model_path='models/smplx',
    model_type='smplx',
    gender='neutral',
)

# Manual pose parameters
body_pose = torch.zeros(1, 63)  # Neutral pose
global_orient = torch.zeros(1, 3)
betas = torch.zeros(1, 10)
transl = torch.zeros(1, 3)

# Generate mesh
output = model(
    body_pose=body_pose,
    global_orient=global_orient,
    betas=betas,
    transl=transl,
)

# Export
vertices = output.vertices.numpy()
# Save as OBJ, FBX, etc.
```

---

## 📊 Comparison

| Method | Pros | Cons | Quality |
|--------|------|------|---------|
| **WHAM** | Automatic, in ComfyUI | Crashes on Thor | High |
| **Rokoko** | Free, easy | External tool | Medium |
| **DeepMotion** | Web-based | Requires upload | High |
| **Plask.ai** | AI-powered | Paid for quality | High |
| **OpenPose** | Fast, CPU | 2D only | Medium |
| **Manual** | Full control | Time-consuming | Highest |

---

## 💡 Recommended Workflow

**For now (until WHAM is fixed):**

1. **Capture video** in ComfyUI (or use existing)

2. **Use external tool:**
   - Upload to DeepMotion or Plask
   - Or use Rokoko Studio
   - Get FBX/BVH animation

3. **Convert to SMPL-X:**
   ```python
   # Use conversion script
   python convert_fbx_to_smplx.py input.fbx output.npz
   ```

4. **Use SMPL-X data:**
   - Import to Blender
   - Retarget to character
   - Or use for match move

---

## 🔧 Quick Fix Attempts

**Try these to fix WHAM:**

```bash
# 1. Pre-download models
cd ~/.cache
mkdir -p wham
cd wham
# Download WHAM checkpoint manually
wget https://download.is.tue.mpg.de/wham/wham_vit_w_3dpw.pth.tar

# 2. Install DPVO
pip install dpvo

# 3. Increase memory limits
ulimit -s unlimited

# 4. Try CPU mode
# (Edit WHAM code to force CPU)
```

---

## 📚 Resources

**SMPL-X:**
- Official: https://smpl-x.is.tue.mpg.de/
- GitHub: https://github.com/vchoutas/smplx
- Paper: SMPL-X: A new joint 3D model

**External Tools:**
- Rokoko Studio: https://www.rokoko.com/
- DeepMotion: https://www.deepmotion.com/
- Plask: https://plask.ai/

**Conversion:**
- FBX to SMPL-X scripts available on GitHub
- Blender SMPL-X addon

---

## ✅ Summary

**SMPL-X = Output Format** (not tied to WHAM)

**WHAM = One method** to get motion data (currently broken)

**Alternatives:**
1. Use external mocap tools
2. Try different ComfyUI nodes
3. Fix WHAM crash
4. Manual animation in Blender

**For video inpainting:** Use the working workflows! They're great!

**For motion capture:** Need to either fix WHAM or use external tools

---

**The video inpainting workflows work perfectly - use those!** 🎬✨

**Motion capture needs alternative solution until WHAM is fixed.**
