from _authoring import Bank

B = Bank("Microbiology")
L = "Microbiology L3 slides (infective endocarditis)"

B.concept("micro-ie-types", "Infective endocarditis: classification and organisms", [
    "IE: infection of the endocardium and its valves (native or prosthetic) with septic vegetations; left-sided in over 95% of cases.",
    "Acute IE: rapid (hours to days), mostly healthy valves, severe symptoms; S. aureus, S. pyogenes; mitral and aortic valves.",
    "Subacute IE: slow (weeks to months), preexisting valve disease, low-grade fever, weight loss; viridans streptococci, enterococci, HACEK.",
    "Prosthetic valve IE: early (within 12 months, intraoperative contamination) or late; mostly S. epidermidis and S. aureus.",
    "IV drug use IE: mainly the tricuspid valve; S. aureus, Pseudomonas aeruginosa, Candida.",
], L)

B.mc("A 32-year-old man presents to the emergency department with fever, fatigue, and shortness of breath for 2 weeks. He reports painful nodules on his fingertips and a new heart murmur. His past medical history is significant for intravenous drug use. Temperature 38.9°C, HR 110 bpm, BP 110/65 mmHg, RR 20/min; WBC 15,000/µL, ESR elevated; 3 sets of blood cultures show Gram-positive cocci in clusters; echocardiography shows vegetations on the tricuspid valve. Which of the following is the most likely causative organism?",
     "Staphylococcus aureus",
     [("Streptococcus viridans", "Viridans streptococci are Gram-positive cocci in CHAINS that cause subacute IE on damaged valves, often after oral sources.", "picks viridans for any endocarditis"),
      ("Enterococcus faecalis", "Enterococcus faecalis causes IE in the elderly after GU or GI procedures; it does not grow in clusters."),
      ("Haemophilus parainfluenzae", "Haemophilus is a HACEK Gram-negative bacillus, not a Gram-positive coccus.")],
     "Intravenous drug use endocarditis mainly affects the tricuspid valve, and Staphylococcus aureus is its main cause and the most common cause of IE overall. S. aureus is a Gram-positive coccus in clusters, catalase and coagulase positive, and causes an acute, aggressive infection with rapid valve destruction. Painful finger-pad nodules are Osler nodes.",
     L + ", in-class case", last=True)

B.mc("A client with known rheumatic valve disease has had low-grade fever, malaise and weight loss for 6 weeks after a dental extraction. Which organism should the nurse suspect?",
     "Viridans group streptococci",
     [("Staphylococcus aureus", "S. aureus causes ACUTE, rapidly progressive IE, often on healthy valves.", "mixes up acute and subacute organisms"),
      ("Staphylococcus epidermidis", "S. epidermidis is typical of prosthetic valve and device infections."),
      ("Streptococcus bovis", "S. bovis is associated with colorectal carcinoma or GI lesions, not dental sources.")],
     "Subacute IE progresses slowly over weeks to months, usually in people with preexisting valve disease such as rheumatic heart disease, and causes milder symptoms such as low-grade fever, malaise, chills and weight loss. It is caused by less virulent organisms: viridans streptococci (notably S. mutans) from the oral cavity, enterococci and the HACEK group. A dental procedure is a classic source of the transient bacteremia.",
     L)

B.mc("A client who had a prosthetic valve inserted 3 months ago develops endocarditis. Which organism is most likely?",
     "Staphylococcus epidermidis",
     [("Viridans streptococci", "Viridans streptococci cause subacute IE on damaged native valves after oral sources.", "picks viridans for any endocarditis"),
      ("Streptococcus bovis", "S. bovis is linked to colorectal carcinoma and GI lesions."),
      ("Streptococcus pneumoniae", "S. pneumoniae is a rare cause of IE.")],
     "Prosthetic valve endocarditis is early when it develops within 12 months of surgery, often from intraoperative contamination, and late after 12 months from community-acquired infection. It is caused mostly by Staphylococcus epidermidis and Staphylococcus aureus; S. epidermidis is closely associated with indwelling devices and catheters.",
     L)

