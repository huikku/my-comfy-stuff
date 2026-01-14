# Google Drive Setup with Rclone 🚀

Rclone v1.72.1 has been successfully installed on your system!

## What is Rclone?

Rclone is a powerful command-line tool that allows you to:
- Mount Google Drive as a local directory
- Sync files between your computer and Google Drive
- Access multiple cloud storage providers
- Work with Google Drive from the terminal or file manager

## Quick Setup Guide

### Step 1: Configure Rclone with Google Drive

Run the configuration wizard:
```bash
rclone config
```

Follow these steps in the wizard:
1. Type `n` for "New remote"
2. Name it `gdrive` (or any name you prefer)
3. Choose `drive` (Google Drive) from the list (usually option 18)
4. Press Enter for Client ID (leave blank for default)
5. Press Enter for Client Secret (leave blank for default)
6. Choose scope: `1` for full access to all files
7. Press Enter for root_folder_id (leave blank)
8. Press Enter for service_account_file (leave blank)
9. Type `n` for "Edit advanced config"
10. Type `y` for "Use web browser to automatically authenticate"
11. Follow the browser authentication flow
12. Type `n` for "Configure this as a Shared Drive"
13. Type `y` to confirm the configuration
14. Type `q` to quit the config

### Step 2: Mount Google Drive

Create a mount point directory:
```bash
mkdir -p ~/GoogleDrive
```

Mount Google Drive:
```bash
rclone mount gdrive: ~/GoogleDrive --vfs-cache-mode writes --daemon
```

Your Google Drive will now be accessible at `~/GoogleDrive`!

### Step 3: Access Your Files

You can now:
- Browse files: `ls ~/GoogleDrive`
- Open in file manager: `nautilus ~/GoogleDrive` or `xdg-open ~/GoogleDrive`
- Copy files: `cp myfile.txt ~/GoogleDrive/`
- Use it like any local folder!

## Common Rclone Commands

### Sync local folder to Google Drive
```bash
rclone sync /path/to/local/folder gdrive:FolderName
```

### Copy files from Google Drive to local
```bash
rclone copy gdrive:FolderName /path/to/local/folder
```

### List files in Google Drive
```bash
rclone ls gdrive:
```

### Check size of Google Drive
```bash
rclone size gdrive:
```

### Unmount Google Drive
```bash
fusermount -u ~/GoogleDrive
```

## Auto-Mount on Startup

To automatically mount Google Drive when you log in, create a systemd service:

```bash
mkdir -p ~/.config/systemd/user/
```

Create the service file `~/.config/systemd/user/rclone-gdrive.service`:
```ini
[Unit]
Description=RClone Google Drive Mount
After=network-online.target

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount gdrive: %h/GoogleDrive --vfs-cache-mode writes
ExecStop=/bin/fusermount -u %h/GoogleDrive
Restart=on-failure

[Install]
WantedBy=default.target
```

Enable and start the service:
```bash
systemctl --user enable rclone-gdrive.service
systemctl --user start rclone-gdrive.service
```

## Useful Mount Options

For better performance, you can use these options:
```bash
rclone mount gdrive: ~/GoogleDrive \
  --vfs-cache-mode writes \
  --vfs-cache-max-age 24h \
  --vfs-read-chunk-size 128M \
  --vfs-read-chunk-size-limit off \
  --buffer-size 256M \
  --daemon
```

## Troubleshooting

### Mount not working?
- Check if already mounted: `mount | grep GoogleDrive`
- Unmount first: `fusermount -u ~/GoogleDrive`
- Try mounting again

### Authentication issues?
- Re-run: `rclone config reconnect gdrive:`
- Or delete and recreate the remote: `rclone config`

### Check connection
```bash
rclone about gdrive:
```

## Alternative: GUI for Rclone

If you prefer a graphical interface, you can use:
```bash
rclone rcd --rc-web-gui
```

This will open a web-based GUI at http://localhost:5572

## Documentation

- Official Rclone docs: https://rclone.org/docs/
- Google Drive specific: https://rclone.org/drive/
- Mount command: https://rclone.org/commands/rclone_mount/

## Next Steps

1. Run `rclone config` to set up your Google Drive connection
2. Create the mount point: `mkdir -p ~/GoogleDrive`
3. Mount your drive: `rclone mount gdrive: ~/GoogleDrive --vfs-cache-mode writes --daemon`
4. Start using your Google Drive like a local folder!

---

**Note**: This is the best free solution for Google Drive on Linux. For a more native desktop experience with a GUI, consider paid options like Insync ($29.99 one-time payment).
