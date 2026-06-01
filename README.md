# <div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020024,50:090979,100:00d4ff&height=250&section=header&text=Deepfake%20Audio%20Detection&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>

# 🎧 Deepfake Audio Detection

[![AI Powered](https://img.shields.io/badge/AI%20Powered-00e5ff?style=for-the-badge)](https://github.com/Akshay001-A/Deepfake-Audio-Detection)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Deepfake%20Detection-blue?style=for-the-badge)](https://github.com/Akshay001-A/Deepfake-Audio-Detection)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python)](https://www.python.org/)

</div>

---

## Table of Contents
- [Project Overview](#project-overview)
- [Why Choose This Solution?](#why-choose-this-solution)
- [Live Interface Preview](#live-interface-preview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Machine Learning Architecture](#machine-learning-architecture)
- [Supported Audio Formats & Conversion](#supported-audio-formats--conversion)
- [FFmpeg Installation (Windows)](#ffmpeg-installation-windows)
- [Quick Start](#quick-start)
- [Docker Deployment](#docker-deployment)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Author](#author)
- [Thanks](#thanks)

---

## Project Overview
Deepfake Audio Detection is an advanced AI‑powered web application designed to determine whether an uploaded or recorded audio clip is:
- 🟢 **Authentic Human Voice**
- 🔴 **Synthetic / AI Generated Voice**

The system leverages:
- ✅ Machine Learning
- ✅ Audio Signal Processing
- ✅ MFCC & LFCC Feature Extraction
- ✅ Real‑Time Prediction Techniques

It features a modern dark‑themed UI with seamless browser‑based recording and upload capabilities.

---

## Why Choose This Solution?
- State‑of‑the‑art audio forensics
- Fast inference on CPU
- Simple Docker deployment
- Open‑source and extensible

---

## Live Interface Preview
### Home Page
<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/homeD.png" width="100%"/>

### Upload Audio Detection
<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/upload.png" width="100%"/>

### Real Audio Prediction Result
<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/real.png" width="100%"/>

### Fake Audio Prediction Result
<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/fake.png" width="100%"/>

### Browser Audio Recording
<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/record.png" width="100%"/>

---

## Features
- **Real vs. Fake Classification** – Accurate distinction between authentic and AI‑generated speech.
- **Confidence Scoring** – Probability score for each prediction.
- **AI‑Generated Voice Detection** – Specialized models to spot synthetic speech artifacts.
- **In‑Browser Playback** – Seamless audio playback after upload or recording.
- **Detailed Analysis** – Actionable insights and recommendations.
- **Real‑Time Processing** – Near‑instant predictions for an interactive experience.
- **Browser Recording** – Record, pause, resume, re‑record, download, and playback within the browser.
- **Drag‑&‑Drop Upload** – Supports WAV, MP3, and WEBM (auto‑converted via FFmpeg).

---

## Tech Stack
<div align="center">
| Category | Technologies |
|---|---|
| Backend | Flask, Python |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit‑learn |
| Audio Processing | Librosa, FFmpeg |
| Model Storage | Joblib |
| Feature Extraction | MFCC, LFCC |
</div>

---

## Machine Learning Architecture
The system uses a **Hybrid Voting‑Based Model** that combines three classifiers:
- Support Vector Machine (SVM)
- Random Forest
- Logistic Regression

These models are merged via **majority voting** to produce stable, reliable predictions.

---

## Supported Audio Formats & Conversion
| Format | Support |
|---|---|
| WAV | ✅ |
| MP3 | ✅ |
| WEBM | ✅ |

All uploaded files are internally converted to **.wav** using **FFmpeg** before inference.

---

## FFmpeg Installation (Windows)
FFmpeg is required for MP3 support, WEBM conversion, and audio preprocessing.
1. Download from https://www.gyan.dev/ffmpeg/builds/ (choose `ffmpeg-release-essentials.zip`).
2. Extract to `C:\ffmpeg`.
3. Add `C:\ffmpeg\bin` to the system **PATH**.
4. Verify installation with `ffmpeg -version`.

---

## Quick Start
```bash
# Clone the repository
git clone https://github.com/Akshay001-A/Deepfake-Audio-Detection.git
cd Deepfake-Audio-Detection
# Install dependencies
pip install -r requirements.txt
# Run the application
python app.py
```
Open your browser at `http://127.0.0.1:5000`.

---

## Docker Deployment
[![Docker Pulls](https://img.shields.io/docker/pulls/akshayauthentic/deepfake-audio-detect?style=for-the-badge)](https://hub.docker.com/r/akshayauthentic/deepfake-audio-detect)
```bash
# Pull the image
docker pull akshayauthentic/deepfake-audio-detect:latest
# Run the container (exposes Flask on port 5000)
docker run -p 5000:5000 akshayauthentic/deepfake-audio-detect:latest
```
The app will be reachable at `http://localhost:5000`.

---

## Project Structure
```text
Deepfake-Audio-Detection/
│
├── models/
│   └── final_model.pkl
│
├── static/
│   ├── css/
│   ├── images/
│   ├── uploads/
│   └── recordings/
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── record.html
│   └── result.html
│
├── uploads/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Requirements
```text
flask
numpy
librosa
scikit-learn
joblib
soundfile
scipy
ffmpeg
```
Install them with `pip install -r requirements.txt`.

---

## Future Enhancements
- ✅ Improve prediction accuracy
- 🧠 Integrate CNN/LSTM deep‑learning models
- ☁ Deploy to cloud platforms
- 📱 Mobile application support
- 🔐 User authentication system
- 🎵 Additional audio format support
- 🌍 Multi‑language audio detection

---

## Contributing
Contributions are welcome! Fork the repo, create a feature branch, and submit a pull request. Ensure code follows the existing style, updates documentation, and passes all tests.

---

## License
This project is licensed under the **MIT License**.

---

## Contact
- GitHub: [Akshay001-A](https://github.com/Akshay001-A)
- LinkedIn: [Akshay Official](https://www.linkedin.com/in/akshayofficial0207)
- Instagram: [akshay_authentic](https://www.instagram.com/akshay_authentic)

---

## Author
<div align="center">
# Akshay R 🚀
<p align="center">
  <a href="https://github.com/Akshay001-A"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github"/></a>
  <a href="https://www.linkedin.com/in/akshayofficial0207"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin"/></a>
  <a href="https://www.instagram.com/akshay_authentic"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram"/></a>
</p>
</div>

---

## Thanks
<div align="center">
# ⭐ Thanks for Visiting This Project ⭐
### 🚀 If you found this project useful, don't forget to star the repository.
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3000&color=00F7FF&center=true&vCenter=true&width=700&lines=AI-Powered+Deepfake+Audio+Detection;Built+With+Python+%26+Machine+Learning;Made+by+Akshay+R"/>
</div>