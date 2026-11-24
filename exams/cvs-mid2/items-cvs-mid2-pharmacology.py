from _authoring import Bank

B = Bank("Pharmacology")
L = "Pharmacology L2-L4 slides (treatment of hypertension)"

B.concept("pharm-classes", "Hypertension: definition and drug classes", [
    "Hypertension is defined as 130/80 mm Hg or higher (ACC/AHA 2023 and Saudi Heart Association).",
    "Classes: diuretics, calcium channel blockers, drugs acting on the renin-angiotensin system, sympatholytic drugs, vasodilators.",
    "Drug list: hydrochlorothiazide, indapamide, furosemide, spironolactone (diuretics); clonidine, methyldopa, prazosin, propranolol, labetalol, esmolol (sympathoplegic); hydralazine, nitroprusside, minoxidil, diazoxide, fenoldopam, CCBs (vasodilators); captopril, enalapril, enalaprilat (ACE inhibitors); losartan (ARB); aliskiren (renin inhibitor).",
], L)

B.mc("A 52-year-old client's average blood pressure over several visits is 132/82 mm Hg. How should the nurse interpret this reading?",
     "It meets the definition of hypertension.",
     [("It is normal because hypertension starts at 140/90 mm Hg.", "The current definition (ACC/AHA 2023 and SHA) is 130/80 mm Hg or higher.", "uses the old 140/90 threshold"),
      ("It is hypertension only if the systolic reading is 140 or more.", "Either value at or above 130/80 meets the definition; 132/82 exceeds both."),
      ("It cannot be classified without a renin level.", "Hypertension is defined by blood pressure, not by renin.")],
     "Both the ACC/AHA (2023) and the Saudi Heart Association define hypertension as a blood pressure of 130/80 mm Hg or higher. A reading of 132/82 is above both numbers. Hypertension affects 1 in 3 US adults and is more common with age and obesity.",
     L)

B.match("A nurse reviews a client's antihypertensive medication list. Match each drug to its class.",
        [("Hydrochlorothiazide", "Diuretic"),
         ("Clonidine", "Sympathoplegic drug"),
         ("Hydralazine", "Vasodilator"),
         ("Losartan", "Angiotensin receptor blocker (ARB)")],
        [("ACE inhibitor", "ACE inhibitors on the list are captopril, enalapril and enalaprilat.", "mixes up ARBs and ACE inhibitors"),
         ("Renin inhibitor", "The only renin inhibitor is aliskiren.")],
        "The drug list groups antihypertensives by where they act: diuretics (hydrochlorothiazide, indapamide, furosemide, spironolactone), sympathoplegic drugs (clonidine, methyldopa, prazosin, propranolol, labetalol, esmolol), vasodilators (hydralazine, nitroprusside, minoxidil, diazoxide, fenoldopam, CCBs) and inhibitors of the renin-angiotensin system: ACE inhibitors (captopril, enalapril, enalaprilat), ARBs (losartan) and renin inhibitors (aliskiren).",
        L + ", drug list slide",
        row_stems={
            "Hydrochlorothiazide": "A client is started on hydrochlorothiazide for hypertension. To which drug class does it belong?",
            "Clonidine": "A client's medication list includes clonidine. Which drug class should the nurse identify?",
            "Hydralazine": "A client receives hydralazine for blood pressure. Which drug class does it belong to?",
            "Losartan": "A client who could not tolerate captopril is switched to losartan. Which drug class is losartan?",
        }, last=True)

B.concept("pharm-diuretics", "Diuretics in hypertension", [
    "Early: diuretics lower plasma volume and cardiac output. After 4-8 weeks volume and output return toward normal while peripheral vascular resistance falls (arteriolar vasodilation).",
    "Main mechanism of the vasodilation: depletion of body Na+, lowering smooth muscle Na+ and then intracellular Ca++ via the Na/Ca exchanger.",
    "Thiazides are first choice; antihypertensive doses are lower than diuretic doses.",
    "Loop diuretics are preferable in malignant hypertension and chronic kidney disease.",
    "Potassium-sparing diuretics are used with thiazides to counteract hypokalemia; spironolactone is used in hyperaldosteronism.",
], L)

