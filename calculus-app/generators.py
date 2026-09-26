# generators.py
# =============================================================================
# Exercise generators per topic + Black Board generator.
# =============================================================================

import random

# -----------------------------------------------------------------------------
# REWARD POOL FOR THE BLACK BOARD
# -----------------------------------------------------------------------------
REWARDS = [
    {"e": "⭐", "n": {"en": "Star", "fr": "Étoile"}},
    {"e": "🏆", "n": {"en": "Trophy", "fr": "Trophée"}},
    {"e": "🎯", "n": {"en": "Bullseye", "fr": "Cible"}},
    {"e": "💎", "n": {"en": "Diamond", "fr": "Diamant"}, "legendary": True},
    {"e": "🥇", "n": {"en": "Gold Medal", "fr": "Médaille d'Or"}},
    {"e": "🚀", "n": {"en": "Rocket", "fr": "Fusée"}},
    {"e": "🎉", "n": {"en": "Party", "fr": "Fête"}},
    {"e": "🔥", "n": {"en": "Fire", "fr": "Feu"}},
    {"e": "⚡", "n": {"en": "Lightning", "fr": "Éclair"}},
    {"e": "🧠", "n": {"en": "Brain", "fr": "Cerveau"}},
    {"e": "💡", "n": {"en": "Lightbulb", "fr": "Ampoule"}},
    {"e": "👑", "n": {"en": "Crown", "fr": "Couronne"}, "legendary": True},
    {"e": "✨", "n": {"en": "Sparkles", "fr": "Étincelles"}},
    {"e": "🌈", "n": {"en": "Rainbow", "fr": "Arc-en-ciel"}},
    {"e": "🦄", "n": {"en": "Unicorn", "fr": "Licorne"}, "legendary": True},
    {"e": "🐉", "n": {"en": "Dragon", "fr": "Dragon"}, "legendary": True},
    {"e": "🦁", "n": {"en": "Lion", "fr": "Lion"}},
    {"e": "🦅", "n": {"en": "Eagle", "fr": "Aigle"}},
    {"e": "🎓", "n": {"en": "Graduation", "fr": "Diplôme"}},
    {"e": "🛡️", "n": {"en": "Shield", "fr": "Bouclier"}},
    {"e": "⚔️", "n": {"en": "Swords", "fr": "Épées"}},
    {"e": "🎖️", "n": {"en": "Medal", "fr": "Médaille"}},
    {"e": "💯", "n": {"en": "Perfect", "fr": "Parfait"}},
    {"e": "🎸", "n": {"en": "Guitar", "fr": "Guitare"}},
    {"e": "🏅", "n": {"en": "Medal", "fr": "Médaille"}},
    {"e": "💥", "n": {"en": "Explosion", "fr": "Explosion"}},
    {"e": "☄️", "n": {"en": "Comet", "fr": "Comète"}},
]


def _loc(d, lang):
    """Localize a dict with en/fr keys."""
    if isinstance(d, dict):
        return d.get(lang, d.get("en", ""))
    return str(d)


# -----------------------------------------------------------------------------
# BASICS
# -----------------------------------------------------------------------------
def gen_numbers(lang="en"):
    n = random.randint(2, 9)
    modes = [
        {
            "q": {"en": f"Classify {n}", "fr": f"Classer {n}"},
            "a": "natural",
            "hint": {"en": "Which set does it belong to?",
                     "fr": "À quel ensemble appartient-il ?"},
            "solution": {"en": f"{n} is a natural number.",
                         "fr": f"{n} est un nombre naturel."},
        },
        {
            "q": {"en": f"Classify √{n * n}", "fr": f"Classer √{n * n}"},
            "a": "natural",
            "hint": {"en": "Which set does it belong to?",
                     "fr": "À quel ensemble appartient-il ?"},
            "solution": {"en": f"√{n * n} = {n}.", "fr": f"√{n * n} = {n}."},
        },
    ]
    m = random.choice(modes)
    return {
        "q": _loc(m["q"], lang),
        "a": m["a"],
        "hint": _loc(m["hint"], lang),
        "solution": _loc(m["solution"], lang),
    }


def gen_exponents(lang="en"):
    b = random.randint(2, 5)
    m = random.randint(2, 4)
    n = random.randint(2, 4)
    return {
        "q": f"{b}^{m} · {b}^{n} = ?",
        "a": str(b ** (m + n)),
        "hint": "Additionnez les exposants." if lang == "fr" else "Add the exponents.",
        "solution": f"{b}^{m + n} = {b ** (m + n)}",
    }


def gen_functions(lang="en"):
    m = random.randint(2, 5)
    b = random.randint(1, 10)
    x = random.randint(1, 8)
    verb = "calculer" if lang == "fr" else "find"
    return {
        "q": f"f(x) = {m}x + {b}, {verb} f({x}) = ?",
        "a": str(m * x + b),
        "hint": ("Remplacez x par la valeur donnée." if lang == "fr"
                 else "Replace x with the given value."),
        "solution": f"f({x}) = {m * x + b}",
    }


