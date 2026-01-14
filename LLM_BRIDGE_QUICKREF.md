# Quick Reference - ComfyUI LLM Bridge

## ✅ Setup Complete!

### Directory Structure:
```
/home/john/comfyui/
├── .agent/                    # AI rules & workflows
│   ├── rules/comfyui.md
│   └── workflows/comfyui.md
│
├── nodes/                     # Node definitions (symlink)
│   ├── core.txt              # 269 essential nodes
│   ├── video.txt             # 95 video nodes
│   ├── segmentation.txt      # 45 masking nodes (SAM2/3, RMBG)
│   ├── api.txt               # 136 API nodes
│   ├── advanced.txt          # 135 advanced nodes
│   ├── 3d.txt                # 17 3D nodes
│   ├── training.txt          # 33 training nodes
│   └── full.txt              # 828 all nodes
│
└── refresh-nodes.py          # Refresh script (top level!)
```

---

## 🚀 Quick Commands

### Refresh Node Definitions
```bash
cd /home/john/comfyui
python refresh-nodes.py
```

**Run this after:**
- Installing new custom nodes
- Updating ComfyUI
- Before generating workflows

---

## 📊 What's Indexed

**Total: 792 nodes**

**Your custom nodes included:**
- ✅ SAM2, SAM3 (segmentation)
- ✅ RMBG (background removal)
- ✅ DepthAnythingV2/V3
- ✅ VideoHelperSuite (VHS)
- ✅ ProPainter
- ✅ Temporal Mask Tools
- ✅ Feathered Inpaint
- ✅ VRAM Monitor
- ✅ rgthree-comfy (48 nodes)
- ✅ All ComfyUI core nodes

---

## 🤖 AI Workflow Generation

**Use the `/comfyui` workflow to:**
1. Generate ComfyUI workflows from descriptions
2. AI reads appropriate node definitions
3. Creates valid workflow JSON
4. Uses only installed nodes

**Example:**
```
"Create a workflow to remove a person from video"

AI will:
1. Read nodes/segmentation.txt (SAM3, RMBG)
2. Read nodes/video.txt (VHS, ProPainter)
3. Generate complete workflow JSON
4. Validate all connections
```

---

## 📁 Files Location

**Everything is in the top level now:**
- `/home/john/comfyui/.agent/` - Rules & workflows
- `/home/john/comfyui/nodes/` - Node definitions
- `/home/john/comfyui/refresh-nodes.py` - Refresh script

**Easy to access and use!** ✨
