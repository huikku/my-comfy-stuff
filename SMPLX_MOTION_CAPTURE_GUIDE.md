# SMPL-X Motion Capture Workflow

Human motion capture and match move tracking using WHAM + SMPL-X export.

## 📦 What's Included

### Workflow
- `smplx_motion_capture_v1.json` - Complete motion capture with SMPL-X parameter export

### Custom Node
- `ComfyUI-SMPLX-Export` - Save SMPL-X parameters and export meshes

## 🎯 What It Does

**Complete Pipeline:**
```
1. Load Video (VHS)
   ↓
2. Load WHAM Model
   ↓
3. Motion Capture (WHAM Inference)
   ↓
4. Save SMPL-X Parameters (.npz, .json, or .pkl)
   ↓
5. Save Visualization Video
```

**Outputs:**
- SMPL-X parameters (body_pose, global_orient, betas, transl)
- Visualization video showing tracked skeleton
- Compatible with official SMPL-X library

## 🚀 Quick Start

### 1. Install Dependencies

**Required ComfyUI nodes:**
```bash
# Already installed:
- ComfyUI-VideoHelperSuite (VHS)
- ComfyUI-WHAM
```

**Install SMPL-X library:**
```bash
cd /path/to/comfyui
source venv/bin/activate
pip install smplx
```

**Copy custom node:**
```bash
cp -r custom_nodes/ComfyUI-SMPLX-Export /path/to/comfyui/custom_nodes/
```

### 2. Download SMPL-X Models

**Get models from:** https://smpl-x.is.tue.mpg.de/

1. Register and download SMPL-X models
2. Extract to `/path/to/comfyui/models/smplx/`
3. Should have: `SMPLX_NEUTRAL.pkl`, `SMPLX_MALE.pkl`, `SMPLX_FEMALE.pkl`

### 3. Run Workflow

1. Open ComfyUI
2. Load `smplx_motion_capture_v1.json`
3. Set video path in "VHS_LoadVideoPath" node
4. Click "Queue Prompt"
5. Check output in `/path/to/comfyui/output/smplx/`

## 📊 Output Formats

### NPZ (NumPy Archive) - Recommended
```python
import numpy as np
data = np.load('motion_capture_20260114.npz')
body_pose = data['body_pose']      # (N, 63) - body joint rotations
global_orient = data['global_orient']  # (N, 3) - global orientation
betas = data['betas']              # (10,) - body shape parameters
transl = data['transl']            # (N, 3) - global translation
```

### JSON (Human Readable)
```json
{
  "body_pose": [[...], ...],
  "global_orient": [[...], ...],
  "betas": [...],
  "transl": [[...], ...]
}
```

### PKL (Pickle)
```python
import pickle
with open('motion_capture_20260114.pkl', 'rb') as f:
    data = pickle.load(f)
```

## 🎬 Using SMPL-X Parameters

### Load in Python
```python
import numpy as np
import smplx

# Load parameters
params = np.load('output/smplx/motion_capture_20260114.npz')

# Create SMPL-X model
model = smplx.create(
    model_path='models/smplx',
    model_type='smplx',
    gender='neutral',
)

# Generate mesh for frame 0
output = model(
    body_pose=torch.tensor(params['body_pose'][0:1]),
    global_orient=torch.tensor(params['global_orient'][0:1]),
    betas=torch.tensor(params['betas']),
    transl=torch.tensor(params['transl'][0:1]),
)

vertices = output.vertices.numpy()
```

### Export to Blender
```python
# Use the ExportSMPLXMesh node in ComfyUI
# Or export manually:
import trimesh

mesh = trimesh.Trimesh(vertices=vertices[0], faces=model.faces)
mesh.export('output.obj')
```

### Match Move in DCC Apps

**Blender:**
1. Install SMPL-X Blender addon
2. Import .npz parameters
3. Use for match move/animation

**Maya:**
1. Use SMPL-X Maya plugin
2. Import parameters
3. Retarget to rig

**Houdini:**
1. Import .obj sequence
2. Or use Python to load parameters
3. Apply to character rig

