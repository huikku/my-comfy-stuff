# ComfyUI Network Access Troubleshooting Guide 🔧

## ✅ Server Status: RUNNING

**ComfyUI is running and accessible on the network!**

- **Server IP:** `10.0.0.39`
- **Port:** `8188`
- **Status:** Listening on all interfaces (0.0.0.0)
- **Firewall:** Inactive (not blocking)
- **Local Test:** ✅ Working

---

## 🔍 Troubleshooting Steps

### Step 1: Verify from Client Computer

**On the computer that can't connect, try these tests:**

#### Test 1: Ping the Server
```bash
ping 10.0.0.39
```
**Expected:** You should get replies
**If fails:** Network connectivity issue - check if both devices are on same network

#### Test 2: Check Port Connectivity
```bash
# Windows (PowerShell):
Test-NetConnection -ComputerName 10.0.0.39 -Port 8188

# Mac/Linux:
nc -zv 10.0.0.39 8188
# or
telnet 10.0.0.39 8188
```
**Expected:** Connection successful
**If fails:** Port is blocked somewhere

#### Test 3: Try with curl (if available)
```bash
curl http://10.0.0.39:8188
```
**Expected:** HTML response
**If fails:** HTTP issue

---

## 🌐 Browser-Specific Issues

### Try These URLs (in order):

1. **Primary:** `http://10.0.0.39:8188`
2. **With trailing slash:** `http://10.0.0.39:8188/`
3. **Explicit index:** `http://10.0.0.39:8188/index.html`

### Clear Browser Cache:
- **Chrome/Edge:** Ctrl+Shift+Delete → Clear cache
- **Firefox:** Ctrl+Shift+Delete → Clear cache
- **Safari:** Cmd+Option+E

### Try Different Browser:
- If Chrome doesn't work, try Firefox
- Try incognito/private mode
- Disable browser extensions

---

## 🔥 Common Issues & Solutions

### Issue 1: "This site can't be reached"
**Cause:** Network connectivity problem

**Solutions:**
1. Verify both computers are on same WiFi/network
2. Check client computer's IP (should be 10.0.0.x):
   ```bash
   # Windows: ipconfig
   # Mac/Linux: ip addr show
   ```
3. Restart router if needed
4. Try connecting client via Ethernet cable

### Issue 2: "Connection refused"
**Cause:** Port blocked or service not running

**Solutions:**
1. Verify ComfyUI is running on server:
   ```bash
   curl http://localhost:8188
   ```
2. Check if server firewall is blocking:
   ```bash
   sudo ufw status
   ```

### Issue 3: "Connection timed out"
**Cause:** Firewall or router blocking

**Solutions:**
1. **Check client firewall** (Windows Defender, etc.)
2. **Check router firewall:**
   - Log into router (usually 10.0.0.1 or 192.168.1.1)
   - Check if client isolation is enabled (disable it)
   - Check if AP isolation is enabled (disable it)
3. **Try from different network location**

### Issue 4: Page loads but shows errors
**Cause:** CORS or WebSocket issues

**Solutions:**
1. Check browser console (F12) for errors
2. Ensure you're using `http://` not `https://`
3. Check if antivirus is blocking WebSockets

---

## 🏠 Router-Specific Issues

### AP Isolation / Client Isolation
Some routers have "AP Isolation" or "Client Isolation" enabled, which prevents devices from talking to each other.

**To fix:**
1. Log into your router (usually `10.0.0.1` or `192.168.1.1`)
2. Look for:
   - "AP Isolation"
   - "Client Isolation"  
   - "Station Isolation"
   - "Wireless Isolation"
3. **Disable** this feature
4. Save and reboot router

### Guest Network
If your client is on a "Guest" network, it typically can't access devices on the main network.

**Solution:** Move client to main network

---

## 📱 Device-Specific Tips

