"""Shams Practices CVS MID-2 QB (past papers): Biochemistry. Wording, options and key as printed (typos fixed).

Lipoprotein metabolism, apolipoproteins, statins' enzyme and eicosanoids are not in the
two uploaded biochemistry lectures; those answers come from the bank's key.
"""
from _authoring import Bank

B = Bank("Biochemistry")
L5 = "Shams Practices QB, %s; Biochemistry L5 slides (diet fat and CHD)"
L6 = "Shams Practices QB, %s; Biochemistry L6 slides (oxidative stress)"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"
X = "is an unrelated enzyme, not part of cholesterol or lipoprotein metabolism."

# ---------------------------------------------------------------- oxidative stress / NO (on slides)
B.join("bio-burst-no")
B.keyed("Which antioxidant enzyme contains selenium in its active site and uses reduced glutathione to break down peroxides?",
        ["Glutathione peroxidase", "Catalase", "Superoxide dismutase", "Glutathione reductase"], "a",
        "Glutathione peroxidase uses reduced glutathione to break down peroxides and contains selenium. Your slides list glutathione peroxidase among the enzymatic antioxidants and selenium among the nutrient antioxidants; the link between them is from the bank's key.",
        {"b": "Catalase breaks down H2O2 without glutathione or selenium.",
         "c": "Superoxide dismutase converts superoxide into H2O2.",
         "d": "Glutathione reductase regenerates reduced glutathione; it does not break down peroxides."},
        L6 % "2025 Q21", labels={"d": "mixes up glutathione peroxidase and reductase"})

B.keyed("Which molecule mediates vasodilation after administration of sublingual nitroglycerin?",
        ["Endothelin-1", "Angiotensin II", "Thromboxane A₂", "Nitric oxide (NO)"], "d",
        "Nitroglycerin is metabolized into nitric oxide, which relaxes vascular smooth muscle and relieves coronary spasm in angina.",
        {"a": "Endothelin-1 is a vasoconstrictor.", "b": "Angiotensin II is a vasoconstrictor.", "c": "Thromboxane A2 is a vasoconstrictor that promotes platelet aggregation."},
        L6 % "2025 Q24")

B.keyed("Nitroglycerin is metabolized into?",
        ["Angiotensin II", "Nitric oxide", "Endothelin-1", "Thromboxane A₂"], "b",
        "Vasodilators such as nitroglycerin are metabolized into NO, which dilates coronary arteries in spasm.",
        {"a": "Angiotensin II is a vasoconstrictor.", "c": "Endothelin-1 is a vasoconstrictor.", "d": "Thromboxane A2 is a vasoconstrictor."},
        L6 % "2023 Q108")

B.keyed("Which of the following converts molecular oxygen into superoxide to help kill bacteria?",
        ["Catalase", "Glutathione reductase", "Carbonic anhydrase", "NADPH oxidase"], "d",
        "In the respiratory burst of phagocytes, NADPH oxidase converts molecular oxygen into superoxide, which leads on to H2O2 and hypochlorous acid. (The paper calls it a \"ROS\"; it is the enzyme that makes ROS.)",
        {"a": "Catalase breaks down H2O2; it is an antioxidant enzyme.",
         "b": "Glutathione reductase regenerates glutathione, an antioxidant role.",
         "c": "Carbonic anhydrase makes bicarbonate from CO2 and water."},
        L6 % "2024 May Q81")

B.keyed("In microbial killing, molecular oxygen is converted into superoxide by?",
        ["NADPH oxidase", "Catalase", "Pancreatic amylase", "Creatine kinase"], "a",
        "NADPH oxidase in neutrophils and monocytes converts O2 into superoxide during the respiratory burst.",
        {"b": "Catalase breaks down H2O2.", "c": "Pancreatic amylase digests starch.", "d": "Creatine kinase transfers phosphate in muscle energy metabolism."},
        L6 % "2022 Q119")

