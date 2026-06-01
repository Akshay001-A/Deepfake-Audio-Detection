<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020024,50:090979,100:00d4ff&height=250&section=header&text=Deepfake%20Audio%20Detection&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>

# 🎧 Deepfake Audio Detection

[![AI Powered](https://img.shields.io/badge/AI%20Powered-00e5ff?style=for-the-badge)](https://github.com/Akshay001-A/Deepfake-Audio-Detection)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Deepfake%20Detection-blue?style=for-the-badge)](https://github.com/Akshay001-A/Deepfake-Audio-Detection)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python)](https://www.python.org/)

--- 

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

# 🌟 Project Overview

Deepfake Audio Detection is an advanced AI-powered web application developed to identify whether an uploaded or recorded audio clip is:

- 🟢 **Authentic Human Voice**
- 🔴 **Synthetic / AI Generated Voice**

The system leverages:

✅ Machine Learning  
✅ Audio Signal Processing  
✅ MFCC & LFCC Feature Extraction  
✅ Real-Time Prediction Techniques  

to accurately classify audio authenticity.

This project was built with a modern dark-themed interface and provides seamless browser-based recording and upload functionality.

**Why choose this solution?**
- State‑of‑the‑art audio forensics.
- Fast inference on CPU.
- Easy deployment via Docker.
- Open‑source and extensible.


---

# ✨ Live Interface Preview

---

## 🏠 Home Page

Modern landing page with futuristic dark UI.

<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/homeD.png" width="100%"/>
---

## 📂 Upload Audio Detection

Upload or drag & drop audio files for instant prediction.

<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/upload.png" width="100%"/>
---

## 🟢 Real Audio Prediction Result

Displays confidence score and detailed analysis.

<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/real.png" width="100%"/>
---

## 🔴 Fake Audio Prediction Result

Detects AI-generated or manipulated audio.

<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/fake.png" width="100%"/>
---

## 🎤 Browser Audio Recording

Record audio directly from browser with playback support.

<img src="https://raw.githubusercontent.com/Akshay001-A/Deepfake-Audio-Detection/main/static/images/record.png" width="100%"/>
---

# 🎯 Main Features

---

## 🎧 Audio Deepfake Detection

**Key Features**
- **Real vs. Fake Classification** – Accurate distinction between authentic human voice and AI‑generated audio.
- **Confidence Scoring** – Provides a probability score for each prediction.
- **AI‑Generated Voice Detection** – Specialized models to spot synthetic speech artifacts.
- **In‑Browser Playback** – Seamless audio playback after upload or recording.
- **Detailed Analysis** – Offers actionable insights and recommendations.
- **Real‑Time Processing** – Near‑instant predictions for an interactive experience.

---

## 🎤 Browser Audio Recording

- **Record Directly** – Capture audio via the browser with a single click.
- **Pause / Resume** – Flexible control during the recording session.
- **Stop & Re‑record** – Easily discard and start over.
- **Download** – Save the captured WAV file locally.
- **Playback** – Immediate playback of the recorded clip.

---

## 📂 Audio Upload System

- **Drag & Drop** – Intuitive drop zone for rapid file uploads.
- **File Upload Button** – Classic browse‑and‑select option.
- **Supported Formats** – WAV, MP3, WEBM (auto‑converted to WAV via FFmpeg).
- **Instant Processing** – Real‑time prediction once the audio is uploaded.

---

## 🎨 Professional UI/UX

🌑 Futuristic Dark Theme  
📱 Responsive Design  
✨ Smooth Animations  
📋 Sidebar Navigation  
⚡ Interactive Interface  

---

# 🛠 Tech Stack

<div align="center">

| Category | Technologies |
|---|---|
| Backend | Flask, Python |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-learn |
| Audio Processing | Librosa, FFmpeg |
| Model Storage | Joblib |
| Feature Extraction | MFCC, LFCC |

</div>

---

# 🧠 Machine Learning Architecture

The system uses a **Hybrid Voting-Based Machine Learning Model** for improved prediction accuracy.

---

## 🤖 Models Used

### 🔹 Support Vector Machine (SVM)

### 🔹 Random Forest

### 🔹 Logistic Regression

These models are combined using:

# 🗳 Majority Voting Technique

to generate stable and reliable predictions.

---

# 🎼 Audio Feature Extraction

The application extracts powerful acoustic features from audio samples including:

✅ MFCC (Mel Frequency Cepstral Coefficients)  
✅ LFCC (Linear Frequency Cepstral Coefficients)  

These features help identify:

- Speech patterns
- Voice inconsistencies
- Frequency anomalies
- AI-generated artifacts

---

# 🎵 Supported Audio Formats

| Format | Support |
|---|---|
| WAV | ✅ |
| MP3 | ✅ |
| WEBM | ✅ |

---

# 🔄 Automatic Audio Conversion

The prediction model processes:

```text
.wav
```

format internally.

Uploaded audio formats such as:

```text
.mp3
.webm
```

are automatically converted into:

```text
.wav
```

using:

# 🎬 FFmpeg

for accurate prediction.

---

# ⚙️ FFmpeg Installation (Windows)

FFmpeg is required for:

✅ MP3 Support  
✅ WEBM Conversion  
✅ Browser Recording Processing  
✅ Audio Preprocessing  

---

## 📥 Download FFmpeg

🔗 https://www.gyan.dev/ffmpeg/builds/

Download:

```text
ffmpeg-release-essentials.zip
```

---

## 📦 Extract ZIP

Extract into:

```text
C:\ffmpeg
```

---

## 🌍 Add to Environment Variables

Add this path:

```text
C:\ffmpeg\bin
```

inside:

```text
Environment Variables → Path
```

---

## ✅ Verify Installation

Run:

```bash
ffmpeg -version
```

If installed correctly, version details will appear.

---

# 🚀 Quick Start

---

## 📥 Clone Repository

```bash
git clone https://github.com/Akshay001-A/Deepfake-Audio-Detection.git
```

---

## 📂 Open Project Folder

```bash
cd Deepfake-Audio-Detection
```

---

## 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

---

## 🚢 Docker Deployment

[![Docker Pulls](https://img.shields.io/docker/pulls/akshayauthentic/deepfake-audio-detect?style=for-the-badge)](https://hub.docker.com/r/akshayauthentic/deepfake-audio-detect)

Pull the pre‑built image from Docker Hub:

```bash
docker pull akshayauthentic/deepfake-audio-detect:latest
```

Run the container (exposes Flask on port 5000):

```bash
docker run -p 5000:5000 akshayauthentic/deepfake-audio-detect:latest
```

The application will be available at `http://localhost:5000`.

---

```bash
python app.py
```

---

## 🌐 Open Browser

```text
http://127.0.0.1:5000
```

---

# 📁 Project Structure

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

# 📦 Requirements

Main dependencies used:

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

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Enhancements

✅ Improve prediction accuracy  
🧠 Integrate CNN/LSTM Deep Learning Models  
☁ Deploy to Cloud Platform  
📱 Mobile Application Support  
🔐 User Authentication System  
🎵 Additional Audio Format Support  
🌍 Multi-language Audio Detection  

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. Ensure your code follows the existing style, includes documentation updates, and passes all tests.

## 📞 Contact

- GitHub: [Akshay001-A](https://github.com/Akshay001-A)
- LinkedIn: [Akshay Official](https://www.linkedin.com/in/akshayofficial0207)
- Instagram: [akshay_authentic](https://www.instagram.com/akshay_authentic)

---

# 👨‍💻 Author

<div align="center">

# Akshay R 🚀

<p align="center">
  <a href="https://github.com/Akshay001-A">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github"/>
  </a>

  <a href="https://www.linkedin.com/in/akshayofficial0207">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin"/>
  </a>

  <a href="https://www.instagram.com/akshay_authentic">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram"/>
  </a>
</p>

</div>

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

# ⭐ Thanks for Visiting This Project ⭐

### 🚀 If you found this project useful, don't forget to star the repository.

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3000&color=00F7FF&center=true&vCenter=true&width=700&lines=AI-Powered+Deepfake+Audio+Detection;Built+With+Python+%26+Machine+Learning;Made+by+Akshay+R"/>

</div>