from _authoring import Bank

B = Bank("Biochemistry")
L5 = "Biochemistry L5 slides (diet fat and CHD)"
L6 = "Biochemistry L6 slides (oxidative stress)"

B.concept("bio-lipids-chd", "Blood lipids and coronary heart disease", [
    "Total blood cholesterol comes from diet and endogenous synthesis and is carried by lipoproteins, especially LDL and HDL.",
    "CHD risk rises with total and LDL cholesterol; high HDL-cholesterol is associated with decreased risk.",
    "Diet control lowers TC and LDL-C by 10-20%; statins lower them by 30-40%.",
], L5)

B.blanks("A client with high LDL-cholesterol asks how much treatment can lower it. The nurse explains that diet control lowers total and LDL-cholesterol by about {1}, while a statin lowers them by about {2}.",
         [("10-20%", [("30-40%", "30-40% is the reduction with statins.", "swaps diet and statin effects"),
                      ("1-2%", "1-2% is not the figure given; diet control gives 10-20%.")]),
          ("30-40%", [("10-20%", "10-20% is the reduction with diet control.", "swaps diet and statin effects"),
                      ("60-70%", "60-70% is not the figure given; statins give 30-40%.")])],
         "Total blood cholesterol varies with diet and endogenous synthesis. Treating hypercholesterolemia by diet control or by drugs lowers LDL-cholesterol, raises HDL-cholesterol and reduces CHD risk. Diet control alone gives a 10-20% reduction in total and LDL-cholesterol; hypocholesterolemic drugs such as statins give 30-40%.",
         L5)

B.concept("bio-fats", "Types of dietary fat and their effects", [
    "Saturated fats (no double bonds; dairy, meat, coconut and palm oils) raise TC and LDL-C and CHD risk.",
    "Monounsaturated fats (one double bond; olive oil, oleic acid, omega-9) lower TC and LDL-C and raise HDL-C when substituted for saturated fats.",
    "Omega-6 fats (first double bond at carbon 6 from the methyl end; corn, sesame, cottonseed, sunflower oils) lower TC and LDL-C but also lower HDL-C and are proinflammatory.",
    "Omega-3 fats suppress arrhythmia, reduce blood triacylglycerol, decrease thrombosis and inflammation, with little effect on LDL-C and HDL-C.",
    "Trans fats are chemically unsaturated but behave like saturated fats: they raise LDL-C and lower HDL-C; formed by partial hydrogenation of vegetable oils (margarine).",
], L5)

B.sata("A client asks which foods are main sources of saturated fat. Which foods should the nurse include?",
       ["Dairy products", "Meat products", "Coconut oil", "Palm oil"],
       [("Olive oil", "Olive oil is mainly monounsaturated (oleic acid).", "thinks all oils are unsaturated or all are saturated"),
        ("Corn oil", "Corn oil is an omega-6 polyunsaturated fat."),
        ("Flaxseed oil", "Flaxseed oil is a plant source of omega-3 alpha-linolenic acid.")],
       "Saturated fats are triacylglycerols whose fatty acids have no double bonds. Their main sources are dairy and meat products and some vegetable oils, notably coconut and palm oils. Saturated fat intake is strongly associated with high total and LDL-cholesterol and high CHD risk, so intake should be limited.",
       L5)

B.mc("A client replaces butter with olive oil in cooking. Which change in blood lipids should the nurse expect?",
     "Lower total and LDL-cholesterol with higher HDL-cholesterol",
     [("Lower total and LDL-cholesterol with lower HDL-cholesterol", "Lowering HDL too is the pattern of omega-6 fats.", "mixes up MUFA and omega-6 effects"),
      ("Higher LDL-cholesterol with lower HDL-cholesterol", "This is the pattern of trans fats.", "mixes up MUFA and trans fat effects"),
      ("Lower triacylglycerol with little effect on LDL or HDL", "This is the pattern of omega-3 fats.", "mixes up MUFA and omega-3 effects")],
     "Olive oil is rich in monounsaturated fat (oleic acid, one double bond). Substituting monounsaturated for saturated fatty acids lowers total and LDL-cholesterol and increases HDL-cholesterol, lowering CHD risk. Mediterranean diets rich in olive oil show a low incidence of CHD.",
     L5)

