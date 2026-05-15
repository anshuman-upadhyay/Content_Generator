# Content Generator

An automated Python pipeline that converts plain text into long-form videos, YouTube Shorts, and Instagram Reels using AI narration, subtitles, and gameplay footage.

This project automates the repetitive workflow of creating short-form content by combining:

- AI narration generation
- Background music mixing
- Random gameplay footage selection
- Automatic subtitles
- Vertical formatting for reels/shorts
- Automatic short clip generation

---

# Features

✅ Reads script from text file  
✅ Converts text to speech using Kokoro ONNX  
✅ Adds background music  
✅ Randomly selects gameplay footage  
✅ Extracts random clip based on narration duration  
✅ Converts horizontal video → vertical format (9:16)  
✅ Generates subtitles using faster-whisper  
✅ Burns subtitles into final video  
✅ Splits final video into short clips  
✅ Organizes outputs by timestamped runs  
✅ Cleans temporary files automatically  
✅ Handles failures gracefully with cleanup system  

---

# Workflow

```text
input/script.txt
      ↓
Read Script
      ↓
Kokoro TTS Narration
      ↓
Background Music Mixing
      ↓
Random Gameplay Selection
      ↓
Random Clip Extraction
      ↓
Vertical Video Conversion
      ↓
Audio + Video Merge
      ↓
Subtitle Generation
      ↓
Subtitle Burning
      ↓
Short Generation
      ↓
Cleanup
```

---

# Project Structure

```bash
Content_Generator/
│
├── input/
│   ├── script.txt
│   └── config.json
│
├── raw_videos/
│
├── assets/
│   ├── music.mp3
│   └── reference_voice.wav
│
├── models/
│   ├── kokoro-v1.0.onnx
│   └── voices-v1.0.bin
│
├── output/
│   └── run_timestamp/
│       ├── long/
│       └── shorts/
│
├── temp/
│
├── src/
│   ├── audio/
│   ├── subtitles/
│   ├── text/
│   ├── utils/
│   ├── video/
│   └── pipeline/
│
├── tests/
├── main.py
└── requirements.txt
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/anshuman-upadhyay/Content_Generator.git
cd Content_Generator
```

Create virtual environment:

```bash
python3 -m venv short
source short/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Model Setup

Download Kokoro model files and place them inside:

```bash
models/
```

Required files:

- `kokoro-v1.0.onnx`
- `voices-v1.0.bin`

For Kokoro ONNX:

[Kokoro ONNX GitHub](https://github.com/thewh1teagle/kokoro-onnx?utm_source=chatgpt.com)

---

# Required Inputs

## Script

Add narration text:

```bash
input/script.txt
```

---

## Gameplay Videos

Add gameplay clips inside:

```bash
raw_videos/
```

Example:

- :contentReference[oaicite:3]{index=3} parkour gameplay
- satisfying gameplay footage
- looping gameplay clips

---

## Background Music

Add music file:

```bash
assets/music.mp3
```

---

# Run Project

```bash
python main.py
```

---

# Output

Generated content is stored in:

```bash
output/run_timestamp/
```

Structure:

```bash
output/
└── run_timestamp/
    ├── long/
    │   └── Finalize_work.mp4
    │
    └── shorts/
        ├── short_1.mp4
        ├── short_2.mp4
        └── short_n.mp4
```

---

# Tech Stack

- Python  
- :contentReference[oaicite:4]{index=4}  
- :contentReference[oaicite:5]{index=5}  
- :contentReference[oaicite:6]{index=6}  
- :contentReference[oaicite:7]{index=7}  

---

# Current Limitations

- Manual script input  
- Manual gameplay sourcing  
- Manual uploads to platforms  
- Fixed subtitle styling  
- Fixed vertical crop logic  

---

# Future Improvements

- Voice cloning support  
- AI script generation using :contentReference[oaicite:8]{index=8}  
- Auto upload to :contentReference[oaicite:9]{index=9}  
- Auto upload to :contentReference[oaicite:10]{index=10}  
- Better subtitle animations  
- Smarter gameplay cropping  
- Web dashboard for one-click generation  

---

# Author

**Anshuman Upadhyay**

GitHub: [Anshuman Upadhyay GitHub](https://github.com/anshuman-upadhyay?utm_source=chatgpt.com)