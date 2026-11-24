"""Shams Practices CVS MID-2 QB (past papers): Physiology. Wording, options and key as printed (typos fixed)."""
from _authoring import Bank

B = Bank("Physiology")
L6 = "Shams Practices QB, %s; Physiology L6 slides (ECG I)"
L7 = "Shams Practices QB, %s; Physiology L7 slides (ECG II)"
L8 = "Shams Practices QB, %s; Physiology L8 slides (cardiac output)"
L9 = "Shams Practices QB, %s; Physiology L9 slides (coronary circulation)"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"

# ---------------------------------------------------------------- ECG
B.join("phys-ecg-waves")
B.keyed("Which ECG wave represents atrial depolarization initiated by the sinoatrial (SA) node?",
        ["Q wave", "R wave", "P wave", "T wave"], "c",
        "The SA node starts each beat by depolarizing the atria, which the ECG records as the P wave. The QRS complex is ventricular depolarization and the T wave ventricular repolarization.",
        {"a": "The Q wave is the first downward part of the QRS complex, ventricular depolarization.",
         "b": "The R wave is the upward part of the QRS complex, ventricular depolarization.",
         "d": "The T wave is ventricular repolarization."},
        L6 % "2025 Q8", labels={"d": "mixes up P and T waves"})

B.keyed("What represents the function of the SA node?",
        ["Q wave", "P wave", "T wave", "U wave"], "b",
        "The SA node's impulse depolarizes the atria, recorded as the P wave.",
        {"a": "The Q wave belongs to the QRS complex, ventricular depolarization.",
         "c": "The T wave is ventricular repolarization.",
         "d": "The U wave is not described on your slides and does not represent the SA node."},
        L6 % "2024 May Q89")

B.keyed("ECG paper contains many small squares in a horizontal line. Each small square equals?",
        ["0.04 second", "0.40 second", "1 second"], "a",
        "At the standard paper speed of 25 mm/sec, each 1-mm small box horizontally is 0.04 s, and a large box (5 small boxes) is 0.20 s. (Stem fixed from \"The ESG paper contain...\"; the paper prints only three options.)",
        {"b": "0.40 s is ten small boxes (two large boxes), not one.",
         "c": "1 second is 25 small boxes (five large boxes)."},
        L6 % "2023 Q97", labels={"b": "confuses small and large boxes"})

B.keyed("PR segment is an indication for?",
        ["Ventricular repolarization", "AVN delay", "Ventricular ejection", "Isovolumetric relaxation"], "b",
        "The PR interval covers atrial depolarization plus the delay in the AV junction (AV node and bundle of His), and the flat PR segment is that AV-nodal delay. The delay lets the atria contract before the ventricles.",
        {"a": "Ventricular repolarization is the T wave.",
         "c": "Ventricular ejection is a mechanical event, not shown by the PR segment.",
         "d": "Isovolumetric relaxation is a mechanical event, not shown by the PR segment."},
        L6 % "2023 Q98")

B.keyed("PR segment indicates which of the following?",
        ["Ventricular ejection", "Ventricular repolarization", "Isovolumetric relaxation", "AV node delay"], "d",
        "The PR segment reflects the delay of the impulse in the AV junction, which gives the atria time to contract before the ventricles contract.",
        {"a": "Ventricular ejection is a mechanical event, not shown by the PR segment.",
         "b": "Ventricular repolarization is the T wave.",
         "c": "Isovolumetric relaxation is a mechanical event, not shown by the PR segment."},
        L6 % "2022 Q123")

B.join("phys-ecg-leads")
B.keyed("A patient with myocardial infarction has ECG changes in leads II, III, and aVF. Which wall of the heart do these leads view?",
        ["Inferior wall", "Anterior wall", "Lateral wall", "Septal wall"], "a",
        "Leads II, III and aVF view the inferior portion of the heart. I, aVL, V5 and V6 view the left lateral wall, V1-V2 the septum and V3-V4 the anterior wall.",
        {"b": "The anterior wall is viewed by V3 and V4.",
         "c": "The lateral wall is viewed by I, aVL, V5 and V6.",
         "d": "The septum is viewed by V1 and V2."},
        L7 % "2025 Q9")

B.keyed("Myocardial ischemia with ST-segment elevation was seen in leads II, III and aVF. Which part of the heart is affected?",
        ["Inferior wall", "Anterior wall", "Lateral wall"], "a",
        "Leads II, III and aVF look at the inferior wall, so ST elevation there points to an inferior infarct. (The paper prints only three options.)",
        {"b": "The anterior wall is viewed by V3 and V4.",
         "c": "The lateral wall is viewed by I, aVL, V5 and V6."},
        L7 % "2024 Nov Q37")