B.mc("A client uses large amounts of corn and sunflower oil to protect the heart. Which effect of these oils limits their benefit?",
     "They lower HDL-cholesterol as well and have a proinflammatory effect.",
     [("They raise LDL-cholesterol.", "Omega-6 oils LOWER total and LDL-cholesterol; raising LDL is a trans fat effect.", "thinks omega-6 raises LDL"),
      ("They contain dietary cholesterol.", "Dietary cholesterol is found only in animal products."),
      ("They are not essential fatty acids.", "Linoleic acid, the omega-6 in these oils, IS an essential fatty acid.")],
     "Corn, sesame, cottonseed and sunflower oils are rich in omega-6 polyunsaturated fat such as linoleic acid (18:2 n-6), an essential fatty acid needed for membrane fluidity and eicosanoid synthesis. They lower total and LDL-cholesterol, but they also lower HDL-cholesterol and are proinflammatory, which decreases their effect on CHD.",
     L5)

B.sata("A client with high triglycerides asks about eating fatty fish such as salmon and sardines. Which effects of omega-3 fats should the nurse describe?",
       ["Suppressing cardiac arrhythmia", "Reducing blood triacylglycerol", "Decreasing the tendency to vascular thrombosis", "Reducing inflammation"],
       [("Markedly lowering LDL-cholesterol", "Omega-3 fats have LITTLE effect on LDL- and HDL-cholesterol.", "thinks omega-3 mainly lowers LDL"),
        ("Lowering HDL-cholesterol", "Lowering HDL is an omega-6 effect.", "mixes up omega-3 and omega-6 effects")],
       "Omega-3 fats come from plants (alpha-linolenic acid in flaxseed and walnuts) and fatty fish (EPA and DHA in salmon, mackerel, anchovies, sardines, herring and tuna). They reduce CHD risk by suppressing arrhythmia, reducing blood triacylglycerol, decreasing thrombosis and reducing inflammation, with little effect on LDL- and HDL-cholesterol.",
       L5)

B.fill("A nurse explains fatty acid naming to a client. In an omega-3 fat, the first double bond begins at carbon number ____ counting from the methyl end.",
       "3",
       [("6", "Carbon 6 marks omega-6 fats such as linoleic acid.", "mixes up omega-3 and omega-6"),
        ("9", "Carbon 9 marks omega-9 fats such as oleic acid (monounsaturated).")],
       "The omega number is the position of the first double bond counted from the methyl end of the fatty acid. Omega-3 fats begin at the 3rd carbon, omega-6 fats (linoleic acid) at the 6th and the monounsaturated oleic acid is omega-9.",
       L5)

B.mc("A vegetarian client wants an essential omega-3 fatty acid from plant foods. Which fatty acid should the nurse identify?",
     "Alpha-linolenic acid (ALA) from flaxseed oil and walnuts",
     [("Eicosapentaenoic acid (EPA) from flaxseed", "EPA comes from fatty fish oils and is not an essential fatty acid.", "thinks EPA is a plant essential fatty acid"),
      ("Docosahexaenoic acid (DHA) from walnuts", "DHA (22 carbons, 6 double bonds) comes from fatty fish oils, not walnuts."),
      ("Oleic acid from olive oil", "Oleic acid is a monounsaturated omega-9 fat.")],
     "Plant sources (flaxseed oils, walnuts) provide alpha-linolenic acid, an essential omega-3 fatty acid needed at 0.6-1.2% of total calories, with double bonds at carbons 9, 12 and 15. Fatty fish provide EPA (20 carbons, 5 double bonds) and DHA (22 carbons, 6 double bonds), which are not essential.",
     L5)

B.mc("A nurse teaches a client how to spot trans fats when shopping. Which words on an ingredient list indicate trans fatty acids?",
     "\"Partially hydrogenated\"",
     [("\"Cold-pressed olive oil\"", "Olive oil is a monounsaturated fat, not a trans fat."),
      ("\"Contains plant sterols\"", "Plant sterols lower LDL by blocking cholesterol absorption.", "confuses plant sterols with trans fats"),
      ("\"Fish oil (EPA/DHA)\"", "Fish oils are omega-3 fats.")],
     "Trans fatty acids are not found in plants and occur only in small amounts in animal foods, but they are formed during hydrogenation of liquid vegetable oils, as in margarine manufacture. The key to their presence in a food is the words \"partially hydrogenated\" on the ingredient list.",
     L5 + ", slide note (key to trans fats)", last=True)