B.tf("A nurse states that endocarditis in clients who inject drugs mainly affects the tricuspid valve.", True,
     "True. Intravenous drug abuse endocarditis mainly affects the tricuspid valve and is caused mostly by S. aureus, Pseudomonas aeruginosa and Candida.",
     L, "This statement is true: IVDU endocarditis is mainly tricuspid.")

B.tf("A nurse states that subacute infective endocarditis usually affects healthy valves and is mostly caused by Staphylococcus aureus.", False,
     "False. That describes ACUTE IE. Subacute IE usually occurs on preexisting diseased valves, progresses over weeks to months and is caused by less virulent organisms such as viridans streptococci, enterococci and HACEK.",
     L, "That is acute IE; subacute IE affects diseased valves with less virulent organisms.", "mixes up acute and subacute IE")

B.concept("micro-organisms", "Specific organisms and their associations", [
    "S. aureus: most common overall, IV drug users and healthcare-associated IE; acute, rapid valve destruction.",
    "Streptococcus bovis is associated with colorectal carcinoma or GI lesions.",
    "Enterococcus faecalis: elderly and hospital-acquired IE, after genitourinary or gastrointestinal procedures.",
    "HACEK (Haemophilus, Aggregatibacter, Cardiobacterium hominis, Eikenella corrodens, Kingella): slow-growing fastidious Gram-negative bacilli of pharyngeal flora; subacute IE with negative cultures unless special media are used.",
    "Cardiac device IE (pacemaker, ICD) usually comes from skin contamination at implantation; mostly staphylococci.",
], L)

B.mc("A client's blood cultures grow Streptococcus bovis and echocardiography confirms endocarditis. Which follow-up evaluation should the nurse anticipate?",
     "Evaluation for colorectal carcinoma or another GI lesion",
     [("A dental examination for an oral source", "An oral source is typical of viridans streptococci.", "links S. bovis to the mouth"),
      ("A review of recent genitourinary procedures", "GU and GI procedures are linked with Enterococcus faecalis."),
      ("Inspection of a pacemaker pocket for skin contamination", "Skin contamination at implantation causes cardiac device IE, usually staphylococcal.")],
     "Streptococcus bovis endocarditis is associated with colorectal carcinoma or other gastrointestinal lesions, so finding it should prompt a search of the bowel. Viridans streptococci point to the mouth, enterococci to GU or GI procedures and staphylococci to skin and devices.",
     L)

B.mc("An 80-year-old client develops endocarditis two weeks after a urinary tract procedure in the hospital. Which organism should the nurse suspect?",
     "Enterococcus faecalis",
     [("Streptococcus mutans", "S. mutans (viridans group) comes from the oral cavity.", "picks viridans for any endocarditis"),
      ("Staphylococcus epidermidis", "S. epidermidis is linked to prosthetic valves and indwelling devices."),
      ("Kingella", "Kingella belongs to the HACEK group of pharyngeal flora.")],
     "Enterococcus faecalis is common in elderly and hospital-acquired IE and is often associated with genitourinary or gastrointestinal procedures. It adheres to the damaged valve using teichoic acid.",
     L)

B.sata("A client has culture-negative endocarditis and HACEK organisms are suspected. Which organisms belong to the HACEK group?",
       ["Haemophilus", "Aggregatibacter", "Cardiobacterium hominis", "Eikenella corrodens", "Kingella"],
       [("Klebsiella", "Klebsiella is a rare Gram-negative cause of IE, mainly in immunocompromised clients, not a HACEK member.", "thinks the K in HACEK is Klebsiella"),
        ("Enterococcus faecalis", "Enterococcus faecalis is a Gram-positive coccus, not a HACEK member.", "thinks the E in HACEK is Enterococcus"),
        ("Escherichia coli", "E. coli is a rare Gram-negative cause, not a HACEK member.", "thinks the E in HACEK is E. coli")],
       "HACEK stands for Haemophilus, Aggregatibacter, Cardiobacterium hominis, Eikenella corrodens and Kingella. They are slow-growing, fastidious Gram-negative bacilli of the pharyngeal flora that cause subacute IE with negative blood cultures unless special media are used.",
       L)