B.keyed("ECG showed myocardial infarction in leads I, aVL, V5 and V6. Where is the infarction located?",
        ["Inferior wall", "Septal wall", "Right ventricular free wall", "Left lateral portion of heart"], "d",
        "Leads I, aVL, V5 and V6 give a good view of the left lateral portion of the heart.",
        {"a": "The inferior wall is viewed by II, III and aVF.",
         "b": "The septum is viewed by V1 and V2.",
         "c": "No lead group on your slides is described as viewing the right ventricular free wall."},
        L7 % "2024 May Q90")

B.keyed("A patient with MI has signs in ECG leads I, II and aVF. Which view of the heart is given by these leads?",
        ["Anterior view", "Septal view", "Right ventricular view", "Inferior view"], "d",
        "The key answer is the inferior view, which on your slides is given by leads II, III and aVF. Note: the paper says \"I, II, aVF\"; lead I is a lateral lead, so this is almost certainly a typo for II, III, aVF.",
        {"a": "The anterior wall is viewed by V3 and V4.",
         "b": "The septum is viewed by V1 and V2.",
         "c": "No lead group on your slides is described as viewing the right ventricle."},
        L7 % "2023 Q99")

B.keyed("A patient with myocardial infarction had signs in ECG leads II, III and aVF. These leads give which view of the heart?",
        ["Anterior view", "Inferior view", "Lateral view", "Septal view"], "b",
        "Leads II, III and aVF view the inferior portion of the heart.",
        {"a": "The anterior wall is viewed by V3 and V4.",
         "c": "The lateral wall is viewed by I, aVL, V5 and V6.",
         "d": "The septum is viewed by V1 and V2."},
        L7 % "2022 Q122")

B.join("phys-axis")
B.keyed("Normal QRS axis?",
        ["−180° to −120°", "+120° to +180°", "−30° to +90°", "−120° to −90°"], "c",
        "A normal axis points leftward and downward. The key answer, -30 to +90 degrees, is the only option inside the normal range. Note: your slides give the normal axis as -30 to +110 degrees, so expect either upper limit; the other options are all abnormal.",
        {"a": "-180 to -120 degrees lies in the indeterminate (extreme right) zone.",
         "b": "+120 to +180 degrees is right axis deviation.",
         "d": "-120 to -90 degrees lies in the indeterminate (extreme right) zone."},
        L6 % "2024 Nov Q38")

B.join("phys-sinus")
B.keyed("What is the rhythm?",
        ["Sinus bradycardia", "Ventricular fibrillation", "Asystole", "Ventricular tachycardia"], "a",
        "The strip shows a normal P wave before every narrow QRS, with a regular rhythm but the beats far apart: a slow sinus rhythm, sinus bradycardia. Ventricular rhythms would have wide bizarre QRS complexes, and asystole has none.",
        {"b": "Ventricular fibrillation has no organized complexes, only chaotic waves.",
         "c": "Asystole is a flat line with no complexes.",
         "d": "Ventricular tachycardia is fast with wide, bizarre QRS complexes."},
        L7 % "2024 Nov Q39")

B.join("phys-autonomic")
B.keyed("A healthy man undergoes an ECG while running. What change in the PR interval is expected compared with rest?",
        ["The PR interval increases to more than 200 ms", "The PR interval remains unchanged", "The PR interval varies randomly because the P waves and QRS complexes become independent", "The PR interval decreases"], "d",
        "During exercise sympathetic activity rises. Sympathetic stimulation increases AV-node excitability and decreases AV nodal delay, so the PR interval shortens.",
        {"a": "A PR above 0.20 s (200 ms) is first-degree AV block, not the effect of exercise.",
         "b": "The PR does change: sympathetic stimulation shortens AV delay.",
         "c": "P waves independent of QRS complexes describes third-degree AV block."},
        L8 % "2025 Q10", labels={"a": "thinks sympathetic stimulation slows AV conduction"})

B.keyed("A man was running and an ECG was performed. What is expected to appear?",
        ["Complete atrioventricular block", "Increased PR interval", "Ventricular fibrillation", "Decreased PR interval"], "d",
        "Exercise raises sympathetic activity, which decreases AV nodal delay and so shortens the PR interval. Note: the paper prints only options a-c but keys \"D\"; option d, \"Decreased PR interval\", is restored here from the matching 2025 question.",
        {"a": "Complete AV block is a conduction disease, not a normal response to exercise.",
         "b": "Sympathetic stimulation DEcreases AV delay, so the PR shortens.",
         "c": "Ventricular fibrillation is a lethal arrhythmia, not a normal response to exercise."},
        L8 % "2024 May Q88", labels={"b": "thinks sympathetic stimulation slows AV conduction"})

