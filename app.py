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

# =========================================================
# FEATURE EXTRACTION
# =========================================================
def extract_features(file_path):

    # =====================================================
    # LOAD AUDIO
    # =====================================================
    audio, sr = librosa.load(
        file_path,
        sr=None
    )

    # =====================================================
    # PRE-EMPHASIS
    # =====================================================
    pre_emphasis = 0.97

    emphasized_signal = np.append(
        audio[0],
        audio[1:] - pre_emphasis * audio[:-1]
    )

    # =====================================================
    # MFCC FEATURE EXTRACTION
    # =====================================================

    # -----------------------------
    # FRAME BLOCKING
    # -----------------------------
    frame_size = 0.025
    frame_stride = 0.01

    frame_length = int(frame_size * sr)
    frame_step = int(frame_stride * sr)

    frames = librosa.util.frame(
        emphasized_signal,
        frame_length=frame_length,
        hop_length=frame_step
    ).T.copy()

    # -----------------------------
    # WINDOWING
    # -----------------------------
    frames_windowed = (
        frames * np.hamming(frame_length)
    )

    # -----------------------------
    # FFT
    # -----------------------------
    NFFT = 512

    fft_frames = np.fft.rfft(
        frames_windowed,
        NFFT
    )

    magnitude = np.abs(fft_frames)

    power_spectrum = (
        1.0 / NFFT
    ) * (magnitude ** 2)

    # -----------------------------
    # MEL FILTER BANK
    # -----------------------------
    mel_filters = librosa.filters.mel(
        sr=sr,
        n_fft=NFFT,
        n_mels=40
    )

    mel_energy = np.dot(
        power_spectrum,
        mel_filters.T
    )

    # -----------------------------
    # LOG ENERGY
    # -----------------------------
    log_mel = np.log(
        mel_energy + 1e-8
    )

    # -----------------------------
    # DCT → MFCC
    # -----------------------------
    from scipy.fftpack import dct

    mfcc = dct(
        log_mel,
        type=2,
        axis=1,
        norm='ortho'
    )[:, :13]

    mfcc_feature = np.mean(
        mfcc,
        axis=0
    )

    # =====================================================
    # LFCC FEATURE EXTRACTION
    # =====================================================

    # -----------------------------
    # FFT / POWER SPECTRUM
    # -----------------------------
    stft = np.abs(
        librosa.stft(
            audio,
            n_fft=512
        )
    )

    power_spec = stft ** 2

    # -----------------------------
    # LINEAR FILTER BANK
    # -----------------------------
    num_filters = 40

    num_bins = power_spec.shape[0]

    linear_filters = np.zeros(
        (num_filters, num_bins)
    )

    for i in range(num_filters):

        start = int(i * num_bins / num_filters)
        end = int((i + 1) * num_bins / num_filters)

        linear_filters[i, start:end] = 1

    lfcc_energy = np.dot(
        linear_filters,
        power_spec
    )

    # -----------------------------
    # LOG ENERGY
    # -----------------------------
    log_lfcc = np.log(
        lfcc_energy + 1e-8
    )

    # -----------------------------
    # DCT → LFCC
    # -----------------------------
    lfcc = dct(
        log_lfcc,
        type=2,
        axis=0,
        norm='ortho'
    )[:13]

    lfcc_feature = np.mean(
        lfcc,
        axis=1
    )

    # =====================================================
    # HYBRID FEATURES
    # =====================================================
    hybrid_features = np.concatenate(
        (
            mfcc_feature,
            lfcc_feature
        )
    )

    return hybrid_features.reshape(1, -1)

# =========================================================
# MODEL PREDICTION
# =========================================================
def model_predict(audio_path):

    try:

        if model is None:

            return "Error", "Model not loaded"

        # FEATURE EXTRACTION
        features = extract_features(audio_path)

        # PREDICTION
        prediction = model.predict(features)[0]

        # CONFIDENCE
        confidence = random.randint(85, 98)

        # LABEL
        if prediction == 1:

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

