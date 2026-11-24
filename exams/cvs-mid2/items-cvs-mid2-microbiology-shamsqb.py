"""Shams Practices CVS MID-2 QB (past papers): Microbiology. Wording, options and key as printed (typos fixed).

Myocarditis, Chagas disease, tick-borne and portal infections are not in the uploaded
endocarditis lecture; those answers come from the bank's key.
"""
from _authoring import Bank

B = Bank("Microbiology")
SL = "Shams Practices QB, %s; Microbiology L3 slides (infective endocarditis)"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"
VIR = "is a virus that is not a cause of endocarditis."

B.join("micro-dx-tx")
B.keyed("Which organism is a recognized cause of blood culture-negative endocarditis?",
        ["Rhinovirus", "Rotavirus", "Norovirus", "Coxiella burnetii"], "d",
        "Culture-negative endocarditis comes from prior antibiotics, fungi, or fastidious bacteria such as Coxiella burnetii, Bartonella, Brucella and the HACEK group, confirmed by serology or PCR.",
        {"a": "Rhinovirus " + VIR + " It causes the common cold.",
         "b": "Rotavirus " + VIR + " It causes diarrhea.",
         "c": "Norovirus " + VIR + " It causes gastroenteritis."},
        SL % "2025 Q14")

B.join("micro-patho")
B.keyed("A blood culture grows gram-positive cocci in chains that are resistant to optochin. Which bacterial product helps viridans streptococci adhere to damaged heart valves?",
        ["Coagulase", "Dextran", "Catalase", "Urease"], "b",
        "Viridans streptococci (optochin-resistant cocci in chains) adhere to the fibrin-platelet matrix on damaged valves using dextran, a sticky polysaccharide.",
        {"a": "Coagulase is the identifying enzyme of S. aureus; its adherence factors are clumping factor and fibronectin-binding protein.",
         "c": "Catalase is the staphylococcal test enzyme, not an adherence factor; streptococci are catalase negative.",
         "d": "Urease is not an adherence factor of any endocarditis organism on your slides."},
        SL % "2025 Q15", labels={"a": "mixes up staphylococcal and streptococcal factors"})

B.keyed("First step of infective endocarditis (from the following)?",
        ["Expression of Beta 1 integrin", "Breakdown of skeletal muscle glycogen", "Secretion of insulin by pancreatic beta cells", "Reabsorption of glucose in the proximal renal tubule"], "a",
        "The bank keys expression of beta-1 integrin. Note: your slides describe the first step as endothelial injury with platelets and fibrin forming a sterile microthrombus; integrins on injured endothelium help that matrix and the bacteria bind. It is the only option related to endocarditis.",
        {"b": "Muscle glycogen breakdown is energy metabolism, unrelated to endocarditis.",
         "c": "Insulin secretion is unrelated to endocarditis.",
         "d": "Renal glucose reabsorption is unrelated to endocarditis."},
        NS % "2024 Nov Q51")

B.join("micro-lab-id")
B.keyed("Endocarditis in a prosthetic valve; the organism is gram-positive, catalase-negative and alpha-hemolytic. What is it?",
        ["Staphylococcus aureus", "Pseudomonas aeruginosa", "Escherichia coli", "Viridans streptococci"], "d",
        "Gram-positive, catalase-negative cocci with alpha hemolysis are viridans streptococci (staphylococci are catalase positive). Note: your slides name S. epidermidis and S. aureus as the main causes of prosthetic valve endocarditis; here the lab findings decide.",
        {"a": "S. aureus is catalase POSITIVE and beta hemolytic.",
         "b": "Pseudomonas is a Gram-negative bacillus.",
         "c": "E. coli is a Gram-negative bacillus."},
        SL % "2024 Nov Q54", labels={"a": "ignores the catalase result"})

B.keyed("A patient presents with chest pain and a tender, painful red pustule on the finger. Blood culture shows gram-positive cocci, catalase negative, alpha hemolytic. What is the causative agent?",
        ["Staphylococcus aureus", "Escherichia coli", "Viridans streptococci", "Pseudomonas aeruginosa"], "c",
        "Catalase-negative, alpha-hemolytic Gram-positive cocci are viridans streptococci, a common cause of subacute endocarditis. The painful finger lesion is an Osler node.",
        {"a": "S. aureus is catalase POSITIVE and beta hemolytic.",
         "b": "E. coli is a Gram-negative bacillus.",
         "d": "Pseudomonas is a Gram-negative bacillus."},
        SL % "2024 May Q68", labels={"a": "ignores the catalase result"})