B.mc("A client who has taken a thiazide for 6 weeks asks why the blood pressure stays down even though urination is back to normal. Which explanation by the nurse is accurate?",
     "Peripheral vascular resistance has fallen because body sodium depletion lowers calcium in vascular smooth muscle.",
     [("Plasma volume and cardiac output stay reduced for as long as the drug is taken.", "Volume and cardiac output return toward normal after 4-8 weeks; the early effect does not persist.", "thinks diuretics work only by volume loss"),
      ("The thiazide blocks L-type calcium channels in the arterioles.", "Blocking L-type Ca++ channels is the mechanism of calcium channel blockers."),
      ("The thiazide blocks beta-1 receptors on the heart.", "Beta-1 blockade is the mechanism of beta blockers.")],
     "Diuretics first lower blood pressure by reducing plasma volume and cardiac output. After 4-8 weeks of therapy volume and output return toward normal, but peripheral vascular resistance falls through arteriolar vasodilation. The likely main mechanism is depletion of body Na+ stores: less Na+ in smooth muscle lowers intracellular Ca++ through the Na/Ca exchanger. Renal prostaglandins and K channel opening may also contribute. This is why diuretic efficacy does not strictly match antihypertensive efficacy.",
     L)

B.mc("A client with chronic kidney disease has hypertension that needs a diuretic. Which diuretic class should the nurse anticipate?",
     "A loop diuretic such as furosemide",
     [("A thiazide such as hydrochlorothiazide", "Thiazides are first choice in patients with NORMAL renal function.", "uses thiazides in CKD"),
      ("A potassium-sparing diuretic alone", "Potassium-sparing diuretics are used only combined with thiazides to counteract hypokalemia.", "thinks K-sparing diuretics are used alone"),
      ("Diazoxide", "Diazoxide is a potassium channel opener that does not cause diuresis.")],
     "Thiazides and thiazide-like drugs are the first-choice antihypertensive diuretics and the most effective in patients with normal renal function. Loop diuretics are preferable only in specific situations such as malignant hypertension and concomitant chronic kidney disease.",
     L)

B.mc("A client on hydrochlorothiazide has a low serum potassium. Which drug should the nurse anticipate being added?",
     "Spironolactone",
     [("Furosemide", "Furosemide is a loop diuretic; it would not correct hypokalemia.", "adds a K-wasting diuretic"),
      ("Indapamide", "Indapamide is a thiazide-like diuretic, which also lowers potassium."),
      ("Fenoldopam", "Fenoldopam is an IV D1 agonist that itself decreases serum potassium.")],
     "Potassium-sparing diuretics are used only in combination with thiazides, to counteract the hypokalemia thiazides cause. Spironolactone is the potassium-sparing diuretic on the list and is also used for hypertension due to hyperaldosteronism.",
     L)

B.tf("A nurse explains that the antihypertensive doses of thiazides are lower than those required for a diuretic effect.", True,
     "True. Thiazides lower blood pressure at doses lower than those needed for diuresis, another sign that they do not work only by increasing urine output.",
     L, "This statement is true: antihypertensive doses are lower than diuretic doses.")

B.concept("pharm-ccb", "Calcium channel blockers", [
    "CCBs bind the L-type voltage-gated Ca++ channel from the inner side of the membrane.",
    "Verapamil and diltiazem block Ca++ channels in heart and vessels; dihydropyridines (nifedipine, nicardipine) block vessels only.",
    "Heart rate: increased with dihydropyridines; unchanged or decreased with verapamil and diltiazem. Postural hypotension is negligible.",
    "First-choice drugs, more effective in African patients; nicardipine for hypertensive emergencies; short-acting nifedipine increases mortality.",
], L)

B.mc("A client starts nifedipine for hypertension. Which change in heart rate should the nurse expect?",
     "Heart rate may increase.",
     [("Heart rate will decrease.", "Unchanged or decreased heart rate is the pattern of verapamil and diltiazem.", "mixes up dihydropyridine and non-dihydropyridine effects"),
      ("Heart rate will fall and AV block will develop.", "Bradycardia and AV block are risks of central sympatholytics and of beta blockers."),
      ("Marked postural drops in heart rate will occur.", "Postural hypotension with CCBs is negligible.")],
     "Dihydropyridines such as nifedipine block Ca++ channels in the vessels only, so they lower peripheral resistance and heart rate (and cardiac output) may increase. Verapamil and diltiazem also block cardiac channels, so heart rate is unchanged or decreased. All CCBs lower peripheral resistance with negligible postural hypotension.",
     L)

B.sata("A nurse reviews the pharmacology of calcium channel blockers. Which statements are accurate?",
       ["They bind L-type voltage-gated Ca++ channels from the inner side of the membrane.", "Verapamil and diltiazem block Ca++ channels in both heart and vessels.", "Dihydropyridines block Ca++ channels in the vessels only.", "Their blockade can be partly reversed by beta-1 agonists."],
       [("Nicardipine has low vascular selectivity.", "Nicardipine has VERY HIGH vascular selectivity; verapamil and diltiazem have low selectivity.", "mixes up vascular selectivity of CCBs"),
        ("Short-acting nifedipine is preferred for long-term hypertension.", "Short-acting nifedipine has been linked to increased mortality in hypertension.", "thinks short-acting nifedipine is safe")],
       "Calcium channel blockers bind the L-type voltage-gated Ca++ channel from the inner side of the membrane. Verapamil and diltiazem (low vascular selectivity) block channels in heart and vessels, while dihydropyridines (nifedipine high, nicardipine very high selectivity) act only on vessels. Drugs that increase Ca++ flux, such as beta-1 agonists, can partly reverse the blockade.",
       L)