B.join("bio-oxldl")
B.keyed("Which modification of LDL occurs early in atherosclerosis and promotes foam cell formation?",
        ["Conversion of LDL into HDL", "Conversion of LDL into chylomicrons", "Oxidation of LDL", "Conversion of LDL into albumin"], "c",
        "LDL that enters the intima is oxidized by free radicals; macrophages take up oxidized LDL via scavenger receptors and become foam cells.",
        {"a": "LDL is not converted into HDL.", "b": "Chylomicrons are made in the intestine from dietary fat, not from LDL.", "d": "Albumin is a plasma protein, not made from LDL."},
        L6 % "2025 Q22")

B.keyed("Which of the following is the first step in formation of atherosclerotic plaques?",
        ["Calcification of the plaque", "Rupture of the fibrous cap", "Oxidized LDL", "Hemorrhage into the plaque"], "c",
        "Among these options, LDL oxidation in the intima comes earliest; your slides list endothelial dysfunction first, then LDL retention and oxidation. Calcification, cap rupture and hemorrhage are late changes.",
        {"a": "Calcification is a late change in a progressed plaque.", "b": "Rupture of the fibrous cap is a late complication.", "d": "Hemorrhage into a plaque is an acute plaque change."},
        L6 % "2024 May Q82")

B.keyed("The core of an atherosclerotic plaque contains:",
        ["Oxidized LDL", "Bile salts", "Glycogen granules", "Keratin"], "a",
        "The plaque core is rich in lipid, including oxidized LDL, debris and dead foam cells. (Stem fixed from \"Atherosclerosis contain in its core :\".)",
        {"b": "Bile salts are in bile, not plaques.", "c": "Glycogen is a stored carbohydrate in liver and muscle.", "d": "Keratin is a skin and hair protein."},
        L6 % "Unknown-1 Q140")

# ---------------------------------------------------------------- dietary fat (on slides)
B.join("bio-fats")
B.keyed("Which effect of omega-3 fatty acids may help lower the risk of coronary heart disease?",
        ["Increased platelet aggregation", "Reduced vascular thrombosis", "Increased coronary vasoconstriction", "Increased formation of blood clots"], "b",
        "Omega-3 fats suppress arrhythmia, reduce triacylglycerol, decrease the tendency to vascular thrombosis and reduce inflammation.",
        {"a": "More platelet aggregation would RAISE risk.", "c": "Vasoconstriction would raise risk.", "d": "More clots would raise risk."},
        L5 % "2025 Q23")

B.keyed("A doctor advises a patient to reduce dietary trans fat intake. How does trans fat affect blood LDL cholesterol?",
        ["It increases LDL cholesterol", "It decreases LDL cholesterol", "It leaves LDL cholesterol unchanged", "It removes all LDL cholesterol from the bloodstream"], "a",
        "Trans fats are chemically unsaturated but behave like saturated fats: they raise LDL-cholesterol and lower HDL-cholesterol.",
        {"b": "Lowering LDL is the effect of MUFA and omega-6 fats.", "c": "Trans fats do change LDL: they raise it.", "d": "No fat removes all LDL."},
        L5 % "2025 Q25", labels={"b": "thinks trans fats behave like unsaturated fats"})

B.keyed("HDL is increased by:",
        ["Olive oil – Fish oil", "Cigarette smoking", "Physical inactivity", "Industrial trans fat intake"], "a",
        "Substituting monounsaturated fat (olive oil) for saturated fat raises HDL-cholesterol; fish oils are the protective omega-3 fats. (Stem fixed from \"increase HDL by :\".)",
        {"b": "Smoking is a coronary risk factor.", "c": "Lack of exercise is a coronary risk factor.", "d": "Trans fats LOWER HDL."},
        L5 % "Unknown-1 Q144")

