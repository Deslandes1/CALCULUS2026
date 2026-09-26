# tts_engine.py
# =============================================================================
# Female-voice text-to-speech engine.
#
# Priority:
#   1. edge-tts  ->  en-US-JennyNeural  /  fr-FR-DeniseNeural   (FEMALE neural)
#   2. gTTS      ->  default female timbre
#
# Both produce MP3 bytes which we embed in the page with autoplay.
# =============================================================================

from __future__ import annotations

import asyncio
import base64
import io

import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# FEMALE neural voices (Microsoft Edge TTS) — explicit female selection
# -----------------------------------------------------------------------------
FEMALE_VOICES = {
    "en":    "en-US-JennyNeural",
    "en-gb": "en-GB-LibbyNeural",
    "fr":    "fr-FR-DeniseNeural",
    "fr-ca": "fr-CA-SylvieNeural",
}

# gTTS language codes (female by default)
GTTS_LANGS = {"en": "en", "en-gb": "en", "fr": "fr", "fr-ca": "fr"}


# -----------------------------------------------------------------------------
# EDGE-TTS BACKEND
# -----------------------------------------------------------------------------
async def _edge_speak(text: str, voice: str, rate: str) -> bytes:
    """Return raw MP3 bytes from edge-tts."""
    import edge_tts
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    audio = b""
    async for chunk in communicate.stream():
        if chunk.get("type") == "audio":
            audio += chunk["data"]
    return audio


def _run_async(coro):
    """Run an async coroutine on a fresh event loop (Streamlit-safe)."""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        try:
            loop.close()
        except Exception:
            pass


# -----------------------------------------------------------------------------
# GTTS FALLBACK
# -----------------------------------------------------------------------------
def _gtts_bytes(text: str, lang: str) -> bytes | None:
    try:
        from gtts import gTTS
        buf = io.BytesIO()
        gTTS(text=text, lang=GTTS_LANGS.get(lang, "en"), slow=False).write_to_fp(buf)
        return buf.getvalue()
    except Exception:
        return None


# -----------------------------------------------------------------------------
# TEXT CLEANING FOR SPEECH
# -----------------------------------------------------------------------------
def _clean_for_speech(text: str) -> str:
    """Light math-to-speech normalization + emoji strip."""
    import re

    s = str(text)
    s = re.sub(r"<[^>]+>", " ", s)

    replacements = {
        "∫": " the integral of ",
        "√": " the square root of ",
        "π": " pi ",
        "θ": " theta ",
        "→": " approaches ",
        "≤": " is less than or equal to ",
        "≥": " is greater than or equal to ",
        "≠": " is not equal to ",
        "≈": " is approximately ",
        "∞": " infinity ",
        "×": " times ",
        "÷": " divided by ",
        "·": " times ",
        "−": " minus ",
        "–": " minus ",
        "—": " minus ",
        "°": " degrees ",
        "²": " squared ",
        "³": " cubed ",
        "⁴": " to the fourth ",
        "⁵": " to the fifth ",
        "⁶": " to the sixth ",
        "ⁿ": " to the n ",
        "⁻": " to the minus ",
        "∪": " union ",
        "⊂": " is a subset of ",
        "∈": " is an element of ",
        "ℝ": " the real numbers ",
        "ℚ": " the rational numbers ",
        "ℤ": " the integers ",
        "ℕ": " the natural numbers ",
        "𝕎": " the whole numbers ",
        "^": " to the power of ",
        "=": " equals ",
        "+": " plus ",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)

    # Strip emojis / pictographs
    s = re.sub(
        r"[\U0001F000-\U0001FAFF\U00002600-\U000027BF"
        r"\U0001F1E6-\U0001F1FF\U00002B00-\U00002BFF"
        r"\uFE0F\u200D]",
        " ",
        s,
    )
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# -----------------------------------------------------------------------------
# PUBLIC API
# -----------------------------------------------------------------------------
def synthesize(text: str, lang: str = "en", rate: str = "+0%") -> bytes | None:
    """
    Return MP3 bytes for *text*, using a FEMALE voice.
    Tries edge-tts first, then gTTS.
    """
    if not text or not text.strip():
        return None

    text = _clean_for_speech(text)
    if not text:
        return None

    # 1. edge-tts (explicit female neural voice)
    try:
        voice = FEMALE_VOICES.get(lang, FEMALE_VOICES["en"])
        mp3 = _run_async(_edge_speak(text, voice, rate))
        if mp3:
            return mp3
    except Exception:
        pass

    # 2. gTTS fallback (female by default)
    return _gtts_bytes(text, lang)


def speak(
    text: str,
    lang: str = "en",
    rate: str = "+0%",
    autoplay: bool = True,
    key: str | None = None,
) -> None:
    """
    Synthesize + autoplay a FEMALE voice inside the Streamlit page.
    Renders a small audio player under the calling widget.
    """
    mp3 = synthesize(text, lang, rate)
    if not mp3:
        st.warning("🔇 Voice synthesis unavailable right now.")
        return

    b64 = base64.b64encode(mp3).decode("ascii")
    autoplay_attr = "autoplay" if autoplay else ""
    uid = key or f"tts_{abs(hash(text)) % (10**10)}"

    html = f"""
    <div id="{uid}_wrap" style="margin:6px 0;">
      <audio id="{uid}" {autoplay_attr} controls preload="auto"
             style="width:100%;height:38px;border-radius:10px;
                    filter:invert(0.92) hue-rotate(180deg);">
        <source src="data:audio/mpeg;base64,{b64}" type="audio/mpeg">
      </audio>
    </div>
    <script>
      (function() {{
        var a = document.getElementById("{uid}");
        if (!a) return;
        var p = a.play();
        if (p && p.catch) {{
          p.catch(function(err) {{
            console.log("Autoplay blocked — user can press play.", err);
          }});
        }}
      }})();
    </script>
    """
    components.html(html, height=52, scrolling=False)