B.mc("A client is admitted with a hypertensive emergency. Which calcium channel blocker should the nurse anticipate?",
     "Nicardipine",
     [("Short-acting nifedipine", "Short-acting nifedipine is linked to increased mortality in hypertension."),
      ("Verapamil", "Verapamil is not the CCB named for hypertensive emergencies; it also blocks cardiac channels."),
      ("Diltiazem", "Diltiazem is not the CCB named for hypertensive emergencies.")],
     "Calcium channel blockers are first-choice drugs in hypertension and are more effective in African patients. For hypertensive emergencies nicardipine is used. Long-term studies have linked short-acting nifedipine to increased mortality, whereas slow-release formulations apparently do not increase the risk.",
     L)

B.tf("A nurse states that short-acting nifedipine is preferred for long-term hypertension because it lowers mortality.", False,
     "False. Long-term epidemiological studies report an INCREASED risk of mortality with short-acting nifedipine in hypertension; slow-release formulations apparently do not increase this risk.",
     L, "Short-acting nifedipine is linked to increased mortality.", "thinks short-acting nifedipine is safe")

B.concept("pharm-ras", "Renin inhibitors, ACE inhibitors and ARBs", [
    "Aliskiren competitively inhibits renin: angiotensin I, II and aldosterone fall and renin rises; hyperkalemia when combined with ACE inhibitors or ARBs.",
    "ACE inhibitors block conversion of angiotensin I to II and raise bradykinin; less angiotensin II removes negative feedback, so renin rises.",
    "Captopril, lisinopril and enalaprilat are active drugs; enalapril, benazepril and fosinopril are prodrugs activated by the liver; enalaprilat is the IV form.",
    "ACE inhibitor adverse effects: first-dose hypotension, dry cough (bradykinin, prostaglandins or substance P), renal insufficiency in bilateral renal artery stenosis, hyperkalemia, angioedema; pregnancy category D.",
    "ARBs (losartan) selectively block AT1 receptors, inhibit angiotensin more completely and have no effect on bradykinin; contraindicated in bilateral renal artery stenosis and pregnancy.",
], L)

B.mc("A client is started on aliskiren. Which laboratory pattern should the nurse expect?",
     "Decreased angiotensin II and aldosterone with increased renin concentration",
     [("Increased angiotensin II with decreased renin", "Aliskiren lowers angiotensin II; renin RISES because feedback is removed.", "reverses the renin response"),
      ("Decreased renin, angiotensin II and aldosterone", "Renin concentration increases, not decreases.", "thinks renin falls with a renin inhibitor"),
      ("Increased bradykinin with unchanged angiotensin II", "Raised bradykinin is an effect of ACE inhibitors.", "mixes up renin and ACE inhibitors")],
     "Aliskiren, the only renin inhibitor on the market, competitively inhibits renin, the enzyme that converts angiotensinogen to angiotensin I (the rate-limiting step). Angiotensin I, angiotensin II and aldosterone fall, and with less negative feedback the renin level rises. It is usually well tolerated but can cause hyperkalemia when combined with ACE inhibitors or ARBs.",
     L)

B.mc("A client taking captopril reports a dry, irritating cough. Which explanation should the nurse give?",
     "Accumulation of bradykinin, prostaglandins or substance P in the lungs",
     [("Accumulation of angiotensin II in the lungs", "ACE inhibitors DECREASE angiotensin II formation.", "thinks ACE inhibitors raise angiotensin II"),
      ("Excess aldosterone secretion", "ACE inhibitors reduce angiotensin II-driven aldosterone; aldosterone does not cause cough."),
      ("Blockade of beta-2 receptors in the airways", "Bronchoconstriction from beta blockade is a beta-blocker effect.", "mixes up ACE inhibitor cough and beta-blocker bronchospasm")],
     "The converting enzyme both forms angiotensin II and inactivates bradykinin. Inhibiting it lowers angiotensin II and raises bradykinin. The dry, disturbing cough may be mediated by accumulation in the lungs of bradykinin and prostaglandins or, more likely, substance P. ARBs have no effect on bradykinin, which is why they are the alternative.",
     L)

