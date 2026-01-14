# Synchronized Video Preview Playback in ComfyUI

## ✅ Built-in Solution: VideoHelperSuite (VHS)

You already have **ComfyUI-VideoHelperSuite** installed, which includes sync features!

---

## 🎬 How to Sync Video Previews (VHS)

### Method 1: Using VHS "Sync Preview" Feature

**In your workflow:**

1. **Load videos** using VHS "Load Video" nodes
2. **Enable "Sync preview"** option in the node settings
3. **All VHS preview nodes will sync** when you play/pause

**Steps:**
- Right-click on VHS Load Video node
- Look for "sync_preview" or similar option
- Enable it
- All VHS nodes will play in sync!

---

### Method 2: Using VHS Preview Controls

**VHS nodes have built-in controls:**
- ▶️ Play
- ⏸️ Pause
- ⏮️ Previous frame
- ⏭️ Next frame
- 🔁 Loop

**To sync multiple videos:**
1. Load all videos with VHS nodes
2. Use the same frame range settings
3. Enable sync mode in VHS settings

---

## 🎯 Advanced: Custom Sync Control

For more advanced control, here's what you can do:

### Option 1: Use Browser DevTools

Press **F12** in your browser and run this in Console:

```javascript
// Sync all video elements on the page
function syncAllVideos() {
    const videos = document.querySelectorAll('video');
    let mainVideo = videos[0];
    
    // Play/Pause all videos together
    window.playAllVideos = () => videos.forEach(v => v.play());
    window.pauseAllVideos = () => videos.forEach(v => v.pause());
    
    // Sync time to main video
    mainVideo.addEventListener('timeupdate', () => {
        videos.forEach((v, i) => {
            if (i > 0 && Math.abs(v.currentTime - mainVideo.currentTime) > 0.1) {
                v.currentTime = mainVideo.currentTime;
            }
        });
    });
    
    console.log(`Synced ${videos.length} videos!`);
    console.log('Use: playAllVideos() or pauseAllVideos()');
}

syncAllVideos();
```

Then use:
- `playAllVideos()` - Play all
- `pauseAllVideos()` - Pause all

---

### Option 2: Keyboard Shortcuts

**Create keyboard shortcuts for video control:**

```javascript
// Add to browser console
document.addEventListener('keydown', (e) => {
    const videos = document.querySelectorAll('video');
    
    if (e.key === ' ' && e.ctrlKey) {  // Ctrl+Space
        e.preventDefault();
        videos.forEach(v => v.paused ? v.play() : v.pause());
    }
    
    if (e.key === 'ArrowRight' && e.ctrlKey) {  // Ctrl+Right
        e.preventDefault();
        videos.forEach(v => v.currentTime += 1/30);  // Next frame (30fps)
    }
    
    if (e.key === 'ArrowLeft' && e.ctrlKey) {  // Ctrl+Left
        e.preventDefault();
        videos.forEach(v => v.currentTime -= 1/30);  // Previous frame
    }
});

console.log('Video shortcuts enabled!');
console.log('Ctrl+Space: Play/Pause all');
console.log('Ctrl+Right: Next frame');
console.log('Ctrl+Left: Previous frame');
```

---

## 🔧 VHS Settings for Sync

**In VHS Load Video node:**

1. **frame_load_cap** - Set same value for all videos
2. **skip_first_frames** - Set same value for all videos
3. **select_every_nth** - Set same value for all videos
4. **fps** - Make sure all videos have same FPS

**This ensures all videos:**
- Start at same frame
- Play at same speed
- Have same duration

---

## 📱 Using ComfyUI Manager

**Alternative approach:**

1. Open **ComfyUI Manager**
2. Search for "video preview" or "video player" nodes
3. Install nodes with sync features
4. Look for:
   - Video Player nodes
   - Preview sync nodes
   - Timeline control nodes

---

## 🎨 Workflow Tips

### For Side-by-Side Comparison:

1. **Load same video** in multiple VHS nodes
2. **Apply different processing** to each
3. **Use sync preview** to compare results frame-by-frame
4. **All previews play in sync**

### For Multi-Camera Sync:

1. **Load multiple camera angles**
2. **Set same frame range**
3. **Enable sync mode**
4. **Play all cameras simultaneously**

---

## 🚀 Quick Setup Guide

**Right now, try this:**

1. **Create a workflow** with 2+ VHS "Load Video" nodes
2. **Load videos** into each node
3. **Execute the workflow**
4. **Click play** on one video preview
5. **Check if others sync** (VHS may auto-sync)

**If they don't auto-sync:**
- Use the browser console method above
- Or check VHS node settings for sync option

---

## 📝 Feature Request

If you want native sync controls in ComfyUI:

1. **Open an issue** on ComfyUI-VideoHelperSuite GitHub
2. **Request:** "Global play/pause/sync controls for all video previews"
3. **Or use ComfyUI-Manager** to suggest the feature

---

## 💡 Recommended Workflow

**Best way to sync videos right now:**

1. ✅ Use VHS Load Video nodes
2. ✅ Set same frame range on all nodes
3. ✅ Use browser console sync script (above)
4. ✅ Create keyboard shortcuts for easy control

**This gives you:**
- Play/pause all videos
- Frame-by-frame control
- Synchronized playback
- Easy keyboard shortcuts

---

## 🎯 Summary

**You have 3 options:**

1. **VHS built-in sync** (easiest)
   - Already installed
   - Check node settings for sync option

2. **Browser console script** (most powerful)
   - Copy/paste JavaScript above
   - Full control over all videos

3. **Install additional nodes** (if needed)
   - Use ComfyUI Manager
   - Search for video player nodes

---

**Try the VHS sync feature first, then use the browser console script if you need more control!** 🎬✨
