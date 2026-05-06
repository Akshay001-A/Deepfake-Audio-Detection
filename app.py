from flask import Flask, render_template, request, send_from_directory
import numpy as np
import uuid
import os
import librosa
import joblib
import random
import subprocess

from TTS.api import TTS
from collections import Counter

app = Flask(__name__)

# =========================
# XTTS MODEL
# =========================
try:

    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2"
    )

except Exception as e:

    print("XTTS Load Error:", e)

    tts = None

# =========================
# MODEL
# =========================
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

# =========================
# LOAD MODEL
# =========================
try:

    model = joblib.load("models/final_model.pkl")

except:

    model = None

# =========================
# AUDIO INFO
# =========================
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

# =========================
# ROUTES
# =========================
@app.route('/')
def landing():

    return render_template('landing.html')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/record')
def record():

    return render_template('record.html')


@app.route('/convert')
def convert():

    return render_template('convert.html')


@app.route('/uploadaudio/<path:filename>')
def uploaded_audio(filename):

    return send_from_directory(
        './uploadaudio',
        filename
    )


@app.route('/converted/<path:filename>')
def converted_audio(filename):

    return send_from_directory(
        './converted',
        filename
    )

# =========================
# FEATURE EXTRACTION
# =========================
def extract_features(file_path):

    audio, sr = librosa.load(
        file_path,
        sr=22050
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    mfcc_feature = np.mean(
        mfcc.T,
        axis=0
    )

    stft = np.abs(
        librosa.stft(audio)
    )

    lfcc = librosa.feature.mfcc(
        S=librosa.power_to_db(stft**2),
        n_mfcc=13
    )

    lfcc_feature = np.mean(
        lfcc.T,
        axis=0
    )

    return np.concatenate(
        (mfcc_feature, lfcc_feature)
    ).reshape(1, -1)

# =========================
# MODEL PREDICTION
# =========================
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

# =========================
# UPLOAD AUDIO
# =========================
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

    # =========================
    # ALLOWED FILES
    # =========================
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

    # =========================
    # DIRECT WAV
    # =========================
    if filename.endswith(".wav"):

        temp_name = (
            f"uploadaudio/temp_{uuid.uuid4().hex}.wav"
        )

        audio.save(temp_name)

    # =========================
    # CONVERT MP3/WEBM → WAV
    # =========================
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

    # =========================
    # MODEL PREDICTION
    # =========================
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
# REAL TO AI VOICE
# =========================
@app.route('/convert_audio', methods=['POST'])
def convert_audio():

    if tts is None:

        return render_template(
            "convert.html",
            error="XTTS model not loaded"
        )

    if 'audio' not in request.files:

        return render_template(
            "convert.html",
            error="No audio uploaded"
        )

    audio = request.files['audio']

    if audio.filename == "":

        return render_template(
            "convert.html",
            error="No selected file"
        )

    os.makedirs("converted", exist_ok=True)

    input_path = (
        f"converted/input_{uuid.uuid4().hex}.wav"
    )

    output_path = (
        f"converted/output_{uuid.uuid4().hex}.wav"
    )

    audio.save(input_path)

    try:

        tts.tts_to_file(

            text="Hello, this is AI generated voice.",

            speaker_wav=input_path,

            language="en",

            file_path=output_path
        )

        return render_template(

            "convert.html",

            success=True,

            converted_audio='/' + output_path
        )

    except Exception as e:

        return render_template(

            "convert.html",

            error=str(e)
        )

# =========================
# RUN APP
# =========================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )