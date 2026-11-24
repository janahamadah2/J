"""Shams Practices CVS MID-2 QB (past papers): Pharmacology. Wording, options and key as printed (typos fixed).

Antiarrhythmics, lipid-lowering drugs and nitrates are not in the uploaded hypertension
lecture; those answers come from the bank's key.
"""
from _authoring import Bank

B = Bank("Pharmacology")
SL = "Shams Practices QB, %s; Pharmacology L2-L4 slides (treatment of hypertension)"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"
GI = "is a gastrointestinal drug (acid suppression or laxative), unrelated to the heart."

# ---------------------------------------------------------------- hypertension (on slides)
B.join("pharm-ras")
B.keyed("A woman with hypertension is in early pregnancy. Which antihypertensive is contraindicated because it is an angiotensin-converting enzyme (ACE) inhibitor?",
        ["Labetalol", "Methyldopa", "Enalapril", "Extended-release nifedipine"], "c",
        "ACE inhibitors such as enalapril are pregnancy category D and should not be used in pregnancy. Methyldopa is often preferred and labetalol is used for hypertension in pregnancy.",
        {"a": "Labetalol is an alpha-beta blocker used for hypertension in pregnancy.",
         "b": "Methyldopa is often preferred in pregnancy because it is not harmful to the fetus.",
         "d": "Nifedipine is a dihydropyridine CCB, not an ACE inhibitor."},
        SL % "2025 Q26", labels={"b": "thinks methyldopa is unsafe in pregnancy"})

B.keyed("A patient taking lisinopril and amlodipine for hypertension develops hyperkalemia. Which medication is the most likely cause?",
        ["Amlodipine", "Lisinopril", "Acetaminophen", "Loratadine"], "b",
        "ACE inhibitors such as lisinopril reduce angiotensin II and aldosterone and cause hyperkalemia. Amlodipine is a dihydropyridine CCB and does not raise potassium.",
        {"a": "Amlodipine is a calcium channel blocker, which does not cause hyperkalemia.",
         "c": "Acetaminophen is a pain reliever, not an antihypertensive.",
         "d": "Loratadine is an antihistamine."},
        SL % "2025 Q27")

B.keyed("Which ACE inhibitor can be administered intravenously to treat hypertension when oral therapy is impractical?",
        ["Captopril", "Lisinopril", "Ramipril", "Enalaprilat"], "d",
        "All ACE inhibitors except enalaprilat are given orally only; enalaprilat is the IV form used in hypertensive emergencies.",
        {"a": "Captopril is given by mouth only.",
         "b": "Lisinopril is given by mouth only.",
         "c": "Ramipril is an oral ACE inhibitor (a prodrug)."},
        SL % "2025 Q30", labels={"a": "thinks captopril can be given IV"})

B.join("pharm-diuretics")
B.keyed("Which change has been proposed to contribute to the long-term vasodilator effect of thiazide diuretics?",
        ["Increased intracellular calcium in vascular smooth muscle", "Increased alpha₁-receptor stimulation in vascular smooth muscle", "Increased endothelin-mediated vasoconstriction", "Decreased sodium content in vascular smooth muscle"], "d",
        "Depletion of body Na+ lowers smooth muscle Na+, which lowers intracellular Ca++ through the Na/Ca exchanger and relaxes arterioles.",
        {"a": "Intracellular calcium FALLS, which is why the vessels relax.",
         "b": "Alpha-1 stimulation would constrict vessels.",
         "c": "Endothelin-mediated vasoconstriction would raise resistance."},
        SL % "2025 Q28", labels={"a": "reverses the calcium effect of diuretics"})

B.join("pharm-vasodilators")
B.keyed("Which potentially toxic metabolite can accumulate during a prolonged intravenous infusion of sodium nitroprusside?",
        ["Urea", "Thiocyanate", "Bilirubin", "Creatinine"], "b",
        "Red blood cells metabolize nitroprusside, releasing cyanide, which is converted to thiocyanate; both can accumulate with prolonged infusion.",
        {"a": "Urea is a normal nitrogen waste product.",
         "c": "Bilirubin comes from hemoglobin breakdown.",
         "d": "Creatinine comes from muscle creatine."},
        SL % "2025 Q29")

