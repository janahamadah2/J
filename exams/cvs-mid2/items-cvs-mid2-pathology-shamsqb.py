"""Shams Practices CVS MID-2 QB (past papers): Pathology. Wording, options and key as printed (typos fixed)."""
from _authoring import Bank

B = Bank("Pathology")
L2 = "Shams Practices QB, %s; Pathology L2 slides (hemodynamic disorders II)"
L3 = "Shams Practices QB, %s; Pathology L3 slides (rheumatic fever)"
L4 = "Shams Practices QB, %s; Pathology L4 slides (atherosclerosis)"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"

# ---------------------------------------------------------------- thrombosis and embolism
B.join("path-virchow")
B.keyed("Phlebothrombosis is associated with which factor of Virchow's triad?",
        ["Increased fibrinolysis", "Hypercoagulability", "Increased arterial oxygen saturation", "Decreased plasma glucose"], "b",
        "Venous thrombi (phlebothrombosis) are the most common type and are associated with stasis and a hypercoagulable state, two arms of Virchow's triad.",
        {"a": "Fibrinolysis dissolves thrombi; more of it would oppose thrombosis.",
         "c": "Arterial oxygen saturation is not part of Virchow's triad.",
         "d": "Plasma glucose is not part of Virchow's triad."},
        L2 % "2022 Q132")

B.join("path-embolism")
B.keyed("Which complication can occur when a thrombus from a deep leg vein embolizes to a pulmonary artery and causes ischemic necrosis of lung tissue?",
        ["Renal infarction", "Pulmonary infarction", "Splenic infarction", "Hepatic infarction"], "b",
        "A leg DVT embolizes through the right heart to the pulmonary arteries; the complication of DVT is embolism to the lungs with pulmonary infarction (especially in a congested lung).",
        {"a": "Renal infarcts come from SYSTEMIC (arterial) emboli, such as left heart thrombi.",
         "c": "Splenic infarcts come from systemic emboli.",
         "d": "Hepatic infarcts are not a result of a venous embolus to the lungs."},
        L2 % "2025 Q19", labels={"a": "sends venous emboli to the systemic circulation"})

B.join("path-systemic-emboli")
B.keyed("What is the most common cause of fat embolism following trauma?",
        ["Isolated ankle sprain", "Superficial skin laceration", "Isolated shoulder dislocation", "Long bone fracture"], "d",
        "Fracture of long bones is the most common cause of fat embolism, followed by soft tissue trauma and burns.",
        {"a": "An ankle sprain does not release marrow fat.",
         "b": "A superficial laceration does not release marrow fat.",
         "c": "A dislocation without fracture does not release marrow fat."},
        L2 % "2025 Q20")

B.keyed("Most common cause of fat embolism is?",
        ["Multiple fractures of long bones", "An isolated ankle sprain", "A superficial skin laceration", "An isolated finger dislocation"], "a",
        "Long bone fractures are the most common cause; fat embolism occurs in 90% of people with severe skeletal injuries, though fewer than 10% develop symptoms.",
        {"b": "An ankle sprain does not release marrow fat.",
         "c": "A superficial laceration does not release marrow fat.",
         "d": "A finger dislocation does not release marrow fat."},
        L2 % "2023 Q104")

B.keyed("A pregnant woman, after giving birth, developed dyspnea, cyanosis, pulmonary edema and seizures. What is the cause?",
        ["Carpal tunnel syndrome", "Iron-deficiency anemia", "Uncomplicated cystitis", "Amniotic fluid embolism"], "d",
        "Amniotic fluid entering the maternal circulation through torn membranes or ruptured uterine veins causes sudden dyspnea, cyanosis, shock, seizures, pulmonary edema and DIC.",
        {"a": "Carpal tunnel syndrome is a wrist nerve compression and causes none of these.",
         "b": "Iron-deficiency anemia does not cause sudden seizures and pulmonary edema.",
         "c": "Cystitis is a bladder infection and causes none of these."},
        L2 % "2023 Q103")

B.keyed("A woman, after giving birth, developed dyspnea, pulmonary edema and seizures. What is the cause?",
        ["Amniotic fluid embolism", "Uncomplicated cystitis", "Carpal tunnel syndrome", "Allergic rhinitis"], "a",
        "Sudden dyspnea, pulmonary edema and seizures at delivery are the picture of amniotic fluid embolism, which has 80% mortality.",
        {"b": "Cystitis is a bladder infection and causes none of these.",
         "c": "Carpal tunnel syndrome is a wrist nerve compression.",
         "d": "Allergic rhinitis is nasal allergy."},
        L2 % "2022 Q133")