B.join("phys-av-block")
B.keyed("Prolonged duration of PR segment?",
        ["1st degree AV block", "Ventricular fibrillation", "Ventricular tachycardia", "Asystole"], "a",
        "First-degree AV block is a PR interval longer than 0.20 s, from prolonged conduction delay in the AV node or bundle of His; every P wave still conducts.",
        {"b": "Ventricular fibrillation has no organized P waves or QRS complexes.",
         "c": "Ventricular tachycardia is a fast rhythm with wide QRS complexes.",
         "d": "Asystole is a flat line with no complexes."},
        L7 % "2023 Q100")

# ---------------------------------------------------------------- cardiac output
B.join("phys-co")
B.keyed("In which condition may left ventricular ejection fraction fall to 30% or less?",
        ["Normal left ventricular systolic function", "Hyperdynamic left ventricular systolic function", "Isolated first-degree atrioventricular block with normal ventricular function", "Cardiac failure with reduced ejection fraction"], "d",
        "Normal EF is 50-75% at rest and up to 90% in strenuous exercise; a failing heart may eject 30% or less.",
        {"a": "Normal function gives an EF of 50-75%.",
         "b": "A hyperdynamic ventricle ejects MORE, raising the EF.",
         "c": "First-degree block only lengthens the PR interval; with normal ventricles the EF is normal."},
        L8 % "2025 Q6")

B.keyed("Increase COP by:",
        ["Increase heart rate and stroke volume", "Decrease heart rate and stroke volume", "Decrease heart rate while stroke volume remains constant", "Decrease stroke volume while heart rate remains constant"], "a",
        "Cardiac output = heart rate x stroke volume, so it rises when either or both rise; in exercise it can reach 20-25 L/min by increasing both.",
        {"b": "Lowering both factors lowers cardiac output.",
         "c": "Lowering heart rate with constant stroke volume lowers cardiac output.",
         "d": "Lowering stroke volume with constant heart rate lowers cardiac output."},
        L8 % "Unknown-1 Q158")

B.join("phys-starling")
B.keyed("Frank-Starling law depends on:",
        ["Plasma glucose concentration", "End diastolic volume", "Arterial oxygen saturation", "Serum sodium concentration"], "b",
        "The Frank-Starling law states that the force of contraction is proportional to the initial length of the cardiac fiber, set by the end-diastolic volume (preload). (The paper's stem is just \"Frank-Starling law\".)",
        {"a": "Plasma glucose does not set fiber length.",
         "c": "Arterial oxygen saturation does not set fiber length.",
         "d": "Serum sodium does not set fiber length."},
        L8 % "Unknown-1 Q155")

B.join("phys-venous-return")
B.keyed("Which mechanism directly increases systemic venous return to the heart during normal spontaneous inspiration?",
        ["Respiratory pump", "Arterial baroreceptor reflex", "Coronary autoregulation"], "a",
        "During inspiration intrathoracic pressure falls (to about -5 mmHg), drawing blood from the lower veins into the chest: the respiratory pump. (The paper prints three options.)",
        {"b": "The baroreceptor reflex adjusts blood pressure; it is not the inspiratory mechanism.",
         "c": "Coronary autoregulation adjusts flow in the heart's own vessels."},
        L8 % "2025 Q7")

B.keyed("Which part of the vascular tree has high compliance?",
        ["Arterioles", "Veins", "Capillaries", "Muscular arteries"], "b",
        "Veins are capacitance vessels that hold about 60-70% of the blood volume, which is what high compliance means. (Stem lightly reworded from \"vascular tree with high Compliance\".)",
        {"a": "Arterioles are the resistance vessels.",
         "c": "Capillaries are exchange vessels and hold little blood.",
         "d": "Muscular arteries distribute blood and are not the capacitance vessels."},
        L8 % "Unknown-1 Q156", labels={"a": "mixes up compliance and resistance vessels"})

# ---------------------------------------------------------------- coronary
B.join("phys-coronary-flow")
B.keyed("When the heart needs more oxygen, such as during exercise, how is the additional oxygen delivered?",
        ["By decreasing coronary blood flow", "By diverting blood away from the myocardium", "By increasing coronary blood flow", "By reducing arterial oxygen saturation"], "c",
        "At rest the heart already extracts 60-70% of the oxygen it receives, so when more is needed, delivery can rise only by increasing coronary blood flow.",
        {"a": "Less flow would deliver less oxygen.",
         "b": "Diverting blood away would starve the myocardium.",
         "d": "Lower arterial saturation would deliver less oxygen."},
        L9 % "2025 Q4")