B.tf("A nurse explains that trans fatty acids are chemically unsaturated but behave more like saturated fatty acids.", True,
     "True. Trans fatty acids are chemically classified as unsaturated, but they behave more like saturated fatty acids: they raise LDL-cholesterol, lower HDL-cholesterol and increase CHD risk.",
     L5, "This statement is true: trans fats are unsaturated yet act like saturated fats.")

B.tf("A nurse states that WHO recommends limiting trans fat to less than 10% of total energy intake.", False,
     "False. WHO recommends limiting trans fat to less than 1% of total energy intake, which is less than 2.2 g per day on a 2000-calorie diet.",
     L5, "The WHO limit is less than 1% of energy (under 2.2 g/day on 2000 kcal).", "overestimates the trans fat limit")

B.match("A nurse reviews dietary fats with a client. Match each type of fat to its effect on blood lipids.",
        [("Saturated fat", "Raises total and LDL-cholesterol"),
         ("Trans fat", "Raises LDL-cholesterol and lowers HDL-cholesterol"),
         ("Monounsaturated fat", "Lowers LDL-cholesterol and raises HDL-cholesterol"),
         ("Omega-3 fat", "Lowers triacylglycerol with little effect on LDL or HDL")],
        [("Lowers both LDL- and HDL-cholesterol", "Lowering both LDL and HDL is the effect of omega-6 fats.", "mixes up omega-3 and omega-6 effects")],
        "Each fat has a signature effect. Saturated fats raise total and LDL-cholesterol. Trans fats raise LDL and lower HDL. Monounsaturated fats lower LDL and raise HDL. Omega-6 fats lower both LDL and HDL. Omega-3 fats lower triacylglycerol, suppress arrhythmia, thrombosis and inflammation, with little effect on LDL or HDL.",
        L5,
        row_stems={
            "Saturated fat": "A client eats a diet high in saturated fat. Which effect on blood lipids should the nurse expect?",
            "Trans fat": "A client eats many foods made with partially hydrogenated oil. Which lipid effect should the nurse expect?",
            "Monounsaturated fat": "A client substitutes monounsaturated fat for saturated fat. Which lipid effect should the nurse expect?",
            "Omega-3 fat": "A client adds fish oil (omega-3) to the diet. Which lipid effect should the nurse expect?",
        })

B.concept("bio-cholesterol-sterols", "Dietary cholesterol, plant sterols and cholesterol-lowering factors", [
    "Dietary cholesterol is found only in animal products; its effect on blood cholesterol is less important than the amount and type of fatty acids.",
    "Plant sterols reduce LDL-cholesterol by inhibiting intestinal absorption of cholesterol.",
    "Dietary factors that decrease blood cholesterol: omega-6 PUFA, MUFA, antioxidants (beta carotene, vitamins E and C), plant sterols, vegetable fiber, large-dose vitamin B3.",
], L5)

B.mc("A nurse teaches a client about diet and cholesterol. Which statement by the client indicates a need for further teaching?",
     "\"The cholesterol I eat affects my blood cholesterol more than the type of fat I eat.\"",
     [("\"Cholesterol is found only in animal products.\"", "This is accurate: dietary cholesterol is found only in animal products, so no teaching is needed."),
      ("\"Plant sterols lower LDL by blocking cholesterol absorption in my gut.\"", "This is accurate: plant sterols inhibit intestinal absorption of cholesterol."),
      ("\"Fish oils can lower my triglycerides.\"", "This is accurate: omega-3 fish oils reduce blood triacylglycerol.")],
     "Dietary cholesterol is found only in animal products, but its effect on blood cholesterol is LESS important than the amount and type of fatty acids eaten. A client who believes the opposite needs more teaching. Plant sterols in fortified margarines reduce LDL by blocking cholesterol absorption, and fish oils reduce triacylglycerol.",
     L5)

B.sata("A client with high cholesterol asks which dietary factors help lower blood cholesterol. Which factors should the nurse include?",
       ["Monounsaturated fats", "Plant sterols", "Vegetable fiber", "Antioxidants such as vitamins E and C", "Large doses of vitamin B3"],
       [("Saturated fats", "Saturated fats RAISE total and LDL-cholesterol.", "thinks saturated fat lowers cholesterol"),
        ("Partially hydrogenated oils", "Partially hydrogenated oils contain trans fats, which raise LDL.", "thinks margarine trans fats are protective")],
       "The dietary factors listed as decreasing blood cholesterol are omega-6 polyunsaturated fats, monounsaturated fats, antioxidants (beta carotene, vitamins E and C), plant sterols, vegetable fiber and large doses of vitamin B3. Saturated and trans fats push cholesterol the other way.",
       L5)