# ---------------------------------------------------------------- rheumatic fever and valves
B.join("path-jones")
B.keyed("A patient is suspected of having acute rheumatic fever. Which pair of findings are both major Jones criteria?",
        ["Fever and elevated C-reactive protein", "Prolonged PR interval and elevated erythrocyte sedimentation rate", "Fever and a positive throat culture for group A streptococci", "Carditis and erythema marginatum"], "d",
        "The major Jones criteria are carditis, migratory polyarthritis, Sydenham chorea, erythema marginatum and subcutaneous nodules.",
        {"a": "Fever and a raised CRP are both MINOR criteria.",
         "b": "A prolonged PR interval and a raised ESR are both MINOR criteria.",
         "c": "Fever is minor and a positive throat culture is supporting evidence of strep, not a major criterion."},
        L3 % "2025 Q16", labels={"a": "mixes up major and minor Jones criteria", "b": "mixes up major and minor Jones criteria"})

B.join("path-arf")
B.keyed("Anitschkow cells are seen in:",
        ["Acute rheumatic carditis", "Calcific aortic stenosis", "Viral pericarditis", "Aortic dissection"], "a",
        "Anitschkow (caterpillar) cells are macrophages with a slender wavy ribbon of chromatin found in Aschoff bodies, the pathognomonic lesion of acute rheumatic carditis. (Stem fixed from \"Antischow cell?\".)",
        {"b": "Calcific aortic stenosis is not described with Aschoff bodies.",
         "c": "Viral pericarditis is not described with Aschoff bodies.",
         "d": "Aortic dissection is not described with Aschoff bodies."},
        L3 % "2024 May Q47")

B.keyed("Lesion of acute rheumatic fever?",
        ["Aschoff bodies", "Psammoma bodies", "Negri bodies", "Lewy bodies"], "a",
        "Aschoff bodies (focal necrosis, T lymphocytes and Anitschkow cells) are pathognomonic for acute rheumatic fever and appear in all layers of the heart.",
        {"b": "Psammoma bodies are calcified bodies in some tumors, not rheumatic fever.",
         "c": "Negri bodies are seen in rabies.",
         "d": "Lewy bodies are seen in Parkinson disease."},
        L3 % "2022 Q130")

B.join("path-rhd")
B.keyed("A patient has left atrial enlargement and pulmonary edema. Which valvular lesion directly obstructs blood flow from the left atrium to the left ventricle?",
        ["Mitral valve stenosis", "Pulmonary valve stenosis", "Tricuspid valve stenosis", "Aortic valve regurgitation"], "a",
        "Mitral stenosis obstructs flow from the left atrium, which dilates; back pressure causes chronic pulmonary venous congestion and edema, then pulmonary hypertension and right failure.",
        {"b": "Pulmonary stenosis obstructs the right ventricular outflow.",
         "c": "Tricuspid stenosis obstructs flow from the RIGHT atrium.",
         "d": "Aortic regurgitation is leakage at the left ventricular outflow, not obstruction of the left atrium."},
        L3 % "2025 Q17")

B.keyed("Left atrial enlargement, pulmonary edema?",
        ["Pulmonary valve stenosis", "Tricuspid valve stenosis", "Pulmonary valve regurgitation", "Mitral valve stenosis"], "d",
        "Left atrial dilatation and pulmonary congestion are the first consequences of mitral stenosis.",
        {"a": "Pulmonary stenosis affects the right ventricular outflow.",
         "b": "Tricuspid stenosis affects the right atrium.",
         "c": "Pulmonary regurgitation affects the right side of the heart."},
        L3 % "2024 May Q46")

B.keyed("A patient came into the ER with pulmonary edema and an enlarged atrium. What is the lesion?",
        ["Tricuspid stenosis", "Mitral stenosis", "Pulmonary stenosis", "Pulmonary regurgitation"], "b",
        "Mitral stenosis dilates the left atrium and backs blood into the lungs, causing pulmonary edema. (Stem completed from \"patient came into the ER with pulmonary edema, enlarged atrium...\".)",
        {"a": "Tricuspid stenosis enlarges the right atrium and does not cause pulmonary edema.",
         "c": "Pulmonary stenosis affects the right ventricular outflow.",
         "d": "Pulmonary regurgitation affects the right side of the heart."},
        L3 % "2024 May Q71")

B.keyed("Physical examination of an asymptomatic 29-year-old woman with a history of rheumatic fever during childhood finds an early diastolic opening snap with a rumbling late diastolic murmur. These findings are most suggestive of?",
        ["Aortic stenosis", "Mitral stenosis", "Pulmonary stenosis", "Mitral regurgitation"], "b",
        "Chronic rheumatic heart disease most commonly scars the mitral valve into stenosis, decades after ARF. A diastolic opening snap and rumbling murmur are the sounds of a stenotic mitral valve; the murmur detail is from the bank, not your slides.",
        {"a": "Aortic stenosis gives a SYSTOLIC murmur.",
         "c": "Pulmonary stenosis gives a systolic murmur and is not the usual rheumatic lesion.",
         "d": "Mitral regurgitation gives a SYSTOLIC murmur."},
        L3 % "2023 Q102")