_SPECIAL_ANGLES = {
    0:  {"s": "0",    "c": "1"},
    30: {"s": "1/2",  "c": "√3/2"},
    45: {"s": "√2/2", "c": "√2/2"},
    60: {"s": "√3/2", "c": "1/2"},
    90: {"s": "1",    "c": "0"},
}


def gen_trig(lang="en"):
    a = random.choice(list(_SPECIAL_ANGLES.keys()))
    m = random.choice(["sin", "cos"])
    val = _SPECIAL_ANGLES[a][m[0]]
    return {
        "q": f"{m}({a}°) = ?",
        "a": val,
        "hint": ("Table des angles remarquables." if lang == "fr"
                 else "Special angles table."),
        "solution": f"{m}({a}°) = {val}",
    }


# -----------------------------------------------------------------------------
# BEGINNER
# -----------------------------------------------------------------------------
def gen_limits(lang="en"):
    a = random.randint(1, 5)
    m = random.randint(2, 6)
    b = random.randint(-5, 10)
    sign = f"+ {b}" if b >= 0 else f"− {abs(b)}"
    return {
        "q": f"lim (x→{a}) ({m}x {sign})",
        "a": str(m * a + b),
        "hint": "Substitution directe." if lang == "fr" else "Direct substitution.",
        "solution": f"{m * a + b}",
    }


def gen_deriv_intro(lang="en"):
    n = random.randint(2, 5)
    c = random.randint(1, 9)
    return {
        "q": f"d/dx ({c}x^{n}) = ?",
        "a": f"{c * n}x^{n - 1}",
        "hint": "Règle de puissance." if lang == "fr" else "Power rule.",
        "solution": f"{c * n}x^{n - 1}",
    }


def gen_continuity(lang="en"):
    a = random.randint(1, 5)
    if lang == "fr":
        q = f"f(x) = x² + 3 est-elle continue en x = {a} ? (oui/non)"
        ans = "oui"
    else:
        q = f"f(x) = x² + 3 continuous at x = {a}? (yes/no)"
        ans = "yes"
    return {
        "q": q,
        "a": ans,
        "hint": ("Les polynômes sont partout continus." if lang == "fr"
                 else "Polynomials are continuous everywhere."),
        "solution": "Oui." if lang == "fr" else "Yes.",
    }


# -----------------------------------------------------------------------------
# INTERMEDIATE
# -----------------------------------------------------------------------------
def gen_product(lang="en"):
    a = random.randint(2, 6)
    return {
        "q": f"d/dx [x² · x^{a}] = ?",
        "a": f"{a + 2}x^{a + 1}",
        "hint": ("Combinez les exposants." if lang == "fr"
                 else "Combine exponents first."),
        "solution": f"{a + 2}x^{a + 1}",
    }


def gen_quotient(lang="en"):
    a = random.randint(1, 6)
    return {
        "q": f"d/dx [x/(x + {a})] = ?",
        "a": f"{a}/(x+{a})²",
        "hint": ("Utilisez la règle du quotient." if lang == "fr"
                 else "Use the quotient rule."),
        "solution": f"{a}/(x+{a})²",
    }


def gen_chain(lang="en"):
    k = random.randint(2, 6)
    n = random.randint(2, 5)
    return {
        "q": f"d/dx [(x + {k})^{n}] = ?",
        "a": f"{n}(x+{k})^{n - 1}",
        "hint": ("Règle de chaîne : extérieur × intérieur." if lang == "fr"
                 else "Chain rule: outer × inner."),
        "solution": f"{n}(x+{k})^{n - 1}",
    }


# -----------------------------------------------------------------------------
# ADVANCED
# -----------------------------------------------------------------------------
def gen_integrals(lang="en"):
    n = random.randint(1, 5)
    c = random.randint(1, 7)
    return {
        "q": f"∫ {c}x^{n} dx = ?",
        "a": f"({c}/{n + 1})x^{n + 1} + C",
        "hint": ("+1 à l'exposant, divisez, +C." if lang == "fr"
                 else "Add 1 to exponent, divide, +C."),
        "solution": f"({c}/{n + 1})x^{n + 1} + C",
    }


def gen_definite(lang="en"):
    b = random.randint(1, 3)
    n = random.randint(1, 2)
    ans = (b ** (n + 1)) / (n + 1)
    return {
        "q": f"∫[0,{b}] x^{n} dx = ?",
        "a": str(round(ans, 3)),
        "hint": "F(b) − F(a).",
        "solution": f"{ans}",
    }