# ---------------------------------------------------------------- oxidative stress
B.concept("bio-ros", "Free radicals, ROS and RNS", [
    "Oxidative stress: an imbalance favoring oxidants and/or disfavoring antioxidants, potentially leading to damage.",
    "A free radical is a molecule with an unpaired electron in an outer valence shell; it plucks an electron from the nearest molecule.",
    "ROS radicals: superoxide, hydroxyl, peroxyl. ROS non-radicals: hydrogen peroxide, hypochlorous acid, ozone.",
    "RNS radicals: nitric oxide, nitrogen dioxide. RNS non-radical: peroxynitrite.",
    "Endogenous sources: electron leak from the respiratory chain, oxidases (xanthine oxidase), prostaglandin synthesis, NO from arginine, phagocytosis. Exogenous: drug metabolism (halothane, cytochrome P450), ionizing radiation, cigarette smoke.",
], L6)

B.mc("A nurse explains oxidative stress to a client with coronary disease. Which definition is accurate?",
     "An imbalance favoring oxidants and/or disfavoring antioxidants that can lead to damage",
     [("Any production of reactive oxygen species in the body", "ROS are made normally and can be useful (e.g. microbial killing); stress is the IMBALANCE.", "thinks any ROS is oxidative stress"),
      ("An excess of antioxidants over oxidants", "That is the opposite of oxidative stress.", "reverses the imbalance"),
      ("The buildup of lipid-rich plaque in the intima", "That describes atherosclerosis, which oxidative stress helps cause.")],
     "Oxidative stress is a state in which reactive species increase without a matching increase in antioxidants: an imbalance favoring oxidants and/or disfavoring antioxidants, potentially leading to damage. Reactive oxygen species are not always harmful; phagocytes use them to kill microbes. The imbalance is what has been implicated in diseases such as atherosclerosis.",
     L6)

B.mc("A nurse reviews reactive nitrogen species. Which one is a NON-radical?",
     "Peroxynitrite",
     [("Nitric oxide", "Nitric oxide (NO.) is a free radical.", "thinks NO is a non-radical"),
      ("Nitrogen dioxide", "Nitrogen dioxide (NO2.) is a free radical."),
      ("Superoxide", "Superoxide is a reactive OXYGEN species and a radical.")],
     "Reactive species are split into radicals, which carry an unpaired electron, and non-radicals, which are strong oxidants or favor strong oxidant formation. Among reactive nitrogen species, nitric oxide and nitrogen dioxide are radicals and peroxynitrite is a non-radical. Among reactive oxygen species, superoxide, hydroxyl and peroxyl are radicals; hydrogen peroxide, hypochlorous acid and ozone are not.",
     L6)

B.tf("A nurse states that hydrogen peroxide is a free radical because it has an unpaired electron.", False,
     "False. Hydrogen peroxide (H2O2) is a NON-radical reactive oxygen species: a strong oxidant without an unpaired electron. The ROS radicals are superoxide, hydroxyl and peroxyl.",
     L6, "H2O2 is a non-radical ROS.", "thinks H2O2 is a radical")

B.sata("A nurse reviews ENDOGENOUS sources of free radicals in a client's cells. Which sources apply?",
       ["Leakage of electrons from the respiratory chain", "Xanthine oxidase activity", "Synthesis of prostaglandins", "Phagocytosis by white cells"],
       [("Cigarette smoke", "Cigarette smoke is an exogenous (environmental) source.", "mixes up endogenous and exogenous sources"),
        ("X-ray exposure", "Ionizing radiation is an exogenous source.", "mixes up endogenous and exogenous sources"),
        ("Halothane metabolism", "Drug metabolism (halothane, cytochrome P450) is listed as exogenous.")],
       "Endogenous free radicals come from cellular metabolism: electron leakage from the respiratory chain, oxidase enzymes such as xanthine oxidase, prostaglandin synthesis, production of nitric oxide from arginine and phagocytosis (myeloperoxidase, NADPH oxidase). Exogenous sources are drug metabolism, ionizing radiation and cigarette smoke.",
       L6)

