"""Mastery Study Guide part: Biochemistry.

SECTIONS: one section per concept, in lecture order. "key" holds the Key ideas box;
every fact on a linked concept card must appear in its section (build-guide checks).
PROSE fills mechanism, priority actions, patient example, trap, memory trick and
tap-to-reveal blanks ([[answer]])."""

SECTIONS = [
    {"id": "bio-lipids-chd", "unit": "Biochemistry", "title": "Blood lipids and coronary heart disease", "source": "Biochemistry L5 slides (diet fat and CHD)",
     "key": [
         "Total blood cholesterol comes from diet and endogenous synthesis and is carried by lipoproteins, especially LDL and HDL.",
         "CHD risk rises with total and LDL cholesterol; high HDL-cholesterol is associated with decreased risk.",
         "Diet control lowers TC and LDL-C by 10-20%; statins lower them by 30-40%.",
     ]},
    {"id": "bio-fats", "unit": "Biochemistry", "title": "Types of dietary fat and their effects", "source": "Biochemistry L5 slides (diet fat and CHD)",
     "key": [
         "Saturated fats (no double bonds; dairy, meat, coconut and palm oils) raise TC and LDL-C and CHD risk.",
         "Monounsaturated fats (one double bond; olive oil, oleic acid, omega-9) lower TC and LDL-C and raise HDL-C when substituted for saturated fats.",
         "Omega-6 fats (first double bond at carbon 6 from the methyl end; corn, sesame, cottonseed, sunflower oils) lower TC and LDL-C but also lower HDL-C and are proinflammatory.",
         "Omega-3 fats suppress arrhythmia, reduce blood triacylglycerol, decrease thrombosis and inflammation, with little effect on LDL-C and HDL-C.",
         "Trans fats are chemically unsaturated but behave like saturated fats: they raise LDL-C and lower HDL-C; formed by partial hydrogenation of vegetable oils (margarine).",
     ]},
    {"id": "bio-cholesterol-sterols", "unit": "Biochemistry", "title": "Dietary cholesterol, plant sterols and cholesterol-lowering factors", "source": "Biochemistry L5 slides (diet fat and CHD)",
     "key": [
         "Dietary cholesterol is found only in animal products; its effect on blood cholesterol is less important than the amount and type of fatty acids.",
         "Plant sterols reduce LDL-cholesterol by inhibiting intestinal absorption of cholesterol.",
         "Dietary factors that decrease blood cholesterol: omega-6 PUFA, MUFA, antioxidants (beta carotene, vitamins E and C), plant sterols, vegetable fiber, large-dose vitamin B3.",
     ]},
    {"id": "bio-ros", "unit": "Biochemistry", "title": "Free radicals, ROS and RNS", "source": "Biochemistry L6 slides (oxidative stress)",
     "key": [
         "Oxidative stress: an imbalance favoring oxidants and/or disfavoring antioxidants, potentially leading to damage.",
         "A free radical is a molecule with an unpaired electron in an outer valence shell; it plucks an electron from the nearest molecule.",
         "ROS radicals: superoxide, hydroxyl, peroxyl. ROS non-radicals: hydrogen peroxide, hypochlorous acid, ozone.",
         "RNS radicals: nitric oxide, nitrogen dioxide. RNS non-radical: peroxynitrite.",
         "Endogenous sources: electron leak from the respiratory chain, oxidases (xanthine oxidase), prostaglandin synthesis, NO from arginine, phagocytosis. Exogenous: drug metabolism (halothane, cytochrome P450), ionizing radiation, cigarette smoke.",
     ]},
    {"id": "bio-burst-no", "unit": "Biochemistry", "title": "Respiratory burst, nitric oxide and antioxidants", "source": "Biochemistry L6 slides (oxidative stress)",
     "key": [
         "Respiratory burst: NADPH oxidase converts O2 to superoxide; superoxide dismutase makes H2O2; myeloperoxidase converts H2O2 and chloride to hypochlorous acid, which kills bacteria.",
         "NO is a free radical gas with a half-life of seconds, made from L-arginine by NO synthase.",
         "eNOS and nNOS are constitutive and make low levels of NO; iNOS (macrophages, neutrophils; induced by bacterial toxins, TNF, cytokines) makes large amounts for hours or days.",
         "eNOS-derived NO improves vascular dilation and perfusion; nitroglycerin is metabolized to NO and relieves coronary spasm in angina.",
         "Enzymatic antioxidants: superoxide dismutase, catalase, glutathione peroxidase. Nutrient antioxidants: vitamins A, E, C, selenium. Metabolic: glutathione, ceruloplasmin, albumin, transferrin, ferritin, uric acid.",
     ]},
    {"id": "bio-oxldl", "unit": "Biochemistry", "title": "Oxidized LDL and the stages of atherosclerosis", "source": "Biochemistry L6 slides (oxidative stress)",
     "key": [
         "Free radicals oxidize LDL cholesterol; oxidized LDL triggers inflammation and plaque buildup.",
         "Stages: endothelial dysfunction, LDL retention and oxidation in the intima, recruitment of monocytes and T cells by VCAM-1, ICAM-1 and MCP-1, foam cell formation (fatty streak), SMC migration and fibrous cap, necrotic core and calcification, rupture or erosion with thrombosis.",
         "Macrophages engulf oxidized LDL via scavenger receptors and become lipid-laden foam cells.",
         "Failure to clear dead macrophages and SMCs (impaired efferocytosis) enlarges an acellular necrotic core.",
     ]},
]
PROSE = {
"bio-lipids-chd": dict(
    mechanism="Cholesterol travels in blood packed in lipoproteins. LDL carries it to tissues and raises coronary risk; HDL is associated with lower risk. Lowering LDL by diet or drugs lowers risk.",
    actions=["Encourage diet control and expect a 10-20% fall; expect 30-40% with statins.",
             "Read a high HDL as protective."],
    example="A client with high LDL asks whether diet alone is enough: it lowers LDL by about 10-20%.",
    trap="Treating all cholesterol as bad: high HDL lowers risk.",
    trick="LDL = Lousy, HDL = Helpful.",
    blanks=["Elevated [[LDL]] cholesterol increases the risk of CHD."]),
"bio-fats": dict(
    mechanism="A fat's effect depends on its fatty acids: saturation, the number and position of double bonds, and cis or trans shape. Omega numbers count from the methyl end to the first double bond.",
    actions=["Advise limiting saturated and trans fats.",
             "Suggest olive oil (MUFA) and fatty fish (omega-3).",
             "Teach the label clue \"partially hydrogenated\"."],
    example="A client switches butter for olive oil: LDL falls and HDL rises.",
    trap="Thinking omega-3 mainly lowers LDL; its main effect is on triacylglycerol, arrhythmia, thrombosis and inflammation.",
    trick="SMASH fish for omega-3: salmon, mackerel, anchovies, sardines, herring.",
    blanks=["Trans fats should be under [[1%]] of energy (under 2.2 g per day on 2000 kcal).",
            "EPA has [[20]] carbons and 5 double bonds; DHA has 22 carbons and 6."]),
"bio-cholesterol-sterols": dict(
    mechanism="Dietary cholesterol matters less than the fat mix. Plant sterols compete with cholesterol in the gut, so less is absorbed and LDL falls.",
    actions=["Correct a client who focuses only on dietary cholesterol.",
             "Suggest plant-sterol margarines, fiber and MUFA."],
    example="A client says eaten cholesterol matters more than fat type: needs further teaching.",
    trap="Thinking plant foods contain cholesterol.",
    trick="Cholesterol only comes with a face (animal products).",
    blanks=["Plant sterols reduce LDL by inhibiting intestinal [[absorption]] of cholesterol."]),
"bio-ros": dict(
    mechanism="A free radical has an unpaired outer electron and steals one from the nearest molecule, starting chain damage to lipids, proteins and DNA. Non-radicals have no unpaired electron but are strong oxidants. Damage occurs when oxidants outrun antioxidants.",
    actions=["Classify each species as radical or non-radical.",
             "Separate endogenous (metabolism, phagocytosis) from exogenous (drugs, radiation, smoke) sources."],
    example="A smoker has an exogenous source of free radicals in cigarette smoke.",
    trap="Calling H2O2 a radical.",
    trick="Radicals end with a dot: O2.-, OH., NO.",
    blanks=["Peroxynitrite is a reactive nitrogen [[non-radical]]."]),
"bio-burst-no": dict(
    mechanism="Reactive species are also tools. Neutrophils make superoxide, H2O2 and hypochlorous acid to kill bacteria. Endothelial NO dilates vessels. Antioxidant enzymes and nutrients keep the balance.",
    actions=["Link sepsis and inflammation to large iNOS output.",
             "Explain nitroglycerin works by becoming NO."],
    example="A client's angina is relieved by nitroglycerin, which is metabolized to nitric oxide.",
    trap="Mixing up constitutive eNOS (low, steady) with inducible iNOS (large, prolonged).",
    trick="i for inducible and inflammatory.",
    blanks=["The enzyme that converts H2O2 and chloride into hypochlorous acid is [[myeloperoxidase]].",
            "NO synthase uses [[L-arginine]] as its precursor."]),
"bio-oxldl": dict(
    mechanism="Oxidation turns LDL into a danger signal. Oxidized LDL in the intima activates endothelium to recruit monocytes; macrophages take it up by scavenger receptors and become foam cells. Smooth muscle cells build a cap, dead cells pile up into a necrotic core, and a vulnerable plaque can rupture.",
    actions=["Trace the stages in order from endothelial dysfunction to thrombosis.",
             "Link impaired efferocytosis to the necrotic core."],
    example="A client's plaque ruptures and exposes thrombogenic material, causing an MI.",
    trap="Thinking VCAM-1 is on macrophages; it is on activated endothelial cells.",
    trick="Dysfunction, Oxidation, Recruitment, Foam, Cap, Core, Clot.",
    blanks=["Monocytes are captured by [[VCAM-1]] and ICAM-1 on activated endothelium."]),
}
for _s in SECTIONS:
    _s.update(PROSE[_s["id"]])