def gen_series(lang="en"):
    a1 = random.randint(1, 6)
    r_den = random.randint(2, 6)
    s = a1 / (1 - 1 / r_den)
    label = "Somme" if lang == "fr" else "Sum"
    return {
        "q": f"{label}: {a1} + {a1}/{r_den} + {a1}/{r_den * r_den} + … = ?",
        "a": str(round(s, 3)),
        "hint": "S = a₁/(1−r).",
        "solution": f"{round(s, 3)}",
    }


# -----------------------------------------------------------------------------
# REGISTRY
# -----------------------------------------------------------------------------
GENERATORS = {
    "gen_numbers": gen_numbers,
    "gen_exponents": gen_exponents,
    "gen_functions": gen_functions,
    "gen_trig": gen_trig,
    "gen_limits": gen_limits,
    "gen_deriv_intro": gen_deriv_intro,
    "gen_continuity": gen_continuity,
    "gen_product": gen_product,
    "gen_quotient": gen_quotient,
    "gen_chain": gen_chain,
    "gen_integrals": gen_integrals,
    "gen_definite": gen_definite,
    "gen_series": gen_series,
}


# -----------------------------------------------------------------------------
# BLACK BOARD GENERATORS
# -----------------------------------------------------------------------------
def _bb_basics(lang):
    mode = random.choice(["add", "sub", "mul", "div", "exp", "sqrt",
                          "eval", "trig"])
    if mode == "add":
        a, b = random.randint(5, 50), random.randint(5, 50)
        return {"q": f"{a} + {b} = ?", "a": str(a + b),
                "hint": "Addition simple." if lang == "fr" else "Simple addition.",
                "solution": f"{a} + {b} = {a + b}"}
    if mode == "sub":
        a, b = random.randint(20, 80), random.randint(2, 20)
        return {"q": f"{a} − {b} = ?", "a": str(a - b),
                "hint": "Soustraction simple." if lang == "fr" else "Simple subtraction.",
                "solution": f"{a} − {b} = {a - b}"}
    if mode == "mul":
        a, b = random.randint(2, 12), random.randint(2, 12)
        return {"q": f"{a} × {b} = ?", "a": str(a * b),
                "hint": ("Multiplication simple." if lang == "fr"
                         else "Simple multiplication."),
                "solution": f"{a} × {b} = {a * b}"}
    if mode == "div":
        b, q = random.randint(2, 10), random.randint(2, 10)
        a = b * q
        return {"q": f"{a} ÷ {b} = ?", "a": str(q),
                "hint": "Division simple." if lang == "fr" else "Simple division.",
                "solution": f"{a} ÷ {b} = {q}"}
    if mode == "exp":
        b, n = random.randint(2, 5), random.randint(2, 5)
        return {"q": f"{b}^{n} = ?", "a": str(b ** n),
                "hint": ("Multipliez la base par elle-même." if lang == "fr"
                         else "Multiply base by itself n times."),
                "solution": f"{b}^{n} = {b ** n}"}
    if mode == "sqrt":
        n = random.randint(2, 12)
        return {"q": f"√{n * n} = ?", "a": str(n),
                "hint": ("Quel nombre au carré donne ceci ?" if lang == "fr"
                         else "What number times itself gives this?"),
                "solution": f"√{n * n} = {n}"}
    if mode == "eval":
        m, b, x = random.randint(2, 7), random.randint(1, 10), random.randint(1, 8)
        verb = "calculer" if lang == "fr" else "find"
        return {"q": f"f(x) = {m}x + {b}, {verb} f({x}) = ?",
                "a": str(m * x + b),
                "hint": ("Remplacez x par la valeur donnée." if lang == "fr"
                         else "Replace x with the given number."),
                "solution": f"f({x}) = {m * x + b}"}
    # trig
    a = random.choice(list(_SPECIAL_ANGLES.keys()))
    m = random.choice(["sin", "cos"])
    val = _SPECIAL_ANGLES[a][m[0]]
    return {"q": f"{m}({a}°) = ?", "a": val,
            "hint": ("Table des angles remarquables." if lang == "fr"
                     else "Special-angle table."),
            "solution": f"{m}({a}°) = {val}"}


def _bb_beginner(lang):
    mode = random.choice(["limit", "deriv", "cont"])
    if mode == "limit":
        return gen_limits(lang)
    if mode == "deriv":
        return gen_deriv_intro(lang)
    return gen_continuity(lang)


def _bb_intermediate(lang):
    mode = random.choice(["product", "quotient", "chain"])
    return {"product": gen_product, "quotient": gen_quotient,
            "chain": gen_chain}[mode](lang)


def _bb_advanced(lang):
    mode = random.choice(["integral", "definite", "series"])
    return {"integral": gen_integrals, "definite": gen_definite,
            "series": gen_series}[mode](lang)


def generate_bb_question(level, lang="en"):
    if level == "basics":
        return _bb_basics(lang)
    if level == "beginner":
        return _bb_beginner(lang)
    if level == "intermediate":
        return _bb_intermediate(lang)
    return _bb_advanced(lang)
