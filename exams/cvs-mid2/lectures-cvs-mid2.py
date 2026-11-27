"""Lectures in teaching order. Every concept card (and its guide section) belongs to exactly one.

Questions inherit their lecture from their concept card. "Past papers" groups hold the
Shams bank questions on lectures that were not uploaded.
"""
LECTURES = [
    {"id": "anat-l4", "unit": "Anatomy", "short": "Anatomy L4", "title": "Blood supply and surface anatomy of the heart",
     "concepts": ["anat-coronary", "anat-dominance", "anat-cardiac-veins", "anat-surface", "anat-pci"]},
    {"id": "anat-l5", "unit": "Anatomy", "short": "Anatomy L5", "title": "Blood supply of the head and neck",
     "concepts": ["anat-carotid", "anat-subclavian", "anat-facial-veins", "anat-neck-veins"]},
    {"id": "anat-pp", "unit": "Anatomy", "short": "Anatomy past papers", "title": "Limb vessels (past papers, no lecture uploaded)",
     "concepts": ["anat-limb-vessels"]},

    {"id": "phys-l6", "unit": "Physiology", "short": "Physiology L6", "title": "Electrocardiogram I: basic principles",
     "concepts": ["phys-ecg-leads", "phys-ecg-waves"]},
    {"id": "phys-l7", "unit": "Physiology", "short": "Physiology L7", "title": "Electrocardiogram II: analysis",
     "concepts": ["phys-ecg-rate", "phys-sinus", "phys-arrhythmia", "phys-av-block", "phys-axis"]},
    {"id": "phys-l8", "unit": "Physiology", "short": "Physiology L8", "title": "Cardiac output and venous return",
     "concepts": ["phys-co", "phys-autonomic", "phys-starling", "phys-venous-return", "phys-co-measure"]},
    {"id": "phys-l9", "unit": "Physiology", "short": "Physiology L9", "title": "Coronary circulation",
     "concepts": ["phys-coronary-flow", "phys-phasic-flow", "phys-coronary-control", "phys-ihd"]},
    {"id": "phys-pp", "unit": "Physiology", "short": "Physiology past papers", "title": "Resistance, baroreceptors and cardiac markers (past papers)",
     "concepts": ["phys-past"]},

    {"id": "path-l1", "unit": "Pathology", "short": "Pathology L1", "title": "Hemodynamic disorders I: hyperemia, edema, ischemia, infarction",
     "concepts": ["path-congestion", "path-edema", "path-ischemia-infarct"]},
    {"id": "path-l2", "unit": "Pathology", "short": "Pathology L2", "title": "Hemodynamic disorders II: thrombosis and embolism",
     "concepts": ["path-virchow", "path-thrombus-types", "path-embolism", "path-systemic-emboli"]},
    {"id": "path-l3", "unit": "Pathology", "short": "Pathology L3", "title": "Rheumatic fever and rheumatic heart disease",
     "concepts": ["path-arf", "path-jones", "path-rhd"]},
    {"id": "path-l4", "unit": "Pathology", "short": "Pathology L4", "title": "Atherosclerosis",
     "concepts": ["path-arteriosclerosis", "path-athero", "path-athero-complications"]},
    {"id": "path-pp", "unit": "Pathology", "short": "Pathology past papers", "title": "Endocarditis types, pyemia and MI healing (past papers)",
     "concepts": ["path-past"]},

    {"id": "pharm-l2-4", "unit": "Pharmacology", "short": "Pharmacology L2-L4", "title": "Treatment of hypertension",
     "concepts": ["pharm-classes", "pharm-diuretics", "pharm-ccb", "pharm-ras", "pharm-central", "pharm-alpha-beta", "pharm-vasodilators"]},
    {"id": "pharm-pp", "unit": "Pharmacology", "short": "Pharmacology past papers", "title": "Antiarrhythmics, lipid-lowering drugs and antianginals (past papers)",
     "concepts": ["pharm-antiarrhythmic", "pharm-lipid", "pharm-antianginal"]},

    {"id": "bio-l5", "unit": "Biochemistry", "short": "Biochemistry L5", "title": "Diet fat and coronary heart disease",
     "concepts": ["bio-lipids-chd", "bio-fats", "bio-cholesterol-sterols"]},
    {"id": "bio-l6", "unit": "Biochemistry", "short": "Biochemistry L6", "title": "Oxidative stress and atherosclerosis",
     "concepts": ["bio-ros", "bio-burst-no", "bio-oxldl"]},
    {"id": "bio-pp", "unit": "Biochemistry", "short": "Biochemistry past papers", "title": "Lipoproteins and eicosanoids (past papers)",
     "concepts": ["bio-lipoproteins", "bio-eicosanoids"]},

    {"id": "micro-l3", "unit": "Microbiology", "short": "Microbiology L3", "title": "Infective endocarditis",
     "concepts": ["micro-ie-types", "micro-organisms", "micro-patho", "micro-signs", "micro-dx-tx", "micro-lab-id"]},
    {"id": "micro-pp", "unit": "Microbiology", "short": "Microbiology past papers", "title": "Myocarditis and other CVS infections (past papers)",
     "concepts": ["micro-past"]},

    {"id": "emb-l3", "unit": "Embryology", "short": "Embryology L3", "title": "Development of the aortic arches and veins",
     "concepts": ["emb-arches", "emb-sac-dorsal", "emb-anomalies", "emb-veins"]},
    {"id": "emb-pp", "unit": "Embryology", "short": "Embryology past papers", "title": "Septum intermedium and umbilical ligaments (past papers)",
     "concepts": ["emb-past"]},
]