# ---------------------------------------------------------------- past-paper sections (Shams Practices QB)
SECTIONS += [
    {"id": "bio-lipoproteins", "unit": "Biochemistry", "title": "Lipoproteins and cholesterol metabolism (past papers)", "source": "Shams Practices QB (past papers); not in your uploaded slides",
     "key": [
         "Statins competitively inhibit HMG CoA reductase, the enzyme insulin activates in the fed state.",
         "In hypothyroidism cholesterol is high because conversion of cholesterol to bile acids is impaired.",
         "Apo B-100 is the structural apolipoprotein of VLDL; nascent chylomicrons and VLDL get apo C-II and apo E from HDL.",
         "Apo C-II activates lipoprotein lipase; apo A-I activates LCAT, which converts free cholesterol to cholesterol esters.",
         "Fatty liver: the liver makes more triglyceride than it can export as VLDL.",
         "Tangier disease: low HDL. Abetalipoproteinemia: decreased VLDL and chylomicrons.",
     ]},
    {"id": "bio-eicosanoids", "unit": "Biochemistry", "title": "Eicosanoids: COX-2 and prostacyclin (past papers)", "source": "Shams Practices QB (past papers); not in your uploaded slides",
     "key": [
         "COX-2 makes the prostaglandins of the inflammatory response.",
         "Prostacyclin (PGI2) is a vasodilator.",
     ]},
]
PROSE_PAST = {'bio-lipoproteins': {'mechanism': 'Lipoproteins carry fat in the blood: the intestine makes chylomicrons (apo B-48) and the liver makes VLDL (apo B-100). HDL donates apo C-II and apo E to them; apo C-II activates lipoprotein lipase to unload triglyceride, and apo A-I activates LCAT to esterify cholesterol on HDL. Cholesterol synthesis is controlled at HMG CoA reductase (activated by insulin, blocked by statins), and cholesterol leaves the body as bile acids. Your uploaded lectures do not cover this; the facts come from the past-paper keys.', 'actions': ['Match each apo to its job: B-100 VLDL structure, B-48 chylomicron, C-II activates LPL, A-I activates LCAT.', 'Hypothyroidism with high cholesterol: less conversion to bile acids.', 'Fatty liver: triglyceride made faster than VLDL can export it.'], 'example': 'A client with Tangier disease has orange tonsils and a very low HDL.', 'trap': 'Mixing up apo B-100 (VLDL, LDL) and apo B-48 (chylomicrons).', 'trick': "B-48 is the Bowel's apo; B-100 is the liver's full-length one.", 'blanks': ['Apo C-II activates [[lipoprotein lipase]].', 'Abetalipoproteinemia lowers both [[VLDL]] and chylomicrons.']}, 'bio-eicosanoids': {'mechanism': 'Eicosanoids are made from fatty acids. COX-2 is induced in inflammation and makes inflammatory prostaglandins; prostacyclin (PGI2) from the vessel wall dilates vessels. Your slides list prostaglandin synthesis as a source of free radicals; the rest comes from the past-paper keys.', 'actions': ['Link COX-2 to inflammation and PGI2 to vasodilation.'], 'example': 'A question on the enzyme behind inflammatory prostaglandins: COX-2.', 'trap': 'Calling PGI2 a promoter of platelet aggregation; that is thromboxane A2.', 'trick': 'PGI2 = Protects (dilates, stops platelets).', 'blanks': ['PGI2 is a [[vasodilator]].']}}
for _s in SECTIONS:
    if _s["id"] in PROSE_PAST:
        _s.update(PROSE_PAST[_s["id"]])
