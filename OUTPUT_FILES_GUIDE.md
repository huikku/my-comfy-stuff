# ComfyUI Output Files - Where They Go

## 📁 Output Location

When you run ComfyUI from **any computer**, all generated files are saved on **this Thor DevKit system** at:

```
/home/john/comfyui/output/
```

**The output does NOT go to the computer you're browsing from!**

---

## 🌐 How It Works

### When You Access ComfyUI from Another Computer:

1. **You browse to:** http://10.0.0.39:8188 (from your PC/Mac)
2. **ComfyUI runs on:** Thor DevKit (10.0.0.39)
3. **Output saves to:** `/home/john/comfyui/output/` on Thor DevKit
4. **You can view in browser:** Images/videos show in the ComfyUI web interface
5. **To download:** Right-click image → Save, or use network share

---

## ✅ Best Ways to Access Output Files

### Option 1: Download from Browser ⭐ Easiest

**In ComfyUI web interface:**
- Generated images appear in the preview
- Right-click → "Save image as..."
- Downloads to your PC's Downloads folder

### Option 2: Network Share 🔥 Recommended

**Access the output folder directly from your PC:**

**Run this setup script:**
```bash
cd /home/john/comfyui
./setup_output_share.sh
```

**Then from Windows:**
1. Open File Explorer
2. Type in address bar: `\\10.0.0.39\ComfyUI-Output`
3. Enter username: `john`
4. Enter password (you'll set during setup)
5. Browse/copy files directly!

**From Mac:**
1. Finder → Go → Connect to Server
2. Enter: `smb://10.0.0.39/ComfyUI-Output`
3. Login with username: `john`
4. Access files!

### Option 3: SCP/SFTP (Advanced)

**Use file transfer tools:**
- **WinSCP** (Windows)
- **Cyberduck** (Mac/Windows)
- **FileZilla** (Any OS)

**Connection details:**
- Host: `10.0.0.39`
- Protocol: SFTP
- Username: `john`
- Path: `/home/john/comfyui/output/`

---

## 📂 Folder Structure

```
/home/john/comfyui/
├── input/          ← Put source images/videos here
├── output/         ← Generated files go here
├── models/         ← AI models
└── workflows/      ← Saved workflows
```

---

## 🎯 Workflow

### Typical Usage:

1. **Put input files** in `/home/john/comfyui/input/` (via network share)
2. **Open ComfyUI** from any computer: http://10.0.0.39:8188
3. **Run your workflow**
4. **Output saves** to `/home/john/comfyui/output/` on Thor
5. **Access output:**
   - View in browser
   - Download via right-click
   - Browse via network share

---

## 🚀 Quick Setup for Network Access

**Run this now to enable network share:**

```bash
cd /home/john/comfyui
./setup_output_share.sh
```

This will:
- ✅ Install Samba (network sharing)
- ✅ Share the `output` folder
- ✅ Share the `input` folder
- ✅ Set up password protection
- ✅ Enable access from Windows/Mac

**After setup, you can browse to:**
- `\\10.0.0.39\ComfyUI-Output` (Windows)
- `smb://10.0.0.39/ComfyUI-Output` (Mac)

---

## 💡 Pro Tips

### Automatic Download:
Some ComfyUI nodes have "auto-save" options that can:
- Save to specific folders
- Add timestamps to filenames
- Organize by workflow name

### Batch Processing:
- All outputs from a batch go to `/home/john/comfyui/output/`
- Files are numbered sequentially
- Easy to grab entire batch via network share

### Cloud Sync (Optional):
You could set up:
- Google Drive sync on the output folder
- Dropbox sync
- OneDrive sync
- Then files auto-upload to cloud!

---

## 📝 Summary

**Where output goes:** `/home/john/comfyui/output/` on Thor DevKit (10.0.0.39)

**Best way to access:**
1. Set up network share (run `./setup_output_share.sh`)
2. Browse from your PC: `\\10.0.0.39\ComfyUI-Output`
3. Copy files as needed!

**Alternative:** Download directly from ComfyUI web interface

---

**Run the setup script to enable easy file access from your other computers!** 📁✨
