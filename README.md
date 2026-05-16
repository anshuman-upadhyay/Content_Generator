# Project Reels

An automated AI-powered content pipeline that transforms raw stories into ready-to-upload:

- YouTube Long Videos  
- YouTube Shorts  
- TikTok Videos  
- Instagram Reels  

using fully local narration, subtitles, gameplay footage, dynamic overlays, premium thumbnails, metadata logging, and automated cleanup.

Built to automate short-form storytelling content creation workflows completely locally.

---

# Features

## Smart Story Processing

✅ Reads raw stories from `input/raw_script.txt`  

✅ Automatically splits raw stories into:

- Title  
- Story Content  

and stores them inside:

```bash
input/script.json
```

Example:

```json
{
  "title": "AITA for exposing my cheating boyfriend?",
  "content": "He lied to me for months..."
}
```

---

## Text Cleaning

✅ Fixes punctuation issues  
✅ Removes formatting problems  
✅ Optional grammar correction using LanguageTool  
✅ Cleans title and content separately  

---

## AI Narration

✅ Uses Kokoro ONNX for local narration generation  

✅ Random voice selection  

✅ No paid APIs required  

---

## Subtitle Generation

✅ Uses faster-whisper for subtitle generation  

✅ Burns subtitles directly into final videos  

---

## Video Pipeline

✅ Random gameplay selection  

✅ Random clip extraction  

✅ Auto vertical formatting (9:16)  

✅ Audio/video merging  

✅ Dynamic story title overlays  

✅ Short splitting  

---

## Story Overlay System

Uses only story titles for cleaner retention:

```text
🔥 STORY TIME
AITA for exposing my cheating boyfriend?
```

No more large text blocks.

---

## Premium Thumbnail Generation

✅ Mobile-friendly vertical thumbnails  

✅ Dynamic white title cards  

✅ Auto-generated:

- PART 1  
- PART 2  
- FULL STORY  

✅ Premium custom background design  

---

## Audio Processing

✅ Random background music selection  

✅ Audio balancing  

✅ Audio looping  

---

## Metadata Logging

Every run stores:

- selected gameplay  
- selected music  
- selected voice  
- selected font  
- runtime metadata  

---

## Cleanup System

Automatically removes:

- narration files  
- subtitles  
- temporary clips  
- overlay assets  
- script.json  
- raw script text  

after pipeline completion.

---

# Full Workflow

```text
raw_script.txt
      ↓
Split Raw Script
      ↓
script.json
      ↓
Clean Title + Content
      ↓
Title → Overlay + Thumbnail
Content → Narration + Subtitles
      ↓
Random Gameplay Selection
      ↓
Audio/Video Merge
      ↓
Short Generation
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
│   ├── backgrounds/
│   ├── fonts/
│   ├── gameplay/
│   └── music/
│
├── input/
│   ├── raw_script.txt
│   ├── script.json
│   └── config.json
│
├── models/
│   ├── kokoro-v1.0.onnx
│   └── voices-v1.0.bin
│
├── output/
│   └── run_timestamp/
│
├── temp/
│
├── src/
│   ├── audio/
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

Clone repo:

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

Download Kokoro model files:

https://github.com/thewh1teagle/kokoro-onnx

Place inside:

```bash
models/
```

Required files:

- kokoro-v1.0.onnx  
- voices-v1.0.bin  

---

# Required Inputs

## Story

Paste story into:

```bash
input/raw_script.txt
```

Format:

```text
AITA for exposing my cheating boyfriend?

He lied to me for months...
```

---

## Gameplay Clips

Add gameplay videos inside:

```bash
assets/gameplay/
```

Examples:

- Minecraft Parkour  
- Subway Surfers  
- Satisfying videos  

---

## Music

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

Each run generates:

- Long-form video  
- Shorts  
- Thumbnails  
- Metadata logs  

inside:

```bash
output/run_timestamp/
```

---

# Tech Stack

- Python  
- FFmpeg  
- Kokoro ONNX  
- faster-whisper  
- Pillow  
- LanguageTool  

---

# Future V2 Ideas

- Reddit scraping automation  
- Auto uploads  
- AI hook generation  
- Analytics dashboard  
- Multi-niche expansion  