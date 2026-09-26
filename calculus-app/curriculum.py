# curriculum.py
# =============================================================================
# Full bilingual curriculum: levels → topics → lessons → tutor KB.
# =============================================================================

CURRICULUM = {
    # =========================================================================
    # BASICS
    # =========================================================================
    "basics": {
        "label": {"en": "BASICS", "fr": "BASES"},
        "icon": "📘",
        "color": "#3fd0c9",
        "topics": [
            {
                "id": "numbers", "icon": "1",
                "name": {"en": "Numbers & Real Number System",
                         "fr": "Nombres & Système des Nombres Réels"},
                "sub": {"en": "Natural · Integer · Rational",
                        "fr": "Naturel · Entier · Rationnel"},
                "lesson": {
                    "intro": {
                        "en": ("Numbers are the foundation of all mathematics. "
                               "Calculus deals with real numbers — naturals, integers, "
                               "rationals, and irrationals."),
                        "fr": ("Les nombres sont la fondation de toutes les mathématiques. "
                               "Le calcul utilise les nombres réels — naturels, entiers, "
                               "rationnels et irrationnels."),
                    },
                    "sections": [
                        {
                            "h": {"en": "The Real Number System",
                                  "fr": "Le Système des Nombres Réels"},
                            "p": {"en": "Every real number belongs to a nested set:",
                                  "fr": "Chaque nombre réel appartient à un ensemble imbriqué :"},
                            "list": {
                                "en": [
                                    "<b>Natural (ℕ):</b> 1, 2, 3, …",
                                    "<b>Whole (𝕎):</b> 0, 1, 2, 3, …",
                                    "<b>Integers (ℤ):</b> …, −2, −1, 0, 1, 2, …",
                                    "<b>Rational (ℚ):</b> fractions a/b, b ≠ 0",
                                    "<b>Irrational:</b> √2, π, e",
                                    "<b>Real (ℝ):</b> all together",
                                ],
                                "fr": [
                                    "<b>Naturels (ℕ) :</b> 1, 2, 3, …",
                                    "<b>Entiers naturels (𝕎) :</b> 0, 1, 2, 3, …",
                                    "<b>Entiers relatifs (ℤ) :</b> …, −2, −1, 0, 1, 2, …",
                                    "<b>Rationnels (ℚ) :</b> fractions a/b, b ≠ 0",
                                    "<b>Irrationnels :</b> √2, π, e",
                                    "<b>Réels (ℝ) :</b> tous ensemble",
                                ],
                            },
                        }
                    ],
                    "formula": "ℝ = ℚ ∪ Irrationals",
                    "examples": [
                        {"t": {"en": "Classify √9", "fr": "Classer √9"},
                         "expr": "√9",
                         "sol": {"en": "= 3, a natural number.",
                                 "fr": "= 3, un nombre naturel."}},
                        {"t": {"en": "Classify √7", "fr": "Classer √7"},
                         "expr": "√7 ≈ 2.6457…",
                         "sol": {"en": "Irrational — decimal never repeats.",
                                 "fr": "Irrationnel — le décimal ne se répète jamais."}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": ("The real number system is the complete set of numbers "
                                 "used in calculus — naturals, integers, rationals, and "
                                 "irrationals."),
                        "formula": ("<code>ℝ = ℚ ∪ Irrationals</code> means: every real "
                                    "number is either rational or irrational."),
                        "real": ("Real numbers are used for every measurement: distance, "
                                 "time, weight, price, and temperature."),
                        "tip": "Memorize: ℕ ⊂ 𝕎 ⊂ ℤ ⊂ ℚ ⊂ ℝ.",
                    },
                    "fr": {
                        "what": ("Le système des nombres réels est l'ensemble complet "
                                 "utilisé en calcul — naturels, entiers, rationnels et "
                                 "irrationnels."),
                        "formula": ("<code>ℝ = ℚ ∪ Irrationnels</code> signifie : tout "
                                    "nombre réel est rationnel ou irrationnel."),
                        "real": ("Les nombres réels servent à toute mesure : distance, "
                                 "temps, poids, prix, température."),
                        "tip": "Mémorisez : ℕ ⊂ 𝕎 ⊂ ℤ ⊂ ℚ ⊂ ℝ.",
                    },
                },
                "gen": "gen_numbers",
            },
            {
                "id": "exponents", "icon": "2",
                "name": {"en": "Exponents & Powers",
                         "fr": "Exposants & Puissances"},
                "sub": {"en": "Laws · Simplification",
                        "fr": "Lois · Simplification"},
                "lesson": {
                    "intro": {
                        "en": "Exponents are shorthand for repeated multiplication.",
                        "fr": "Les exposants sont une abréviation pour la multiplication répétée.",
                    },
                    "sections": [
                        {
                            "h": {"en": "Laws of Exponents", "fr": "Lois des Exposants"},
                            "p": {"en": "Five essential rules:",
                                  "fr": "Cinq règles essentielles :"},
                            "list": {
                                "en": ["aᵐ · aⁿ = aᵐ⁺ⁿ", "aᵐ ÷ aⁿ = aᵐ⁻ⁿ",
                                       "(aᵐ)ⁿ = aᵐⁿ", "a⁰ = 1", "a⁻ⁿ = 1/aⁿ"],
                                "fr": ["aᵐ · aⁿ = aᵐ⁺ⁿ", "aᵐ ÷ aⁿ = aᵐ⁻ⁿ",
                                       "(aᵐ)ⁿ = aᵐⁿ", "a⁰ = 1", "a⁻ⁿ = 1/aⁿ"],
                            },
                        }
                    ],
                    "formula": "aᵐ · aⁿ = aᵐ⁺ⁿ",
                    "examples": [
                        {"t": {"en": "Simplify", "fr": "Simplifier"},
                         "expr": "2³ · 2⁴",
                         "sol": {"en": "= 2⁷ = 128", "fr": "= 2⁷ = 128"}},
                        {"t": {"en": "Simplify", "fr": "Simplifier"},
                         "expr": "5⁻²",
                         "sol": {"en": "= 1/25", "fr": "= 1/25"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": ("Exponents are shorthand for repeated multiplication: "
                                 "aⁿ means a multiplied by itself n times."),
                        "formula": ("When multiplying the same base, add exponents: "
                                    "aᵐ · aⁿ = aᵐ⁺ⁿ."),
                        "real": "Compound interest, population growth, radioactive decay.",
                        "tip": ("Practice on numbers first (2³ · 2⁴), then variables "
                                "(x⁵ · x²)."),
                    },
                    "fr": {
                        "what": ("Les exposants sont une abréviation pour la multiplication "
                                 "répétée : aⁿ signifie a multiplié par lui-même n fois."),
                        "formula": ("En multipliant la même base, on additionne les "
                                    "exposants : aᵐ · aⁿ = aᵐ⁺ⁿ."),
                        "real": ("Intérêts composés, croissance démographique, "
                                 "décroissance radioactive."),
                        "tip": ("Entraînez-vous d'abord avec des nombres (2³ · 2⁴), puis "
                                "des variables (x⁵ · x²)."),
                    },
                },
                "gen": "gen_exponents",
            },
            {
                "id": "functions", "icon": "3",
                "name": {"en": "Functions & Graphs",
                         "fr": "Fonctions & Graphiques"},
                "sub": {"en": "Domain · Range", "fr": "Domaine · Image"},
                "lesson": {
                    "intro": {
                        "en": "A function assigns exactly one output to each input.",
                        "fr": "Une fonction assigne exactement une sortie à chaque entrée.",
                    },
                    "sections": [
                        {"h": {"en": "Notation", "fr": "Notation"},
                         "p": {"en": 'f(x) means "output of f when input is x".',
                               "fr": 'f(x) signifie « sortie de f quand l\'entrée est x ».'}},
                    ],
                    "formula": "f(x) = y",
                    "examples": [
                        {"t": {"en": "Evaluate", "fr": "Évaluer"},
                         "expr": {"en": "f(x) = 2x + 3, find f(5)",
                                  "fr": "f(x) = 2x + 3, calculer f(5)"},
                         "sol": {"en": "= 13", "fr": "= 13"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": ("A function is a rule that takes an input and gives "
                                 "exactly one output."),
                        "formula": 'f(x) = y means "putting x into f gives y".',
                        "real": "Position, temperature, price are all functions of time.",
                        "tip": "Practice graphing 5 basic function shapes.",
                    },
                    "fr": {
                        "what": ("Une fonction est une règle qui prend une entrée et "
                                 "donne exactement une sortie."),
                        "formula": 'f(x) = y signifie « mettre x dans f donne y ».',
                        "real": "Position, température, prix sont tous des fonctions du temps.",
                        "tip": "Entraînez-vous à tracer 5 formes de fonctions de base.",
                    },
                },
                "gen": "gen_functions",
            },
            {
                "id": "trig", "icon": "4",
                "name": {"en": "Trigonometry Foundations",
                         "fr": "Fondations de Trigonométrie"},
                "sub": {"en": "Sin · Cos · Tan", "fr": "Sin · Cos · Tan"},
                "lesson": {
                    "intro": {
                        "en": "Trigonometry studies angles and triangles.",
                        "fr": "La trigonométrie étudie les angles et les triangles.",
                    },
                    "sections": [
                        {
                            "h": {"en": "Special Angles", "fr": "Angles Remarquables"},
                            "p": {"en": "Memorize these:", "fr": "Mémorisez ces valeurs :"},
                            "list": {
                                "en": ["sin 0° = 0, cos 0° = 1",
                                       "sin 30° = 1/2, cos 30° = √3/2",
                                       "sin 45° = √2/2, cos 45° = √2/2",
                                       "sin 60° = √3/2, cos 60° = 1/2",
                                       "sin 90° = 1, cos 90° = 0"],
                                "fr": ["sin 0° = 0, cos 0° = 1",
                                       "sin 30° = 1/2, cos 30° = √3/2",
                                       "sin 45° = √2/2, cos 45° = √2/2",
                                       "sin 60° = √3/2, cos 60° = 1/2",
                                       "sin 90° = 1, cos 90° = 0"],
                            },
                        }
                    ],
                    "formula": "sin²θ + cos²θ = 1",
                    "examples": [
                        {"t": {"en": "Evaluate", "fr": "Évaluer"},
                         "expr": "sin 30° + cos 60°",
                         "sol": {"en": "= 1", "fr": "= 1"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Trigonometry studies triangles and angles.",
                        "formula": "The Pythagorean identity: sin²θ + cos²θ = 1.",
                        "real": "GPS, music, engineering, astronomy.",
                        "tip": "Memorize the unit circle.",
                    },
                    "fr": {
                        "what": "La trigonométrie étudie les triangles et les angles.",
                        "formula": "L'identité de Pythagore : sin²θ + cos²θ = 1.",
                        "real": "GPS, musique, ingénierie, astronomie.",
                        "tip": "Mémorisez le cercle trigonométrique.",
                    },
                },
                "gen": "gen_trig",
            },
        ],
    },

    # =========================================================================
    # BEGINNER
    # =========================================================================
    "beginner": {
        "label": {"en": "BEGINNER", "fr": "DÉBUTANT"},
        "icon": "📗",
        "color": "#3aa0ff",
        "topics": [
            {
                "id": "limits", "icon": "1",
                "name": {"en": "Introduction to Limits",
                         "fr": "Introduction aux Limites"},
                "sub": {"en": "Concept · Notation", "fr": "Concept · Notation"},
                "lesson": {
                    "intro": {
                        "en": "A limit describes what value a function approaches.",
                        "fr": "Une limite décrit vers quelle valeur tend une fonction.",
                    },
                    "sections": [
                        {"h": {"en": "Intuitive Idea", "fr": "Idée Intuitive"},
                         "p": {"en": "As x approaches a, f(x) approaches L.",
                               "fr": "Quand x tend vers a, f(x) tend vers L."},
                         "formula": "lim (x→a) f(x) = L"},
                    ],
                    "formula": "lim (x→a) f(x) = L",
                    "examples": [
                        {"t": {"en": "Evaluate", "fr": "Évaluer"},
                         "expr": "lim (x→2) (3x + 1)",
                         "sol": {"en": "= 7", "fr": "= 7"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "A limit tells you what value a function approaches.",
                        "formula": ("lim (x→a) f(x) = L means as x approaches a, "
                                    "f(x) approaches L."),
                        "real": "Cooling coffee, terminal velocity, converging series.",
                        "tip": "Try direct substitution first.",
                    },
                    "fr": {
                        "what": ("Une limite indique vers quelle valeur tend une "
                                 "fonction."),
                        "formula": ("lim (x→a) f(x) = L signifie : quand x tend vers a, "
                                    "f(x) tend vers L."),
                        "real": "Café qui refroidit, vitesse limite, séries convergentes.",
                        "tip": "Essayez d'abord la substitution directe.",
                    },
                },
                "gen": "gen_limits",
            },
            {
                "id": "deriv-intro", "icon": "2",
                "name": {"en": "Introduction to Derivatives",
                         "fr": "Introduction aux Dérivées"},
                "sub": {"en": "Slope · Rate of Change",
                        "fr": "Pente · Taux de Variation"},
                "lesson": {
                    "intro": {
                        "en": "The derivative measures how fast a function changes.",
                        "fr": "La dérivée mesure la vitesse de changement d'une fonction.",
                    },
                    "sections": [
                        {"h": {"en": "Definition", "fr": "Définition"},
                         "p": {"en": "Limit of the difference quotient.",
                               "fr": "Limite du taux d'accroissement."},
                         "formula": "f'(x) = lim (h→0) [f(x+h) − f(x)] / h"},
                        {"h": {"en": "Power Rule", "fr": "Règle de Puissance"},
                         "p": {"en": "The main shortcut:",
                               "fr": "Le raccourci principal :"},
                         "formula": "d/dx(xⁿ) = n·xⁿ⁻¹"},
                    ],
                    "formula": "d/dx(xⁿ) = n·xⁿ⁻¹",
                    "examples": [
                        {"t": {"en": "Differentiate", "fr": "Dériver"},
                         "expr": "f(x) = x³",
                         "sol": {"en": "f'(x) = 3x²", "fr": "f'(x) = 3x²"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "The derivative measures instantaneous rate of change.",
                        "formula": ("d/dx(xⁿ) = n·xⁿ⁻¹ — bring down the exponent, "
                                    "subtract 1."),
                        "real": "Speed, acceleration, marginal cost.",
                        "tip": "The derivative of a constant is 0.",
                    },
                    "fr": {
                        "what": "La dérivée mesure le taux de variation instantané.",
                        "formula": ("d/dx(xⁿ) = n·xⁿ⁻¹ — abaissez l'exposant, "
                                    "soustrayez 1."),
                        "real": "Vitesse, accélération, coût marginal.",
                        "tip": "La dérivée d'une constante est 0.",
                    },
                },
                "gen": "gen_deriv_intro",
            },
            {
                "id": "continuity", "icon": "3",
                "name": {"en": "Continuity", "fr": "Continuité"},
                "sub": {"en": "At a point · On an interval",
                        "fr": "En un point · Sur un intervalle"},
                "lesson": {
                    "intro": {
                        "en": "A function is continuous if its graph has no breaks.",
                        "fr": "Une fonction est continue si son graphe n'a pas de sauts.",
                    },
                    "sections": [
                        {"h": {"en": "Three Conditions", "fr": "Trois Conditions"},
                         "list": {
                             "en": ["f(a) is defined", "lim exists", "lim = f(a)"],
                             "fr": ["f(a) est défini", "lim existe", "lim = f(a)"],
                         }},
                    ],
                    "formula": "lim (x→a) f(x) = f(a)",
                    "examples": [
                        {"t": {"en": "Is x² continuous at 3?",
                               "fr": "x² est-elle continue en 3 ?"},
                         "expr": {"en": "Check", "fr": "Vérifier"},
                         "sol": {"en": "Yes.", "fr": "Oui."}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Continuity means the graph has no breaks.",
                        "formula": "lim = f(a) — the limit equals the value.",
                        "real": "Temperature, pressure, position.",
                        "tip": "Ask: Is f(a) defined? Does lim exist? Are they equal?",
                    },
                    "fr": {
                        "what": "Continuité signifie que le graphe n'a pas de sauts.",
                        "formula": "lim = f(a) — la limite est égale à la valeur.",
                        "real": "Température, pression, position.",
                        "tip": ("Demandez : f(a) est-il défini ? lim existe-t-elle ? "
                                "Sont-elles égales ?"),
                    },
                },
                "gen": "gen_continuity",
            },
        ],
    },

    # =========================================================================
    # INTERMEDIATE
    # =========================================================================
    "intermediate": {
        "label": {"en": "INTERMEDIATE", "fr": "INTERMÉDIAIRE"},
        "icon": "📙",
        "color": "#ff8a2b",
        "topics": [
            {
                "id": "product", "icon": "1",
                "name": {"en": "Product Rule", "fr": "Règle du Produit"},
                "sub": {"en": "Derivative of product",
                        "fr": "Dérivée d'un produit"},
                "lesson": {
                    "intro": {
                        "en": "Rule for differentiating a product.",
                        "fr": "Règle pour dériver un produit.",
                    },
                    "sections": [
                        {"h": {"en": "The Product Rule", "fr": "La Règle du Produit"},
                         "p": {"en": "If u and v are functions:",
                               "fr": "Si u et v sont des fonctions :"},
                         "formula": "(uv)' = u'v + uv'"},
                    ],
                    "formula": "(uv)' = u'v + uv'",
                    "examples": [
                        {"t": {"en": "Differentiate", "fr": "Dériver"},
                         "expr": "f(x) = x²·sin(x)",
                         "sol": {"en": "= 2x·sin(x) + x²·cos(x)",
                                 "fr": "= 2x·sin(x) + x²·cos(x)"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": ("The product rule gives the derivative of two "
                                 "functions multiplied."),
                        "formula": "(uv)' = u'v + uv'.",
                        "real": "Force = mass × acceleration.",
                        "tip": "Label u and v first, then plug in.",
                    },
                    "fr": {
                        "what": ("La règle du produit donne la dérivée de deux "
                                 "fonctions multipliées."),
                        "formula": "(uv)' = u'v + uv'.",
                        "real": "Force = masse × accélération.",
                        "tip": "Étiquetez d'abord u et v, puis appliquez.",
                    },
                },
                "gen": "gen_product",
            },
            {
                "id": "quotient", "icon": "2",
                "name": {"en": "Quotient Rule", "fr": "Règle du Quotient"},
                "sub": {"en": "Derivative of fraction",
                        "fr": "Dérivée d'une fraction"},
                "lesson": {
                    "intro": {
                        "en": "Rule for differentiating a fraction.",
                        "fr": "Règle pour dériver une fraction.",
                    },
                    "sections": [
                        {"h": {"en": "The Quotient Rule",
                               "fr": "La Règle du Quotient"},
                         "p": {"en": "If u and v are functions, v ≠ 0:",
                               "fr": "Si u et v sont des fonctions, v ≠ 0 :"},
                         "formula": "(u/v)' = (u'v − uv')/v²"},
                    ],
                    "formula": "(u/v)' = (u'v − uv')/v²",
                    "examples": [
                        {"t": {"en": "Differentiate", "fr": "Dériver"},
                         "expr": "f(x) = x/(x+1)",
                         "sol": {"en": "= 1/(x+1)²", "fr": "= 1/(x+1)²"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": ("Rule for differentiating one function divided "
                                 "by another."),
                        "formula": "(u/v)' = (u'v − uv')/v².",
                        "real": "Speed = distance/time, density = mass/volume.",
                        "tip": "Low d-high minus high d-low, all over low squared.",
                    },
                    "fr": {
                        "what": ("Règle pour dériver une fonction divisée par "
                                 "une autre."),
                        "formula": "(u/v)' = (u'v − uv')/v².",
                        "real": "Vitesse = distance/temps, densité = masse/volume.",
                        "tip": "Bas d-haut moins haut d-bas, sur bas au carré.",
                    },
                },
                "gen": "gen_quotient",
            },
            {
                "id": "chain", "icon": "3",
                "name": {"en": "Chain Rule", "fr": "Règle de Chaîne"},
                "sub": {"en": "Composite functions",
                        "fr": "Fonctions composées"},
                "lesson": {
                    "intro": {
                        "en": "Rule for differentiating a function inside another function.",
                        "fr": "Règle pour dériver une fonction dans une autre.",
                    },
                    "sections": [
                        {"h": {"en": "The Chain Rule", "fr": "La Règle de Chaîne"},
                         "p": {"en": "If y = f(g(x)):",
                               "fr": "Si y = f(g(x)) :"},
                         "formula": "dy/dx = f'(g(x))·g'(x)"},
                    ],
                    "formula": "d/dx[f(g(x))] = f'(g(x))·g'(x)",
                    "examples": [
                        {"t": {"en": "Differentiate", "fr": "Dériver"},
                         "expr": "f(x) = (2x+1)⁵",
                         "sol": {"en": "= 10(2x+1)⁴", "fr": "= 10(2x+1)⁴"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Rule for composite functions.",
                        "formula": ("Differentiate outside, keep inside, multiply "
                                    "by inside derivative."),
                        "real": "Any chain of dependencies.",
                        "tip": "Identify outside and inside first.",
                    },
                    "fr": {
                        "what": "Règle pour les fonctions composées.",
                        "formula": ("Dérivez l'extérieur, gardez l'intérieur, "
                                    "multipliez par la dérivée de l'intérieur."),
                        "real": "Toute chaîne de dépendances.",
                        "tip": "Identifiez d'abord extérieur et intérieur.",
                    },
                },
                "gen": "gen_chain",
            },
        ],
    },

    # =========================================================================
    # ADVANCED
    # =========================================================================
    "advanced": {
        "label": {"en": "ADVANCED", "fr": "AVANCÉ"},
        "icon": "📕",
        "color": "#a86bff",
        "topics": [
            {
                "id": "integrals", "icon": "1",
                "name": {"en": "Introduction to Integrals",
                         "fr": "Introduction aux Intégrales"},
                "sub": {"en": "Antiderivatives", "fr": "Primitives"},
                "lesson": {
                    "intro": {
                        "en": "Integration is the reverse of differentiation.",
                        "fr": "L'intégration est l'inverse de la différenciation.",
                    },
                    "sections": [
                        {"h": {"en": "Definition", "fr": "Définition"},
                         "p": {"en": "F is an antiderivative of f if F' = f.",
                               "fr": "F est une primitive de f si F' = f."},
                         "formula": "∫ f(x)dx = F(x) + C"},
                        {"h": {"en": "Power Rule for Integrals",
                               "fr": "Règle de Puissance"},
                         "formula": "∫ xⁿ dx = xⁿ⁺¹/(n+1) + C  (n ≠ −1)"},
                    ],
                    "formula": "∫ xⁿ dx = xⁿ⁺¹/(n+1) + C",
                    "examples": [
                        {"t": {"en": "Integrate", "fr": "Intégrer"},
                         "expr": "∫ x³ dx",
                         "sol": {"en": "= x⁴/4 + C", "fr": "= x⁴/4 + C"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Integration is the reverse of differentiation.",
                        "formula": "∫ xⁿ dx = xⁿ⁺¹/(n+1) + C. Always add + C.",
                        "real": "Area, volume, distance from velocity.",
                        "tip": "Verify by differentiating your answer.",
                    },
                    "fr": {
                        "what": "L'intégration est l'inverse de la différenciation.",
                        "formula": "∫ xⁿ dx = xⁿ⁺¹/(n+1) + C. Ajoutez toujours + C.",
                        "real": "Aire, volume, distance à partir de la vitesse.",
                        "tip": "Vérifiez en dérivant votre réponse.",
                    },
                },
                "gen": "gen_integrals",
            },
            {
                "id": "definite", "icon": "2",
                "name": {"en": "Definite Integrals",
                         "fr": "Intégrales Définies"},
                "sub": {"en": "Area · FTC", "fr": "Aire · TFC"},
                "lesson": {
                    "intro": {
                        "en": "A definite integral computes exact area under a curve.",
                        "fr": "Une intégrale définie calcule l'aire exacte sous une courbe.",
                    },
                    "sections": [
                        {"h": {"en": "Fundamental Theorem",
                               "fr": "Théorème Fondamental"},
                         "p": {"en": "If F is an antiderivative of f:",
                               "fr": "Si F est une primitive de f :"},
                         "formula": "∫[a,b] f(x) dx = F(b) − F(a)"},
                    ],
                    "formula": "∫[a,b] f(x) dx = F(b) − F(a)",
                    "examples": [
                        {"t": {"en": "Evaluate", "fr": "Évaluer"},
                         "expr": "∫[0,2] x dx",
                         "sol": {"en": "= 2", "fr": "= 2"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Definite integral computes area under a curve.",
                        "formula": ("F(b) − F(a) — plug in upper then lower, "
                                    "subtract."),
                        "real": "Distance traveled, work, total revenue.",
                        "tip": "Write [F(x)] from a to b to avoid sign errors.",
                    },
                    "fr": {
                        "what": "L'intégrale définie calcule l'aire sous une courbe.",
                        "formula": ("F(b) − F(a) — remplacez par la borne supérieure "
                                    "puis inférieure."),
                        "real": "Distance parcourue, travail, revenu total.",
                        "tip": ("Écrivez [F(x)] de a à b pour éviter les erreurs "
                                "de signe."),
                    },
                },
                "gen": "gen_definite",
            },
            {
                "id": "series", "icon": "3",
                "name": {"en": "Sequences & Series",
                         "fr": "Suites & Séries"},
                "sub": {"en": "Convergence", "fr": "Convergence"},
                "lesson": {
                    "intro": {
                        "en": "A series is the sum of a sequence.",
                        "fr": "Une série est la somme d'une suite.",
                    },
                    "sections": [
                        {"h": {"en": "Geometric Series",
                               "fr": "Série Géométrique"},
                         "p": {"en": "For |r| < 1:", "fr": "Pour |r| < 1 :"},
                         "formula": "S = a₁/(1 − r)"},
                    ],
                    "formula": "S = a₁/(1 − r)",
                    "examples": [
                        {"t": {"en": "Sum", "fr": "Somme"},
                         "expr": "1 + 1/2 + 1/4 + …",
                         "sol": {"en": "= 2", "fr": "= 2"}},
                    ],
                },
                "tutor": {
                    "en": {
                        "what": "Series study sums of sequences.",
                        "formula": ("S = a₁/(1−r) for infinite geometric series "
                                    "with |r| < 1."),
                        "real": "Finance, physics, signal processing.",
                        "tip": "Always check |r| < 1 first.",
                    },
                    "fr": {
                        "what": "Les séries étudient les sommes de suites.",
                        "formula": ("S = a₁/(1−r) pour une série géométrique infinie "
                                    "avec |r| < 1."),
                        "real": "Finance, physique, traitement du signal.",
                        "tip": "Vérifiez toujours |r| < 1 d'abord.",
                    },
                },
                "gen": "gen_series",
            },
        ],
    },
}
