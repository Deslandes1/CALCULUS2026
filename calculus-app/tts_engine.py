# tts_engine.py
# =============================================================================
# Female-voice TTS engine — NATIVE French / English
#
# Fixes:
#   • Math→speech is now LANGUAGE-AWARE (no more English words inside French).
#   • French uses fr-FR-DeniseNeural (native French female).
#   • English uses en-US-JennyNeural (native English female).
#   • gTTS fallback uses the correct language code so it stays native.
# =============================================================================

from __future__ import annotations

import asyncio
import base64
import io
import re

import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# FEMALE neural voices (Microsoft Edge TTS) — native female speakers
# -----------------------------------------------------------------------------
FEMALE_VOICES = {
    "en":    "en-US-JennyNeural",     # native US English female
    "en-gb": "en-GB-LibbyNeural",     # native UK English female
    "fr":    "fr-FR-DeniseNeural",    # native FRENCH female (France)
    "fr-ca": "fr-CA-SylvieNeural",    # native FRENCH female (Canada)
}

# gTTS language codes (gTTS default voice is female, native per language)
GTTS_LANGS = {
    "en": "en", "en-gb": "en",
    "fr": "fr", "fr-ca": "fr",
}

# -----------------------------------------------------------------------------
# LANGUAGE-AWARE MATH DICTIONARIES
# -----------------------------------------------------------------------------
MATH_MAP = {
    "en": {
        "∫":  " the integral of ",
        "√":  " the square root of ",
        "π":  " pi ",
        "θ":  " theta ",
        "α":  " alpha ",
        "β":  " beta ",
        "Δ":  " delta ",
        "Σ":  " the sum of ",
        "→":  " approaches ",
        "≤":  " is less than or equal to ",
        "≥":  " is greater than or equal to ",
        "≠":  " is not equal to ",
        "≈":  " is approximately ",
        "∞":  " infinity ",
        "×":  " times ",
        "÷":  " divided by ",
        "·":  " times ",
        "−":  " minus ",
        "–":  " minus ",
        "—":  " minus ",
        "°":  " degrees ",
        "²":  " squared ",
        "³":  " cubed ",
        "⁴":  " to the fourth ",
        "⁵":  " to the fifth ",
        "⁶":  " to the sixth ",
        "⁷":  " to the seventh ",
        "⁸":  " to the eighth ",
        "⁹":  " to the ninth ",
        "⁰":  " to the zero ",
        "ⁿ":  " to the n ",
        "ᵐ":  " to the m ",
        "⁻":  " to the minus ",
        "⁺":  " to the plus ",
        "₁":  " one ",
        "₂":  " two ",
        "∪":  " union ",
        "∩":  " intersect ",
        "⊂":  " is a subset of ",
        "∈":  " is an element of ",
        "ℝ":  " the real numbers ",
        "ℚ":  " the rational numbers ",
        "ℤ":  " the integers ",
        "ℕ":  " the natural numbers ",
        "𝕎":  " the whole numbers ",
        "^":  " to the power of ",
        "=":  " equals ",
        "+":  " plus ",
    },
    "fr": {
        "∫":  " l'intégrale de ",
        "√":  " la racine carrée de ",
        "π":  " pi ",
        "θ":  " thêta ",
        "α":  " alpha ",
        "β":  " bêta ",
        "Δ":  " delta ",
        "Σ":  " la somme de ",
        "→":  " tend vers ",
        "≤":  " inférieur ou égal à ",
        "≥":  " supérieur ou égal à ",
        "≠":  " différent de ",
        "≈":  " approximativement ",
        "∞":  " l'infini ",
        "×":  " fois ",
        "÷":  " divisé par ",
        "·":  " fois ",
        "−":  " moins ",
        "–":  " moins ",
        "—":  " moins ",
        "°":  " degrés ",
        "²":  " au carré ",
        "³":  " au cube ",
        "⁴":  " puissance quatre ",
        "⁵":  " puissance cinq ",
        "⁶":  " puissance six ",
        "⁷":  " puissance sept ",
        "⁸":  " puissance huit ",
        "⁹":  " puissance neuf ",
        "⁰":  " puissance zéro ",
        "ⁿ":  " puissance n ",
        "ᵐ":  " puissance m ",
        "⁻":  " puissance moins ",
        "⁺":  " puissance plus ",
        "₁":  " un ",
        "₂":  " deux ",
        "∪":  " union ",
        "∩":  " intersection ",
        "⊂":  " inclus dans ",
        "∈":  " appartient à ",
        "ℝ":  " l'ensemble des nombres réels ",
        "ℚ":  " l'ensemble des nombres rationnels ",
        "ℤ":  " l'ensemble des nombres entiers relatifs ",
        "ℕ":  " l'ensemble des nombres entiers naturels ",
        "𝕎":  " l'ensemble des entiers naturels avec zéro ",
        "^":  " puissance ",
        "=":  " égale ",
        "+":  " plus ",
    },
}


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
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        try:
            loop.close()
        except Exception:
            pass