B.sata("A client is started on enalapril. Which adverse effects should the nurse monitor for?",
       ["Hypotension after the first doses", "Dry cough", "Hyperkalemia", "Angioedema", "Renal insufficiency in bilateral renal artery stenosis"],
       [("Hypokalemia", "ACE inhibitors cause HYPERkalemia.", "reverses the potassium effect of ACE inhibitors"),
        ("Hypertrichosis", "Hypertrichosis is an adverse effect of minoxidil."),
        ("Positive Coombs' test", "A positive Coombs' test is caused by methyldopa.")],
       "ACE inhibitor adverse effects follow from less angiotensin II and more bradykinin: hypotension and postural hypotension mainly after the first doses (in salt- and water-depleted or heart failure patients), dry cough, renal insufficiency in bilateral renal artery stenosis or a stenosed solitary kidney, hyperkalemia and rare but possibly fatal angioedema. They are pregnancy category D.",
       L)

B.mc("A client who started lisinopril last week reports swelling of the lips and tongue. Which action should the nurse take first?",
     "Treat it as a potentially fatal reaction and report it immediately.",
     [("Reassure the client that this is the common ACE inhibitor cough.", "The cough is a different, non-dangerous adverse effect; swelling of lips and tongue is angioedema.", "confuses angioedema with ACE inhibitor cough"),
      ("Tell the client it happens only after the first dose and will settle.", "First-dose hypotension, not angioedema, is the effect linked to initial doses.", "confuses angioedema with first-dose hypotension"),
      ("Advise taking the next dose with food.", "Taking the drug with food does nothing for angioedema.")],
     "Angioneurotic edema is a rare adverse effect of ACE inhibitors (up to 0.3%) but it may be fatal; inhibition of bradykinin metabolism may be involved. Swelling of the lips and tongue therefore needs immediate action, unlike the common dry cough.",
     L)

B.mc("A client has liver disease and needs an ACE inhibitor. Which ACE inhibitor must be activated by the liver before it works?",
     "Enalapril",
     [("Captopril", "Captopril is an active drug and needs no activation.", "thinks all ACE inhibitors are prodrugs"),
      ("Lisinopril", "Lisinopril is an active drug and needs no activation.", "thinks all ACE inhibitors are prodrugs"),
      ("Enalaprilat", "Enalaprilat is the active form of enalapril, given IV.", "mixes up enalapril and enalaprilat")],
     "Captopril, lisinopril and enalaprilat are active drugs. All other ACE inhibitors (enalapril, benazepril, fosinopril and others) are prodrugs that the liver converts into active metabolites. Enalaprilat is also the only one given intravenously.",
     L)

B.mc("A client in a hypertensive emergency needs an ACE inhibitor intravenously. Which drug should the nurse anticipate?",
     "Enalaprilat",
     [("Enalapril", "Enalapril is an oral prodrug.", "mixes up enalapril and enalaprilat"),
      ("Captopril", "Captopril is given by mouth only."),
      ("Losartan", "Losartan is an ARB given by mouth only.")],
     "All ACE inhibitors except enalaprilat are given by the oral route only. Enalaprilat, the active form of enalapril, is given IV and is the ACE inhibitor used in hypertensive emergencies.",
     L)

B.sata("A pregnant client at 20 weeks has hypertension. Which drug orders should the nurse question?",
       ["Losartan", "Enalapril"],
       [("Methyldopa", "Methyldopa is often preferred in pregnancy; long experience shows it is not harmful to the fetus.", "thinks methyldopa is unsafe in pregnancy"),
        ("Labetalol", "Labetalol is used to treat hypertension in pregnancy.", "thinks labetalol is unsafe in pregnancy")],
       "ACE inhibitors and ARBs are pregnancy category D; ARBs carry a substantial teratogenic risk. Orders for losartan or enalapril in pregnancy should be questioned. Methyldopa is often preferred in pregnancy, and labetalol is used for hypertension in pregnancy.",
       L)

B.mc("A client who developed a cough on captopril is switched to losartan. Which statement by the client indicates correct understanding?",
     "\"Losartan blocks the angiotensin receptor, so it should not cause the same cough.\"",
     [("\"Losartan works the same way as captopril by blocking the converting enzyme.\"", "Losartan blocks AT1 receptors; it does not inhibit ACE.", "thinks ARBs inhibit ACE"),
      ("\"Losartan raises bradykinin even more than captopril.\"", "ARBs have no effect on bradykinin metabolism."),
      ("\"Losartan is safe if I become pregnant.\"", "ARBs are pregnancy category D with substantial teratogenic risk.", "thinks ARBs are safe in pregnancy")],
     "Losartan competitively and selectively blocks AT1 receptors. It prevents or reverses most actions of angiotensin II and inhibits them more completely than ACE inhibitors, because enzymes other than ACE can still make angiotensin II. It has no effect on bradykinin, so it does not cause the bradykinin-related cough, which makes it the alternative to ACE inhibitors.",
     L)