# ---------------------------------------------------------------- antiarrhythmics (past papers)
B.concept("pharm-antiarrhythmic", "Antiarrhythmic drugs (past papers)", [
    "Class I antiarrhythmics block Na+ channels: quinidine and procainamide (IA, also block K+), lidocaine (IB), flecainide (IC, no effect on action potential duration).",
    "Quinidine causes cinchonism: headache, dizziness and tinnitus.",
    "Class III antiarrhythmics block K+ channels: sotalol (also a beta blocker) and amiodarone.",
    "Amiodarone treats both ventricular and supraventricular arrhythmias; it can cause pulmonary fibrosis and gray-blue (smurf) skin.",
    "Adenosine is the choice for paroxysmal supraventricular tachycardia; esmolol is used intraoperatively.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("Beta blocker drug that can also block K channels?",
        ["Atenolol", "Metoprolol", "Sotalol", "Esmolol"], "c",
        "Sotalol is a beta blocker that also blocks K+ channels, so it acts as a class III antiarrhythmic. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Atenolol is a selective beta-1 blocker without K+ channel block.",
         "b": "Metoprolol is a selective beta-1 blocker without K+ channel block.",
         "d": "Esmolol is a short-acting beta-1 blocker without K+ channel block."},
        NS % "2024 Nov Q56")

B.keyed("During antiarrhythmic treatment a patient suffers from headache and tinnitus. Which drug is the cause?",
        ["Quinidine", "Omeprazole", "Metformin", "Levothyroxine"], "a",
        "Quinidine causes cinchonism: headache, dizziness and tinnitus. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Omeprazole " + GI, "c": "Metformin is a diabetes drug.", "d": "Levothyroxine is thyroid hormone replacement."},
        NS % "2024 Nov Q57")

B.keyed("In paroxysmal supraventricular tachycardia we choose?",
        ["Atorvastatin", "Adenosine", "Levothyroxine", "Omeprazole"], "b",
        "Adenosine is the drug of choice to stop paroxysmal supraventricular tachycardia. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Atorvastatin is a statin for high cholesterol.", "c": "Levothyroxine is thyroid hormone replacement.", "d": "Omeprazole " + GI},
        NS % "2024 Nov Q59")

B.keyed("Which drug blocks Na and K channels?",
        ["Procainamide", "Omeprazole", "Metformin", "Levothyroxine"], "a",
        "Procainamide is a class IA antiarrhythmic that blocks both Na+ and K+ channels. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Omeprazole " + GI, "c": "Metformin is a diabetes drug.", "d": "Levothyroxine is thyroid hormone replacement."},
        NS % "2024 May Q83")

B.keyed("A patient came to the ER complaining of ventricular arrhythmia. After treatment the patient complained of headaches, dizziness and tinnitus. Which drug caused those symptoms?",
        ["Adenosine", "Esmolol", "Atropine", "Quinidine"], "d",
        "Headache, dizziness and tinnitus are cinchonism, the classic adverse effect of quinidine. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Adenosine causes brief flushing and chest discomfort, not tinnitus.",
         "b": "Esmolol is a short-acting beta blocker.",
         "c": "Atropine is an anticholinergic used for bradycardia."},
        NS % "2024 May Q84")

B.keyed("Which drug works on both ventricular and supraventricular arrhythmias?",
        ["Atorvastatin", "Amiodarone", "Famotidine", "Levothyroxine"], "b",
        "Amiodarone is a broad-spectrum antiarrhythmic effective in both ventricular and supraventricular arrhythmias. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Atorvastatin is a statin.", "c": "Famotidine " + GI, "d": "Levothyroxine is thyroid hormone replacement."},
        NS % "2024 May Q85")

