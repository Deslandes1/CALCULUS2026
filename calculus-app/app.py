# app.py
# =============================================================================
# CALCULUS — Built by Gesner Deslandes
# Streamlit app · bilingual EN/FR · female neural voice · AI tutor · Black Board
# =============================================================================

import random

import streamlit as st

from curriculum import CURRICULUM
from generators import GENERATORS, REWARDS, generate_bb_question
from tts_engine import speak

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CALCULUS · Built by Gesner Deslandes",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# GLOBAL CSS
# -----------------------------------------------------------------------------
CSS = """
<style>
  .stApp {
    background:
      radial-gradient(1200px 700px at 50% -10%, rgba(0,229,255,.10), transparent 65%),
      radial-gradient(900px 600px at 10% 110%, rgba(255,217,59,.05), transparent 60%),
      radial-gradient(900px 600px at 90% 110%, rgba(168,107,255,.05), transparent 60%),
      #05070c !important;
    color: #d8e4f0;
  }
  h1.brand {
    font-family: Georgia, serif !important;
    font-size: clamp(2rem, 6vw, 3.6rem) !important;
    font-weight: 900 !important;
    letter-spacing: 12px !important;
    background: linear-gradient(90deg, #ffd93b, #ff8a2b, #ffd93b, #a86bff, #ffd93b);
    background-size: 200% 100%;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    color: transparent !important;
    text-align: center;
    margin-bottom: 4px !important;
    animation: shimmer 6s linear infinite;
  }
  @keyframes shimmer {
    0%   { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
  }
  .sub-bar {
    text-align: center;
    font-size: .72rem; font-weight: 900; letter-spacing: 4px;
    color: #ffe680; text-transform: uppercase;
    margin-bottom: 8px;
  }
  .credit {
    text-align: center;
    font-family: Georgia, serif;
    font-size: .82rem; font-weight: 900; letter-spacing: 1.6px;
    color: #ffd93b;
    margin-bottom: 4px;
  }
  .credit small {
    display: block;
    font-family: 'Courier New', monospace;
    font-size: .72rem; color: #6b7c92;
    letter-spacing: 1.4px; margin-top: 4px;
  }
  .lesson-title {
    font-family: Georgia, serif !important;
    font-size: 1.6rem !important;
    font-weight: 900 !important;
    letter-spacing: 1.6px;
    color: #ffd93b !important;
    margin-bottom: 4px;
  }
  .lesson-sub {
    font-family: 'Courier New', monospace;
    font-size: .74rem; font-weight: 900;
    letter-spacing: 1.8px; text-transform: uppercase;
    color: #6b7c92; margin-bottom: 16px;
  }
  .lesson-section {
    border-left: 4px solid #ffd93b;
    padding: 12px 16px;
    border-radius: 10px;
    background: rgba(6,10,16,.55);
    margin-bottom: 14px;
  }
  .lesson-section h4 {
    font-family: Georgia, serif;
    font-size: .95rem; font-weight: 900;
    letter-spacing: 1.2px; color: #ffd93b;
    margin: 0 0 8px 0;
  }
  .lesson-section p, .lesson-section li {
    font-size: .88rem; line-height: 1.7; color: #c8d6f0;
  }
  .lesson-section ul { padding-left: 20px; margin: 6px 0; }
  .formula {
    font-family: 'Courier New', monospace;
    font-size: 1rem; font-weight: 900;
    letter-spacing: .8px; text-align: center;
    padding: 10px 14px; border-radius: 10px;
    background: rgba(0,229,255,.08);
    border: 1.5px solid rgba(0,229,255,.35);
    color: #9ff3ff; margin: 10px 0;
  }
  .example {
    font-family: 'Courier New', monospace;
    font-size: .85rem; line-height: 1.8; font-weight: 700;
    padding: 12px 14px; border-radius: 10px;
    background: rgba(34,255,136,.06);
    border: 1.5px solid rgba(34,255,136,.3);
    color: #a8ffd0; margin: 10px 0; white-space: pre-wrap;
  }
  .question-box {
    padding: 20px; border-radius: 12px;
    background: rgba(3,6,12,.9);
    border: 2px solid rgba(255,217,59,.4);
    text-align: center; margin-bottom: 14px;
  }
  .question-label {
    font-family: 'Courier New', monospace;
    font-size: .64rem; font-weight: 900;
    letter-spacing: 2px; text-transform: uppercase;
    color: #6b7c92; margin-bottom: 10px;
  }
  .question-text {
    font-family: 'Courier New', monospace;
    font-size: clamp(1.1rem, 2.6vw, 1.5rem);
    font-weight: 900; color: #fff5c4;
    line-height: 1.5; letter-spacing: 1px;
    word-break: break-word;
  }
  .bb-surface {
    border-radius: 14px; padding: 24px 26px 20px;
    min-height: 380px;
    background:
      radial-gradient(ellipse at 30% 20%, rgba(40,60,50,.8), transparent 60%),
      radial-gradient(ellipse at 70% 80%, rgba(30,50,40,.6), transparent 60%),
      linear-gradient(180deg, #0f1a14 0%, #0a1210 50%, #08110d 100%);
    box-shadow: inset 0 0 80px rgba(0,0,0,.85);
    font-family: 'Courier New', monospace;
    color: #e8f0e8;
    border: 3px solid #1a0e02;
    margin-bottom: 12px;
  }
  .bb-question {
    font-family: 'Courier New', monospace;
    font-size: clamp(1.2rem, 3vw, 1.9rem);
    font-weight: 900; color: #f4faf4;
    letter-spacing: 1.2px; line-height: 1.5;
    text-align: center;
    text-shadow: 0 0 12px rgba(232,240,232,.55),
                 0 0 30px rgba(232,240,232,.25);
    padding: 18px 0;
    border-bottom: 2px dashed rgba(232,240,232,.25);
    margin-bottom: 18px;
  }
  .reward-shelf {
    text-align: center;
    font-size: 2rem; letter-spacing: 6px;
    padding: 12px 0;
    min-height: 60px;
  }
  .stat-pill {
    display: inline-block;
    font-family: 'Courier New', monospace;
    font-size: .7rem; font-weight: 900;
    padding: 5px 12px; margin: 0 4px;
    border-radius: 999px;
    background: rgba(0,229,255,.10);
    border: 1.5px solid rgba(0,229,255,.35);
    color: #7fe8ff; letter-spacing: 1px;
  }
  div[data-testid="stButton"] > button {
    border-radius: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    transition: all .15s;
  }
  div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 16px rgba(255,217,59,.35);
  }
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea {
    background: rgba(3,6,12,.9) !important;
    color: #fff !important;
    border: 2px solid rgba(58,160,255,.5) !important;
    border-radius: 10px !important;
    font-family: 'Courier New', monospace !important;
    font-weight: 800 !important;
  }
  .stTabs [data-baseweb="tab-list"] { gap: 6px; }
  .stTabs [data-baseweb="tab"] {
    background: rgba(6,10,16,.7);
    border: 1.5px solid rgba(148,163,255,.22);
    border-radius: 10px;
    padding: 8px 16px;
    font-weight: 800;
    letter-spacing: 1px;
  }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
def init_state():
    defaults = {
        "lang": "en",
        "completed": set(),
        "solved": 0,
        "attempts": 0,
        "streak": 0,
        "bb_level": "basics",
        "bb_current": None,
        "bb_correct": 0,
        "bb_streak": 0,
        "bb_rewards": [],
        "tutor_history": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()
LANG = st.session_state.lang


def T(d):
    """Localize a {en, fr} dict."""
    if isinstance(d, dict):
        return d.get(LANG, d.get("en", ""))
    return str(d)


# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown('<h1 class="brand">CALCULUS</h1>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-bar">'
    '<span>BASICS</span> · <span>BEGINNER</span> · '
    '<span>INTERMEDIATE</span> · <span>ADVANCED</span> · '
    '<span>BLACK BOARD</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="credit">BUILT BY GESNER DESLANDES · SOFTWARE ENGINEER'
    '<small>📞 (509)-47385663 · ✉️ deslandes78@gmail.com</small></div>',
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# LANGUAGE TOGGLE
# -----------------------------------------------------------------------------
lc1, lc2, lc3 = st.columns([1, 1, 6])
with lc1:
    if st.button("🇺🇸 EN", use_container_width=True,
                 type="primary" if LANG == "en" else "secondary",
                 key="lang_en"):
        if st.session_state.lang != "en":
            st.session_state.lang = "en"
            st.rerun()
with lc2:
    if st.button("🇫🇷 FR", use_container_width=True,
                 type="primary" if LANG == "fr" else "secondary",
                 key="lang_fr"):
        if st.session_state.lang != "fr":
            st.session_state.lang = "fr"
            st.rerun()

# -----------------------------------------------------------------------------
# SIDEBAR — PROGRESS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 📊 PROGRESS")
    total_topics = sum(len(CURRICULUM[l]["topics"]) for l in CURRICULUM)
    done = len(st.session_state.completed)
    st.markdown(f"**{done} / {total_topics}** " +
                ("sujets terminés" if LANG == "fr" else "topics completed"))
    st.progress(min(1.0, done / max(1, total_topics)))
    st.write(f"**{'Résolus' if LANG == 'fr' else 'Solved'}**: {st.session_state.solved}")
    st.write(f"**{'Tentatives' if LANG == 'fr' else 'Attempts'}**: {st.session_state.attempts}")
    st.write(f"**{'Série' if LANG == 'fr' else 'Streak'}**: {st.session_state.streak}")
    acc = (f"{round(100 * st.session_state.solved / st.session_state.attempts)}%"
           if st.session_state.attempts else "—")
    st.write(f"**{'Précision' if LANG == 'fr' else 'Accuracy'}**: {acc}")

# -----------------------------------------------------------------------------
# LEVEL SELECTOR
# -----------------------------------------------------------------------------
level_labels = {
    "basics":       "📘 " + ("BASES" if LANG == "fr" else "BASICS"),
    "beginner":     "📗 " + ("DÉBUTANT" if LANG == "fr" else "BEGINNER"),
    "intermediate": "📙 " + ("INTERMÉDIAIRE" if LANG == "fr" else "INTERMEDIATE"),
    "advanced":     "📕 " + ("AVANCÉ" if LANG == "fr" else "ADVANCED"),
    "blackboard":   "🎓 " + ("TABLEAU NOIR" if LANG == "fr" else "BLACK BOARD"),
}

level = st.radio(
    "Level",
    list(level_labels.keys()),
    format_func=lambda k: level_labels[k],
    horizontal=True,
    label_visibility="collapsed",
    key="main_level",
)


# -----------------------------------------------------------------------------
# RENDER: LESSON
# -----------------------------------------------------------------------------
def render_lesson(topic):
    st.markdown(f'<div class="lesson-title">{topic["icon"]}. '
                f'{T(topic["name"])}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="lesson-sub">{T(topic["sub"])}</div>',
                unsafe_allow_html=True)

    st.markdown(
        f'<div class="lesson-section"><h4>'
        f'{"Leçon" if LANG == "fr" else "Lesson"}</h4>'
        f'<p>{T(topic["lesson"]["intro"])}</p></div>',
        unsafe_allow_html=True,
    )

    for sec in topic["lesson"].get("sections", []):
        html = f'<div class="lesson-section"><h4>{T(sec["h"])}</h4>'
        if "p" in sec:
            html += f'<p>{T(sec["p"])}</p>'
        if "list" in sec:
            items = sec["list"].get(LANG) or sec["list"].get("en") or []
            html += "<ul>" + "".join(f"<li>{li}</li>" for li in items) + "</ul>"
        if "formula" in sec:
            html += f'<div class="formula">{sec["formula"]}</div>'
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)

    if topic["lesson"].get("formula"):
        st.markdown(
            f'<div class="lesson-section"><h4>'
            f'{"★ Formule clé" if LANG == "fr" else "★ Key Formula"}'
            f'</h4><div class="formula">{topic["lesson"]["formula"]}</div></div>',
            unsafe_allow_html=True,
        )

    if topic["lesson"].get("examples"):
        header = "📝 Exemples résolus" if LANG == "fr" else "📝 Worked Examples"
        html = f'<div class="lesson-section"><h4>{header}</h4>'
        for i, ex in enumerate(topic["lesson"]["examples"], 1):
            label = (f'Exemple {i}' if LANG == "fr" else f'Example {i}')
            html += f'<p><b>{label}: {T(ex["t"])}</b></p>'
            html += f'<div class="example">{T(ex["expr"])}\n\n{T(ex["sol"])}</div>'
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)

    # Read Lesson button
    lesson_text = (f"{T(topic['name'])}. {T(topic['lesson']['intro'])}. "
                   f"{'Formule clé' if LANG == 'fr' else 'Key formula'}: "
                   f"{topic['lesson'].get('formula', '')}")
    if st.button("🔊 " + ("Lire la leçon" if LANG == "fr" else "Read Lesson"),
                 key=f"read_lesson_{topic['id']}"):
        speak(lesson_text, lang=LANG, key=f"tts_lesson_{topic['id']}")


# -----------------------------------------------------------------------------
# RENDER: TUTOR
# -----------------------------------------------------------------------------
def render_tutor(topic):
    st.markdown("### 🤖 " + ("Tuteur IA de Calcul" if LANG == "fr"
                             else "AI Calculus Tutor"))
    st.caption("Powered by Gesner AI Engine")

    kb = topic["tutor"].get(LANG, topic["tutor"]["en"])

    quick = st.selectbox(
        "Quick question",
        ["what", "formula", "example", "mistakes", "real", "tip"],
        format_func=lambda k: {
            "what":     "C'est quoi ce sujet ?" if LANG == "fr" else "What is this topic?",
            "formula":  "Explique la formule" if LANG == "fr" else "Explain the formula",
            "example":  "Exemple résolu" if LANG == "fr" else "Worked example",
            "mistakes": "Erreurs fréquentes" if LANG == "fr" else "Common mistakes",
            "real":     "Utilisation réelle" if LANG == "fr" else "Real-world use",
            "tip":      "Conseil d'étude" if LANG == "fr" else "Study tip",
        }[k],
        key=f"quick_{topic['id']}",
    )

    user_q = st.text_input(
        "Ask the AI tutor anything…" if LANG == "en" else "Posez votre question…",
        key=f"tutor_q_{topic['id']}",
    )

    if st.button("Ask AI" if LANG == "en" else "Demander",
                 key=f"tutor_ask_{topic['id']}"):
        if user_q.strip():
            q_low = user_q.lower()
        else:
            q_low = quick

        if "what" in q_low or "quoi" in q_low or quick == "what":
            reply = kb.get("what", "")
        elif "formula" in q_low or "formule" in q_low or quick == "formula":
            reply = kb.get("formula", "")
        elif "example" in q_low or "exemple" in q_low or quick == "example":
            ex = topic["lesson"]["examples"][0]
            reply = f"**{T(ex['t'])}**\n\n{T(ex['expr'])}\n\n{T(ex['sol'])}"
        elif "real" in q_low or "réel" in q_low or quick == "real":
            reply = kb.get("real", "")
        elif "tip" in q_low or "conseil" in q_low or quick == "tip":
            reply = kb.get("tip", "")
        elif "mistake" in q_low or "erreur" in q_low or quick == "mistakes":
            reply = kb.get("tip", "")
        else:
            reply = (f"**{T(topic['name'])}**\n\n"
                     f"{T(topic['lesson']['intro'])}\n\n"
                     + ("Essayez les questions rapides ci-dessus."
                        if LANG == "fr"
                        else "Try the quick questions above."))

        st.session_state.tutor_history.append({
            "topic": topic["id"], "q": user_q or quick, "reply": reply,
        })
        st.info(reply)

    # Last answer + Read Answer
    if st.session_state.tutor_history:
        last = st.session_state.tutor_history[-1]
        if last["topic"] == topic["id"]:
            if st.button("🔊 " + ("Lire la dernière réponse" if LANG == "fr"
                                  else "Read Last Answer"),
                         key=f"read_last_{topic['id']}"):
                speak(last["reply"], lang=LANG,
                      key=f"tts_last_{topic['id']}")


# -----------------------------------------------------------------------------
# RENDER: PRACTICE
# -----------------------------------------------------------------------------
def render_practice(topic):
    st.markdown("### ✏️ " + ("Exercices pratiques" if LANG == "fr"
                             else "Practice Exercises"))

    key_ex = f"ex_{topic['id']}"
    key_ans = f"ans_{topic['id']}"
    key_fb = f"fb_{topic['id']}"

    cols = st.columns([1, 1, 1, 1])
    with cols[0]:
        if st.button("↻ " + ("Nouvel exercice" if LANG == "fr" else "New Exercise"),
                     key=f"new_{topic['id']}", use_container_width=True):
            gen_fn = GENERATORS[topic["gen"]]
            st.session_state[key_ex] = gen_fn(LANG)
            st.session_state[key_fb] = None

    ex = st.session_state.get(key_ex)
    if not ex:
        st.info("Cliquez sur « Nouvel exercice » pour commencer."
                if LANG == "fr"
                else 'Click "New Exercise" to begin.')
        return

    # Question box
    st.markdown(
        f'<div class="question-box">'
        f'<div class="question-label">'
        f'{"Résoudre" if LANG == "fr" else "Solve the following"}'
        f'</div>'
        f'<div class="question-text">{ex["q"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    if st.button("🔊 " + ("Lire" if LANG == "fr" else "Read"),
                 key=f"read_q_{topic['id']}"):
        speak(ex["q"], lang=LANG, key=f"tts_q_{topic['id']}")

    ans = st.text_input(
        "Votre réponse" if LANG == "fr" else "Your answer",
        key=key_ans,
    )

    bcols = st.columns([1, 1, 1, 1])
    with bcols[0]:
        if st.button("✓ " + ("Vérifier" if LANG == "fr" else "Check"),
                     key=f"chk_{topic['id']}", use_container_width=True):
            st.session_state.attempts += 1
            user = str(ans).strip().lower().replace(" ", "")
            target = str(ex["a"]).strip().lower().replace(" ", "")
            ok = user == target
            if not ok:
                try:
                    ok = float(user) == float(target)
                except Exception:
                    ok = False
            if ok:
                st.session_state.solved += 1
                st.session_state.streak += 1
                st.session_state.completed.add(topic["id"])
                st.session_state[key_fb] = (
                    "ok", ex["a"],
                    "Correct !" if LANG == "fr" else "Correct!"
                )
            else:
                st.session_state.streak = 0
                st.session_state[key_fb] = (
                    "bad", ex["hint"],
                    "Pas tout à fait." if LANG == "fr" else "Not quite."
                )
    with bcols[1]:
        if st.button("💡 " + ("Indice" if LANG == "fr" else "Hint"),
                     key=f"hint_{topic['id']}", use_container_width=True):
            st.session_state[key_fb] = (
                "info", ex["hint"],
                "Indice" if LANG == "fr" else "Hint"
            )
    with bcols[2]:
        if st.button("📖 Solution", key=f"sol_{topic['id']}",
                     use_container_width=True):
            st.session_state[key_fb] = ("info", ex["solution"], "Solution")
    with bcols[3]:
        if st.button("🔊 " + ("Lire" if LANG == "fr" else "Read"),
                     key=f"read_fb_{topic['id']}", use_container_width=True):
            fb = st.session_state.get(key_fb)
            if fb:
                speak(fb[1], lang=LANG, key=f"tts_fb_{topic['id']}")

    fb = st.session_state.get(key_fb)
    if fb:
        kind, msg, label = fb
        if kind == "ok":
            st.success(f"✅ {label} — {msg}")
        elif kind == "bad":
            st.error(f"❌ {label} — {msg}")
        else:
            st.info(f"ℹ️ {label} — {msg}")


# -----------------------------------------------------------------------------
# RENDER: BLACK BOARD
# -----------------------------------------------------------------------------
def render_blackboard():
    st.markdown("### 🎓 " + ("LE TABLEAU NOIR" if LANG == "fr"
                             else "THE BLACK BOARD"))
    st.caption(
        "Zone d'entraînement · Chaque bonne réponse débloque une récompense"
        if LANG == "fr"
        else "Practice Zone · Every correct answer unlocks a reward"
    )

    bb_level = st.radio(
        "BB Level",
        ["basics", "beginner", "intermediate", "advanced"],
        format_func=lambda k: level_labels[k],
        horizontal=True, label_visibility="collapsed",
        key="bb_level_radio",
    )
    st.session_state.bb_level = bb_level

    if st.button("↻ " + ("Nouveau problème" if LANG == "fr" else "New Problem"),
                 key="bb_new"):
        st.session_state.bb_current = generate_bb_question(bb_level, LANG)

    ex = st.session_state.bb_current
    if not ex:
        st.info("Choisissez un niveau ci-dessus et cliquez sur « Nouveau problème »."
                if LANG == "fr"
                else 'Choose a level above and click "New Problem".')
    else:
        st.markdown(
            f'<div class="bb-surface">'
            f'<div class="bb-question">'
            f'{"RÉSOUDRE AU TABLEAU NOIR" if LANG == "fr" else "SOLVE ON THE BLACK BOARD"}'
            f'<br><br>{ex["q"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        if st.button("🔊 " + ("Lire" if LANG == "fr" else "Read"),
                     key="bb_read_q"):
            speak(ex["q"], lang=LANG, key="tts_bb_q")

        bb_ans = st.text_input(
            "Écrivez votre réponse…" if LANG == "fr" else "Write your answer…",
            key="bb_ans",
        )
        if st.button("✓ " + ("VÉRIFIER" if LANG == "fr" else "CHECK"),
                     key="bb_check", use_container_width=True):
            user = str(bb_ans).strip().lower().replace(" ", "")
            target = str(ex["a"]).strip().lower().replace(" ", "")
            ok = user == target
            if not ok:
                try:
                    ok = float(user) == float(target)
                except Exception:
                    ok = False
            if ok:
                st.session_state.bb_correct += 1
                st.session_state.bb_streak += 1
                reward = random.choice(REWARDS)
                st.session_state.bb_rewards.append(reward)
                st.success(f"✅ {'CORRECT !' if LANG == 'fr' else 'CORRECT!'} "
                           f"{ex['a']}  ·  Reward: {reward['e']}")
                speak(f"Correct! {ex['a']}", lang=LANG, key="tts_bb_ok")
                st.session_state.bb_current = None
            else:
                st.session_state.bb_streak = 0
                st.error(f"❌ {'Pas tout à fait.' if LANG == 'fr' else 'Not quite.'} "
                         f"{'Indice' if LANG == 'fr' else 'Hint'}: {ex['hint']}")
                speak(f"{'Pas tout à fait. Indice: ' if LANG == 'fr' else 'Not quite. Hint: '}"
                      f"{ex['hint']}", lang=LANG, key="tts_bb_bad")

    st.markdown(
        f'<div style="text-align:center;margin:12px 0;">'
        f'<span class="stat-pill">{"Répondu" if LANG == "fr" else "Answered"}: '
        f'{st.session_state.bb_correct}</span>'
        f'<span class="stat-pill">{"Série" if LANG == "fr" else "Streak"}: '
        f'{st.session_state.bb_streak}</span>'
        f'<span class="stat-pill">{"Récompenses" if LANG == "fr" else "Rewards"}: '
        f'{len(st.session_state.bb_rewards)}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### 🏆 " + ("RÉCOMPENSES DÉBLOQUÉES" if LANG == "fr"
                              else "REWARDS UNLOCKED"))
    if st.session_state.bb_rewards:
        icons = " ".join(r["e"] for r in st.session_state.bb_rewards)
        st.markdown(f'<div class="reward-shelf">{icons}</div>',
                    unsafe_allow_html=True)
    else:
        st.caption("Répondez correctement pour débloquer votre première récompense."
                   if LANG == "fr"
                   else "Answer correctly to unlock your first reward.")


# -----------------------------------------------------------------------------
# MAIN ROUTER
# -----------------------------------------------------------------------------
if level == "blackboard":
    render_blackboard()
else:
    level_data = CURRICULUM[level]
    topic_names = [T(t["name"]) for t in level_data["topics"]]
    selected = st.selectbox("Topic", topic_names, key=f"topic_sel_{level}")
    topic = level_data["topics"][topic_names.index(selected)]

    tab_lesson, tab_tutor, tab_practice = st.tabs([
        "📘 " + ("Leçon" if LANG == "fr" else "Lesson"),
        "🤖 " + ("Tuteur IA" if LANG == "fr" else "AI Tutor"),
        "✏️ " + ("Exercices" if LANG == "fr" else "Practice"),
    ])
    with tab_lesson:
        render_lesson(topic)
    with tab_tutor:
        render_tutor(topic)
    with tab_practice:
        render_practice(topic)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown(
    '<div style="text-align:center;margin-top:36px;color:#6b7c92;'
    'font-family:Courier New,monospace;font-size:.72rem;letter-spacing:1.6px;">'
    'CALCULUS · BUILT BY GESNER DESLANDES · SOFTWARE ENGINEER<br>'
    '📞 (509)-47385663 · ✉️ deslandes78@gmail.com'
    '</div>',
    unsafe_allow_html=True,
)