B.join("phys-phasic-flow")
B.keyed("What change in the cardiac cycle affects coronary perfusion during tachycardia?",
        ["Diastole becomes longer", "Diastole becomes shorter", "Diastolic duration remains unchanged", "Diastole disappears completely"], "b",
        "With a faster heart rate the period of diastole is shorter, and since most left ventricular coronary flow happens in diastole, coronary flow falls.",
        {"a": "Diastole shortens, not lengthens, as rate rises.",
         "c": "Diastole does shorten with tachycardia.",
         "d": "Diastole shortens but does not disappear."},
        L9 % "2025 Q5")

B.keyed("Left ventricular coronary blood flow is at its highest during?",
        ["Isovolumetric contraction", "Rapid ventricular ejection", "Reduced ventricular ejection", "Diastole"], "d",
        "In systole the contracting left ventricle compresses its coronary vessels and the open aortic valve partly blocks their entrance, so LV flow is highest in diastole. (Option d printed as \"Increased Diastole\".)",
        {"a": "Isovolumetric contraction is part of systole, when LV vessels are compressed.",
         "b": "Rapid ejection is systole, when LV vessels are compressed.",
         "c": "Reduced ejection is still systole."},
        L9 % "Unknown-2 Q166")

B.keyed("Coronary circulation during diastole is increased due to?",
        ["Increased compression of coronary vessels", "Increased coronary arteriolar resistance", "Decreased aortic diastolic pressure", "Increased adenosine"], "d",
        "The key answer is adenosine, a coronary vasodilator formed from ATP. Note: your slides explain higher diastolic flow mainly by the RELIEF of systolic compression (aorta-LV gradient 80 mmHg in diastole); among these options, adenosine is the only one that increases flow.",
        {"a": "Compression REDUCES flow; it is what happens in systole.",
         "b": "Higher resistance reduces flow.",
         "c": "A low aortic diastolic pressure reduces coronary flow."},
        L9 % "Unknown-2 Q164")

B.concept("phys-past", "Resistance, blood pressure regulation and cardiac markers (past papers)", [
    "Arterioles are the vessels with maximum resistance.",
    "Blood pressure on standing up from lying down is regulated through the baroreceptors.",
    "Troponin I (cTnI) stays elevated about 10 days after a myocardial infarction.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("Maximum resistance vessels?",
        ["Aorta", "Venae cavae", "Large veins", "Arterioles"], "d",
        "Arterioles are the resistance vessels of the circulation. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The aorta is a large elastic artery with low resistance.",
         "b": "The venae cavae are large, low-resistance veins.",
         "c": "Large veins are capacitance vessels with low resistance."},
        NS % "Unknown-1 Q157", labels={"c": "mixes up compliance and resistance vessels"})

B.keyed("Which of the following blood vessels has maximum resistance?",
        ["Aorta", "Vena cava", "Large vein", "Arteriole"], "d",
        "Arterioles have the greatest resistance. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The aorta is a large elastic artery with low resistance.",
         "b": "The vena cava is a large, low-resistance vein.",
         "c": "Large veins are capacitance vessels with low resistance."},
        NS % "Unknown-2 Q178")

B.keyed("When lying down and then standing up, blood pressure is regulated through?",
        ["Baroreceptors", "Photoreceptors", "Olfactory receptors", "Taste receptors"], "a",
        "Baroreceptors sense the fall in pressure on standing and reflexly restore it. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Photoreceptors sense light in the retina.",
         "c": "Olfactory receptors sense smell.",
         "d": "Taste receptors sense taste."},
        NS % "Unknown-2 Q165")

B.keyed("A patient had a myocardial infarction 10 days ago. Which marker is still elevated?",
        ["Myoglobin", "CK-MB", "Serum amylase", "cTn I"], "d",
        "Cardiac troponin I stays elevated for about 10 days after an MI, much longer than myoglobin or CK-MB. Your slides list cardiac enzymes (CK, LDH, troponin) as investigations but not their timing; answer from the bank's key. (Stem fixed from \"patient with myocardial infarction before 10 days, then it elevated by\".)",
        {"a": "Myoglobin rises and falls within about a day, so it is gone by day 10.",
         "b": "CK-MB returns to normal within a few days.",
         "c": "Serum amylase is a pancreatic enzyme, not a cardiac marker."},
        NS % "Unknown-1 Q141")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
IMAGES = {"What is the rhythm?": "img/qb-2024nov-q39-ecg.png"}