### Windows Client:
```powershell
# Check if you can reach the server:
Test-NetConnection -ComputerName 10.0.0.39 -Port 8188

# Check your IP:
ipconfig

# Flush DNS:
ipconfig /flushdns
```

### Mac Client:
```bash
# Check connectivity:
nc -zv 10.0.0.39 8188

# Check your IP:
ifconfig | grep "inet "

# Flush DNS:
sudo dscacheutil -flushcache
```

### Linux Client:
```bash
# Check connectivity:
telnet 10.0.0.39 8188

# Check your IP:
ip addr show

# Test with curl:
curl -v http://10.0.0.39:8188
```

---

## 🔐 Advanced Diagnostics

### On the Server (this computer):

#### Check what's listening:
```bash
ss -tlnp | grep 8188
```
**Should show:** `0.0.0.0:8188` (listening on all interfaces)

#### Check ComfyUI logs:
```bash
# If running in background, check process:
ps aux | grep main.py

# Check if accessible locally:
curl http://localhost:8188
curl http://10.0.0.39:8188
```

#### Restart ComfyUI:
```bash
# Kill existing process:
pkill -f "python main.py"

# Start fresh:
cd /home/john/comfyui
./start_comfyui.sh
```

---

## 🌟 Alternative Access Methods

### Method 1: Use Server's Hostname
Instead of IP, try:
```
http://john-pc:8188
```
(Replace `john-pc` with actual hostname)

### Method 2: Use localhost tunnel (temporary test)
**On client computer:**
```bash
ssh -L 8188:localhost:8188 john@10.0.0.39
```
Then access: `http://localhost:8188`

### Method 3: Use VPN (Tailscale)
If local network is problematic, use Tailscale:
```bash
# Install on both computers:
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

# Access via Tailscale IP
```

---

## ✅ Quick Checklist

**On Server (10.0.0.39):**
- [ ] ComfyUI is running: `ps aux | grep main.py`
- [ ] Listening on 0.0.0.0:8188: `ss -tlnp | grep 8188`
- [ ] Firewall is off or allows 8188: `sudo ufw status`
- [ ] Can access locally: `curl http://localhost:8188`

**On Client Computer:**
- [ ] On same network (IP is 10.0.0.x)
- [ ] Can ping server: `ping 10.0.0.39`
- [ ] Can reach port: `telnet 10.0.0.39 8188`
- [ ] Tried different browser
- [ ] Cleared browser cache
- [ ] Disabled VPN/proxy

**On Router:**
- [ ] AP/Client Isolation is disabled
- [ ] Not on Guest network
- [ ] No firewall rules blocking

---

## 🆘 Still Not Working?

### Get Detailed Error Information:

**From client browser:**
1. Press F12 to open Developer Tools
2. Go to Console tab
3. Try loading the page
4. Share any red error messages

**From client command line:**
```bash
curl -v http://10.0.0.39:8188
```
Share the full output

---

## 📞 Quick Test Command

**Run this on the CLIENT computer:**
```bash
curl -v http://10.0.0.39:8188 2>&1 | grep -E "Connected|HTTP|error|refused|timeout"
```

**Expected output:**
```
* Connected to 10.0.0.39 (10.0.0.39) port 8188
> GET / HTTP/1.1
< HTTP/1.1 200 OK
```

**If you see "Connection refused":** Server not running or firewall blocking
**If you see "Connection timed out":** Network/router issue
**If you see "Could not resolve host":** DNS/network issue

---

## 🎯 Most Likely Causes (in order):

1. **AP Isolation enabled on router** (80% of cases)
2. **Client on different network/subnet**
3. **Client firewall blocking**
4. **Router firewall blocking**
5. **ComfyUI not actually running**

---

**Current Server Status:**
- ✅ ComfyUI is running
- ✅ Listening on 0.0.0.0:8188
- ✅ Firewall inactive
- ✅ Responding to local requests

**The server side is working correctly. The issue is likely on the client side or router.**