# -----------------------------------------------------------------------------
# gTTS FALLBACK
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
# LANGUAGE-AWARE TEXT CLEANING FOR SPEECH
# -----------------------------------------------------------------------------
def _strip_emoji_and_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(
        r"[\U0001F000-\U0001FAFF\U00002600-\U000027BF"
        r"\U0001F1E6-\U0001F1FF\U00002B00-\U00002BFF"
        r"\uFE0F\u200D\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF]",
        " ",
        s,
    )
    return s


def _normalize_lang(lang: str) -> str:
    """Map any of en/en-gb/fr/fr-ca to 'en' or 'fr'."""
    return "fr" if str(lang).lower().startswith("fr") else "en"


def _clean_for_speech(text: str, lang: str = "en") -> str:
    """Language-aware math→speech conversion. Guarantees native output."""
    base = _normalize_lang(lang)
    s = _strip_emoji_and_html(str(text))

    # --- Whole-word / phrase handling first (must come before symbol map) ---
    if base == "fr":
        # "d/dx" → "d sur d x", "dy/dx" → "d y sur d x"
        s = re.sub(r"\bd\s*/\s*dx\b", " d sur d x ", s)
        s = re.sub(r"\bdy\s*/\s*dx\b", " d y sur d x ", s)
        s = re.sub(r"\bdx\b", " d x ", s)
        s = re.sub(r"\blim\b", " la limite quand ", s, flags=re.IGNORECASE)
        # f'(x) → f prime de x
        s = re.sub(r"([a-zA-Z])'\(([^)]*)\)", r"\1 prime de \2", s)
        # f(x) → f de x   (only single-letter function names, avoid URLs)
        s = re.sub(r"\b([a-zA-Z])\(([^()]+)\)", r"\1 de \2", s)
        # ℝ = ℚ ∪ Irrationals  → French
        s = s.replace("Irrationals", "les irrationnels")
        s = s.replace("Irrational", "irrationnel")
    else:
        s = re.sub(r"\bd\s*/\s*dx\b", " d by d x ", s)
        s = re.sub(r"\bdy\s*/\s*dx\b", " d y by d x ", s)
        s = re.sub(r"\bdx\b", " d x ", s)
        s = re.sub(r"\blim\b", " the limit as ", s, flags=re.IGNORECASE)
        s = re.sub(r"([a-zA-Z])'\(([^)]*)\)", r"\1 prime of \2", s)
        s = re.sub(r"\b([a-zA-Z])\(([^()]+)\)", r"\1 of \2", s)

    # --- Symbol-by-symbol replacement using the language-specific map ---
    table = MATH_MAP[base]
    for symbol, spoken in table.items():
        s = s.replace(symbol, spoken)

    # --- Cleanup whitespace and punctuation ---
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([.,!?;:])\s*", r"\1 ", s)
    s = re.sub(r"(?:\.\s*){3,}", ". ", s)
    return s.strip()


# -----------------------------------------------------------------------------
# PUBLIC API
# -----------------------------------------------------------------------------
def synthesize(text: str, lang: str = "en", rate: str = "+0%") -> bytes | None:
    """
    Return MP3 bytes for *text*, spoken in a NATIVE female voice of *lang*.
    Tries edge-tts (Jenny / Denise) first, then gTTS.
    """
    if not text or not text.strip():
        return None

    base = _normalize_lang(lang)
    clean = _clean_for_speech(text, base)
    if not clean:
        return None

    # 1. edge-tts — native female neural voice
    try:
        voice = FEMALE_VOICES.get(base, FEMALE_VOICES["en"])
        mp3 = _run_async(_edge_speak(clean, voice, rate))
        if mp3:
            return mp3
    except Exception:
        pass

    # 2. gTTS fallback — native female per language
    return _gtts_bytes(clean, base)


def speak(
    text: str,
    lang: str = "en",
    rate: str = "+0%",
    autoplay: bool = True,
    key: str | None = None,
    show_voice_label: bool = True,
) -> None:
    """
    Synthesize + autoplay a NATIVE female voice inside the Streamlit page.
    """
    base = _normalize_lang(lang)
    mp3 = synthesize(text, base, rate)
    if not mp3:
        st.warning("🔇 Voice synthesis unavailable right now.")
        return

    b64 = base64.b64encode(mp3).decode("ascii")
    autoplay_attr = "autoplay" if autoplay else ""
    uid = key or f"tts_{abs(hash(text + base)) % (10**10)}"

    voice_name = FEMALE_VOICES.get(base, FEMALE_VOICES["en"])
    flag = "🇫🇷" if base == "fr" else "🇺🇸"
    label = f"{flag} {voice_name}" if show_voice_label else ""

    label_html = (
        f'<div style="font-family:Courier New,monospace;font-size:.66rem;'
        f'color:#6b7c92;letter-spacing:1px;margin-bottom:2px;">{label}</div>'
        if label else ""
    )

    html = f"""
    <div id="{uid}_wrap" style="margin:6px 0;">
      {label_html}
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
    components.html(html, height=70 if label else 52, scrolling=False)