B.keyed("Which of the following drugs is not in class I?",
        ["Quinidine", "Lidocaine", "Flecainide", "Amiodarone"], "d",
        "Quinidine (IA), lidocaine (IB) and flecainide (IC) are class I Na+ channel blockers; amiodarone is class III. Note: the paper prints only options a-c but keys \"d\"; option d, \"Amiodarone\", is restored here as the class III drug used elsewhere in this bank. Not in your uploaded Mid 2 slides.",
        {"a": "Quinidine is a class IA antiarrhythmic.", "b": "Lidocaine is a class IB antiarrhythmic.", "c": "Flecainide is a class IC antiarrhythmic."},
        NS % "2023 Q111")

B.keyed("A patient came to the clinic with pulmonary fibrosis; respiratory cultures were negative, and he noted he had taken an antiarrhythmic drug. Which drug do you suspect?",
        ["Amiodarone", "Adenosine", "Esmolol", "Lidocaine"], "a",
        "Amiodarone causes pulmonary fibrosis. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Adenosine acts for seconds and does not cause fibrosis.",
         "c": "Esmolol is a short-acting beta blocker.",
         "d": "Lidocaine is a class IB drug that does not cause lung fibrosis."},
        NS % "2023 Q114")

B.keyed("A patient was having side effects of headache, tinnitus and dizziness. Which drug is most likely to cause such side effects?",
        ["Polyethylene glycol", "Quinidine", "Docusate", "Calcium carbonate"], "b",
        "Quinidine causes cinchonism: headache, tinnitus and dizziness. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Polyethylene glycol " + GI, "c": "Docusate " + GI, "d": "Calcium carbonate is an antacid and calcium supplement."},
        NS % "2022 Q126")

B.keyed("This drug blocks Na+ channels with no effect on the action potential duration:",
        ["Flecainide", "Amlodipine", "Lisinopril", "Losartan"], "a",
        "Flecainide (class IC) blocks Na+ channels strongly with little effect on action potential duration. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Amlodipine is a dihydropyridine calcium channel blocker.",
         "c": "Lisinopril is an ACE inhibitor.",
         "d": "Losartan is an angiotensin receptor blocker."},
        NS % "2022 Q128")

B.keyed("Class 3 antiarrhythmics are:",
        ["Sodium channel blockers", "Beta receptor blockers", "Calcium channel blockers", "Potassium channel blockers"], "d",
        "Class III antiarrhythmics (amiodarone, sotalol) block K+ channels and prolong repolarization. Class I block Na+, class II are beta blockers, class IV block Ca++. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Sodium channel blockers are class I.", "b": "Beta blockers are class II.", "c": "Calcium channel blockers are class IV."},
        NS % "Unknown-1 Q152")

B.keyed("Drug for intraoperative use:",
        ["Ezetimibe", "Cholestyramine", "Esmolol", "Fenofibrate"], "c",
        "Esmolol is a very short-acting IV beta blocker, so it suits intraoperative control of heart rate and pressure. It is on your hypertension drug list; its intraoperative use is from the bank's key.",
        {"a": "Ezetimibe blocks intestinal cholesterol absorption.", "b": "Cholestyramine binds bile acids in the gut.", "d": "Fenofibrate lowers triglycerides."},
        NS % "Unknown-1 Q153")

B.keyed("Gray-blue skin discoloration in sun-exposed areas (smurf skin) is caused by:",
        ["Amiodarone", "Adenosine", "Esmolol", "Diltiazem"], "a",
        "Amiodarone can cause blue-gray discoloration of sun-exposed skin. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Adenosine acts for seconds and has no skin effect.", "c": "Esmolol is a short-acting beta blocker.", "d": "Diltiazem is a non-dihydropyridine CCB."},
        NS % "Unknown-1 Q154")