B.tf("A nurse states that losartan lowers blood pressure by inhibiting the converting enzyme that forms angiotensin II.", False,
     "False. Losartan is an angiotensin II receptor antagonist: it competitively blocks AT1 receptors. Inhibiting the converting enzyme is the mechanism of ACE inhibitors such as captopril.",
     L, "Losartan blocks AT1 receptors; ACE inhibitors block the enzyme.", "thinks ARBs inhibit ACE")

B.mc("A client with diabetes and early glomerular disease is prescribed an ACE inhibitor. How does the drug slow progression of the kidney disease?",
     "It prevents angiotensin II-induced vasoconstriction of the efferent glomerular arteriole.",
     [("It dilates the afferent arteriole by releasing nitric oxide.", "Nitric oxide release is the mechanism of nitroprusside."),
      ("It increases aldosterone to retain sodium.", "ACE inhibitors reduce angiotensin II-driven aldosterone secretion."),
      ("It blocks D1 receptors in the renal vessels.", "Fenoldopam ACTIVATES D1 receptors; ACE inhibitors do not act on them.")],
     "In diabetic glomerulopathy and hypertensive nephroangiosclerosis, ACE inhibitors decrease disease progression by preventing angiotensin II-induced vasoconstriction of the efferent glomerular arteriole. They are also first-choice in hypertension and are used after myocardial infarction and in chronic heart failure.",
     L)

B.concept("pharm-central", "Centrally acting sympatholytics", [
    "Clonidine and methyldopa are alpha-2 receptor agonists; methyldopa is a false neurotransmitter converted to methylnorepinephrine; clonidine also acts on imidazoline receptors in the medulla.",
    "The final common effect is a decrease in central adrenergic tone.",
    "Second-choice drugs; methyldopa is often preferred in pregnancy.",
    "Adverse effects: sedation, depression, bradycardia, AV block, sexual dysfunction; clonidine withdrawal can cause a hypertensive crisis; methyldopa can cause a positive Coombs' test.",
], L)

B.mc("A pregnant client needs treatment for chronic hypertension. Which drug is often preferred because long experience shows it is not harmful to the fetus?",
     "Methyldopa",
     [("Losartan", "Losartan is pregnancy category D with substantial teratogenic risk.", "thinks ARBs are safe in pregnancy"),
      ("Enalapril", "ACE inhibitors are pregnancy category D.", "thinks ACE inhibitors are safe in pregnancy"),
      ("Minoxidil", "Minoxidil is reserved for severe resistant hypertension because of its toxicity.")],
     "Methyldopa is taken up by adrenergic neurons and converted to methylnorepinephrine, which activates central alpha-2 receptors and lowers sympathetic tone. It is a second-choice drug in general, but it is often preferred for hypertension in pregnancy because long experience shows it does not harm the fetus.",
     L)

B.mc("A client taking clonidine plans to stop the drug suddenly because it causes drowsiness. Which response by the nurse is best?",
     "\"Stopping clonidine suddenly can cause a hypertensive crisis, so talk with your provider before stopping.\"",
     [("\"Stopping suddenly is safe because clonidine has no withdrawal effects.\"", "Sudden withdrawal of clonidine can cause a hypertensive crisis.", "thinks clonidine can be stopped abruptly"),
      ("\"Drowsiness means the dose is too low; take an extra tablet.\"", "Sedation and drowsiness are adverse effects, not a sign of under-dosing."),
      ("\"Clonidine only causes problems when given through the skin.\"", "Transdermal clonidine causes skin eruptions, but withdrawal crisis can occur with any route.")],
     "Clonidine and methyldopa lower central adrenergic tone. Their CNS adverse effects include sedation and drowsiness, and clonidine (rarely methyldopa) can cause a hypertensive crisis when suddenly withdrawn. The client should not stop it abruptly.",
     L)

B.mc("A client on long-term methyldopa needs a blood transfusion and the crossmatch shows a problem. Which adverse effect of methyldopa explains this?",
     "A positive Coombs' test",
     [("Lupoid syndrome", "Lupoid syndrome is an immunological adverse effect of hydralazine.", "mixes up methyldopa and hydralazine immune effects"),
      ("Hyperkalemia", "Hyperkalemia is an adverse effect of ACE inhibitors and aliskiren combinations."),
      ("Cyanide toxicity", "Cyanide toxicity is an adverse effect of nitroprusside.")],
     "Methyldopa is a false neurotransmitter that becomes methylnorepinephrine and stimulates central alpha-2 receptors. Besides sedation and sexual dysfunction, it can cause a positive Coombs' test, which matters when blood is crossmatched.",
     L)