B.keyed("A drug abuser's tricuspid valve is infected; in the lab the organism is gram-positive and catalase-positive. What is this organism?",
        ["Staphylococcus aureus", "Streptococcus pyogenes", "Escherichia coli", "Pseudomonas aeruginosa"], "a",
        "IV drug use endocarditis mainly affects the tricuspid valve and is mostly due to S. aureus, a Gram-positive, catalase-positive (and coagulase-positive) coccus in clusters.",
        {"b": "S. pyogenes is catalase NEGATIVE.",
         "c": "E. coli is a Gram-negative bacillus.",
         "d": "Pseudomonas causes IV drug use endocarditis too, but it is a Gram-negative bacillus."},
        SL % "2023 Q106")

B.keyed("A case of endocarditis: culture shows gram-positive, catalase-negative, non-hemolytic cocci. Which microorganism could be the causative agent?",
        ["Enterococcus", "Staphylococcus aureus", "Escherichia coli", "Pseudomonas aeruginosa"], "a",
        "Enterococcus faecalis is a Gram-positive, catalase-negative coccus, often non-hemolytic, and causes endocarditis in the elderly after GU or GI procedures. The non-hemolytic detail is from the bank's key.",
        {"b": "S. aureus is catalase POSITIVE and beta hemolytic.",
         "c": "E. coli is a Gram-negative bacillus.",
         "d": "Pseudomonas is a Gram-negative bacillus."},
        SL % "2022 Q124")

B.join("micro-ie-types")
B.keyed("A patient developed endocarditis due to a prosthetic valve. What could be the causative agent?",
        ["Rhinovirus", "Rotavirus", "Staphylococcus aureus", "Enterobius vermicularis"], "c",
        "Prosthetic valve endocarditis is caused mostly by Staphylococcus epidermidis and Staphylococcus aureus.",
        {"a": "Rhinovirus " + VIR, "b": "Rotavirus " + VIR, "d": "Enterobius vermicularis (pinworm) is an intestinal worm."},
        SL % "2022 Q125")

B.keyed("Common cause of bacterial endocarditis?",
        ["Rhinovirus", "Streptococcus", "Plasmodium falciparum", "Enterobius vermicularis"], "b",
        "Gram-positive cocci (staphylococci and streptococci) are the most common causes of bacterial endocarditis; viridans streptococci are a common cause of subacute IE.",
        {"a": "Rhinovirus " + VIR, "c": "Plasmodium falciparum is the malaria parasite.", "d": "Enterobius vermicularis is an intestinal worm."},
        SL % "Unknown-2 Q169")

B.join("micro-signs")
B.keyed("Small hemorrhagic macular lesions on the palms or soles: what is the name of this lesion?",
        ["Roth spot", "Kayser–Fleischer ring", "Janeway lesion", "Koplik spot"], "c",
        "Janeway lesions are small, nontender, erythematous (hemorrhagic) lesions on the palms and soles in infective endocarditis.",
        {"a": "Roth spots are retinal hemorrhages.",
         "b": "Kayser-Fleischer rings are copper rings in the cornea in Wilson disease.",
         "d": "Koplik spots are mouth lesions in measles."},
        SL % "2023 Q101", labels={"a": "mixes up Janeway lesions and Roth spots"})

B.join("micro-organisms")
B.keyed("Anti-M protein antibodies in a rheumatic fever patient are directed against which organism?",
        ["Staphylococcus epidermidis", "Streptococcus pyogenes", "Haemophilus influenzae", "Neisseria meningitidis"], "b",
        "Rheumatic fever follows group A streptococcal (S. pyogenes) pharyngitis; antibodies against its M protein cross-react with heart antigens.",
        {"a": "S. epidermidis causes prosthetic valve and device infections, not rheumatic fever.",
         "c": "Haemophilus is a HACEK organism.",
         "d": "Neisseria meningitidis causes meningitis, not rheumatic fever."},
        SL % "2024 Nov Q55")

B.concept("micro-past", "Myocarditis and other CVS infections (past papers)", [
    "Coxsackievirus B causes myocarditis; Coxsackievirus also causes pleurodynia.",
    "Trypanosoma cruzi (Chagas disease) is a flagellated protozoan seen in Giemsa stain in South America; acute symptoms include loss of appetite, chronic ones megacolon, megaesophagus and dilated cardiomyopathy.",
    "Ixodes ticks transmit Borrelia and Babesia; Trichinella spiralis gives eosinophilia with encysted larvae.",
    "Portal pyemia (pylephlebitis) after intra-abdominal abscess or enteric infection is caused by Enterococcus and anaerobic bacteria.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("A patient in South America has constipation; microscopy shows a unicellular flagellated organism under Giemsa stain. What is the disease?",
        ["Enterobiasis", "Chagas disease", "Ascariasis", "Schistosomiasis"], "b",
        "Trypanosoma cruzi, the cause of Chagas disease in South America, is a flagellated protozoan seen with Giemsa stain; chronic disease causes megacolon (constipation). Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Enterobiasis is pinworm infection, a worm, not a flagellate.", "c": "Ascariasis is a roundworm infection.", "d": "Schistosomiasis is a fluke infection."},
        NS % "2024 Nov Q49")