# ---------------------------------------------------------------- lipid-lowering drugs (past papers)
B.concept("pharm-lipid", "Lipid-lowering drugs (past papers)", [
    "Statins (lovastatin, atorvastatin) competitively inhibit HMG CoA reductase; they can cause muscle pain and rhabdomyolysis.",
    "Niacin lowers triglycerides and raises HDL; adverse effects are skin flushing and hyperuricemia.",
    "Fenofibrate is the drug of choice for hypertriglyceridemia; ezetimibe selectively inhibits intestinal cholesterol absorption; cholestyramine binds bile acids in the intestine.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("During antihyperlipidemic treatment a patient suffers from muscle pain. Which drug is the cause?",
        ["Famotidine", "Loratadine", "Polyethylene glycol", "Lovastatin"], "d",
        "Statins such as lovastatin cause muscle pain (myopathy). Note: the paper prints only options a-c but keys \"d\"; option d, \"Lovastatin\", is restored from the matching questions in this bank. Not in your uploaded Mid 2 slides.",
        {"a": "Famotidine " + GI, "b": "Loratadine is an antihistamine.", "c": "Polyethylene glycol " + GI},
        NS % "2024 Nov Q58")

B.keyed("Niacin (antihyperlipidemic) can cause?",
        ["Iron-deficiency anemia", "Vitamin B12 deficiency", "Hypocalcemia", "Hyperuricemia"], "d",
        "Niacin can raise uric acid (hyperuricemia) and cause flushing. Your slides mention large-dose vitamin B3 as a cholesterol-lowering dietary factor; its adverse effects are from the bank's key.",
        {"a": "Iron-deficiency anemia is not a niacin effect.", "b": "B12 deficiency is not a niacin effect.", "c": "Hypocalcemia is not a niacin effect."},
        NS % "2024 Nov Q60")

B.keyed("A patient diagnosed with hyperlipidemia is prescribed cholestyramine. What is the action of this drug?",
        ["Blocks beta₁ receptors in the heart", "Inhibits gastric acid secretion", "Blocks sodium channels in peripheral nerves", "Binds bile acids in the intestine and is excreted with them in the stool"], "d",
        "Cholestyramine is a bile acid sequestrant: it binds bile acids in the gut so they are lost in the stool, and the liver uses cholesterol to make more. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Blocking beta-1 receptors is the action of beta blockers.", "b": "Inhibiting gastric acid is the action of drugs such as omeprazole.", "c": "Blocking nerve sodium channels is the action of local anesthetics."},
        NS % "2024 May Q74")

B.keyed("Which of the following is the drug of choice for hypertriglyceridemia?",
        ["Fenofibrate", "Amlodipine", "Omeprazole", "Loratadine"], "a",
        "Fibrates such as fenofibrate are the drugs of choice for high triglycerides. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Amlodipine is a calcium channel blocker.", "c": "Omeprazole " + GI, "d": "Loratadine is an antihistamine."},
        NS % "2024 May Q86")

B.keyed("A woman came to the ER complaining of muscle pain. She has a history of hyperlipidemia and is taking medication to treat it. Which drug caused her pain?",
        ["Pantoprazole", "Cetirizine", "Lovastatin", "Docusate"], "c",
        "Statins such as lovastatin can cause myalgia and myopathy. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Pantoprazole " + GI, "b": "Cetirizine is an antihistamine.", "d": "Docusate " + GI},
        NS % "2024 May Q87")

B.keyed("Which of the following drugs is a selective inhibitor of intestinal cholesterol absorption?",
        ["Fenofibrate", "Ezetimibe", "Atorvastatin", "Niacin"], "b",
        "Ezetimibe selectively blocks cholesterol absorption in the intestine. Your slides describe the same idea for plant sterols. The drug answer is from the bank's key.",
        {"a": "Fenofibrate lowers triglycerides.", "c": "Atorvastatin inhibits HMG CoA reductase.", "d": "Niacin lowers triglycerides and raises HDL."},
        NS % "2023 Q112", labels={"c": "mixes up statins and ezetimibe"})

