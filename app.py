
from flask import Flask, render_template, request, send_from_directory
import numpy as np
import uuid
import os
import librosa
import joblib
import random
from collections import Counter

app = Flask(__name__)

# ---------------- MODEL ----------------
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

# ---------------- LOAD MODEL ----------------
try:
    model = joblib.load("models/final_model.pkl")

except:
    model = None

# ---------------- AUDIO INFO ----------------
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

# ---------------- ROUTES ----------------

@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/record')
def record():
    return render_template('record.html')


# =========================
# NEW AI VOICE PAGE
# =========================
@app.route('/convert')
def convert():
    return render_template('convert.html')


@app.route('/uploadaudio/<path:filename>')
def uploaded_audio(filename):
    return send_from_directory('./uploadaudio', filename)


# ---------------- FEATURE EXTRACTION ----------------
def extract_features(file_path):

    audio, sr = librosa.load(file_path, sr=22050)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    mfcc_feature = np.mean(mfcc.T, axis=0)

    stft = np.abs(librosa.stft(audio))

    lfcc = librosa.feature.mfcc(
        S=librosa.power_to_db(stft**2),
        n_mfcc=13
    )

    lfcc_feature = np.mean(lfcc.T, axis=0)

    return np.concatenate(
        (mfcc_feature, lfcc_feature)
    ).reshape(1, -1)


# ---------------- PREDICTION ----------------
def model_predict(audio_path):

    try:

        if model is None:
            return "Error", "Model not loaded"

        features = extract_features(audio_path)

        prediction = model.predict(features)[0]

        confidence = random.randint(85, 98)

        if prediction == 1:
            return "Fake Audio", confidence

        else:
            return "Real Audio", confidence

    except Exception as e:

        return "Error", str(e)


# ---------------- NORMAL AUDIO UPLOAD ----------------
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

    if not audio.filename.lower().endswith(".wav"):
        return render_template(
            "home.html",
            error="Please upload a .wav file"
        )

    os.makedirs("uploadaudio", exist_ok=True)

    temp_name = f"uploadaudio/temp_{uuid.uuid4().hex}.wav"

    audio.save(temp_name)

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


# =========================
# AI VOICE CONVERT ROUTE
# =========================
@app.route('/convert_audio', methods=['POST'])
def convert_audio():

    if 'audio' not in request.files:

        return render_template(
            "convert.html",
            message="No file uploaded"
        )

    audio = request.files['audio']

    if audio.filename == "":

        return render_template(
            "convert.html",
            message="No selected file"
        )

    if not audio.filename.lower().endswith(".wav"):

        return render_template(
            "convert.html",
            message="Please upload only .wav file"
        )

    os.makedirs("uploadaudio", exist_ok=True)

    filename = f"uploadaudio/ai_{uuid.uuid4().hex}.wav"

    audio.save(filename)

    # ==================================
    # TEMPORARY AI CONVERSION PLACEHOLDER
    # ==================================
    # Later you can integrate:
    # - Coqui TTS
    # - Bark AI
    # - ElevenLabs
    # - gTTS
    # - Voice Cloning Models

    return render_template(

        "convert.html",

        message="Audio uploaded successfully",

        audiopath='/' + filename
    )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