## 🔧 Custom Node Reference

### SaveSMPLXParams

**Inputs:**
- `smpl_params` (SMPL_PARAMS) - From WHAM Inference
- `filename_prefix` (STRING) - Output filename prefix
- `format` (COMBO) - npz, json, or pkl

**Outputs:**
- `file_path` (STRING) - Path to saved file

### ExportSMPLXMesh

**Inputs:**
- `smpl_params` (SMPL_PARAMS) - From WHAM Inference
- `model_path` (STRING) - Path to SMPL-X models
- `gender` (COMBO) - neutral, male, or female
- `filename_prefix` (STRING) - Output filename prefix
- `format` (COMBO) - obj, ply, or fbx
- `frame_index` (INT, optional) - Which frame to export

**Outputs:**
- `mesh_path` (STRING) - Path to exported mesh

## 📐 SMPL-X Parameters Explained

### body_pose (N, 63)
- 21 body joints × 3 rotation values
- Axis-angle representation
- Excludes hands and face

### global_orient (N, 3)
- Root orientation
- Axis-angle representation

### betas (10,)
- Body shape parameters
- PCA coefficients
- Same for all frames

### transl (N, 3)
- Global translation (x, y, z)
- World space position

## ⚙️ Advanced Usage

### Batch Export Meshes

Create workflow with loop:
```
For each frame:
  - ExportSMPLXMesh with frame_index
  - Saves mesh_0000.obj, mesh_0001.obj, etc.
```

### Custom SMPL-X Model

Modify `ExportSMPLXMesh` node:
```python
model = smplx.create(
    model_path='models/smplx',
    model_type='smplx',
    gender='neutral',
    use_face_contour=True,    # Include face
    use_pca=True,             # Use PCA for hands
    num_pca_comps=12,         # Hand PCA components
)
```

### Export with Hands and Face

WHAM outputs SMPL (body only). For full SMPL-X:
- Use different motion capture method
- Or manually add hand/face parameters

## 🎯 Use Cases

**Match Move:**
- Track actor in video
- Export SMPL-X parameters
- Import to Blender/Maya
- Retarget to character rig

**Animation Reference:**
- Capture reference motion
- Use as animation guide
- Blend with keyframe animation

**VFX:**
- Track human for CG replacement
- Generate collision geometry
- Lighting reference

**Mocap Cleanup:**
- Capture rough motion
- Clean up in DCC
- Export final animation

## 📊 Performance

**WHAM Inference:**
- Speed: ~5-10 fps (depends on GPU)
- VRAM: 4-8GB
- Resolution: 1920x1080 recommended

**Parameter Export:**
- Instant (< 1 second)
- File size: ~1-10MB per minute of video

**Mesh Export:**
- ~0.1 seconds per frame
- OBJ: ~5MB per frame
- PLY: ~3MB per frame

## 🔍 Troubleshooting

### "smplx library not installed"
```bash
cd /path/to/comfyui
source venv/bin/activate
pip install smplx
```

### "SMPL-X models not found"
- Download from https://smpl-x.is.tue.mpg.de/
- Extract to `models/smplx/`
- Check paths in ExportSMPLXMesh node

### "WHAM model not loading"
- WHAM models auto-download on first use
- Check internet connection
- Models stored in `models/wham/`

### Poor tracking quality
- Use higher resolution video (1080p+)
- Ensure good lighting
- Full body visible in frame
- Minimal motion blur

## 📚 Resources

**SMPL-X:**
- Official: https://smpl-x.is.tue.mpg.de/
- GitHub: https://github.com/vchoutas/smplx
- Paper: SMPL-X: A new joint 3D model of the human body, face and hands together

**WHAM:**
- Paper: World-Grounded Human Motion Recovery
- Outputs SMPL parameters (body only)

**ComfyUI:**
- WHAM Node: ComfyUI-WHAM
- VHS: ComfyUI-VideoHelperSuite

---

**Version:** 1.0  
**Date:** January 14, 2026  
**Author:** huikku

**Ready for human motion capture and match move tracking!** 🎬🎯
