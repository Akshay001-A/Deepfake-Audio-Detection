🎧 Deepfake Audio Detection








A Machine Learning-based web application that detects whether an audio file is Real or AI-generated (Deepfake) 🤖🎙️

Users can upload a .wav audio file, and the system predicts whether it is Real Audio ✅ or Fake Audio ❌ using a Hybrid Machine Learning model.

📑 Table of Contents
Features
Technologies Used
Quick Start
Model Info
Run the Application
Application Demo
Requirements
Author
Notes
Future Improvements
🚀 Features
📂 Upload .wav audio files
🎼 MFCC + LFCC feature extraction
🤖 Hybrid ML model (SVM + Random Forest + Logistic Regression)
🗳 Majority Voting prediction system
⚡ Real-time detection
📊 Confidence score display
🔊 Audio playback support
📄 Analysis & recommendation output
🎨 Clean and modern UI
🛠 Technologies Used
Python
Flask
Librosa
Scikit-learn
NumPy
HTML
CSS
JavaScript
⚡ Quick Start

Clone the repository:

git clone https://github.com/Akshay001-A/Deepfake-Audio-Detection.git

Navigate to the project folder:

cd Deepfake-Audio-Detection

Install dependencies:

pip install -r requirements.txt
🧠 Model Info

The trained model is included in this repository:

models/final_model.pkl
Model Approach
Support Vector Machine (SVM)
Random Forest
Logistic Regression
Majority Voting (Hybrid Model)
▶️ Run the Application

Start the Flask server:

python app.py

Open your browser:

http://127.0.0.1:5000
📷 Application Demo
🏠 Home Page

Upload .wav audio file

📊 Prediction Result

Displays:

🟢 Real / 🔴 Fake prediction
📈 Confidence score
🔊 Audio playback
📄 Analysis & recommendation
📦 Requirements
flask
numpy
librosa
scikit-learn
joblib

Install using:

pip install -r requirements.txt
👨‍💻 Author
Akshay R – https://github.com/Akshay001-A
💡 Notes
⚠️ Only .wav audio files are supported
📊 Confidence score is based on model predictions
🔄 Model performance may vary on unseen datasets
🎯 Future Improvements
🚀 Improve model accuracy
🧠 Integrate Deep Learning (CNN / LSTM)
🎧 Support additional audio formats
🌍 Deploy as a live web application

📄 License

This project is licensed under the MIT License.
See the LICENSE file for more details.