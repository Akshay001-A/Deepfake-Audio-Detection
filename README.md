<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020024,50:090979,100:00d4ff&height=250&section=header&text=Deepfake%20Audio%20Detection&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>

# 🎧 Deepfake Audio Detection

### 🧠 AI-Powered Audio Deepfake Detection System

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-00e5ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Deepfake%20Detection-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python"/>
</p>

---

### 🚀 Detect Whether an Audio File is:

# ✅ Real Human Voice  
# ❌ AI Generated / Deepfake Audio

🎤 Record Audio • 📂 Upload Audio • 📊 Confidence Prediction • 🔊 Audio Playback

</div>

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

✅ Real vs Fake Audio Classification  
✅ Confidence Score Prediction  
✅ AI-generated Voice Detection  
✅ Audio Playback Support  
✅ Detection Analysis & Recommendations  
✅ Fast Real-Time Processing  

---

## 🎤 Browser Audio Recording

🎙 Record Audio Directly  
⏸ Pause / Resume Recording  
⏹ Stop Recording  
🔄 Record Again Option  
📥 Download Recorded Audio  
🔊 Built-in Audio Playback  

---

## 📂 Audio Upload System

📁 Drag & Drop Upload  
📤 File Upload Button  
🎵 WAV / MP3 / WEBM Support  
🔄 Automatic Audio Conversion  
⚡ Instant Audio Processing  

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

# ⭐ If You Like This Project, Give It a Star ⭐

<img src="https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif" width="220"/>

</div>