B.concept("bio-burst-no", "Respiratory burst, nitric oxide and antioxidants", [
    "Respiratory burst: NADPH oxidase converts O2 to superoxide; superoxide dismutase makes H2O2; myeloperoxidase converts H2O2 and chloride to hypochlorous acid, which kills bacteria.",
    "NO is a free radical gas with a half-life of seconds, made from L-arginine by NO synthase.",
    "eNOS and nNOS are constitutive and make low levels of NO; iNOS (macrophages, neutrophils; induced by bacterial toxins, TNF, cytokines) makes large amounts for hours or days.",
    "eNOS-derived NO improves vascular dilation and perfusion; nitroglycerin is metabolized to NO and relieves coronary spasm in angina.",
    "Enzymatic antioxidants: superoxide dismutase, catalase, glutathione peroxidase. Nutrient antioxidants: vitamins A, E, C, selenium. Metabolic: glutathione, ceruloplasmin, albumin, transferrin, ferritin, uric acid.",
], L6)

B.order("A client's neutrophils engulf bacteria. Arrange the steps of the oxygen-dependent killing pathway in order.",
        ["Bacteria are phagocytosed and ROS production rises (respiratory burst)", "NADPH oxidase converts molecular oxygen into superoxide",
         "Superoxide dismutase converts superoxide into hydrogen peroxide", "Myeloperoxidase converts H2O2 and chloride into hypochlorous acid",
         "Hypochlorous acid kills the bacteria"],
        "Reactive oxygen species are sometimes useful. In neutrophils and monocytes, phagocytosis triggers a rapid rise in ROS called the respiratory burst. NADPH oxidase converts oxygen to superoxide, superoxide dismutase converts it to H2O2, and myeloperoxidase uses H2O2 and chloride ions to make hypochlorous acid, which kills bacteria. H2O2 can also form hydroxyl radicals in a reaction catalyzed by free ferrous ions.",
        L6)

B.mc("A client with severe sepsis has very high nitric oxide production driven by bacterial toxins and cytokines. Which enzyme is responsible?",
     "Inducible nitric oxide synthase (iNOS)",
     [("Endothelial nitric oxide synthase (eNOS)", "eNOS is constitutive and constantly produces LOW levels of NO.", "mixes up eNOS and iNOS"),
      ("Neural nitric oxide synthase (nNOS)", "nNOS is constitutive and produces low levels of NO in neurons."),
      ("Xanthine oxidase", "Xanthine oxidase is an oxidase that produces ROS, not NO.")],
     "Nitric oxide is made from L-arginine by NO synthase. eNOS (endothelium) and nNOS (neural) are constitutive and produce low levels constantly. iNOS is expressed in many cells including macrophages and neutrophils; it is induced by bacterial toxins, TNF and inflammatory cytokines and can produce large amounts of NO for hours or days, so it is linked to inflammation.",
     L6)

B.mc("A client with angina takes sublingual nitroglycerin. How does it relieve coronary spasm?",
     "It is metabolized into nitric oxide, which causes vasodilation.",
     [("It is converted into superoxide, which relaxes smooth muscle.", "Superoxide is a damaging ROS radical, not a vasodilator."),
      ("It acts as an antioxidant that neutralizes oxidized LDL.", "Nitroglycerin works through NO-mediated vasodilation, not as an antioxidant."),
      ("It induces iNOS in macrophages.", "iNOS induction is linked to inflammation, not to nitroglycerin's therapeutic effect.", "mixes up iNOS and therapeutic NO")],
     "NO produced by endothelial NOS improves vascular dilation and perfusion, which is beneficial. Vasodilators such as nitroglycerin are metabolized into NO and so dilate coronary arteries in spasm in angina, a therapeutic and diagnostic use.",
     L6)

B.tf("A nurse explains that nitric oxide is a free-radical gas with a half-life of seconds that is made from L-arginine.", True,
     "True. NO is a free radical gas with a very short half-life (seconds), synthesized by NO synthase from L-arginine and metabolized into nitrates, nitrites and peroxynitrite.",
     L6, "This statement is true: NO is a short-lived radical made from L-arginine.")

