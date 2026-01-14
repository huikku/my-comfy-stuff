# Accessing Your PC's Google Drive from Linux 🚀

Since your work Google Drive is mounted on your PC, you can access it from your Linux system via network sharing!

## ✅ What You Need

1. **Your PC and Linux system on the same network** ✓
2. **Google Drive installed and running on your PC** ✓
3. **Share the Google Drive folder on your PC** (see below)

## 📋 Step-by-Step Setup

### Step 1: Share Google Drive Folder on Your PC

**On your Windows PC:**

1. Open **File Explorer**
2. Navigate to your Google Drive folder (usually `C:\Users\YourName\Google Drive` or `G:\My Drive`)
3. **Right-click** the folder → **Properties**
4. Go to the **Sharing** tab
5. Click **Advanced Sharing**
6. Check ✓ **Share this folder**
7. Note the share name (e.g., "Google Drive")
8. Click **Permissions** → Make sure your user has at least **Read** access
9. Click **OK** to save

**Alternative - Share via "Give access to":**
1. Right-click the Google Drive folder
2. Select **Give access to** → **Specific people**
3. Add your username
4. Set permission level (Read or Read/Write)
5. Click **Share**

### Step 2: Find Your PC's IP Address

**On your Windows PC:**

1. Press `Win + R`
2. Type `cmd` and press Enter
3. Type `ipconfig` and press Enter
4. Look for **IPv4 Address** under your active network adapter
5. Note it down (e.g., `192.168.1.100`)

### Step 3: Mount the Drive on Linux

**On your Linux system (this one):**

Run the helper script:
```bash
cd /home/john/comfyui
./mount_pc_drive.sh
```

The script will ask you for:
- Your PC's IP address
- The share name (e.g., "Google Drive" or "GoogleDrive")
- Your Windows username
- Your Windows password

## 🎯 Quick Manual Mount (Alternative)

If you prefer to mount manually:

```bash
# Create mount point
mkdir -p ~/GoogleDrive

# Mount the share (replace with your details)
sudo mount -t cifs //192.168.1.100/GoogleDrive ~/GoogleDrive \
    -o username=YourWindowsUser,password=YourPassword,uid=$(id -u),gid=$(id -g),vers=3.0
```

## 📂 Accessing Your Files

Once mounted, you can access your Google Drive at:
```bash
cd ~/GoogleDrive
ls ~/GoogleDrive
```

Or open in file manager:
```bash
xdg-open ~/GoogleDrive
```

## 🔄 Auto-Mount on Startup (Optional)

To automatically mount on boot, add to `/etc/fstab`:

```bash
# Create credentials file (more secure than putting password in fstab)
sudo nano /root/.smbcredentials
```

Add:
```
username=YourWindowsUser
password=YourWindowsPassword
```

Save and secure it:
```bash
sudo chmod 600 /root/.smbcredentials
```

Then add to `/etc/fstab`:
```bash
sudo nano /etc/fstab
```

Add this line (replace with your details):
```
//192.168.1.100/GoogleDrive /home/john/GoogleDrive cifs credentials=/root/.smbcredentials,uid=1000,gid=1000,vers=3.0 0 0
```

## 🔧 Troubleshooting

### Mount fails with "Permission denied"
- Check Windows username/password are correct
- Ensure the folder is properly shared on Windows
- Verify your user has permission to access the share

### Mount fails with "Host is down"
- Check PC IP address is correct: `ping 192.168.1.100`
- Ensure both devices are on the same network
- Check Windows firewall allows file sharing

### Mount fails with "Protocol negotiation failed"
Try different SMB versions:
- `vers=3.0` (default, most secure)
- `vers=2.1` (older Windows)
- `vers=2.0` (compatibility mode)
- `vers=1.0` (very old, not recommended)

### "Operation not permitted" errors
Add `noperm` option:
```bash
sudo mount -t cifs //PC_IP/ShareName ~/GoogleDrive \
    -o username=USER,password=PASS,uid=$(id -u),gid=$(id -g),noperm,vers=3.0
```

## 📤 Unmounting

When you're done:
```bash
sudo umount ~/GoogleDrive
```

## 💡 Benefits of This Approach

✅ No authentication issues with Meta/Google
✅ Uses your existing PC's Google Drive
✅ Works on the same network
✅ Full read/write access (if permissions allow)
✅ No additional software needed on Linux
✅ Can access all your work files

## 🎮 Using with ComfyUI

Once mounted, you can:
- Save ComfyUI outputs directly to `~/GoogleDrive/ComfyUI_Output/`
- Load models from `~/GoogleDrive/AI_Models/`
- Access any files from your work Google Drive

---

**Ready to set it up?** Run:
```bash
./mount_pc_drive.sh
```

And follow the prompts!