B.keyed("Biological effect of trans fatty acids is seen with:",
        ["Egg whites", "Table salt", "Palm oil", "Distilled water"], "c",
        "The bank keys palm oil. Note: the question looks garbled; your slides list palm oil as a source of SATURATED fat, and trans fats come from partially hydrogenated vegetable oils. Palm oil is the only fat among the options. (Stem fixed from \"trans fatty acids biologi effect :\".)",
        {"a": "Egg whites are mostly protein and contain no fat.", "b": "Table salt contains no fat.", "d": "Distilled water contains no fat."},
        L5 % "Unknown-1 Q145")

B.keyed("In the diet, which prevents coronary heart disease?",
        ["Industrial trans fat", "Elaidic acid", "Oleic acid"], "c",
        "Oleic acid is the monounsaturated (omega-9) fat of olive oil, linked with low CHD in Mediterranean diets. (The paper prints three options.)",
        {"a": "Industrial trans fat raises LDL and CHD risk.", "b": "Elaidic acid is a trans fatty acid, which raises CHD risk."},
        L5 % "Unknown-2 Q172", labels={"b": "thinks trans fats are protective"})

B.keyed("Which is a beneficial fatty acid?",
        ["Elaidic acid", "Industrial trans fatty acids", "Trans-palmitelaidic acid", "Omega 3"], "d",
        "Omega-3 fatty acids reduce CHD risk; the other options are all trans fatty acids, which raise it.",
        {"a": "Elaidic acid is a trans fatty acid.", "b": "Industrial trans fats raise LDL and lower HDL.", "c": "Trans-palmitelaidic acid is a trans fatty acid."},
        L5 % "Unknown-2 Q174")

# ---------------------------------------------------------------- risk factors
B.join("bio-lipids-chd")
B.keyed("A patient had coronary disease and a lipid profile was done. Which lipoprotein would you expect to find at a very low level?",
        ["LDL", "VLDL", "IDL", "HDL"], "d",
        "High HDL-cholesterol is associated with decreased CHD risk, so a low HDL is expected in coronary disease. Elevated LDL raises risk.",
        {"a": "LDL is expected to be HIGH in coronary disease.", "b": "VLDL is not expected to be very low.", "c": "IDL is not expected to be very low."},
        L5 % "2024 Nov Q44")

B.keyed("Which of the following is a negative risk factor?",
        ["Cigarette smoking", "HDL less than 40 mg/dL", "HDL more than 60 mg/dL", "Hypertension"], "c",
        "A high HDL protects against CHD, so HDL above 60 mg/dL counts as a negative (protective) risk factor. The 60 mg/dL cut-off is from the bank's key.",
        {"a": "Smoking is a positive risk factor.", "b": "A low HDL is a positive risk factor.", "d": "Hypertension is a positive risk factor."},
        L5 % "2023 Q109", labels={"b": "thinks all HDL values raise risk"})

B.keyed("Which of these factors is a negative risk factor?",
        ["Cigarette smoking", "LDL less than 100 mg/dl", "Hypertension", "HDL less than 40 mg/dl"], "b",
        "The bank keys LDL below 100 mg/dL as the protective option. Note: in most risk-factor schemes the classic negative risk factor is HDL of 60 mg/dL or more (as in the 2023 question); here LDL below 100 is simply the only option that is not a risk factor.",
        {"a": "Smoking is a positive risk factor.", "c": "Hypertension is a positive risk factor.", "d": "A low HDL is a positive risk factor."},
        L5 % "2022 Q118")

B.keyed("A 56-year-old male patient smokes cigarettes and has HDL 30. How many risk factors does he have?",
        ["Three", "Zero", "One", "Six"], "a",
        "The key counts three: male age (over 45), cigarette smoking and a low HDL (under 40 mg/dL). The age cut-off and counting scheme are from the bank's key, not your slides.",
        {"b": "Smoking alone is a risk factor, so it cannot be zero.", "c": "Smoking and low HDL are already two.", "d": "Only three listed findings count as risk factors."},
        NS % "2023 Q110")