B.match("A nurse reviews how several antihypertensives act. Match each drug to its mechanism.",
        [("Methyldopa", "False neurotransmitter converted to methylnorepinephrine"),
         ("Clonidine", "Activates imidazoline receptors in the medulla"),
         ("Prazosin", "Selective alpha-1 receptor blockade"),
         ("Propranolol", "Non-selective beta receptor blockade")],
        [("Selective beta-1 blockade", "Selective beta-1 blockers are atenolol, bisoprolol and metoprolol.", "thinks propranolol is beta-1 selective")],
        "Methyldopa is taken up into adrenergic neurons and converted to methylnorepinephrine, an alpha-2 agonist. Clonidine activates central alpha-2 receptors and imidazoline receptors in the medulla. Both reduce central adrenergic tone. Prazosin selectively blocks alpha-1 receptors, dilating resistance and capacitance vessels. Propranolol is a non-selective beta blocker.",
        L,
        row_stems={
            "Methyldopa": "A client asks how methyldopa lowers blood pressure. Which mechanism should the nurse describe?",
            "Clonidine": "A nurse explains clonidine's action. Which receptor site in the medulla does it activate?",
            "Prazosin": "A client starts prazosin. Which mechanism lowers the client's blood pressure?",
            "Propranolol": "A client with asthma is prescribed propranolol. Which mechanism makes the nurse concerned?",
        })

B.concept("pharm-alpha-beta", "Alpha blockers, beta blockers and alpha-beta blockers", [
    "Prazosin and doxazosin selectively block alpha-1 receptors, dilating resistance and capacitance vessels; postural hypotension after the first dose (\"first-dose phenomenon\").",
    "Beta blockers lower cardiac output (cardiac beta-1) and inhibit renin release (juxtaglomerular beta-1); they do not cause postural hypotension.",
    "Selective beta-1: atenolol, bisoprolol, metoprolol. Non-selective: propranolol, penbutolol, timolol.",
    "Beta-blocker adverse effects: bradycardia, rebound hypertension on abrupt withdrawal, bronchoconstriction, insomnia, depression, hypoglycemia, sexual dysfunction.",
    "Labetalol and carvedilol block alpha and beta; labetalol for hypertension in pregnancy and IV in emergencies; carvedilol for heart failure.",
], L)

B.mc("A client receives the first dose of prazosin. Which adverse effect should the nurse monitor for most closely?",
     "Postural hypotension",
     [("Bronchoconstriction", "Bronchoconstriction is an adverse effect of beta blockers.", "mixes up alpha and beta blocker effects"),
      ("Hypertrichosis", "Hypertrichosis is an adverse effect of minoxidil."),
      ("Cyanide toxicity", "Cyanide toxicity is an adverse effect of nitroprusside."),
      ("Dry cough", "Dry cough is an adverse effect of ACE inhibitors.")],
     "Prazosin and doxazosin selectively block alpha-1 receptors and lower blood pressure by dilating both resistance and capacitance (venous) vessels. Dilating the veins reduces venous return on standing, so postural hypotension can occur, mainly after the first dose: the \"first-dose phenomenon\". Tachycardia, palpitations and syncope may accompany it.",
     L)

B.sata("A client is started on a beta blocker for hypertension. Which adverse effects should the nurse teach the client about?",
       ["Bradycardia", "Bronchoconstriction", "Hypoglycemia", "Rebound hypertension if stopped abruptly", "Insomnia or depression"],
       [("Postural hypotension", "Beta blockers do not cause postural hypotension because venous tone is unchanged.", "thinks beta blockers cause postural hypotension"),
        ("Hyperglycemia", "Hyperglycemia is an adverse effect of diazoxide; beta blockers cause HYPOglycemia.", "reverses the glucose effect of beta blockers"),
        ("Hypertrichosis", "Hypertrichosis is an adverse effect of minoxidil.")],
       "Beta blockers lower heart rate and cardiac output and leave venous tone unchanged, so they do not cause postural hypotension. Adverse effects: bradycardia, hypotension and rebound hypertension on abrupt withdrawal; bronchoconstriction; insomnia, depression and nightmares; hypoglycemia because the liver's gluconeogenesis and glycogenolysis are impaired; and sexual dysfunction.",
       L)

