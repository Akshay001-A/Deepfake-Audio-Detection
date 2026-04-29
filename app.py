from flask import Flask, render_template, request, send_from_directory
import numpy as np
import uuid
import os
import librosa
import joblib   # ✅ correct for .pkl

app = Flask(__name__)

# ✅ Load your hybrid ML modelfrom flask import Flask, render_template, request, send_from_directory
import numpy as np
import uuid
import os
import librosa
import joblib
from collections import Counter

app = Flask(__name__)

# 🔥 IMPORTANT: Define class BEFORE loading model
class HybridModel:
    def __init__(self, svm, rf, log, scaler):
        self.svm = svm
        self.rf = rf
        self.log = log
        self.scaler = scaler

    def predict(self, X):
        X = self.scaler.transform(X)

        svm_pred = self.svm.predict(X)
        rf_pred = self.rf.predict(X)
        log_pred = self.log.predict(X)

        final = []
        for i in range(len(svm_pred)):
            votes = [svm_pred[i], rf_pred[i], log_pred[i]]
            final.append(Counter(votes).most_common(1)[0][0])

        return np.array(final)

# ✅ Load model
model = joblib.load("models/final_model.pkl")

# INFO
audio_info = {
    "Real Audio": {
        "analysis": "This audio appears to be natural and not AI-generated.",
        "recommendation": "Safe to use, but verify if the context is critical."
    },
    "Fake Audio": {
        "analysis": "This audio is likely AI-generated or manipulated.",
        "recommendation": "Verify the source before trusting this audio."
    }
}

@app.route('/uploadaudio/<path:filename>')
def uploaded_audio(filename):
    return send_from_directory('./uploadaudio', filename)

@app.route('/')
def home():
    return render_template('home.html')

# 🔥 Feature Extraction (MATCHES TRAINING)
def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=22050)

    # MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    mfcc_feature = np.mean(mfcc.T, axis=0)

    # LFCC
    stft = np.abs(librosa.stft(audio))
    lfcc = librosa.feature.mfcc(
        S=librosa.power_to_db(stft**2),
        n_mfcc=13
    )
    lfcc_feature = np.mean(lfcc.T, axis=0)

    # Combine → 26 features
    hybrid = np.concatenate((mfcc_feature, lfcc_feature))

    return hybrid.reshape(1, -1)

# 🔥 Prediction
def model_predict(audio_path):
    try:
        features = extract_features(audio_path)
        prediction = model.predict(features)[0]

        if prediction == 1:
            return "Fake Audio", 100
        else:
            return "Real Audio", 100

    except Exception as e:
        return "Error", str(e)

@app.route('/upload/', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return "No file uploaded"

    audio = request.files['audio']

    if audio.filename == "":
        return "No selected file"

    # ✅ Only allow .wav
    if not audio.filename.lower().endswith(".wav"):
        return "Please upload a .wav file"

    os.makedirs("uploadaudio", exist_ok=True)

    temp_name = f"uploadaudio/temp_{uuid.uuid4().hex}.wav"
    audio.save(temp_name)

    label, confidence = model_predict(temp_name)

    # If error occurred
    if label == "Error":
        return f"Error processing audio: {confidence}"

    return render_template(
        'home.html',
        result=True,
        audiopath='/' + temp_name,
        prediction=label,
        confidence=confidence,
        analysis=audio_info[label]["analysis"],
        recommendation=audio_info[label]["recommendation"]
    )

if __name__ == "__main__":
    app.run(debug=True)
model = joblib.load("models/final_model.pkl")

# INFO
audio_info = {
    "Real Audio": {
        "analysis": "This audio appears to be natural and not AI-generated.",
        "recommendation": "Safe to use, but verify if the context is critical."
    },
    "Fake Audio": {
        "analysis": "This audio is likely AI-generated or manipulated.",
        "recommendation": "Verify the source before trusting this audio."
    }
}

@app.route('/uploadaudio/<path:filename>')
def uploaded_audio(filename):
    return send_from_directory('./uploadaudio', filename)

@app.route('/')
def home():
    return render_template('home.html')

# 🔥 YOUR ACTUAL TRAINING FEATURE LOGIC (IMPORTANT)
def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=22050)

    # MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    mfcc_feature = np.mean(mfcc.T, axis=0)

    # LFCC
    stft = np.abs(librosa.stft(audio))
    lfcc = librosa.feature.mfcc(
        S=librosa.power_to_db(stft**2),
        n_mfcc=13
    )
    lfcc_feature = np.mean(lfcc.T, axis=0)

    # Combine (26 features)
    hybrid = np.concatenate((mfcc_feature, lfcc_feature))

    return hybrid.reshape(1, -1)

# 🔥 Prediction
def model_predict(audio_path):
    features = extract_features(audio_path)

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "Fake Audio", 100
    else:
        return "Real Audio", 100

@app.route('/upload/', methods=['POST'])
def upload_audio():
    audio = request.files['audio']

    # accept only wav
    if not audio.filename.endswith(".wav"):
        return "Please upload a .wav file"

    os.makedirs("uploadaudio", exist_ok=True)

    temp_name = f"uploadaudio/temp_{uuid.uuid4().hex}.wav"
    audio.save(temp_name)

    label, confidence = model_predict(temp_name)

    return render_template(
        'home.html',
        result=True,
        audiopath='/' + temp_name,
        prediction=label,
        confidence=confidence,
        analysis=audio_info[label]["analysis"],
        recommendation=audio_info[label]["recommendation"]
    )

if __name__ == "__main__":
    app.run(debug=True)