B.keyed("Most affected valves regarding valvular diseases are?",
        ["Aortic and pulmonary", "Tricuspid and pulmonary", "Mitral and Aortic", "Mitral and pulmonary"], "c",
        "Rheumatic vegetations and chronic scarring favor the high-pressure valves: mitral (65%) then aortic (25%).",
        {"a": "The pulmonary valve is rarely affected.",
         "b": "The right-sided valves are rarely affected.",
         "d": "The pulmonary valve is rarely affected."},
        L3 % "Unknown-2 Q176")

# ---------------------------------------------------------------- endocarditis and other lesions (past papers)
B.concept("path-past", "Endocarditis types, pyemia and MI healing (past papers)", [
    "Libman-Sacks endocarditis: sterile, wart-like (verrucous) vegetations on the valves in systemic lupus erythematosus.",
    "Nonbacterial thrombotic endocarditis (NBTE) is associated with mucinous adenocarcinoma.",
    "Acute infective endocarditis is a suppurative inflammation and can cause systemic pyemic abscesses.",
    "Stable angina is caused by an uncomplicated atheroma; granulation tissue appears in an infarct at about 7 days.",
], "Shams Practices QB (past papers); vegetations in SLE are on Pathology L2 slides")

B.keyed("A woman with systemic lupus erythematosus dies, and autopsy reveals sterile, wart-like vegetations on the heart valves. What is the most likely diagnosis?",
        ["Acute bacterial endocarditis", "Calcific aortic stenosis", "Libman–Sacks endocarditis", "Mitral valve prolapse"], "c",
        "Your slides list SLE among the causes of valve vegetations; the name for these sterile verrucous vegetations is Libman-Sacks endocarditis (from the bank's key).",
        {"a": "Bacterial endocarditis has INFECTED (septic) vegetations.",
         "b": "Calcific aortic stenosis has no vegetations.",
         "d": "Mitral valve prolapse has no vegetations."},
        NS % "2025 Q18")

B.keyed("A woman died from systemic lupus. During the autopsy, the medical examiner found vegetations that had a warty (verrucous) appearance. What is the cause?",
        ["Libman–Sacks disease", "Calcific aortic stenosis", "Aortic dissection", "Congenital pulmonary valve stenosis"], "a",
        "Verrucous sterile vegetations in SLE are Libman-Sacks endocarditis.",
        {"b": "Calcific aortic stenosis has no vegetations.",
         "c": "Aortic dissection is a tear in the aortic wall.",
         "d": "Congenital pulmonary stenosis has no vegetations."},
        NS % "2024 May Q69")

B.keyed("A patient known to have SLE with high anti-nuclear antibodies, joint inflammation and renal involvement developed endocarditis. What type of endocarditis is it?",
        ["Acute staphylococcal endocarditis", "Fungal endocarditis", "Libman–Sacks endocarditis", "Prosthetic valve endocarditis"], "c",
        "Endocarditis in SLE is Libman-Sacks endocarditis, with sterile verrucous vegetations.",
        {"a": "Acute staphylococcal endocarditis is infective, with no link to SLE.",
         "b": "Fungal endocarditis occurs mostly in immunocompromised clients, IV drug use or prosthetic valves.",
         "d": "Prosthetic valve endocarditis needs a prosthetic valve."},
        NS % "2022 Q134")

B.keyed("Mucinous adenocarcinoma is associated with which cardiac lesion?",
        ["Congenital pulmonary valve stenosis", "Rheumatic mitral stenosis", "Nonbacterial thrombotic endocarditis (NBTE)", "Libman–Sacks endocarditis"], "c",
        "Mucinous adenocarcinoma is associated with nonbacterial thrombotic endocarditis (sterile vegetations from a hypercoagulable state). Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem expanded from \"Mucinous adenocarcinoma?\".)",
        {"a": "Congenital pulmonary stenosis is a birth defect.",
         "b": "Rheumatic mitral stenosis follows rheumatic fever.",
         "d": "Libman-Sacks endocarditis is associated with SLE."},
        NS % "2024 May Q48", labels={"d": "mixes up NBTE and Libman-Sacks"})