B.mc("A client with asthma needs a beta blocker. Which drug is beta-1 selective?",
     "Metoprolol",
     [("Propranolol", "Propranolol is a non-selective beta blocker.", "thinks propranolol is beta-1 selective"),
      ("Timolol", "Timolol is a non-selective beta blocker."),
      ("Penbutolol", "Penbutolol is a non-selective beta blocker."),
      ("Labetalol", "Labetalol blocks both alpha and beta receptors.")],
     "Beta blockers are divided into beta-1 selective drugs (atenolol, bisoprolol, metoprolol) and non-selective drugs (propranolol, penbutolol, timolol). Bronchoconstriction is a respiratory adverse effect of beta blockade, so selectivity matters in a client with asthma. Labetalol and carvedilol block both alpha and beta receptors.",
     L)

B.mc("A nurse explains how a beta blocker lowers a client's blood pressure. Which explanation is accurate?",
     "It decreases cardiac output and inhibits renin release by blocking beta-1 receptors.",
     [("It dilates both arterioles and veins by blocking alpha-1 receptors.", "Alpha-1 blockade of resistance and capacitance vessels is how prazosin works.", "mixes up alpha and beta blocker mechanisms"),
      ("It opens potassium channels in arteriolar smooth muscle.", "Potassium channel opening is the mechanism of minoxidil and diazoxide."),
      ("It lowers venous tone so blood pools on standing.", "Beta blockers leave venous tone unchanged and do not cause postural hypotension.")],
     "Beta blockers lower blood pressure by two beta-1 effects: blocking cardiac beta-1 receptors lowers heart rate and cardiac output, and blocking beta-1 receptors on juxtaglomerular cells inhibits renin release. Venous tone is unchanged, so they do not cause postural hypotension.",
     L)

B.mc("A client has heart failure and hypertension. Which alpha-beta blocker is used to treat heart failure?",
     "Carvedilol",
     [("Labetalol", "Labetalol is used in pregnancy and IV for hypertensive emergencies, not named for heart failure.", "mixes up labetalol and carvedilol uses"),
      ("Prazosin", "Prazosin is a selective alpha-1 blocker."),
      ("Esmolol", "Esmolol is on the sympathoplegic list but is not an alpha-beta blocker.")],
     "Labetalol and carvedilol block both alpha and beta receptors, causing vasodilation and reduced heart rate and contractility. They are used in black and elderly patients; labetalol in hypertension with pregnancy and IV for hypertensive emergencies; carvedilol to treat heart failure. Their main side effects are orthostatic hypotension and dizziness.",
     L)

B.concept("pharm-vasodilators", "Direct vasodilators", [
    "Nitroprusside: arterioles and veins, nitric oxide; metabolized by red cells releasing cyanide (to thiocyanate); half-life about 2 minutes, continuous infusion; for emergencies, severe heart failure, controlled hypotension.",
    "Hydralazine: arterioles, uncertain mechanism; headache, palpitations, flushing; immunological lupoid syndrome (up to 20% at very high doses).",
    "Minoxidil: arteriolar K+ channel opener, a prodrug; salt and water retention, tachycardia, hypertrichosis; also used for baldness.",
    "Diazoxide: K+ channel opener without diuresis (lacks a sulfonamide group); salt and water retention, hyperglycemia; for hypertensive emergencies.",
    "Fenoldopam: IV D1 agonist, renal and mesenteric vasodilation and natriuresis; reflex tachycardia, raised intraocular pressure, low potassium; contraindicated in angina, glaucoma and hypokalemia.",
], L)

B.match("A nurse reviews the vasodilators used in hypertension. Match each drug to its mechanism of action.",
        [("Nitroprusside", "Production of nitric oxide in arterioles and veins"),
         ("Minoxidil", "K+ channel opening in arterioles"),
         ("Fenoldopam", "D1-receptor activation in arterioles"),
         ("Hydralazine", "Uncertain; perhaps inhibition of Ca++ release and NO release")],
        [("Selective alpha-1 receptor blockade", "Alpha-1 blockade is the mechanism of prazosin, not a direct vasodilator.", "mixes up alpha blockers and direct vasodilators")],
        "The direct vasodilators differ by site and mechanism. Nitroprusside acts on arterioles and veins by producing nitric oxide. Minoxidil and diazoxide open K+ channels in arterioles. Fenoldopam activates D1 receptors in arterioles. Hydralazine relaxes arterioles by an uncertain mechanism, perhaps inhibiting Ca++ release from the sarcoplasmic reticulum and stimulating NO release.",
        L,
        row_stems={
            "Nitroprusside": "A client receives a nitroprusside infusion. Which mechanism produces its vasodilation?",
            "Minoxidil": "A client with resistant hypertension starts minoxidil. Which mechanism lowers the blood pressure?",
            "Fenoldopam": "A client in a hypertensive emergency receives fenoldopam. Which mechanism does it use?",
            "Hydralazine": "A nurse explains hydralazine's mechanism to a client. Which description is accurate?",
        })

