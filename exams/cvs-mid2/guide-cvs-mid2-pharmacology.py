"""Mastery Study Guide part: Pharmacology.

SECTIONS: one section per concept, in lecture order. "key" holds the Key ideas box;
every fact on a linked concept card must appear in its section (build-guide checks).
PROSE fills mechanism, priority actions, patient example, trap, memory trick and
tap-to-reveal blanks ([[answer]])."""

SECTIONS = [
    {"id": "pharm-classes", "unit": "Pharmacology", "title": "Hypertension: definition and drug classes", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Hypertension is defined as 130/80 mm Hg or higher (ACC/AHA 2023 and Saudi Heart Association).",
         "Classes: diuretics, calcium channel blockers, drugs acting on the renin-angiotensin system, sympatholytic drugs, vasodilators.",
         "Drug list: hydrochlorothiazide, indapamide, furosemide, spironolactone (diuretics); clonidine, methyldopa, prazosin, propranolol, labetalol, esmolol (sympathoplegic); hydralazine, nitroprusside, minoxidil, diazoxide, fenoldopam, CCBs (vasodilators); captopril, enalapril, enalaprilat (ACE inhibitors); losartan (ARB); aliskiren (renin inhibitor).",
     ]},
    {"id": "pharm-diuretics", "unit": "Pharmacology", "title": "Diuretics in hypertension", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Early: diuretics lower plasma volume and cardiac output. After 4-8 weeks volume and output return toward normal while peripheral vascular resistance falls (arteriolar vasodilation).",
         "Main mechanism of the vasodilation: depletion of body Na+, lowering smooth muscle Na+ and then intracellular Ca++ via the Na/Ca exchanger.",
         "Thiazides are first choice; antihypertensive doses are lower than diuretic doses.",
         "Loop diuretics are preferable in malignant hypertension and chronic kidney disease.",
         "Potassium-sparing diuretics are used with thiazides to counteract hypokalemia; spironolactone is used in hyperaldosteronism.",
     ]},
    {"id": "pharm-ccb", "unit": "Pharmacology", "title": "Calcium channel blockers", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "CCBs bind the L-type voltage-gated Ca++ channel from the inner side of the membrane.",
         "Verapamil and diltiazem block Ca++ channels in heart and vessels; dihydropyridines (nifedipine, nicardipine) block vessels only.",
         "Heart rate: increased with dihydropyridines; unchanged or decreased with verapamil and diltiazem. Postural hypotension is negligible.",
         "First-choice drugs, more effective in African patients; nicardipine for hypertensive emergencies; short-acting nifedipine increases mortality.",
     ]},
    {"id": "pharm-ras", "unit": "Pharmacology", "title": "Renin inhibitors, ACE inhibitors and ARBs", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Aliskiren competitively inhibits renin: angiotensin I, II and aldosterone fall and renin rises; hyperkalemia when combined with ACE inhibitors or ARBs.",
         "ACE inhibitors block conversion of angiotensin I to II and raise bradykinin; less angiotensin II removes negative feedback, so renin rises.",
         "Captopril, lisinopril and enalaprilat are active drugs; enalapril, benazepril and fosinopril are prodrugs activated by the liver; enalaprilat is the IV form.",
         "ACE inhibitor adverse effects: first-dose hypotension, dry cough (bradykinin, prostaglandins or substance P), renal insufficiency in bilateral renal artery stenosis, hyperkalemia, angioedema; pregnancy category D.",
         "ARBs (losartan) selectively block AT1 receptors, inhibit angiotensin more completely and have no effect on bradykinin; contraindicated in bilateral renal artery stenosis and pregnancy.",
     ]},
    {"id": "pharm-central", "unit": "Pharmacology", "title": "Centrally acting sympatholytics", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Clonidine and methyldopa are alpha-2 receptor agonists; methyldopa is a false neurotransmitter converted to methylnorepinephrine; clonidine also acts on imidazoline receptors in the medulla.",
         "The final common effect is a decrease in central adrenergic tone.",
         "Second-choice drugs; methyldopa is often preferred in pregnancy.",
         "Adverse effects: sedation, depression, bradycardia, AV block, sexual dysfunction; clonidine withdrawal can cause a hypertensive crisis; methyldopa can cause a positive Coombs' test.",
     ]},
    {"id": "pharm-alpha-beta", "unit": "Pharmacology", "title": "Alpha blockers, beta blockers and alpha-beta blockers", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Prazosin and doxazosin selectively block alpha-1 receptors, dilating resistance and capacitance vessels; postural hypotension after the first dose (\"first-dose phenomenon\").",
         "Beta blockers lower cardiac output (cardiac beta-1) and inhibit renin release (juxtaglomerular beta-1); they do not cause postural hypotension.",
         "Selective beta-1: atenolol, bisoprolol, metoprolol. Non-selective: propranolol, penbutolol, timolol.",
         "Beta-blocker adverse effects: bradycardia, rebound hypertension on abrupt withdrawal, bronchoconstriction, insomnia, depression, hypoglycemia, sexual dysfunction.",
         "Labetalol and carvedilol block alpha and beta; labetalol for hypertension in pregnancy and IV in emergencies; carvedilol for heart failure.",
     ]},
    {"id": "pharm-vasodilators", "unit": "Pharmacology", "title": "Direct vasodilators", "source": "Pharmacology L2-L4 slides (treatment of hypertension)",
     "key": [
         "Nitroprusside: arterioles and veins, nitric oxide; metabolized by red cells releasing cyanide (to thiocyanate); half-life about 2 minutes, continuous infusion; for emergencies, severe heart failure, controlled hypotension.",
         "Hydralazine: arterioles, uncertain mechanism; headache, palpitations, flushing; immunological lupoid syndrome (up to 20% at very high doses).",
         "Minoxidil: arteriolar K+ channel opener, a prodrug; salt and water retention, tachycardia, hypertrichosis; also used for baldness.",
         "Diazoxide: K+ channel opener without diuresis (lacks a sulfonamide group); salt and water retention, hyperglycemia; for hypertensive emergencies.",
         "Fenoldopam: IV D1 agonist, renal and mesenteric vasodilation and natriuresis; reflex tachycardia, raised intraocular pressure, low potassium; contraindicated in angina, glaucoma and hypokalemia.",
     ]},
]
PROSE = {
"pharm-classes": dict(
    mechanism="Blood pressure is cardiac output times peripheral resistance, kept up by volume, the sympathetic system and the renin-angiotensin system. Each drug class removes one of these supports: diuretics (volume), sympatholytics (nerves), RAS drugs (angiotensin), CCBs and vasodilators (vessel tone).",
    actions=["Classify every drug on a client's list before giving it.",
             "Use the current threshold: 130/80 mm Hg or higher is hypertension."],
    example="A client's readings average 132/82: hypertension by the ACC/AHA and SHA definitions.",
    trap="Using the old 140/90 threshold.",
    trick="-pril = ACE inhibitor, -sartan = ARB, -olol = beta blocker, -dipine = dihydropyridine CCB.",
    blanks=["The only renin inhibitor listed is [[aliskiren]]."]),
"pharm-diuretics": dict(
    mechanism="Diuretics lower pressure first by shrinking plasma volume and cardiac output. Over 4-8 weeks the volume recovers but resistance falls: sodium depletion lowers smooth muscle Na+, which lowers intracellular Ca++ through the Na/Ca exchanger, relaxing arterioles.",
    actions=["Use thiazides first in normal renal function; loop diuretics in CKD or malignant hypertension.",
             "Add a potassium-sparing diuretic to a thiazide to counteract hypokalemia; spironolactone for hyperaldosteronism."],
    example="A client 6 weeks into thiazide therapy has normal urine output but a lower blood pressure: peripheral resistance has fallen.",
    trap="Believing diuretics work only by making urine.",
    trick="Thiazide first, Loop for kidney failure, K-sparing for K.",
    blanks=["Diuretics can [[enhance]] the hypotensive effects of many antihypertensive agents."]),
"pharm-ccb": dict(
    mechanism="CCBs block L-type Ca++ channels, so less calcium enters smooth muscle (and, for verapamil and diltiazem, heart muscle). Dihydropyridines act on vessels only, so heart rate may rise; verapamil and diltiazem also slow the heart.",
    actions=["Expect a possible rise in heart rate with nifedipine and a fall with verapamil or diltiazem.",
             "Use nicardipine for hypertensive emergencies; avoid short-acting nifedipine."],
    example="A client starting nifedipine has a slightly faster pulse.",
    trap="Expecting nifedipine to slow the heart like verapamil.",
    trick="Dihydropyridine = Dilates only; Verapamil = Ventricle too.",
    blanks=["CCBs are first-choice drugs and are more effective in [[African]] patients.",
            "Nicardipine has [[very high]] vascular selectivity."]),
"pharm-ras": dict(
    mechanism="Renin turns angiotensinogen into angiotensin I, ACE turns angiotensin I into angiotensin II (and breaks down bradykinin), and angiotensin II acts on AT1 receptors. Blocking any step lowers angiotensin II effects; the step blocked decides the side effects: ACE inhibitors raise bradykinin (cough, angioedema), ARBs do not.",
    actions=["Monitor potassium, renal function, first-dose blood pressure and the airway (angioedema).",
             "Question ACE inhibitors and ARBs in pregnancy and bilateral renal artery stenosis.",
             "Switch to an ARB when an ACE inhibitor causes cough."],
    example="A client on captopril develops a dry cough and is switched to losartan.",
    trap="Thinking losartan inhibits ACE.",
    trick="ACE inhibitors Accumulate bradykinin; ARBs Avoid it.",
    blanks=["The ACE inhibitor given intravenously is [[enalaprilat]].",
            "ARBs selectively block [[AT1]] receptors."]),
"pharm-central": dict(
    mechanism="Clonidine and methyldopa act in the brain: they stimulate central alpha-2 (and, for clonidine, imidazoline) receptors that turn down sympathetic outflow. Methyldopa first has to be converted to methylnorepinephrine inside neurons.",
    actions=["Teach clients on clonidine never to stop it suddenly.",
             "Prefer methyldopa in pregnancy.",
             "Expect sedation; check for a positive Coombs' test with methyldopa."],
    example="A client on clonidine wants to stop abruptly; the nurse warns of a hypertensive crisis.",
    trap="Thinking methyldopa is unsafe in pregnancy.",
    trick="Clonidine: don't Cut it suddenly. Methyldopa: Mothers.",
    blanks=["Transdermal clonidine causes skin eruption in up to [[20%]] of clients."]),
"pharm-alpha-beta": dict(
    mechanism="Alpha-1 blockers dilate arterioles and veins, so standing can drop the pressure, especially after the first dose. Beta blockers lower cardiac output and renin release and leave veins alone, so they do not cause postural hypotension but can slow the heart, narrow airways and mask or cause low glucose.",
    actions=["After a first prazosin dose, monitor for postural hypotension.",
             "Choose a beta-1 selective drug (atenolol, bisoprolol, metoprolol) when airways are a concern.",
             "Never stop a beta blocker abruptly: rebound hypertension."],
    example="A client with heart failure and hypertension is treated with carvedilol.",
    trap="Expecting postural hypotension from a pure beta blocker.",
    trick="A for alpha-1 and Arise-dizzy; B for beta and Bradycardia, Bronchospasm, Blood sugar low.",
    blanks=["IV [[labetalol]] is used for hypertensive emergencies.",
            "Peripheral edema with alpha blockers after chronic treatment is due to [[sodium and water]] retention."]),
"pharm-vasodilators": dict(
    mechanism="Direct vasodilators relax vessel smooth muscle by different routes: NO (nitroprusside), K+ channel opening (minoxidil, diazoxide), D1 activation (fenoldopam) or an uncertain mechanism (hydralazine). Their toxicities are drug-specific and well worth memorizing.",
    actions=["During nitroprusside infusion, watch for cyanide toxicity.",
             "Check glucose with diazoxide, hair growth with minoxidil, lupus-like symptoms with high-dose hydralazine.",
             "Question fenoldopam in glaucoma, angina or hypokalemia."],
    example="A client on minoxidil notices new hair growth: hypertrichosis.",
    trap="Expecting diazoxide to cause diuresis like a thiazide.",
    trick="Nitroprusside: Nitric oxide and cyaNide. Minoxidil: More hair. Diazoxide: Diabetes-like sugar.",
    blanks=["Nitroprusside is metabolized by red blood cells, releasing cyanide that becomes [[thiocyanate]].",
            "Hydralazine is combined with isosorbide mononitrate in [[heart failure]]."]),
}
for _s in SECTIONS:
    _s.update(PROSE[_s["id"]])

