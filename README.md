# 📘 CALCULUS — Built by Gesner Deslandes

An interactive bilingual (EN/FR) calculus learning app built with **Streamlit**.
Features: lessons, an AI tutor, practice exercises, a Black Board reward game,
and a **female neural voice** that reads lessons and answers aloud.

## 🚀 Deploy in 5 minutes

### 1. Push to GitHub

```bash
git init calculus-app
cd calculus-app
# copy the files listed below into this folder
git add .
git commit -m "Initial CALCULUS Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/calculus-app.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud

1. Go to <https://share.streamlit.io> and log in with GitHub.
2. Click **Create app** → **Deploy a public app from GitHub**.
3. Fill in:
   - **Repository**: `YOUR_USERNAME/calculus-app`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy**.

Streamlit installs `requirements.txt` and your app goes live at
`https://YOUR_USERNAME-calculus-app.streamlit.app`.

Any `git push` to `main` auto-rebuilds the app.

## 🗂 File structure

```
calculus-app/
├── app.py                 # Main Streamlit app
├── curriculum.py          # Bilingual levels / topics / lessons / tutor KB
├── generators.py          # Exercise generators + Black Board generators
├── tts_engine.py          # Female voice (edge-tts + gTTS fallback)
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml        # Dark theme
```

## 🔊 Female voice — how it works

1. **edge-tts** neural female voices (primary):
   - `en-US-JennyNeural` (English)
   - `fr-FR-DeniseNeural` (French)
2. **gTTS** fallback (female by default) if edge-tts is unavailable.

Each click of a "Read" button synthesizes MP3 bytes and autoplays them
inside the page. Browsers require a user gesture for audio — every read
button is a gesture, so autoplay works reliably.

## 🌍 Languages

Toggle 🇺🇸 EN / 🇫🇷 FR in the top bar — every lesson, exercise, tutor
reply, and voice switches instantly.

## 📞 Contact

Gesner Deslandes · Software Engineer
- 📞 (509)-47385663
- ✉️ deslandes78@gmail.com
