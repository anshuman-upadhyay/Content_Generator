# Content Generator

An automated Python pipeline that creates long-form videos, YouTube Shorts, and Instagram Reels using narration, subtitles, and gameplay footage.

This project automates the process of turning plain text into short-form content by combining:

- AI-generated narration
- Background music
- Random gameplay footage
- Auto subtitles
- Vertical formatting for reels/shorts
- Automatic short clip generation

---

## Features

✅ Reads script from text file  
✅ Converts text to speech using :contentReference[oaicite:1]{index=1} gTTS  
✅ Adds background music  
✅ Randomly selects gameplay footage  
✅ Extracts clip based on narration duration  
✅ Converts horizontal video → vertical format (9:16)  
✅ Generates subtitles using :contentReference[oaicite:2]{index=2}  
✅ Burns subtitles into final video  
✅ Splits final video into short clips  
✅ Automatically organizes outputs by run  
✅ Cleans temporary files after execution  

---

# Workflow

```text
input/script.txt
      ↓
TTS narration generation
      ↓
Background music mixing
      ↓
Random gameplay selection
      ↓
Random clip extraction
      ↓
Vertical video conversion
      ↓
Audio-video merge
      ↓
Subtitle generation
      ↓
Subtitle burning
      ↓
Short generation
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
│
├── output/
│   └── run_timestamp/
│       ├── long/
│       └── shorts/
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

Clone the repo:

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

# Required Inputs

### Script

Add your narration text inside:

```bash
input/script.txt
```

---

### Gameplay videos

Add gameplay videos inside:

```bash
raw_videos/
```

Example: :contentReference[oaicite:3]{index=3} parkour videos

---

### Background music

Add music file inside:

```bash
assets/
```

---

# Run the project

```bash
python main.py
```

---

# Output

Generated content gets stored in:

```bash
output/run_timestamp/
```

Inside:

- `long/` → Full final video  
- `shorts/` → Split short clips  

---

# Tech Stack

- Python  
- :contentReference[oaicite:4]{index=4}  
- :contentReference[oaicite:5]{index=5}  
- :contentReference[oaicite:6]{index=6} gTTS  

---

# Future Improvements

- Better voice cloning using :contentReference[oaicite:7]{index=7}  
- Auto script generation using :contentReference[oaicite:8]{index=8}  
- Auto upload to :contentReference[oaicite:9]{index=9}  
- Auto upload to :contentReference[oaicite:10]{index=10}  
- Better subtitle animations  
- Smarter gameplay cropping  

---

# Author

Anshuman Upadhyay

[GitHub Profile](https://github.com/anshuman-upadhyay?utm_source=chatgpt.com)