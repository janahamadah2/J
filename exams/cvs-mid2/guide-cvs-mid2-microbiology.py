"""Mastery Study Guide part: Microbiology.

SECTIONS: one section per concept, in lecture order. "key" holds the Key ideas box;
every fact on a linked concept card must appear in its section (build-guide checks).
PROSE fills mechanism, priority actions, patient example, trap, memory trick and
tap-to-reveal blanks ([[answer]])."""

SECTIONS = [
    {"id": "micro-ie-types", "unit": "Microbiology", "title": "Infective endocarditis: classification and organisms", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "IE: infection of the endocardium and its valves (native or prosthetic) with septic vegetations; left-sided in over 95% of cases.",
         "Acute IE: rapid (hours to days), mostly healthy valves, severe symptoms; S. aureus, S. pyogenes; mitral and aortic valves.",
         "Subacute IE: slow (weeks to months), preexisting valve disease, low-grade fever, weight loss; viridans streptococci, enterococci, HACEK.",
         "Prosthetic valve IE: early (within 12 months, intraoperative contamination) or late; mostly S. epidermidis and S. aureus.",
         "IV drug use IE: mainly the tricuspid valve; S. aureus, Pseudomonas aeruginosa, Candida.",
     ]},
    {"id": "micro-organisms", "unit": "Microbiology", "title": "Specific organisms and their associations", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "S. aureus: most common overall, IV drug users and healthcare-associated IE; acute, rapid valve destruction.",
         "Streptococcus bovis is associated with colorectal carcinoma or GI lesions.",
         "Enterococcus faecalis: elderly and hospital-acquired IE, after genitourinary or gastrointestinal procedures.",
         "HACEK (Haemophilus, Aggregatibacter, Cardiobacterium hominis, Eikenella corrodens, Kingella): slow-growing fastidious Gram-negative bacilli of pharyngeal flora; subacute IE with negative cultures unless special media are used.",
         "Cardiac device IE (pacemaker, ICD) usually comes from skin contamination at implantation; mostly staphylococci.",
     ]},
    {"id": "micro-patho", "unit": "Microbiology", "title": "Pathophysiology of infective endocarditis", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "IE needs endothelial injury, bacteremia and microbial adherence leading to vegetation formation.",
         "Damaged valvular endothelium collects platelets and fibrin, forming a sterile microthrombus (sterile vegetation).",
         "Adherence factors: S. aureus clumping factor and fibronectin-binding protein; viridans streptococci dextran; E. faecalis teichoic acid; Gram-negatives pili.",
         "Vegetations contain fibrin, platelets, bacteria and inflammatory cells; they are friable and embolize, and the bacteria are protected from phagocytes and antibiotics.",
         "Consequences: valve destruction with regurgitation and heart failure, septic emboli with infarcts or abscesses, immune complex glomerulonephritis and vasculitis.",
     ]},
    {"id": "micro-signs", "unit": "Microbiology", "title": "Clinical features of infective endocarditis", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "Acute: high fever and sepsis. Subacute: mild fever, headache, myalgia, weight loss, night sweats. Cardiac: murmur, heart failure.",
         "Splinter hemorrhages: petechial hemorrhages under the fingernails.",
         "Janeway lesions: small, nontender, erythematous lesions on palms and soles. Osler nodes: painful nodules on the pads of fingers and toes.",
         "Roth spots: retinal hemorrhages.",
     ]},
    {"id": "micro-dx-tx", "unit": "Microbiology", "title": "Diagnosis, treatment and prophylaxis", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "Blood cultures are the gold standard: three sets from different venipuncture sites before treatment.",
         "Culture-negative IE: prior antibiotics, fastidious bacteria (Coxiella burnetii, Bartonella, Brucella, HACEK; confirm by serology or PCR), fungal infection.",
         "Empiric therapy once cultures are drawn: native valve vancomycin + cefepime; prosthetic valve vancomycin + cefepime + gentamicin + rifampin; then targeted therapy.",
         "Prophylaxis before dental or invasive procedures in high-risk clients, 30-60 minutes before: amoxicillin, ampicillin or cefazolin; if penicillin-allergic, a macrolide (azithromycin) or doxycycline.",
     ]},
    {"id": "micro-lab-id", "unit": "Microbiology", "title": "Laboratory identification of IE organisms", "source": "Microbiology L3 slides (infective endocarditis)",
     "key": [
         "S. aureus: Gram-positive cocci in clusters; golden yellow colonies, beta hemolysis, ferments mannitol; catalase and coagulase positive.",
         "S. epidermidis: Gram-positive cocci in clusters; catalase positive, coagulase negative.",
         "Viridans streptococci (S. mutans): Gram-positive cocci in chains; alpha hemolysis; optochin resistant; insoluble in bile.",
         "S. pyogenes: Gram-positive cocci in chains; beta hemolysis; catalase negative.",
         "S. pneumoniae: lancet-shaped capsulated diplococci; alpha hemolysis; optochin sensitive; bile soluble.",
     ]},
]
PROSE = {
"micro-ie-types": dict(
    mechanism="Infective endocarditis is classified by speed (acute vs subacute), by the valve (native, prosthetic, device) and by the route (IV drug use). Virulent organisms attack healthy valves fast; less virulent ones need a damaged valve and take weeks.",
    actions=["Match setting to organism: IV drug use = tricuspid, S. aureus; prosthetic valve = S. epidermidis or S. aureus; damaged valve after dental work = viridans."],
    example="A client who injects drugs has tricuspid vegetations and Gram-positive cocci in clusters: S. aureus.",
    trap="Assuming subacute IE affects healthy valves.",
    trick="Acute = Aureus, Aggressive; Subacute = Slow, Strep viridans.",
    blanks=["Left-sided endocarditis accounts for more than [[95%]] of cases.",
            "Early prosthetic valve endocarditis develops within [[12]] months of surgery."]),
"micro-organisms": dict(
    mechanism="Each organism hints at its source: skin and devices (staphylococci), mouth (viridans), bowel (S. bovis), urinary or GI tract (enterococci), pharynx (HACEK).",
    actions=["After S. bovis endocarditis, expect evaluation of the colon.",
             "Think HACEK when cultures stay negative without special media."],
    example="An elderly client gets endocarditis after a urinary procedure: Enterococcus faecalis.",
    trap="Thinking the K in HACEK is Klebsiella (it is Kingella).",
    trick="HACEK = Haemophilus, Aggregatibacter, Cardiobacterium, Eikenella, Kingella.",
    blanks=["Streptococcus bovis is associated with [[colorectal carcinoma]]."]),
"micro-patho": dict(
    mechanism="Three things must meet: a damaged valve surface with a sterile platelet-fibrin clot, bacteria in the blood, and bacteria able to stick. Inside the vegetation bacteria hide from phagocytes and antibiotics, shed into the blood and break off as emboli.",
    actions=["Ask about recent dental, skin or invasive procedures (transient bacteremia).",
             "Watch for embolic infarcts and abscesses in brain, kidney, spleen and lung."],
    example="A client with valve disease develops a vegetation after a dental procedure.",
    trap="Thinking antibiotics reach organisms in vegetations easily.",
    trick="Injury, bacteremia, adherence, vegetation.",
    blanks=["Viridans streptococci adhere using [[dextran]].",
            "Immune complex deposition can cause [[glomerulonephritis]]."]),
"micro-signs": dict(
    mechanism="The extracardiac signs come from septic emboli and immune-mediated injury: small hemorrhages and lesions in nails, skin and retina.",
    actions=["Inspect nails, palms, soles, finger pads and retina in suspected IE.",
             "Separate IE signs from rheumatic fever signs (erythema marginatum, extensor nodules, chorea)."],
    example="A client has painful nodules on the finger pads: Osler nodes.",
    trap="Mixing up Janeway (painless) and Osler (painful).",
    trick="Osler = Ouch; Janeway = painless palms.",
    blanks=["Roth spots are [[retinal hemorrhages]]."]),
"micro-dx-tx": dict(
    mechanism="Organisms shed continuously from the vegetation, so blood cultures catch them, but only if taken before antibiotics. Empiric treatment starts right after cultures and is narrowed when results arrive. Prophylaxis protects high-risk valves before procedures.",
    actions=["Draw three sets of blood cultures from different sites before the first antibiotic.",
             "Anticipate vancomycin + cefepime for native valves; add gentamicin + rifampin for prosthetic valves.",
             "Give prophylaxis 30-60 minutes before the procedure; use azithromycin or doxycycline if penicillin-allergic."],
    example="A client with a prosthetic valve and penicillin allergy gets azithromycin before a dental extraction.",
    trap="Giving the first antibiotic dose before cultures.",
    trick="Culture first, cure second.",
    blanks=["Fastidious organisms in culture-negative IE are confirmed by serology or [[PCR]]."]),
"micro-lab-id": dict(
    mechanism="Shape and arrangement split staphylococci (clusters) from streptococci (chains). Then catalase, coagulase, hemolysis, optochin and bile solubility separate the species.",
    actions=["Coagulase positive = S. aureus; coagulase negative = S. epidermidis.",
             "Alpha hemolytic: optochin sensitive and bile soluble = pneumococcus; resistant and insoluble = viridans."],
    example="A blood culture shows Gram-positive cocci in clusters that are coagulase positive: S. aureus.",
    trap="Mixing up viridans and pneumococcus, both alpha hemolytic.",
    trick="Pneumococcus is Optochin-sensitive: O-P.",
    blanks=["S. aureus forms golden yellow colonies and ferments [[mannitol]].",
            "Haemophilus grows on [[chocolate]] agar."]),
}
for _s in SECTIONS:
    _s.update(PROSE[_s["id"]])