B.mc("A client has received a nitroprusside infusion for several days. Which toxicity should the nurse monitor for?",
     "Cyanide toxicity",
     [("Lupoid syndrome", "Lupoid syndrome is an immunological adverse effect of hydralazine.", "mixes up nitroprusside and hydralazine toxicity"),
      ("Hypertrichosis", "Hypertrichosis is an adverse effect of minoxidil."),
      ("Hyperglycemia", "Hyperglycemia is an adverse effect of diazoxide.")],
     "Nitroprusside is rapidly metabolized by red blood cells, liberating cyanide, which is then metabolized to thiocyanate. Its half-life is about 2 minutes, so it must be given by continuous infusion. Adverse effects include excessive vasodilation, rebound hypertension, palpitations, nausea, substernal pain and cyanide toxicity.",
     L)

B.tf("A nurse states that nitroprusside has a half-life of about 2 minutes and must be given by continuous infusion.", True,
     "True. Nitroprusside's half-life is about 2 minutes, so it must be given by continuous infusion to be effective.",
     L, "This statement is true: half-life about 2 minutes, continuous infusion.")

B.mc("A client takes high-dose hydralazine. Which adverse effect is immunological rather than an extension of the drug's vasodilator action?",
     "Lupoid syndrome",
     [("Headache", "Headache is an extension of the pharmacological (vasodilator) effect.", "mixes up immune and pharmacological effects"),
      ("Palpitations", "Palpitations are an extension of the pharmacological effect.", "mixes up immune and pharmacological effects"),
      ("Flushing", "Flushing is an extension of the pharmacological effect.", "mixes up immune and pharmacological effects")],
     "Hydralazine relaxes small arteries and arterioles. Headache, dizziness, palpitations and flushing extend that vasodilator effect. Separately, immunological reactions occur: lupoid syndrome (up to 20% with very high doses), fever, serum sickness, hemolytic anemia and vasculitis. It is used with isosorbide mononitrate in heart failure.",
     L)

B.mc("A client on minoxidil for severe hypertension notices increased hair growth on the face and arms. How should the nurse interpret this?",
     "It is hypertrichosis, a known adverse effect of minoxidil.",
     [("It is a sign of cyanide toxicity.", "Cyanide toxicity comes from nitroprusside."),
      ("It is part of a lupoid syndrome.", "Lupoid syndrome is a hydralazine adverse effect.", "mixes up minoxidil and hydralazine effects"),
      ("It means the drug is acting as a diuretic.", "Minoxidil causes salt and water retention, not diuresis.")],
     "Minoxidil is a prodrug that the liver converts to an active K+ channel opener in arterioles. Because of its toxicity it is reserved for severe hypertension that responds poorly to other drugs. Adverse effects are salt and water retention, tachycardia, palpitations, flushing and hypertrichosis, which is why it is also used locally to treat baldness.",
     L)

B.mc("A client with diabetes receives diazoxide for a hypertensive emergency. Which value should the nurse monitor closely?",
     "Blood glucose, because diazoxide causes hyperglycemia",
     [("Urine output, because diazoxide causes strong diuresis", "Diazoxide does NOT cause diuresis (it lacks a sulfonamide group); it causes salt and water retention.", "thinks diazoxide is a diuretic"),
      ("Blood cyanide, because diazoxide releases cyanide", "Cyanide is released from nitroprusside."),
      ("Coombs' test, because diazoxide causes hemolysis", "A positive Coombs' test is caused by methyldopa.")],
     "Diazoxide is a potassium channel opener used for hypertensive emergencies. It resembles the thiazides but does not cause diuresis, apparently because it lacks a sulfonamide group. Adverse effects are salt and water retention with edema, hyperglycemia, and excessive hypotension, flushing and headache.",
     L)

B.mc("Fenoldopam is ordered for several clients with severe hypertension. For which client should the nurse question the order?",
     "A client with glaucoma",
     [("A client with a hypertensive emergency", "A hypertensive emergency is fenoldopam's therapeutic use."),
      ("A client with hyperkalemia", "Fenoldopam lowers potassium; the contraindication is HYPOkalemia.", "reverses the potassium contraindication"),
      ("A client who needs renal vasodilation", "Fenoldopam mainly dilates renal and mesenteric vessels.")],
     "Fenoldopam, the only D1-receptor agonist, is given by IV infusion for hypertensive emergencies. It dilates mainly renal and mesenteric vessels and increases natriuresis. Its adverse effects explain its contraindications: reflex tachycardia (angina), a dose-dependent rise in intraocular pressure (glaucoma) and a fall in serum potassium (hypokalemic states).",
     L)

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