B.keyed("A patient treated with an antihyperlipidemic drug has rhabdomyolysis. Which drug has been used to treat him?",
        ["Loratadine", "Famotidine", "Polyethylene glycol", "Lovastatin"], "d",
        "Statins can cause rhabdomyolysis, the severe form of statin myopathy. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Loratadine is an antihistamine.", "b": "Famotidine " + GI, "c": "Polyethylene glycol " + GI},
        NS % "2023 Q113")

B.keyed("Adverse effect of niacin includes?",
        ["Gingival hyperplasia", "Tooth discoloration", "Orange discoloration of urine", "Skin flushing"], "d",
        "Niacin causes skin flushing. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Gingival hyperplasia is not a niacin effect.", "b": "Tooth discoloration is not a niacin effect.", "c": "Orange urine is not a niacin effect."},
        NS % "2022 Q127")

B.keyed("A 62-year-old patient is on lovastatin; cholesterol levels decreased but he still has high triglycerides and low HDL. Which drug should be used?",
        ["Lisinopril", "Omeprazole", "Niacin", "Loratadine"], "c",
        "Niacin lowers triglycerides and raises HDL, so it covers what a statin leaves. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Lisinopril is an ACE inhibitor for blood pressure.", "b": "Omeprazole " + GI, "d": "Loratadine is an antihistamine."},
        NS % "2022 Q129")

# ---------------------------------------------------------------- antianginal drugs (past papers)
B.concept("pharm-antianginal", "Nitrates and beta blockers in angina (past papers)", [
    "Nitrate tolerance is treated by a nitrate-free interval (no therapy for a brief time).",
    "Beta blockers relieve angina by decreasing myocardial O2 demand.",
], "Shams Practices QB (past papers); nitrates and beta blockers for IHD are on Physiology L9 slides")

B.keyed("A patient with increased nitrate tolerance is treated by?",
        ["Shortening the interval between nitrate doses", "Switching to continuous nitrate infusion", "Adding an extra nitrate dose during the nitrate-free interval", "No therapy for a brief time"], "d",
        "Tolerance to nitrates develops with continuous exposure and is prevented or reversed by a daily nitrate-free interval. Your slides list nitrates as coronary dilators; tolerance is from the bank's key.",
        {"a": "Shorter dosing intervals give more continuous exposure, worsening tolerance.",
         "b": "Continuous infusion is the setting in which tolerance develops.",
         "c": "Filling the nitrate-free interval removes the break that prevents tolerance."},
        NS % "Unknown-2 Q170")

B.keyed("Beta blocker action in angina is to?",
        ["Decrease O₂ demand", "Increase heart rate through β₁ stimulation", "Increase myocardial contractility through β₁ stimulation", "Increase renin release through β₁ stimulation"], "a",
        "Beta blockers block cardiac beta-1 receptors, lowering heart rate and contractility, so the heart needs less oxygen; your slides list exertional angina among their uses.",
        {"b": "Beta blockers DEcrease heart rate by blocking beta-1.", "c": "Beta blockers DEcrease contractility.", "d": "Beta blockers INHIBIT renin release from juxtaglomerular cells."},
        SL % "Unknown-2 Q171", labels={"b": "thinks beta blockers stimulate beta receptors"})

B.keyed("Contraindication of nitrate is?",
        ["Hyperthyroidism", "Myopia", "Lactose intolerance", "Seasonal allergic rhinitis"], "a",
        "The bank keys hyperthyroidism. Note: this is not in your slides, and standard nitrate contraindications are mainly hypotension and recent use of PDE-5 inhibitors; hyperthyroidism is simply the only cardiovascular-relevant option offered here. Check with your instructor.",
        {"b": "Myopia is short-sightedness, unrelated to nitrates.",
         "c": "Lactose intolerance is an enzyme deficiency, unrelated to nitrates.",
         "d": "Allergic rhinitis is nasal allergy, unrelated to nitrates."},
        NS % "Unknown-2 Q175")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