# ---------------------------------------------------------------- lipoproteins and cholesterol metabolism (past papers)
B.concept("bio-lipoproteins", "Lipoproteins and cholesterol metabolism (past papers)", [
    "Statins competitively inhibit HMG CoA reductase, the enzyme insulin activates in the fed state.",
    "In hypothyroidism cholesterol is high because conversion of cholesterol to bile acids is impaired.",
    "Apo B-100 is the structural apolipoprotein of VLDL; nascent chylomicrons and VLDL get apo C-II and apo E from HDL.",
    "Apo C-II activates lipoprotein lipase; apo A-I activates LCAT, which converts free cholesterol to cholesterol esters.",
    "Fatty liver: the liver makes more triglyceride than it can export as VLDL.",
    "Tangier disease: low HDL. Abetalipoproteinemia: decreased VLDL and chylomicrons.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("Statins reduce cholesterol level in blood by competitively inhibiting the?",
        ["Lipoprotein lipase", "Pancreatic lipase", "Lactate dehydrogenase", "HMG CoA reductase"], "d",
        "Statins competitively inhibit HMG CoA reductase, the rate-limiting enzyme of cholesterol synthesis. Your slides say statins lower TC and LDL-C by 30-40%; the enzyme is from the bank's key.",
        {"a": "Lipoprotein lipase breaks down triglycerides in circulating lipoproteins.", "b": "Pancreatic lipase digests dietary fat.", "c": "Lactate dehydrogenase " + X},
        NS % "2024 Nov Q40")

B.keyed("Statin drugs inhibit which enzyme?",
        ["Pancreatic amylase", "HMG CoA reductase", "Creatine kinase", "Lactate dehydrogenase"], "b",
        "Statins inhibit HMG CoA reductase. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Pancreatic amylase digests starch.", "c": "Creatine kinase " + X, "d": "Lactate dehydrogenase " + X},
        NS % "2024 May Q76")

B.keyed("During the fed state, insulin increases the activity of which enzyme?",
        ["Pepsin", "Carbonic anhydrase", "HMG CoA reductase", "Lactase"], "c",
        "Insulin activates HMG CoA reductase in the fed state, increasing cholesterol synthesis. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Pepsin digests protein in the stomach.", "b": "Carbonic anhydrase makes bicarbonate.", "d": "Lactase digests milk sugar."},
        NS % "2022 Q115")

B.keyed("In a hypothyroid patient, the increased cholesterol level is due to impairment in converting cholesterol to?",
        ["Glycogen", "Bile acid", "Lactate", "Creatinine"], "b",
        "Thyroid hormone is needed for converting cholesterol to bile acids; in hypothyroidism this is impaired and cholesterol rises. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Glycogen is stored glucose, not made from cholesterol.", "c": "Lactate is made from glucose.", "d": "Creatinine comes from muscle creatine."},
        NS % "2024 Nov Q41")

B.keyed("A patient came to the clinic with hypothyroidism and hypercholesterolemia. Which conversion of cholesterol is defective?",
        ["Glycogen", "Bile acids", "Lactate", "Creatinine"], "b",
        "Hypothyroidism impairs the conversion of cholesterol to bile acids. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Glycogen is stored glucose.", "c": "Lactate is made from glucose.", "d": "Creatinine comes from muscle creatine."},
        NS % "2024 May Q75")

B.keyed("A hypothyroid patient will develop hypercholesterolemia due to?",
        ["Decrease in conversion of cholesterol to bile acids", "Increased excretion of cholesterol in the stool", "Decreased intestinal cholesterol absorption", "Increased removal of LDL from the blood"], "a",
        "Less cholesterol is converted to bile acids in hypothyroidism, so it accumulates. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "More cholesterol lost in the stool would LOWER blood cholesterol.", "c": "Less absorption would LOWER blood cholesterol.", "d": "More LDL removal would LOWER blood cholesterol."},
        NS % "2022 Q116")