B.keyed("Cause of systemic pyemia?",
        ["Mitral valve prolapse", "Atrial septal defect", "Stable angina", "Infective endocarditis"], "d",
        "Pyemia is spread of infected emboli. Your slides note that septic thrombi produce pyemia and that infective endocarditis vegetations shed septic emboli causing abscesses.",
        {"a": "Mitral valve prolapse is not an infection.",
         "b": "An atrial septal defect is a structural defect, not an infection.",
         "c": "Stable angina is ischemic chest pain, not an infection."},
        NS % "2024 May Q70")

B.keyed("Systemic pyemic abscess is a complication of?",
        ["Stable angina", "Mitral valve prolapse", "Acute infective endocarditis", "Congenital pulmonary stenosis"], "c",
        "Septic emboli from acute infective endocarditis vegetations cause infarcts and abscesses in brain, kidney, spleen and lung.",
        {"a": "Stable angina is ischemic chest pain, not an infection.",
         "b": "Mitral valve prolapse is not an infection.",
         "d": "Congenital pulmonary stenosis is a birth defect, not an infection."},
        NS % "2023 Q105")

B.keyed("Systemic pyemic abscess is a complication of which condition?",
        ["Stable angina", "Mitral valve prolapse", "Atrial septal defect", "Acute infective endocarditis"], "d",
        "Infected emboli from acute infective endocarditis cause abscesses in distant organs (pyemia).",
        {"a": "Stable angina is ischemic chest pain, not an infection.",
         "b": "Mitral valve prolapse is not an infection.",
         "c": "An atrial septal defect is a structural defect, not an infection."},
        NS % "2022 Q131")

B.keyed("Acute infective endocarditis consists of?",
        ["Granulomatous inflammation with caseous necrosis", "Suppurative inflammation", "Sterile fibrin deposition without inflammation", "Calcification without inflammation"], "b",
        "Acute infective endocarditis, usually from virulent organisms such as S. aureus, is a suppurative (pus-forming) inflammation that rapidly destroys the valve. Not in your uploaded pathology slides; answer from the bank's key.",
        {"a": "Caseating granulomas describe tuberculosis-type inflammation.",
         "c": "Sterile fibrin deposits describe NBTE or Libman-Sacks vegetations.",
         "d": "Calcification without inflammation describes degenerative valve disease."},
        NS % "Unknown-2 Q177")

B.keyed("Stable angina is caused by:",
        ["Uncomplicated atheroma", "Acute pericarditis", "Aortic dissection", "Pulmonary embolism"], "a",
        "Stable angina comes from a fixed, uncomplicated atheroma that limits flow on effort; acute plaque changes (rupture, thrombosis) cause infarction instead. The pairing is from the bank's key. (Stem expanded from \"stable angina :\".)",
        {"b": "Acute pericarditis is inflammation of the pericardium.",
         "c": "Aortic dissection is a tear in the aortic wall.",
         "d": "Pulmonary embolism is a blocked pulmonary artery."},
        NS % "Unknown-1 Q148")

B.keyed("Granulation tissue appears in a myocardial infarct after:",
        ["7 days", "30 minutes", "2 hours", "6 months"], "a",
        "Granulation tissue forms in an infarct at about 7 days, as it is repaired; it is replaced by a scar over weeks. Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem expanded from \"Granulation tissue :\".)",
        {"b": "At 30 minutes the infarct shows no visible change.",
         "c": "At 2 hours there is still no granulation tissue.",
         "d": "By 6 months the infarct is a dense scar."},
        NS % "Unknown-1 Q150")

# ---------------------------------------------------------------- atherosclerosis
B.join("path-athero")
B.keyed("Atherosclerosis involves:",
        ["Neutrophils produce antibodies", "Macrophage engulf lipid", "Erythrocytes synthesize collagen", "Platelets produce hemoglobin"], "b",
        "In atherogenesis macrophages and smooth muscle cells engulf lipid and become foam cells, forming the fatty streak. (Stem expanded from \"atherosclerosis :\".)",
        {"a": "Antibodies are made by plasma cells, not neutrophils.",
         "c": "Collagen in plaques is made by smooth muscle cells, not red cells.",
         "d": "Platelets do not make hemoglobin."},
        L4 % "Unknown-1 Q146")

B.join("path-arteriosclerosis")
B.keyed("Arteriolosclerosis is associated with:",
        ["Allergic rhinitis", "Lactose intolerance", "Acute appendicitis", "Hypertension"], "d",
        "Arteriolosclerosis affects small arteries and arterioles and is associated with hypertension and diabetes mellitus. (Stem expanded from \"Arteriolosclerosis\".)",
        {"a": "Allergic rhinitis is nasal allergy.",
         "b": "Lactose intolerance is an enzyme deficiency.",
         "c": "Appendicitis is an acute abdominal infection."},
        L4 % "Unknown-1 Q147")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
