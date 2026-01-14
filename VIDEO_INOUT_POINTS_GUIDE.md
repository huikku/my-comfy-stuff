# Video In/Out Points Guide

## Using VHS_SelectImages for Frame Selection

The SMPL-X workflow now includes a **VHS_SelectImages** node that lets you select specific frame ranges (in/out points).

---

## 📝 Frame Selection Syntax

### Basic Examples

**All frames:**
```
0:-1
```

**First 100 frames:**
```
0:100
```

**Frames 50 to 150:**
```
50:150
```

**Last 100 frames:**
```
-100:-1
```

**Skip first 30 frames, process rest:**
```
30:-1
```

---

## 🎬 Common Use Cases

### Trim Start and End
**Skip first 2 seconds and last 2 seconds (at 30fps):**
```
60:-60
```

### Process Middle Section
**Process frames 300-600:**
```
300:600
```

### Process First 10 Seconds
**At 30fps = 300 frames:**
```
0:300
```

### Skip Introduction
**Skip first 5 seconds (150 frames at 30fps):**
```
150:-1
```

---

## 🔢 Advanced Selection

### Multiple Ranges
**Frames 0-100 and 200-300:**
```
0:100, 200:300
```

### Every Nth Frame
**Every 2nd frame from 0-500:**
```
0:500:2
```

### Specific Frames
**Frames 10, 20, 30, 40:**
```
10, 20, 30, 40
```

---

## ⏱️ Time to Frame Conversion

### At 30 FPS:
- 1 second = 30 frames
- 10 seconds = 300 frames
- 1 minute = 1800 frames

### At 24 FPS:
- 1 second = 24 frames
- 10 seconds = 240 frames
- 1 minute = 1440 frames

### At 60 FPS:
- 1 second = 60 frames
- 10 seconds = 600 frames
- 1 minute = 3600 frames

---

## 📊 Examples by Time

### Process 30-second clip (30fps)
**Frames 0 to 900:**
```
0:900
```

### Skip first 10 seconds, process next 20 seconds (30fps)
**Frames 300 to 900:**
```
300:900
```

### Process last 15 seconds (30fps)
**Last 450 frames:**
```
-450:-1
```

---

## 🎯 Workflow Usage

### In ComfyUI:

1. **Load the workflow**
2. **Find the VHS_SelectImages node** (Node 2)
3. **Set the "indexes" field** with your frame range
4. **Examples:**
   - `0:-1` - All frames
   - `0:300` - First 10 seconds (at 30fps)
   - `100:400` - Frames 100-400
   - `60:-60` - Skip first/last 2 seconds

---

## 💡 Tips

**Check total frames first:**
- Load video in VHS_LoadVideoPath
- Check the frame_count output
- Then calculate your in/out points

**For precise editing:**
- Use video editing software to find exact frames
- Or use timecode: `(minutes * 60 + seconds) * fps`

**Example calculation:**
- Want to start at 1:30 (1 minute 30 seconds)
- At 30fps: `(1 * 60 + 30) * 30 = 2700`
- Use: `2700:-1`

---

## ⚠️ Important Notes

**Frame Indexing:**
- Starts at 0 (first frame is 0, not 1)
- Negative numbers count from end (-1 is last frame)

**Performance:**
- Selecting fewer frames = faster processing
- Use this to test on short clips first

**Memory:**
- Large frame ranges may use more VRAM
- If out of memory, reduce frame range

---

## 🔄 Quick Reference

| Goal | Syntax | Example (30fps) |
|------|--------|-----------------|
| All frames | `0:-1` | Full video |
| First N frames | `0:N` | `0:300` (10 sec) |
| Last N frames | `-N:-1` | `-300:-1` (last 10 sec) |
| Frame range | `START:END` | `300:600` (10-20 sec) |
| Skip start | `N:-1` | `150:-1` (skip 5 sec) |
| Skip start/end | `N:-N` | `60:-60` (skip 2 sec each) |

---

**Now you can precisely control which part of the video to process!** ⏱️✨