B.concept("micro-patho", "Pathophysiology of infective endocarditis", [
    "IE needs endothelial injury, bacteremia and microbial adherence leading to vegetation formation.",
    "Damaged valvular endothelium collects platelets and fibrin, forming a sterile microthrombus (sterile vegetation).",
    "Adherence factors: S. aureus clumping factor and fibronectin-binding protein; viridans streptococci dextran; E. faecalis teichoic acid; Gram-negatives pili.",
    "Vegetations contain fibrin, platelets, bacteria and inflammatory cells; they are friable and embolize, and the bacteria are protected from phagocytes and antibiotics.",
    "Consequences: valve destruction with regurgitation and heart failure, septic emboli with infarcts or abscesses, immune complex glomerulonephritis and vasculitis.",
], L)

B.order("A nurse explains to a client with valve disease how endocarditis develops. Arrange the steps in order.",
        ["Damaged valvular endothelium", "Platelets and fibrin form a sterile microthrombus",
         "Transient bacteremia, e.g. after a dental procedure", "Circulating microbes adhere to the fibrin-platelet matrix",
         "Bacteria proliferate to form a friable vegetation", "Fragments break off as septic emboli"],
        "IE needs endothelial injury, bacteremia and microbial adherence. Damaged valvular endothelium attracts platelets and fibrin, forming a sterile microthrombus. A transient bacteremia from dental procedures, oral or skin infections, IV drug use or invasive procedures seeds the blood, and organisms adhere to the fibrin-platelet matrix. They proliferate inside it to form a vegetation of fibrin, platelets, bacteria and inflammatory cells, which is friable and can fragment into septic emboli.",
        L)

B.match("A nurse reviews how organisms stick to damaged heart valves. Match each organism to its adherence factor.",
        [("Staphylococcus aureus", "Clumping factor and fibronectin-binding protein"),
         ("Viridans streptococci", "Dextran (sticky polysaccharide)"),
         ("Enterococcus faecalis", "Teichoic acid"),
         ("Gram-negative bacteria", "Pili")],
        [("M protein cross-reacting with heart antigens", "M-protein cross-reaction is the immune mechanism of rheumatic fever, not a valve adherence factor.", "confuses rheumatic fever with endocarditis")],
        "After a bacteremia, organisms must adhere to the fibrin-platelet matrix on the valve. S. aureus uses clumping factor and fibronectin-binding protein (protein F), viridans streptococci use dextran, a sticky polysaccharide, Enterococcus faecalis uses teichoic acid, and Gram-negative bacteria use pili.",
        L,
        row_stems={
            "Staphylococcus aureus": "A client has S. aureus endocarditis. Which adherence factor lets this organism stick to the valve?",
            "Viridans streptococci": "A client develops viridans streptococcal endocarditis after dental work. Which adherence factor does the organism use?",
            "Enterococcus faecalis": "A client has Enterococcus faecalis endocarditis. Which adherence factor does this organism use?",
            "Gram-negative bacteria": "A client has Gram-negative bacterial endocarditis. Which structure helps the bacteria adhere?",
        })

B.concept("micro-signs", "Clinical features of infective endocarditis", [
    "Acute: high fever and sepsis. Subacute: mild fever, headache, myalgia, weight loss, night sweats. Cardiac: murmur, heart failure.",
    "Splinter hemorrhages: petechial hemorrhages under the fingernails.",
    "Janeway lesions: small, nontender, erythematous lesions on palms and soles. Osler nodes: painful nodules on the pads of fingers and toes.",
    "Roth spots: retinal hemorrhages.",
], L)

B.sata("A nurse assesses a client with suspected infective endocarditis. Which extracardiac findings are consistent with the diagnosis?",
       ["Splinter hemorrhages under the fingernails", "Painless erythematous lesions on the palms and soles", "Painful nodules on the pads of the fingers", "Retinal hemorrhages"],
       [("Erythema marginatum", "Erythema marginatum is a major Jones criterion of acute rheumatic fever.", "confuses rheumatic fever with endocarditis"),
        ("Firm painless subcutaneous nodules on extensor surfaces", "Subcutaneous nodules on extensor surfaces belong to acute rheumatic fever.", "confuses rheumatic fever with endocarditis"),
        ("Sydenham chorea", "Sydenham chorea is a neurologic manifestation of acute rheumatic fever.")],
       "Septic emboli and immune-mediated injury give IE its extracardiac signs: petechiae, especially splinter hemorrhages under the nails; Janeway lesions (small, nontender, erythematous lesions on palms and soles); Osler nodes (painful nodules on finger and toe pads); and Roth spots (retinal hemorrhages). Rheumatic fever has different skin signs.",
       L)