B.keyed("Pleurodynia, runny nose and pharyngitis. Which finding fits?",
        ["Anti-hepatitis B surface antibodies", "Anti-tetanus toxin antibodies", "Anti-thyroid peroxidase antibodies", "Anti-Coxsackievirus antibodies"], "d",
        "Coxsackievirus causes pleurodynia with upper respiratory symptoms, and Coxsackievirus B is a cause of myocarditis. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Anti-HBs antibodies show hepatitis B immunity.", "b": "Anti-tetanus antibodies show tetanus immunity.", "c": "Anti-TPO antibodies are seen in autoimmune thyroid disease."},
        NS % "2024 Nov Q50")

B.keyed("Ixodes can cause myocarditis and hemolytic anemia by transmitting?",
        ["Salmonella & Shigella", "Giardia & Entamoeba", "Borrelia & Babesia", "Bordetella & Corynebacterium"], "c",
        "Ixodes ticks transmit Borrelia (Lyme disease, which can cause myocarditis) and Babesia (hemolytic anemia). Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Salmonella and Shigella are food-borne gut bacteria.", "b": "Giardia and Entamoeba are water-borne gut protozoa.", "d": "Bordetella and Corynebacterium spread by respiratory droplets."},
        NS % "2024 Nov Q52")

B.keyed("Eosinophilia and encysted larvae in muscle:",
        ["Trichinella spiralis", "Giardia lamblia", "Entamoeba histolytica", "Trichomonas vaginalis"], "a",
        "Trichinella spiralis larvae encyst in muscle (including the heart) and cause eosinophilia. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Giardia is an intestinal protozoan with no larvae.", "c": "Entamoeba is an intestinal protozoan with no larvae.", "d": "Trichomonas is a genital protozoan."},
        NS % "2024 Nov Q53")

B.keyed("Portal phlebitis is caused by",
        ["Enterococcus faecalis", "Rhinovirus", "Varicella-zoster virus", "Trichomonas vaginalis"], "a",
        "Portal phlebitis (pylephlebitis) follows abdominal infection and is caused by gut organisms such as Enterococcus. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Rhinovirus causes the common cold.", "c": "Varicella-zoster causes chickenpox and shingles.", "d": "Trichomonas is a genital protozoan."},
        NS % "2024 May Q67")

B.keyed("Portal pyemia after an intra-abdominal abscess or enteric infection is caused by which organisms?",
        ["Rhinovirus and adenovirus", "Influenza virus and respiratory syncytial virus", "Giardia lamblia and Enterobius vermicularis", "Enterococcus and anaerobic bacteria"], "d",
        "Infection spreading from the gut to the portal vein is caused by enteric organisms: Enterococcus and anaerobic bacteria. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Rhinovirus and adenovirus are respiratory viruses.", "b": "Influenza and RSV are respiratory viruses.", "c": "Giardia and Enterobius are intestinal parasites, not causes of portal pyemia."},
        NS % "2023 Q107")

B.keyed("Bunyaviridae mainly involve which system?",
        ["Skeletal system", "Reticuloendothelial system", "Integumentary system", "Reproductive system"], "b",
        "The bank keys the reticuloendothelial system. Note: the original stem is only \"Bunyaviridae :\", so the question is incomplete; Bunyaviridae (for example hantaviruses and Crimean-Congo hemorrhagic fever virus) cause hemorrhagic fevers. Not in your uploaded Mid 2 slides.",
        {"a": "The skeletal system is not the bank's answer.", "c": "The integumentary system (skin) is not the bank's answer.", "d": "The reproductive system is not the bank's answer."},
        NS % "Unknown-1 Q151")

B.keyed("Which virus causes myocarditis?",
        ["Coxsackievirus B", "Enterobius vermicularis", "Giardia lamblia", "Escherichia coli"], "a",
        "Coxsackievirus B is the classic viral cause of myocarditis. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "Enterobius is a worm, not a virus.", "c": "Giardia is a protozoan, not a virus.", "d": "E. coli is a bacterium, not a virus."},
        NS % "Unknown-2 Q167")

B.keyed("Acute symptom of T. cruzi infection?",
        ["Chronic megaesophagus", "Chronic megacolon", "Loss of appetite", "Chronic dilated cardiomyopathy"], "c",
        "Acute Chagas disease causes nonspecific symptoms such as fever and loss of appetite; megaesophagus, megacolon and dilated cardiomyopathy are CHRONIC complications. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "Megaesophagus is a chronic complication.", "b": "Megacolon is a chronic complication.", "d": "Dilated cardiomyopathy is a chronic complication."},
        NS % "Unknown-2 Q168", labels={"a": "mixes up acute and chronic Chagas", "b": "mixes up acute and chronic Chagas", "d": "mixes up acute and chronic Chagas"})

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