B.match("A nurse reviews the body's antioxidant defenses with a client. Match each antioxidant to its type.",
        [("Superoxide dismutase", "Enzymatic antioxidant"),
         ("Vitamin E (tocopherol)", "Nutrient (non-enzymatic) antioxidant"),
         ("Glutathione", "Metabolic (non-enzymatic) antioxidant"),
         ("Catalase", "Enzymatic antioxidant")],
        [("Pro-oxidant transition metal", "Transition metals favor the formation of strong oxidants; they are not antioxidants.", "thinks metals are antioxidants")],
        "Antioxidants are enzymatic (superoxide dismutase, catalase, glutathione peroxidase with glutathione reductase and G6PD) or non-enzymatic. Non-enzymatic antioxidants are nutrient (carotene, tocopherol, ascorbic acid, selenium) or metabolic (glutathione, thioredoxin, ceruloplasmin, albumin, melatonin, transferrin, ferritin, uric acid).",
        L6,
        row_stems={
            "Superoxide dismutase": "A nurse explains how superoxide dismutase protects cells. What type of antioxidant is it?",
            "Vitamin E (tocopherol)": "A client takes vitamin E supplements. What type of antioxidant is vitamin E?",
            "Glutathione": "A nurse describes glutathione to a client. What type of antioxidant is it?",
            "Catalase": "A nurse reviews catalase. What type of antioxidant is it?",
        })

B.concept("bio-oxldl", "Oxidized LDL and the stages of atherosclerosis", [
    "Free radicals oxidize LDL cholesterol; oxidized LDL triggers inflammation and plaque buildup.",
    "Stages: endothelial dysfunction, LDL retention and oxidation in the intima, recruitment of monocytes and T cells by VCAM-1, ICAM-1 and MCP-1, foam cell formation (fatty streak), SMC migration and fibrous cap, necrotic core and calcification, rupture or erosion with thrombosis.",
    "Macrophages engulf oxidized LDL via scavenger receptors and become lipid-laden foam cells.",
    "Failure to clear dead macrophages and SMCs (impaired efferocytosis) enlarges an acellular necrotic core.",
], L6)

B.order("A nurse explains how oxidized LDL drives atherosclerosis. Arrange the key stages in order.",
        ["Endothelial dysfunction from hypertension, smoking or dyslipidemia", "LDL enters the intima and is oxidized",
         "Adhesion molecules (VCAM-1, ICAM-1) and MCP-1 recruit monocytes", "Macrophages engulf oxidized LDL and become foam cells (fatty streak)",
         "Smooth muscle cells migrate and form a fibrous cap", "Plaque rupture or erosion triggers thrombosis"],
        "Stressors damage the endothelium. LDL passes into the intima and is oxidized by free radicals and lipoxygenases. Activated endothelium expresses VCAM-1, ICAM-1 and MCP-1 that recruit monocytes and T cells. Monocytes become macrophages that engulf oxidized LDL via scavenger receptors and become foam cells, forming the fatty streak. Smooth muscle cells migrate from the media, proliferate and lay down a fibrous cap; a necrotic core and calcification follow, and a vulnerable plaque may rupture and trigger thrombosis.",
        L6 + ", key stages slide", last=True)

B.mc("A nurse explains how fatty streaks form in a client's arteries. How do macrophages take up oxidized LDL?",
     "Through scavenger receptors, turning into lipid-laden foam cells",
     [("Through VCAM-1 and ICAM-1 on the macrophage", "VCAM-1 and ICAM-1 are adhesion molecules on activated ENDOTHELIAL cells that capture monocytes.", "mixes up adhesion molecules and scavenger receptors"),
      ("By efferocytosis of dead smooth muscle cells", "Efferocytosis is clearing dead cells; its failure enlarges the necrotic core."),
      ("By secreting collagen around the lipid", "Collagen and proteoglycans are made by smooth muscle cells forming the fibrous cap.")],
     "Monocytes recruited into the intima differentiate into macrophages and engulf oxidized LDL via scavenger receptors, becoming lipid-laden foam cells. The initial accumulation of foam cells creates the earliest visible lesion, the fatty streak.",
     L6)

B.mc("A nurse reviews why some atherosclerotic plaques develop a large necrotic core. Which process is responsible?",
     "Apoptosis of macrophages and SMCs with impaired clearance of the dead cells (efferocytosis)",
     [("Migration of smooth muscle cells to form a fibrous cap", "SMC migration builds the fibrous cap over the lipid core, not the necrotic core.", "mixes up cap formation and necrotic core"),
      ("Expression of VCAM-1 and ICAM-1 by endothelial cells", "Adhesion molecules recruit monocytes early in the process."),
      ("Inhibition of intestinal cholesterol absorption", "Blocking intestinal cholesterol absorption is how plant sterols lower LDL.")],
     "As plaques progress, macrophages and smooth muscle cells undergo apoptosis and secondary necrosis. When the dead cells are not cleared (impaired efferocytosis), an acellular necrotic core rich in lipids and debris enlarges, and calcium salts deposit, causing calcification. Vulnerable plaques can then rupture or erode and trigger thrombosis.",
     L6)

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