B.match("A nurse documents the skin and eye findings of a client with endocarditis. Match each finding to its description.",
        [("Janeway lesions", "Small, nontender, erythematous lesions on palms and soles"),
         ("Osler nodes", "Painful nodules on the pads of the fingers and toes"),
         ("Roth spots", "Retinal hemorrhages"),
         ("Splinter hemorrhages", "Hemorrhages underneath the fingernails")],
        [("Firm painless nodules on extensor surfaces", "These are the subcutaneous nodules of acute rheumatic fever.", "confuses rheumatic fever with endocarditis")],
        "The four classic extracardiac signs of IE are easy to mix up. Janeway lesions are nontender and on palms and soles; Osler nodes are painful and on finger and toe pads (\"O for ouch\"); Roth spots are in the retina; splinter hemorrhages are under the nails.",
        L,
        row_stems={
            "Janeway lesions": "A client with endocarditis has Janeway lesions. Which description should the nurse document?",
            "Osler nodes": "A client with endocarditis has Osler nodes. Which description fits?",
            "Roth spots": "A client with endocarditis has Roth spots on eye examination. What are they?",
            "Splinter hemorrhages": "A nurse notes splinter hemorrhages in a client with endocarditis. Where are they found?",
        })

B.concept("micro-dx-tx", "Diagnosis, treatment and prophylaxis", [
    "Blood cultures are the gold standard: three sets from different venipuncture sites before treatment.",
    "Culture-negative IE: prior antibiotics, fastidious bacteria (Coxiella burnetii, Bartonella, Brucella, HACEK; confirm by serology or PCR), fungal infection.",
    "Empiric therapy once cultures are drawn: native valve vancomycin + cefepime; prosthetic valve vancomycin + cefepime + gentamicin + rifampin; then targeted therapy.",
    "Prophylaxis before dental or invasive procedures in high-risk clients, 30-60 minutes before: amoxicillin, ampicillin or cefazolin; if penicillin-allergic, a macrolide (azithromycin) or doxycycline.",
], L)

B.mc("A client is admitted with suspected infective endocarditis and empiric antibiotics are ordered. Which action should the nurse take first?",
     "Draw three sets of blood cultures from different venipuncture sites before the first antibiotic dose.",
     [("Give the first antibiotic dose, then draw blood cultures.", "Prior antibiotic therapy is a main cause of culture-negative endocarditis.", "gives antibiotics before cultures"),
      ("Draw one set of blood cultures from the existing IV line.", "The standard is three sets from different venipuncture sites."),
      ("Wait for the echocardiogram before drawing any cultures.", "Blood cultures are the gold standard and are taken before treatment; empiric therapy starts once they are sampled.")],
     "Blood cultures are the gold standard for diagnosing IE: three sets from different venipuncture sites, taken before treatment. Empiric antibiotics start once cultures have been sampled, then switch to targeted therapy when results are available. Giving antibiotics first is a leading cause of culture-negative endocarditis.",
     L + ", slide note (gold standard)", last=True)

B.sata("A client's blood cultures stay negative despite clinical endocarditis. Which causes should the nurse consider?",
       ["Antibiotics given before the cultures were drawn", "A fastidious organism such as Coxiella burnetii or Bartonella", "A HACEK organism", "A fungal infection"],
       [("Infection with Staphylococcus aureus", "S. aureus grows readily; it is the classic culture-positive cause.", "thinks S. aureus is hard to culture"),
        ("Drawing three sets from different venipuncture sites", "Three sets from different sites is the correct technique, not a cause of negative cultures.")],
       "Culture-negative endocarditis has three main causes: prior antibiotic therapy before cultures, fastidious bacteria (Coxiella burnetii, Bartonella, Brucella and the HACEK group), which are confirmed by serology or PCR, and fungal infection.",
       L)

