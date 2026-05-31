# FINAL CORRECT app.py BASED EXACTLY ON YOUR JUPYTER NOTEBOOK


from flask import Flask, render_template, request, send_from_directory
import numpy as np
import uuid
import os
import librosa
import joblib
import random
import subprocess

from collections import Counter

app = Flask(__name__)

# =========================================================
# MODEL
# =========================================================
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

            votes = [
                svm_pred[i],
                rf_pred[i],
                log_pred[i]
            ]

            final.append(
                Counter(votes).most_common(1)[0][0]
            )

        return np.array(final)

# =========================================================
# LOAD MODEL
# =========================================================
try:

    model = joblib.load("models/final_model.pkl")

except Exception as e:

    print("MODEL LOAD ERROR:", e)

    model = None

# =========================================================
# AUDIO INFO
# =========================================================
audio_info = {

    "Real Audio": {

        "analysis":
        "This audio appears to be natural and not AI-generated.",

        "recommendation":
        "Safe to use, but verify if the context is critical."
    },

    "Fake Audio": {

        "analysis":
        "This audio is likely AI-generated or manipulated.",

        "recommendation":
        "Verify the source before trusting this audio."
    }
}

# =========================================================
# ROUTES
# =========================================================
@app.route('/')
def landing():

    return render_template('landing.html')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/record')
def record():

    return render_template('record.html')


@app.route('/uploadaudio/<path:filename>')
def uploaded_audio(filename):

    return send_from_directory(
        './uploadaudio',
        filename
    )

def extract_features(file_path):
    """Hybrid feature extraction (MFCC + LFCC) matching notebook implementation."""
    # Load audio at its native sampling rate
    audio, sr = librosa.load(file_path, sr=None)

    # MFCC features (13 coefficients)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    mfcc_feature = np.mean(mfcc.T, axis=0)

    # LFCC approximation via MFCC of log-power spectrogram
    stft = np.abs(librosa.stft(audio))
    lfcc = librosa.feature.mfcc(S=librosa.power_to_db(stft**2), n_mfcc=13)
    lfcc_feature = np.mean(lfcc.T, axis=0)

    # Concatenate MFCC and LFCC into a single hybrid vector (26 dims)
    hybrid = np.concatenate((mfcc_feature, lfcc_feature))
    return hybrid.reshape(1, -1)
# =========================================================
# MODEL PREDICTION
# =========================================================
def model_predict(audio_path):

    try:

        if model is None:

            return "Error", "Model not loaded"

        # FEATURE EXTRACTION
        features = extract_features(audio_path)

        # Scale features once
        X_scaled = model.scaler.transform(features)

        # Individual classifier predictions
        svm_pred = model.svm.predict(X_scaled)
        rf_pred = model.rf.predict(X_scaled)
        log_pred = model.log.predict(X_scaled)

        # Majority‑vote prediction
        pred = Counter([svm_pred[0], rf_pred[0], log_pred[0]]).most_common(1)[0][0]

        # Compute probabilities for confidence (same as before)
        # SVM probability via sigmoid of decision function
        d_svm = model.svm.decision_function(X_scaled)[0]
        p_svm = 1 / (1 + np.exp(-d_svm))

        # Random Forest probability for class 1
        idx1 = list(model.rf.classes_).index(1)
        p_rf = model.rf.predict_proba(X_scaled)[0][idx1]

        # Logistic Regression probability for class 1
        idx1_log = list(model.log.classes_).index(1)
        p_log = model.log.predict_proba(X_scaled)[0][idx1_log]

        # Average probability for confidence (optional, can be tuned)
        avg_prob = (p_svm + p_rf + p_log) / 3.0
        print('DEBUG: avg_prob =', avg_prob)
        confidence = int(round((avg_prob if pred == 1 else 1 - avg_prob) * 100))
        confidence = max(50, min(100, confidence))

        # Determine label based on majority‑vote prediction
        if pred == 1:
            return "Fake Audio", confidence
        else:
            return "Real Audio", confidence

    except Exception as e:

        return "Error", str(e)

# =========================================================
# UPLOAD AUDIO
# =========================================================
@app.route('/upload/', methods=['POST'])
def upload_audio():

    if 'audio' not in request.files:

        return render_template(
            "home.html",
            error="No file uploaded"
        )

    audio = request.files['audio']

    if audio.filename == "":

        return render_template(
            "home.html",
            error="No selected file"
        )

    filename = audio.filename.lower()

    # =====================================================
    # ALLOWED FILES
    # =====================================================
    allowed_extensions = (
        ".wav",
        ".mp3",
        ".webm"
    )

    if not filename.endswith(allowed_extensions):

        return render_template(
            "home.html",
            error="Please upload .wav, .mp3 or .webm file"
        )

    os.makedirs("uploadaudio", exist_ok=True)

    # =====================================================
    # DIRECT WAV
    # =====================================================
    if filename.endswith(".wav"):

        temp_name = (
            f"uploadaudio/temp_{uuid.uuid4().hex}.wav"
        )

        audio.save(temp_name)

    # =====================================================
    # CONVERT MP3/WEBM → WAV
    # =====================================================
    else:

        input_ext = filename.split(".")[-1]

        input_path = (
            f"uploadaudio/temp_{uuid.uuid4().hex}.{input_ext}"
        )

        wav_path = (
            f"uploadaudio/temp_{uuid.uuid4().hex}.wav"
        )

        audio.save(input_path)

        try:

            subprocess.run(

                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    input_path,
                    wav_path
                ],

                check=True,

                stdout=subprocess.DEVNULL,

                stderr=subprocess.DEVNULL
            )

        except Exception as e:

            return render_template(
                "home.html",
                error=f"Audio conversion failed: {str(e)}"
            )

        temp_name = wav_path

    # =====================================================
    # MODEL PREDICTION
    # =====================================================
    label, confidence = model_predict(temp_name)

    if label == "Error":

        return render_template(
            "home.html",
            error=confidence
        )

    return render_template(

        'home.html',

        result=True,

        audiopath='/' + temp_name,

        prediction=label,

        confidence=confidence,

        analysis=audio_info[label]["analysis"],

        recommendation=audio_info[label]["recommendation"]
    )

# =========================================================
# RUN APP
# =========================================================
if __name__ == "__main__":

   app.run(
       host="0.0.0.0",
       port=5000,
       debug=True
   )