B.keyed("Structural apolipoprotein of VLDL?",
        ["Apo A-I", "Apo A-II", "Apo B-100", "Apo B-48"], "c",
        "Apo B-100 is the structural apolipoprotein of VLDL (and LDL); apo B-48 is the chylomicron's. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Apo A-I is the main apolipoprotein of HDL.", "b": "Apo A-II is an HDL apolipoprotein.", "d": "Apo B-48 is the structural apolipoprotein of chylomicrons."},
        NS % "2024 Nov Q42", labels={"d": "mixes up apo B-100 and apo B-48"})

B.keyed("In fatty liver, production of TG in the liver will be more than ..?",
        ["VLDL", "Chylomicrons", "HDL", "IDL"], "a",
        "The liver exports triglyceride packed in VLDL; fatty liver develops when triglyceride production exceeds VLDL export. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Chylomicrons are made by the intestine, not the liver.", "c": "HDL carries cholesterol, not the liver's triglyceride export.", "d": "IDL is a remnant of VLDL in the blood."},
        NS % "2024 Nov Q43")

B.keyed("Fatty liver is due to accumulation of triglycerides in the liver and a decrease in liver synthesis of?",
        ["Hemoglobin", "Chylomicrons", "Myoglobin", "VLDL"], "d",
        "Less VLDL synthesis means the liver cannot export its triglyceride, which accumulates. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Hemoglobin is the red cell oxygen carrier.", "b": "Chylomicrons are made by the intestine.", "c": "Myoglobin is the muscle oxygen store."},
        NS % "2022 Q121")

B.keyed("Which of the following is activated by apo A-I to convert free cholesterol to cholesterol esters?",
        ["Pancreatic amylase", "LCAT", "Lactate dehydrogenase", "Creatine kinase"], "b",
        "Apo A-I of HDL activates LCAT (lecithin-cholesterol acyltransferase), which esterifies free cholesterol. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Pancreatic amylase digests starch.", "c": "Lactate dehydrogenase " + X, "d": "Creatine kinase " + X},
        NS % "2024 Nov Q45")

B.keyed("The apo A-I of HDL activates which enzyme?",
        ["Pepsin", "Acetylcholinesterase", "LCAT", "Carbonic anhydrase"], "c",
        "Apo A-I activates LCAT. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Pepsin digests protein.", "b": "Acetylcholinesterase breaks down acetylcholine at synapses.", "d": "Carbonic anhydrase makes bicarbonate."},
        NS % "2022 Q120")

B.keyed("Where do nascent chylomicrons and VLDL get apo C-II and apo E?",
        ["Albumin", "Hemoglobin", "Fibrinogen", "HDL"], "d",
        "HDL acts as a reservoir that donates apo C-II and apo E to nascent chylomicrons and VLDL. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Albumin carries free fatty acids, not apolipoproteins.", "b": "Hemoglobin carries oxygen in red cells.", "c": "Fibrinogen is a clotting protein."},
        NS % "2024 May Q77")

B.keyed("Apo C-II activates which enzyme?",
        ["Lipoprotein lipase", "Pepsin", "Carbonic anhydrase", "Acetylcholinesterase"], "a",
        "Apo C-II activates lipoprotein lipase, which breaks down triglycerides in chylomicrons and VLDL. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Pepsin digests protein.", "c": "Carbonic anhydrase makes bicarbonate.", "d": "Acetylcholinesterase breaks down acetylcholine."},
        NS % "2024 May Q78", labels={"b": "mixes up apo C-II and apo A-I targets"})