B.mc("A client with a native valve has suspected endocarditis and blood cultures have been drawn. Which empiric regimen should the nurse anticipate?",
     "Vancomycin plus cefepime",
     [("Vancomycin plus cefepime plus gentamicin plus rifampin", "This four-drug regimen is for PROSTHETIC valve endocarditis.", "mixes up native and prosthetic valve regimens"),
      ("Amoxicillin 30-60 minutes before the procedure", "Amoxicillin is a prophylaxis regimen before dental or invasive procedures.", "confuses prophylaxis with treatment"),
      ("Azithromycin alone", "Azithromycin is a prophylaxis option for penicillin-allergic clients.")],
     "Empiric therapy starts once blood cultures have been sampled. Native valve endocarditis: vancomycin plus cefepime. Prosthetic valve endocarditis: vancomycin plus cefepime plus gentamicin plus rifampin. Therapy is switched to targeted antibiotics when culture results arrive, and antithrombotic agents are part of treatment.",
     L)

B.mc("A client with a prosthetic heart valve and a penicillin allergy is scheduled for a dental extraction. Which prophylaxis should the nurse anticipate?",
     "Azithromycin 30-60 minutes before the procedure",
     [("Amoxicillin 30-60 minutes before the procedure", "Amoxicillin is a penicillin; it is the choice only without penicillin allergy.", "ignores the penicillin allergy"),
      ("Vancomycin plus cefepime for several weeks", "This is empiric TREATMENT of native valve endocarditis, not prophylaxis.", "confuses prophylaxis with treatment"),
      ("No prophylaxis, because dental procedures are low risk", "Prophylaxis is indicated before dental procedures in clients with a prosthetic valve.")],
     "Endocarditis prophylaxis is indicated before dental or invasive procedures in clients with high-risk cardiac features or a prosthetic valve, given 30-60 minutes before. Without penicillin allergy, amoxicillin, ampicillin or cefazolin is used; with penicillin allergy, a macrolide such as azithromycin or doxycycline.",
     L)

B.concept("micro-lab-id", "Laboratory identification of IE organisms", [
    "S. aureus: Gram-positive cocci in clusters; golden yellow colonies, beta hemolysis, ferments mannitol; catalase and coagulase positive.",
    "S. epidermidis: Gram-positive cocci in clusters; catalase positive, coagulase negative.",
    "Viridans streptococci (S. mutans): Gram-positive cocci in chains; alpha hemolysis; optochin resistant; insoluble in bile.",
    "S. pyogenes: Gram-positive cocci in chains; beta hemolysis; catalase negative.",
    "S. pneumoniae: lancet-shaped capsulated diplococci; alpha hemolysis; optochin sensitive; bile soluble.",
], L)

B.match("A nurse reviews laboratory reports from clients with endocarditis. Match each organism to its identifying result.",
        [("Staphylococcus aureus", "Cocci in clusters, coagulase positive"),
         ("Staphylococcus epidermidis", "Cocci in clusters, catalase positive, coagulase negative"),
         ("Viridans streptococci", "Cocci in chains, alpha hemolysis, optochin resistant"),
         ("Streptococcus pneumoniae", "Lancet-shaped diplococci, optochin sensitive, bile soluble")],
        [("Cocci in chains, beta hemolysis, catalase negative", "This is Streptococcus pyogenes.", "mixes up streptococcal hemolysis patterns")],
        "Staphylococci grow in clusters and are catalase positive; coagulase separates S. aureus (positive, golden colonies, beta hemolysis, mannitol fermenter) from S. epidermidis (negative). Streptococci grow in chains: viridans streptococci are alpha hemolytic, optochin resistant and bile insoluble, S. pneumoniae is alpha hemolytic but optochin sensitive and bile soluble, and S. pyogenes is beta hemolytic and catalase negative.",
        L,
        row_stems={
            "Staphylococcus aureus": "A client's blood culture grows S. aureus. Which laboratory result identifies it?",
            "Staphylococcus epidermidis": "A client with a prosthetic valve grows S. epidermidis. Which laboratory result identifies it?",
            "Viridans streptococci": "A client's blood culture grows viridans streptococci. Which laboratory result identifies them?",
            "Streptococcus pneumoniae": "A client's culture grows Streptococcus pneumoniae. Which laboratory result identifies it?",
        })

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
