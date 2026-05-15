# Project Reels

An automated Python pipeline that transforms raw stories into ready-to-upload:

- YouTube long-form videos  
- YouTube Shorts  
- TikTok videos  
- Instagram Reels  

using fully local AI narration, subtitles, gameplay footage, story overlays, thumbnails, and automated post-processing.

This project automates the repetitive workflow of short-form storytelling content creation without paid APIs.

---

# Features

## Text Processing

✅ Reads stories from `input/raw_script.txt`  
✅ Cleans formatting issues automatically  
✅ Optional grammar correction using LanguageTool  
✅ Validates script length before processing  
✅ Saves cleaned output to `input/script.txt`  

---

## AI Narration

✅ Uses Kokoro ONNX for fully local narration  
✅ Random voice selection  
✅ No paid APIs required  
✅ Memory cleanup after generation  

---

## Audio Processing

✅ Random background music selection  
✅ Automatic volume balancing  
✅ Music looping  
✅ Audio trimming  

---

## Video Processing

✅ Random gameplay selection  
✅ Random clip extraction  
✅ Horizontal → vertical conversion (9:16)  
✅ Audio/video merging  
✅ Story overlay generation  
✅ Subtitle burning  
✅ Automatic Shorts splitting  

---

# Story Overlay System

Automatically generates:

✅ Rounded story cards  
✅ Shadow effects  
✅ Random fonts  
✅ Hook previews  
✅ Optimized positioning above subtitles  

---

# Subtitles

✅ Uses faster-whisper for subtitle generation  
✅ Automatically burns subtitles into final videos  

---

# Thumbnail Generation

✅ Auto-generates thumbnails for every run  

---

# Metadata Logging

Every run saves:

- gameplay used  
- music used  
- font used  
- voice used  
- script length  
- runtime metadata  

---

# Cleanup System

✅ Removes temporary files automatically  
✅ Handles failures gracefully  

---

# Full Workflow

```text
raw_script.txt
      ↓
Script Cleaning
      ↓
Script Validation
      ↓
Random Voice Selection
      ↓
Kokoro Narration
      ↓
Random Music Selection
      ↓
Audio Mixing
      ↓
Random Gameplay Selection
      ↓
Random Clip Extraction
      ↓
Vertical Conversion
      ↓
Audio + Video Merge
      ↓
Story Overlay
      ↓
Subtitle Generation
      ↓
Subtitle Burning
      ↓
Short Generation
      ↓
Thumbnail Generation
      ↓
Metadata Logging
      ↓
Cleanup
```

---

# Project Structure

```bash
Project_Reels/
│
├── assets/
│   ├── fonts/
│   ├── gameplay/
│   └── music/
│
├── input/
│   ├── raw_script.txt
│   ├── script.txt
│   └── config.json
│
├── models/
│   ├── kokoro-v1.0.onnx
│   └── voices-v1.0.bin
│
├── output/
│   └── run_timestamp/
│       ├── long/
│       ├── shorts/
│       ├── thumbnail.png
│       └── metadata.json
│
├── temp/
│
├── src/
│   ├── audio/
│   ├── pipeline/
│   ├── subtitles/
│   ├── text/
│   ├── utils/
│   └── video/
│
├── main.py
└── requirements.txt
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/anshuman-upadhyay/Project_Reels.git
cd Project_Reels
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

Download Kokoro ONNX model files from:

https://github.com/thewh1teagle/kokoro-onnx

Place inside:

```bash
models/
```

Required files:

- `kokoro-v1.0.onnx`
- `voices-v1.0.bin`

---

# Required Inputs

## Stories

Paste story content inside:

```bash
input/raw_script.txt
```

---

## Gameplay Videos

Add gameplay footage inside:

```bash
assets/gameplay/
```

Examples:

- Minecraft parkour  
- Subway Surfers  
- Satisfying clips  
- Loopable gameplay footage  

---

## Background Music

Add music files inside:

```bash
assets/music/
```

---

## Fonts

Add fonts inside:

```bash
assets/fonts/
```

---

# Run Project

```bash
python main.py
```

---

# Output

Each run creates:

```bash
output/run_timestamp/
```

Containing:

- final long-form video  
- short-form clips  
- thumbnail  
- metadata logs  

---

# Future V2 Ideas

- Reddit scraping automation  
- Automated upload system  
- Better thumbnail generation  
- AI-generated hooks  
- Multi-language narration  
- Analytics dashboard  
- Multi-niche expansion  

---

# Tech Stack

- Python  
- FFmpeg  
- Kokoro ONNX  
- faster-whisper  
- Pillow  
- LanguageTool