B.keyed("A patient came to the ER with orange-colored tonsils and an enlarged spleen and liver and was diagnosed with Tangier disease. Which lipoprotein is expected to be low?",
        ["VLDL", "Chylomicrons", "HDL", "IDL"], "c",
        "Tangier disease is a defect in cholesterol efflux to HDL, so HDL is very low and cholesterol esters build up in tissues such as the tonsils. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "VLDL is not the lipoprotein lost in Tangier disease.", "b": "Chylomicrons are not the lipoprotein lost in Tangier disease.", "d": "IDL is not the lipoprotein lost in Tangier disease."},
        NS % "2024 May Q79")

B.keyed("A patient with a history of LDL receptor deficiency (type 2 hyperlipoproteinemia) came to the ER with acute pancreatitis and eruptive xanthomas. Deficiency of which of the following caused this condition?",
        ["Hemoglobin A", "Apo B100", "Fibrinogen", "Immunoglobulin A"], "b",
        "The bank keys apo B-100, the ligand the LDL receptor binds. Note: this question looks garbled. Acute pancreatitis with eruptive xanthomas is classically type I (lipoprotein lipase or apo C-II deficiency), while type II is an LDL receptor or apo B-100 problem; apo B-100 is the only lipoprotein-related option.",
        {"a": "Hemoglobin A is the normal adult hemoglobin.", "c": "Fibrinogen is a clotting protein.", "d": "Immunoglobulin A is an antibody."},
        NS % "2024 May Q80")

B.keyed("Effect of abetalipoproteinemia on lipoproteins?",
        ["Increase VLDL + increase chylomicrons", "Increase VLDL + unchanged chylomicrons", "Unchanged VLDL + increase chylomicrons", "Decrease VLDL + decrease chylomicrons"], "d",
        "Abetalipoproteinemia is a failure to assemble apo B-containing lipoproteins, so both VLDL (apo B-100) and chylomicrons (apo B-48) are decreased. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Neither lipoprotein increases; both fall.", "b": "VLDL falls and chylomicrons also fall.", "c": "Chylomicrons fall, and VLDL falls too."},
        NS % "2022 Q117")

# ---------------------------------------------------------------- eicosanoids (past papers)
B.concept("bio-eicosanoids", "Eicosanoids: COX-2 and prostacyclin (past papers)", [
    "COX-2 makes the prostaglandins of the inflammatory response.",
    "Prostacyclin (PGI2) is a vasodilator.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("COX-2 is involved in:",
        ["Hemoglobin synthesis", "Inflammatory response", "DNA replication", "Glycogen breakdown"], "b",
        "COX-2 is the inducible cyclooxygenase that makes prostaglandins in inflammation. Your slides mention prostaglandin synthesis as a free-radical source; COX-2's role is from the bank's key. (Stem expanded from \"COX-2 :\".)",
        {"a": "Hemoglobin synthesis does not involve COX-2.", "c": "DNA replication does not involve COX-2.", "d": "Glycogen breakdown does not involve COX-2."},
        NS % "Unknown-1 Q142")

B.keyed("PGI2 is a:",
        ["Vasoconstrictor", "Platelet aggregation promoter", "Clotting factor", "Vasodilator"], "d",
        "Prostacyclin (PGI2) dilates vessels and opposes platelet aggregation. Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem expanded from \"PGI2 :\".)",
        {"a": "PGI2 dilates, it does not constrict.", "b": "PGI2 INHIBITS platelet aggregation; thromboxane A2 promotes it.", "c": "PGI2 is a prostaglandin, not a clotting factor."},
        NS % "Unknown-1 Q143", labels={"b": "mixes up prostacyclin and thromboxane"})

B.keyed("Which enzyme makes prostaglandins in inflammation?",
        ["Pancreatic amylase", "Cox-2", "Creatine kinase", "Lactase"], "b",
        "COX-2 produces inflammatory prostaglandins. Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem expanded from \"Prostaglandin inflammation ??\".)",
        {"a": "Pancreatic amylase digests starch.", "c": "Creatine kinase " + X, "d": "Lactase digests milk sugar."},
        NS % "Unknown-2 Q173")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
