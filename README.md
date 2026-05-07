<div align="center">

# 🎧 Deepfake Audio Detection 🚀


### 🧠 AI-Powered Audio Deepfake Detection System

Detect whether an audio file is:

## ✅ Real Audio  
## ❌ AI Generated / Deepfake Audio

🎤 Record Audio • 📂 Upload Audio • 📊 Get Predictions • 🔊 Listen to Audio

---

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/Machine_Learning-AI-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FFmpeg-Audio_Processing-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge"/>

</div>

---

# 📌 Project Overview

Deepfake Audio Detection is a Machine Learning-based web application that identifies whether uploaded or recorded audio is:

- 🟢 **Real Human Voice**
- 🔴 **AI Generated / Deepfake Voice**

The system uses a **Hybrid Machine Learning Model** trained using audio feature extraction techniques.

The project provides:

✨ Modern User Interface  
🎤 Browser Audio Recording  
📂 Drag & Drop Upload  
📊 Confidence Score Prediction  
🔊 Audio Playback  
⚡ Real-Time Processing  
🎼 Automatic Audio Conversion

---

# 🎯 Main Features

---

## 🎧 Deepfake Audio Detection

✅ Upload audio files  
✅ Predict Real or Fake audio  
✅ Confidence score display  
✅ Audio analysis output  
✅ Recommendation system  
✅ Real-time detection  

---

## 🎤 Browser Audio Recording

🎙 Record audio directly from browser  
⏸ Pause / Resume recording  
⏹ Stop recording  
🔄 Record again option  
📥 Download recorded audio  
🔊 Playback recorded audio  

---

## 📂 Upload System

📁 Drag & Drop Upload  
📤 File Upload Button  
🎵 WAV / MP3 / WEBM support  
🔄 Automatic audio conversion  
⚡ Fast processing system  

---

## 🎨 Modern UI

🌑 Dark themed design  
📱 Responsive layout  
📋 Sidebar navigation  
✨ Smooth animations  
⚡ User-friendly interface  

---

# 🛠 Technologies Used

<div align="center">

| Backend | Frontend | Audio Processing | ML |
|---|---|---|---|
| Flask | HTML | FFmpeg | Scikit-learn |
| Python | CSS | Librosa | SVM |
| Joblib | JavaScript | WAV Processing | Random Forest |
| NumPy | Responsive UI | Feature Extraction | Logistic Regression |

</div>

---

# 🧠 Machine Learning Model

---

## 📌 Model Used

The trained model is included inside:

```text
models/final_model.pkl
```

---

## 🤖 Hybrid Model Architecture

The prediction system combines:

### 🔹 Support Vector Machine (SVM)

### 🔹 Random Forest

### 🔹 Logistic Regression

using:

# 🗳 Majority Voting Technique

for improved prediction accuracy and stability.

---

# 🎼 Audio Feature Extraction

The system extracts:

✅ MFCC Features  
✅ LFCC Features  

from audio files before prediction.

---

# 🎵 Supported Audio Formats

The application supports:

| Format | Supported |
|---|---|
| WAV | ✅ |
| MP3 | ✅ |
| WEBM | ✅ |

---

# 🔄 Automatic Audio Conversion

The ML model works with:

```text
.wav
```

audio format.

So uploaded:

- `.mp3`
- `.webm`

files are automatically converted into:

```text
.wav
```

before prediction.

This conversion uses:

# 🎬 FFmpeg

---

# 🎤 Audio Recording Workflow

Browser recording generates:

```text
.webm
```

audio files.

The application automatically converts:

```text
.webm → .wav
```

before sending audio to the prediction model.

---

# 🎬 FFmpeg Installation Guide (Windows)

FFmpeg is required for:

✅ MP3 support  
✅ WEBM support  
✅ Browser recording conversion  
✅ Audio preprocessing  

without FFmpeg:

❌ MP3 and WEBM files cannot be processed.

---

## 📥 Step 1 — Download FFmpeg

Download from:

🔗 https://www.gyan.dev/ffmpeg/builds/

Download:

```text
ffmpeg-release-essentials.zip
```

---

## 📦 Step 2 — Extract ZIP

Extract to:

```text
C:\ffmpeg
```

---

## 📁 Step 3 — Verify Folder

Ensure:

```text
C:\ffmpeg\bin
```

contains:

```text
ffmpeg.exe
```

---

## 🌍 Step 4 — Add FFmpeg to Environment Variables

Open:

```text
Edit the system environment variables
```

Then:

```text
Environment Variables → Path → Edit → New
```

Add:

```text
C:\ffmpeg\bin
```

Save all changes.

---

## ✅ Step 5 — Verify Installation

Run:

```bash
ffmpeg -version
```

If installed correctly:

✅ FFmpeg version details will appear.

---

# ⚡ Quick Start

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

# ▶️ Run Application

Start Flask server:

```bash
python app.py
```

---

Open browser:

```text
http://127.0.0.1:5000
```

---

# 📷 Application Workflow

---

## 🏠 Home Page

✨ Upload audio  
✨ Drag & drop support  
✨ Sidebar navigation  
✨ Audio playback  

---

## 🎤 Record Page

🎙 Record voice  
⏸ Pause / Resume  
⏹ Stop recording  
📥 Download audio  

---

## 📊 Prediction Result

Displays:

🟢 Real Audio  
🔴 Fake Audio  
📈 Confidence Score  
🔊 Audio Playback  
📄 Analysis & Recommendation  

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
│   ├── index.html
│   ├── home.html
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

Main Python packages:

```text
flask
numpy
librosa
scikit-learn
joblib
soundfile
scipy
```

Install all using:

```bash
pip install -r requirements.txt
```

---

# 💡 Notes

⚠️ Best performance with clean audio files  
⚠️ FFmpeg required for MP3/WEBM support  
⚠️ Browser microphone permission required  
⚠️ Prediction accuracy may vary on unseen datasets  

---

# 🚀 Future Improvements

✅ Improve model accuracy  
🧠 Integrate Deep Learning (CNN / LSTM)  
🌍 Deploy as live web application  
📱 Mobile app integration  
☁ Cloud storage support  
🔐 User authentication system  
🎵 More audio format support  

---

# 👨‍💻 Author

<div align="center">

# Akshay R 🚀

🔗 GitHub:  
https://github.com/Akshay001-A

</div>

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more details.

---

<div align="center">

# ⭐ If you like this project, give it a star ⭐

<img src="https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif" width="200"/>

</div>