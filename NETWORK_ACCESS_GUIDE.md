# Accessing ComfyUI from Other Computers on Your Network 🌐

## ✅ Your ComfyUI Server is Already Network-Ready!

ComfyUI is currently running with network access enabled (`--listen 0.0.0.0 --port 8188`).

---

## 🖥️ Your Server Information

**Server IP Address:** `10.0.0.39`
**ComfyUI Port:** `8188`

**Access URL:** `http://10.0.0.39:8188`

---

## 📱 How to Access from Other Computers

### From Any Computer on Your Network:

1. **Open a web browser** (Chrome, Firefox, Edge, Safari, etc.)
2. **Enter this URL in the address bar:**
   ```
   http://10.0.0.39:8188
   ```
3. **Press Enter** - ComfyUI should load!

### Supported Devices:
✅ Windows PC
✅ Mac
✅ Linux
✅ iPad/Tablet (with browser)
✅ Phone (works but small screen)

---

## 🔥 Quick Access Methods

### Option 1: Bookmark It
Save this URL as a bookmark in your browser:
```
http://10.0.0.39:8188
```

### Option 2: Create Desktop Shortcut

**On Windows:**
1. Right-click on Desktop → New → Shortcut
2. Enter location: `http://10.0.0.39:8188`
3. Name it: "ComfyUI Server"

**On Mac:**
1. Open the URL in Safari
2. File → Add to Dock
3. Or drag the URL to Desktop

**On Linux:**
Create a `.desktop` file:
```bash
cat > ~/Desktop/ComfyUI.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=ComfyUI Server
Exec=xdg-open http://10.0.0.39:8188
Icon=applications-internet
Terminal=false
EOF
chmod +x ~/Desktop/ComfyUI.desktop
```

---

## 🔍 Finding Your IP Address (If It Changes)

If your server's IP address changes, run this command on the server:

```bash
hostname -I | awk '{print $1}'
```

Or check your router's DHCP client list.

---

## 🛡️ Firewall Configuration

### Check if Firewall is Blocking (if you can't connect):

```bash
# Check firewall status
sudo ufw status

# If firewall is active and blocking, allow port 8188:
sudo ufw allow 8188/tcp
sudo ufw reload
```

---

## 🚀 Advanced: Set Static IP (Recommended)

To prevent your IP from changing, set a static IP on your server:

### Method 1: Via Router (Easiest)
1. Log into your router (usually `192.168.1.1` or `10.0.0.1`)
2. Find DHCP settings
3. Reserve IP `10.0.0.39` for this device's MAC address
4. Save settings

### Method 2: Via Network Manager (Ubuntu)
```bash
# Edit network connection
nmtui
# Select "Edit a connection"
# Choose your network interface
# Set IPv4 Configuration to "Manual"
# Add address: 10.0.0.39/24
# Gateway: 10.0.0.1 (your router)
# DNS: 8.8.8.8
# Save and activate
```

---

## 🌍 Access from Outside Your Network (Optional)

⚠️ **Security Warning:** Only do this if you understand the security implications!

### Option 1: Port Forwarding (Not Recommended for Production)
1. Log into your router
2. Set up port forwarding:
   - External Port: 8188
   - Internal IP: 10.0.0.39
   - Internal Port: 8188
   - Protocol: TCP
3. Access via your public IP: `http://YOUR_PUBLIC_IP:8188`

### Option 2: Tailscale/ZeroTier (Recommended)
Use a VPN service like Tailscale for secure remote access:
```bash
# Install Tailscale
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

### Option 3: Cloudflare Tunnel (Most Secure)
Set up a Cloudflare tunnel for secure HTTPS access without exposing ports.

---

## 🔧 Troubleshooting

### Can't Connect from Other Computer?

**1. Check if ComfyUI is running:**
```bash
# On the server, check if it's running:
curl http://localhost:8188
# Should return HTML
```

**2. Check if server is listening on network:**
```bash
# On the server:
sudo netstat -tulpn | grep 8188
# Should show: 0.0.0.0:8188
```

**3. Test from server itself:**
```bash
# On the server:
curl http://10.0.0.39:8188
# Should return HTML
```

**4. Check firewall:**
```bash
# On the server:
sudo ufw status
# If active, allow port 8188:
sudo ufw allow 8188/tcp
```

**5. Ping the server:**
```bash
# From the client computer:
ping 10.0.0.39
# Should get replies
```

**6. Check if both devices are on same network:**
- Both should have IPs in the same range (10.0.0.x)
- Connected to same WiFi/router

---

## 📊 Performance Tips

### For Best Performance Over Network:

1. **Use Wired Connection** - Ethernet is faster than WiFi
2. **Same Network Segment** - Keep devices on same subnet
3. **Quality Router** - Good router = better performance
4. **Reduce Image Sizes** - Smaller images = faster transfer
5. **Use Batch Processing** - Process multiple images at once

---

## 🎯 Common Use Cases

### Use Case 1: Work from Your Main PC
- Keep this server running 24/7
- Access from your main workstation
- Leverage the powerful GPU remotely

### Use Case 2: Multiple Users
- Share the server with team members
- Everyone accesses same ComfyUI instance
- Collaborative workflow development

### Use Case 3: Mobile Access
- Check generation progress from phone
- Start jobs remotely
- Download results on the go

---

## 📱 Mobile Browser Tips

When accessing from phone/tablet:
- Use landscape mode for better view
- Pinch to zoom on canvas
- Use "Request Desktop Site" if mobile view is weird
- Consider using a tablet for better experience

---

## 🔐 Security Recommendations

### For Local Network Use:
✅ Current setup is fine
✅ Only accessible from your local network
✅ No authentication needed for trusted network

### If Exposing to Internet:
⚠️ **Add authentication** (ComfyUI doesn't have built-in auth)
⚠️ **Use HTTPS** (set up reverse proxy with SSL)
⚠️ **Use VPN** instead of direct exposure
⚠️ **Firewall rules** to limit access

---

## 📝 Quick Reference Card

**Server IP:** `10.0.0.39`
**Port:** `8188`
**URL:** `http://10.0.0.39:8188`

**To check server IP:**
```bash
hostname -I | awk '{print $1}'
```

**To restart ComfyUI:**
```bash
cd /home/john/comfyui
./start_comfyui.sh
```

**To check if running:**
```bash
curl http://localhost:8188
```

---

## ✨ You're All Set!

Just open `http://10.0.0.39:8188` in any browser on your network and start using ComfyUI remotely!

**Pro Tip:** Bookmark this URL on all your devices for quick access! 🚀