# ---------------------------------------------------------------- past-paper sections (Shams Practices QB)
SECTIONS += [
    {"id": "pharm-antiarrhythmic", "unit": "Pharmacology", "title": "Antiarrhythmic drugs (past papers)", "source": "Shams Practices QB (past papers); not in your uploaded slides",
     "key": [
         "Class I antiarrhythmics block Na+ channels: quinidine and procainamide (IA, also block K+), lidocaine (IB), flecainide (IC, no effect on action potential duration).",
         "Quinidine causes cinchonism: headache, dizziness and tinnitus.",
         "Class III antiarrhythmics block K+ channels: sotalol (also a beta blocker) and amiodarone.",
         "Amiodarone treats both ventricular and supraventricular arrhythmias; it can cause pulmonary fibrosis and gray-blue (smurf) skin.",
         "Adenosine is the choice for paroxysmal supraventricular tachycardia; esmolol is used intraoperatively.",
     ]},
    {"id": "pharm-lipid", "unit": "Pharmacology", "title": "Lipid-lowering drugs (past papers)", "source": "Shams Practices QB (past papers); not in your uploaded slides",
     "key": [
         "Statins (lovastatin, atorvastatin) competitively inhibit HMG CoA reductase; they can cause muscle pain and rhabdomyolysis.",
         "Niacin lowers triglycerides and raises HDL; adverse effects are skin flushing and hyperuricemia.",
         "Fenofibrate is the drug of choice for hypertriglyceridemia; ezetimibe selectively inhibits intestinal cholesterol absorption; cholestyramine binds bile acids in the intestine.",
     ]},
    {"id": "pharm-antianginal", "unit": "Pharmacology", "title": "Nitrates and beta blockers in angina (past papers)", "source": "Shams Practices QB (past papers); nitrates and beta blockers for IHD are on Physiology L9 slides",
     "key": [
         "Nitrate tolerance is treated by a nitrate-free interval (no therapy for a brief time).",
         "Beta blockers relieve angina by decreasing myocardial O2 demand.",
     ]},
]
PROSE_PAST = {'pharm-antiarrhythmic': {'mechanism': 'Antiarrhythmics are grouped by the channel or receptor they block: class I sodium channels, class II beta receptors, class III potassium channels and class IV calcium channels. Many questions test one signature adverse effect per drug. This lecture is not among your uploads; the facts come from the past-paper keys.', 'actions': ['Classify first: Na+ = I, beta = II, K+ = III, Ca++ = IV.', 'Match adverse effects: quinidine = cinchonism (headache, tinnitus); amiodarone = pulmonary fibrosis and blue-gray skin.', 'PSVT: adenosine. Intraoperative rate control: esmolol.'], 'example': 'After treatment for a ventricular arrhythmia a client reports tinnitus and headache: quinidine.', 'trap': 'Thinking sotalol is a pure beta blocker; it also blocks K+ channels (class III).', 'trick': 'Quinidine Quiets your hearing (tinnitus); Amiodarone turns you Azure.', 'blanks': ['Class III antiarrhythmics block [[potassium]] channels.', 'Flecainide is class [[IC]].']}, 'pharm-lipid': {'mechanism': 'Lipid-lowering drugs attack different steps: statins block cholesterol synthesis at HMG CoA reductase, ezetimibe blocks intestinal absorption, cholestyramine traps bile acids in the gut, fibrates lower triglycerides, and niacin lowers triglycerides while raising HDL. Your slides cover only the statin effect size (30-40% LDL reduction) and large-dose vitamin B3 as a cholesterol-lowering factor.', 'actions': ['Muscle pain or rhabdomyolysis on a lipid drug: suspect a statin.', 'High triglycerides: fenofibrate; high TG with low HDL despite a statin: niacin.', 'Warn about flushing and hyperuricemia with niacin.'], 'example': 'A client on lovastatin develops muscle pain.', 'trap': 'Mixing up ezetimibe (absorption) and cholestyramine (bile acid binding).', 'trick': 'Statins Stop synthesis; Ezetimibe Excludes absorption; Cholestyramine Captures bile.', 'blanks': ['Statins competitively inhibit [[HMG CoA reductase]].']}, 'pharm-antianginal': {'mechanism': "Your coronary circulation slides list nitrates and beta blockers as treatments for ischemic heart disease. Past papers add how: beta blockers lower heart rate and contractility and so the heart's O2 demand, and continuous nitrate exposure causes tolerance, prevented by a nitrate-free interval.", 'actions': ['Schedule a daily nitrate-free interval to avoid tolerance.', 'Explain beta blockers in angina as lowering O2 demand.'], 'example': 'A client whose nitrates have stopped working is given a nitrate-free interval.', 'trap': 'Treating nitrate tolerance with MORE frequent or continuous nitrate.', 'trick': 'Tolerance? Take a break.', 'blanks': ['Beta blockers relieve angina by decreasing myocardial [[O2 demand]].']}}
for _s in SECTIONS:
    if _s["id"] in PROSE_PAST:
        _s.update(PROSE_PAST[_s["id"]])
