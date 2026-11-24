from _authoring import Bank

B = Bank("Pathology")
L1 = "Pathology L1 slides (hemodynamic disorders I)"
L2 = "Pathology L2 slides (hemodynamic disorders II)"
L3 = "Pathology L3 slides (rheumatic fever)"
L4 = "Pathology L4 slides (atherosclerosis)"

# ---------------------------------------------------------------- hyperemia and congestion
B.concept("path-congestion", "Hyperemia and congestion", [
    "Hyperemia: an active process in which arteriolar dilation increases blood flow; tissue turns red (erythema) from oxygenated blood.",
    "Congestion: a passive process from impaired venous outflow; tissue is dusky reddish-blue (cyanosis) from deoxygenated blood.",
    "Acute localized congestion: sudden complete venous obstruction (DVT, ligature, twisted pedicle of an ovary) causing rapid edema and hemorrhage.",
    "Chronic generalized venous congestion is caused by chronic right-sided heart failure; acute generalized congestion by acute heart failure.",
], L1)

B.mc("A client with a deep vein thrombosis of the left leg has a swollen limb that is dusky reddish-blue. How should the nurse interpret this color change?",
     "Congestion from impaired venous outflow with deoxygenated blood",
     [("Hyperemia from active arteriolar dilation", "Hyperemia makes tissue red (erythema) from oxygenated blood, not reddish-blue.", "mixes up hyperemia and congestion"),
      ("Ischemia from deficient arterial supply", "Ischemia is deficient ARTERIAL supply; DVT obstructs venous outflow.", "mixes up arterial and venous obstruction"),
      ("Infarction from arterial occlusion", "Infarction is ischemic necrosis; the color described is the stasis of congestion.")],
     "Congestion is a passive process caused by impaired venous outflow, such as a DVT. Red cells stagnate and deoxygenated venous blood accumulates, so the tissue turns dusky reddish-blue (cyanosis). Hyperemia is the opposite: an active arteriolar dilation that fills tissue with oxygenated blood and makes it red. Sudden complete venous obstruction also causes rapid edema and hemorrhage.",
     L1)

B.sata("A nurse is teaching about increased local blood volume. Which situations are examples of hyperemia?",
       ["Acute inflammation", "Skeletal muscle during exercise", "The gut following a meal", "Blushing of the face"],
       [("Deep vein thrombosis of the leg", "DVT causes acute localized congestion.", "mixes up hyperemia and congestion"),
        ("Twisting of an ovarian pedicle", "A twisted pedicle obstructs venous outflow: acute localized congestion.", "mixes up hyperemia and congestion"),
        ("Pulmonary veins in left ventricular failure", "This is chronic localized (pulmonary) congestion.")],
       "Hyperemia is active: arterioles dilate and more blood flows in, as in acute inflammation, exercising skeletal muscle, the gut after a meal and blushing. Congestion is passive: venous outflow is impaired, as with DVT, a twisted ovarian pedicle or left ventricular failure backing up into the pulmonary veins.",
       L1)

B.mc("A client with chronic left ventricular failure has sputum containing macrophages filled with hemosiderin. What are these cells called?",
     "Heart failure cells",
     [("Anitschkow cells", "Anitschkow (caterpillar) cells are cardiac histiocytes inside Aschoff bodies of rheumatic fever.", "mixes up heart failure cells and Anitschkow cells"),
      ("Foam cells", "Foam cells are lipid-filled macrophages and smooth muscle cells in atherosclerotic lesions.", "mixes up heart failure cells and foam cells"),
      ("Aschoff bodies", "Aschoff bodies are the pathognomonic lesions of acute rheumatic fever.")],
     "In chronic pulmonary congestion, from chronic left ventricular failure or mitral stenosis, the alveolar capillaries are engorged. Fluid leaks into the alveoli (pulmonary edema) and capillaries rupture so red cells enter the alveoli. Alveolar macrophages phagocytose and degrade the red cells, becoming hemosiderin-laden heart failure cells. Long-standing congestion adds interstitial fibrosis: brown induration of the lung.",
     L1)

B.order("A client has long-standing mitral stenosis. Arrange the changes of chronic pulmonary congestion in the order they develop.",
        ["Congestion of the alveolar capillaries", "Transudation of fluid and passage of red cells into the alveoli",
         "Phagocytosis and degradation of the red cells by macrophages", "Hemosiderin-laden macrophages (heart failure cells) appear",
         "Fibrosis of the interstitium and alveolar septa (brown induration)"],
        "Chronic left ventricular failure or mitral stenosis backs blood up into the alveolar capillaries. Fluid transudes into the alveoli and ruptured capillaries let red cells through; macrophages engulf and degrade the red cells and become hemosiderin-laden heart failure cells. With long-standing congestion, the interstitium and alveolar septa become fibrotic, giving brown induration of the lung.",
        L1)

B.mc("A client with chronic right-sided heart failure has dyspnea, generalized edema and congestion of several organs. Which type of congestion is this?",
     "Chronic generalized venous congestion",
     [("Acute generalized congestion", "Acute generalized congestion follows ACUTE heart failure.", "mixes up acute and chronic generalized congestion"),
      ("Chronic localized congestion", "Localized congestion affects one region, from compression of a vein or left failure in the lung."),
      ("Acute localized congestion", "Acute localized congestion follows a sudden complete venous obstruction such as a DVT.")],
     "Chronic generalized venous congestion is gradual congestion of the whole venous system, caused by chronic right-sided heart failure. Its effects are dyspnea (from pulmonary congestion), chronic venous congestion in different organs and generalized cardiac edema. Acute heart failure instead gives rapid congestion in all viscera.",
     L1)

# ---------------------------------------------------------------- edema
B.concept("path-edema", "Edema: causes and classification", [
    "Edema: an abnormal increase in interstitial fluid within tissues; fluid may be transudate, exudate or lymph.",
    "Causes: increased capillary hydrostatic pressure, decreased plasma colloid osmotic pressure, increased capillary permeability, lymphatic obstruction.",
    "Hypoproteinemia: total plasma proteins below 2.5 gm% or serum albumin below 1.5 gm%.",
    "Pitting edema: generalized edema and obstructive venous edema. Non-pitting: inflammatory and lymphatic edema.",
], L1)

B.match("A nurse cares for several clients with edema. Match each cause to the mechanism that produces the edema.",
        [("Hypoproteinemia", "Decreased plasma colloid osmotic pressure"),
         ("Histamine release in acute inflammation", "Increased capillary permeability"),
         ("Venous congestion", "Increased capillary hydrostatic pressure"),
         ("Filariasis", "Lymphatic obstruction")],
        [("Increased plasma colloid osmotic pressure", "A rise in colloid osmotic pressure would hold fluid in vessels; edema follows a DECREASE.", "reverses the oncotic effect")],
        "Edema has four mechanisms. Venous congestion or sodium and water retention raise capillary hydrostatic pressure; hypoproteinemia lowers plasma colloid osmotic pressure; toxins, hypoxia and chemicals such as histamine increase capillary permeability; and lymphangitis, filariasis, tumors, irradiation fibrosis or lymph node removal obstruct lymphatics.",
        L1,
        row_stems={
            "Hypoproteinemia": "A malnourished client with hypoproteinemia develops edema. Which mechanism should the nurse identify?",
            "Histamine release in acute inflammation": "A client's inflamed ankle swells as histamine is released. Which mechanism causes this edema?",
            "Venous congestion": "A client with venous congestion develops leg edema. Which mechanism causes it?",
            "Filariasis": "A client with filariasis develops massive leg swelling. Which mechanism causes the edema?",
        })

B.fill("A malnourished client's labs are reviewed for nutritional edema. Edema from hypoproteinemia occurs when serum albumin falls below ____.",
       "1.5 gm%",
       [("2.5 gm%", "2.5 gm% is the threshold for TOTAL plasma proteins, not albumin.", "mixes up albumin and total protein thresholds"),
        ("3.5 gm%", "3.5 gm% is not the threshold given; the albumin threshold is 1.5 gm%.")],
       "Decreased plasma colloid osmotic pressure causes edema when the plasma proteins that hold fluid in the vessels fall too low. Hypoproteinemia is defined as total plasma proteins below 2.5 gm% or serum albumin below 1.5 gm%; the resulting generalized edema is called nutritional edema.",
       L1)

B.sata("A nurse assesses several clients for pitting. Which clients would the nurse expect to have non-pitting edema?",
       ["A client with a cellulitis-related inflammatory edema", "A client with lymphatic edema after lymph node removal"],
       [("A client with cardiac edema from heart failure", "Cardiac edema is generalized, and generalized edema is pitting.", "thinks generalized edema is non-pitting"),
        ("A client with nutritional edema from hypoproteinemia", "Nutritional edema is generalized and pitting."),
        ("A client with obstructive venous edema", "Obstructive venous edema is pitting.", "thinks venous edema is non-pitting")],
       "Edema is classified by consistency. Pitting edema is seen in generalized edema (cardiac, renal and nutritional) and in obstructive venous edema. Non-pitting edema is seen in inflammatory edema and lymphatic edema.",
       L1)

B.tf("A nurse states that lymphatic edema, such as that caused by filariasis, is typically pitting.", False,
     "False. Lymphatic edema (and inflammatory edema) is NON-pitting. Pitting edema is seen in generalized edema and obstructive venous edema.",
     L1, "Lymphatic edema is non-pitting.", "thinks lymphatic edema pits")

# ---------------------------------------------------------------- ischemia and infarction
B.concept("path-ischemia-infarct", "Ischemia and infarction", [
    "Ischemia: deficient arterial blood supply due to partial or complete occlusion of the artery; acute (sudden complete) or chronic (gradual partial).",
    "Organs with good collateral circulation show no effect; poor collateral circulation leads to infarction (acute) or chronic ischemic changes.",
    "Infarct: an area of ischemic necrosis from occlusion of the arterial supply or venous drainage; 99% from thrombosis or embolism.",
    "Red infarct: venous occlusion (ovary), loose tissue (lung), dual circulation (lung, liver, small intestine), reperfusion after angioplasty.",
    "White infarct: arterial occlusion in solid organs with end-arterial circulation (heart, spleen, kidney); tissue density limits seepage of blood.",
], L1)

B.tf("A nurse explains that sudden occlusion of an artery in an organ with good collateral circulation may produce no effect.", True,
     "True. In acute ischemia, organs with good collateral circulation show no effect, while organs with poor collateral circulation undergo infarction.",
     L1, "This statement is true: good collaterals can prevent damage.")

B.mc("A client develops a pulmonary infarct after a pulmonary embolism. Which appearance should the nurse expect the infarct to have?",
     "A red (hemorrhagic) infarct",
     [("A white (anemic) infarct", "White infarcts occur in solid organs with end-arterial circulation such as heart, spleen and kidney.", "thinks lung infarcts are white"),
      ("A septic infarct", "A septic infarct is classified by infection, not color; nothing here suggests infection."),
      ("No infarct, because arterial occlusion never causes infarction in the lung", "Pulmonary infarction does occur, e.g. medium emboli in a congested lung.")],
     "Infarcts are red when blood can seep into the necrotic area: with venous occlusion, in loose tissues like the lung, in tissues with a dual circulation (lung, liver, small intestine) and after reperfusion. White infarcts occur where arterial occlusion hits a dense solid organ with end-arterial circulation, which limits seepage of blood.",
     L1)

B.sata("A nurse reviews infarct types. Which situations typically produce a red (hemorrhagic) infarct?",
       ["Venous occlusion of the ovary", "Infarction of the lung", "Infarction of the small intestine", "Reperfusion after angioplasty of an occluded artery"],
       [("Arterial occlusion in the kidney", "The kidney is a solid organ with end-arterial circulation: white infarct.", "thinks solid-organ infarcts are red"),
        ("Arterial occlusion in the spleen", "The spleen gives a white (anemic) infarct.", "thinks solid-organ infarcts are red"),
        ("Coronary arterial occlusion in the heart", "The heart gives a white (anemic) infarct.")],
       "Red infarcts form where blood can enter the dead tissue: venous occlusion (ovary, testis), loose tissue (lung), dual blood supply (lung, liver, small intestine) and restored flow to a previously occluded site after angioplasty. Heart, spleen and kidney are dense end-arterial organs that give white infarcts.",
       L1)

B.mc("A client has an infarct of the testis. Which cause should the nurse recognize as most likely for an infarct in this organ?",
     "Venous thrombosis, because the testis has a single venous outflow",
     [("Arterial occlusion in an organ with a dual blood supply", "Dual circulation describes the lung, liver and small intestine, not the testis."),
      ("Chronic ischemia from gradual atherosclerosis with good collaterals", "Good collaterals prevent damage; this would not produce an infarct."),
      ("Septic embolism from a lung abscess", "Nothing suggests infection; infection defines a septic infarct, not the usual testicular infarct.")],
     "Almost all infarcts (99%) come from thrombosis or embolism, usually arterial. Venous thrombosis causes infarcts mainly in organs with a single venous outflow, such as the testis and ovary, because there is no alternative drainage route once that vein is blocked.",
     L1)

B.tf("A nurse states that white (anemic) infarcts typically occur in the lung because of its dual circulation.", False,
     "False. The lung, with its loose tissue and dual circulation, gives RED (hemorrhagic) infarcts. White infarcts occur with arterial occlusion in solid organs with end-arterial circulation: heart, spleen and kidney.",
     L1, "The lung gives red infarcts; white infarcts are heart, spleen and kidney.", "thinks lung infarcts are white")

# ---------------------------------------------------------------- thrombosis
B.concept("path-virchow", "Thrombosis and Virchow's triad", [
    "Thrombosis: formation of a compact mass of circulating blood elements inside the cardiovascular system during life.",
    "Virchow's triad: endothelial injury/dysfunction, alterations in blood flow (stasis or turbulence), hypercoagulability.",
    "Endothelial dysfunction increases procoagulants (thromboplastin, vWF, PAI) and decreases anticoagulants (thrombomodulin, antithrombin III, NO, PA).",
    "Stasis reduces inflow of fresh blood containing natural anticoagulants and retards removal of small platelet aggregates.",
    "Acquired hypercoagulability: prolonged bed rest, surgery, burns, pregnancy, oral contraceptives, disseminated cancer, smoking, DIC. Hereditary: factor V and prothrombin gene mutations, antithrombin III deficiency.",
], L2)

B.sata("A nurse is assessing a postoperative client for thrombosis risk. Which factors make up Virchow's triad?",
       ["Endothelial injury or dysfunction", "Stasis or turbulence of blood flow", "Hypercoagulability of blood"],
       [("Increased capillary permeability", "Increased capillary permeability is a mechanism of edema.", "mixes up edema and thrombosis mechanisms"),
        ("Lymphatic obstruction", "Lymphatic obstruction is a mechanism of edema.", "mixes up edema and thrombosis mechanisms"),
        ("Active arteriolar dilation", "Arteriolar dilation is hyperemia.")],
       "Thrombosis is inappropriate activation of normal hemostasis, which is regulated by the vessel wall, platelets and coagulation factors. Virchow's triad names the three primary causes: endothelial injury or dysfunction, alterations in normal blood flow (stasis or turbulence) and hypercoagulability of the blood.",
       L2)

B.sata("A nurse reviews a client's history for ACQUIRED causes of hypercoagulability. Which findings apply?",
       ["Prolonged bed rest", "Oral contraceptive use", "Disseminated cancer", "Recent surgery", "Smoking"],
       [("Factor V gene mutation", "A factor V gene mutation is a HEREDITARY cause.", "mixes up hereditary and acquired hypercoagulability"),
        ("Antithrombin III deficiency since birth", "Inherited antithrombin III deficiency is a HEREDITARY cause.", "mixes up hereditary and acquired hypercoagulability")],
       "Hypercoagulability means more coagulation proteins or fewer natural anticoagulants. Hereditary causes include mutations of the factor V and prothrombin genes and antithrombin III deficiency. Acquired causes include prolonged bed rest or immobilization, tissue damage (surgery, burns), hyperestrogenic states (pregnancy, oral contraceptives), disseminated cancer, smoking and DIC.",
       L2)

B.mc("A client with long-standing hypertension has endothelial dysfunction. Which change in the endothelium favors thrombosis?",
     "Decreased production of thrombomodulin and nitric oxide",
     [("Increased production of antithrombin III", "Antithrombin III is an anticoagulant; dysfunction DECREASES it.", "reverses the endothelial effect"),
      ("Decreased production of von Willebrand factor", "vWF is a procoagulant; dysfunction INCREASES it.", "reverses the endothelial effect"),
      ("Increased production of plasminogen activator", "Plasminogen activator (PA) is anticoagulant; dysfunction DECREASES it.", "reverses the endothelial effect")],
     "Hemodynamic stress such as hypertension, trauma, inflammation, atherosclerosis or hyperlipidemia makes the endothelium dysfunctional. A dysfunctional endothelium produces more procoagulants (thromboplastin, vWF, PAI) and fewer anticoagulants (thrombomodulin, antithrombin III, NO, PA). If the endothelium is lost, exposed matrix lets vWF bind platelets and activates the coagulation cascade.",
     L2)

B.mc("A client with varicose veins asks why sluggish blood flow causes clots. Which explanation by the nurse is accurate?",
     "Slow flow reduces the inflow of fresh blood carrying natural anticoagulants and delays removal of platelet clumps.",
     [("Slow flow mechanically tears the endothelium.", "Mechanical injury to endothelium is the effect of TURBULENCE, not stasis.", "mixes up stasis and turbulence effects"),
      ("Slow flow increases plasma colloid osmotic pressure.", "Colloid osmotic pressure relates to edema, not to how stasis causes thrombosis."),
      ("Slow flow lowers the concentration of coagulation proteins.", "Lower coagulation proteins would reduce, not increase, clotting.")],
     "Stasis, mainly in veins with obstruction such as varicose veins, reduces the inflow of fresh blood that carries natural anticoagulants and retards the removal of small platelet aggregates. Turbulence (aneurysms, mitral stenosis, atrial fibrillation) instead injures endothelial cells. Both stasis and turbulence activate procoagulant secretion and bring platelets and leukocytes into contact with the endothelium.",
     L2)

B.concept("path-thrombus-types", "Sites, types and fate of thrombi", [
    "Venous thrombi (phlebothrombosis, red thrombi) are the most common type, associated with stasis and hypercoagulability.",
    "DVT sites: popliteal, femoral and iliac veins; complication: embolism to the lungs (pulmonary infarction).",
    "Arterial thrombosis is less common because of rapid flow and the thick elastic arterial wall; most common cause is atherosclerosis (coronary, cerebral, femoral).",
    "Cardiac thrombi: auricular thrombus in the left atrium in mitral stenosis; mural thrombus in the left ventricle over an infarct; vegetations on valves.",
    "Fate: dissolution, propagation (a tail liable to detach), embolization, organization and recanalization.",
], L2)

B.tf("A nurse states that arterial thrombosis is more common than venous thrombosis because arterial blood flows rapidly.", False,
     "False. Venous thrombi are the MOST common type. Arterial thrombosis is LESS common precisely because of the rapid blood flow and the thick elastic arterial wall that resists injury.",
     L2 + ", slide exercise", "Venous thrombi are most common; rapid arterial flow protects arteries.", "thinks arterial thrombi are most common", last=True)

B.mc("A client is recovering from hip surgery and has a deep vein thrombosis in the femoral vein. Which complication should the nurse monitor for most closely?",
     "Embolization to the lungs causing pulmonary infarction",
     [("Embolization to the brain causing a stroke", "Systemic emboli to the brain come from the left heart or arteries; venous emboli reach the lungs unless there is a septal defect.", "sends venous emboli to the systemic circulation"),
      ("Fat embolism syndrome", "Fat embolism follows long bone fracture, not venous thrombosis."),
      ("Cholesterol emboli to the kidney", "Cholesterol emboli come from ruptured atheromatous plaques.")],
     "Deep vein thrombi form in the popliteal, femoral and iliac veins, mainly through stasis and hypercoagulability after surgery or immobility. Their important complication is embolization to the lungs: about 95% of pulmonary emboli come from DVT, causing pulmonary infarction, hemorrhage or sudden death depending on size.",
     L2)

B.match("A nurse reviews clients with cardiac thrombi. Match each type of cardiac thrombus to its usual setting.",
        [("Auricular thrombus", "Left atrial appendage in mitral stenosis"),
         ("Mural thrombus", "Left ventricular wall over a myocardial infarct"),
         ("Vegetations", "Heart valves in rheumatic fever, SLE or bacterial endocarditis")],
        [("Popliteal vein after surgery", "The popliteal vein is a site of deep vein thrombosis, not a cardiac thrombus.", "confuses venous and cardiac thrombi")],
        "Cardiac thrombi form in chambers and on valves. In mitral stenosis, stasis in the dilated left atrium produces an auricular thrombus over the appendage. Over a myocardial infarct, the damaged left ventricular endocardium carries a mural thrombus. On valves, thrombi appear as vegetations in rheumatic fever, systemic lupus erythematosus and bacterial endocarditis.",
        L2,
        row_stems={
            "Auricular thrombus": "A client with mitral stenosis has an auricular thrombus. Where should the nurse expect it to form?",
            "Mural thrombus": "A client recovering from a myocardial infarction develops a mural thrombus. Where does it form?",
            "Vegetations": "A client's echocardiogram shows vegetations. Where are these thrombi located?",
        })

B.mc("A client's old thrombus is examined and shows ingrowth of endothelial cells, smooth muscle cells and fibroblasts with new capillary channels. Which fate of a thrombus is this?",
     "Organization and recanalization",
     [("Dissolution", "Dissolution is rapid shrinkage and disappearance of a RECENT thrombus by fibrinolysis.", "mixes up dissolution and organization"),
      ("Propagation", "Propagation is growth of the thrombus by adding platelets and fibrin, forming a tail."),
      ("Embolization", "Embolization is detachment of the thrombus from the vessel wall.")],
     "Thrombi have four fates. Recent thrombi can dissolve by fibrinolysis. They can propagate, adding platelets and fibrin and forming a tail that is liable to detach. They can embolize. Older thrombi become organized by ingrowth of endothelial cells, smooth muscle cells and fibroblasts, and capillary channels form that re-establish the lumen (recanalization).",
     L2)

B.mc("A nurse explains why a growing thrombus with a long tail is dangerous. What happens during propagation?",
     "The thrombus adds platelets and fibrin, forming a tail that is more liable to detach and embolize.",
     [("Fibrinolysis shrinks the thrombus until it disappears.", "That is dissolution.", "mixes up propagation and dissolution"),
      ("Fibroblasts grow in and form new channels through it.", "That is organization and recanalization."),
      ("The thrombus becomes infected and produces pyemia.", "Septic thrombi produce pyemia when they embolize; that is not propagation.")],
     "Propagation means the thrombus keeps accumulating platelets and fibrin. The tail that forms is more liable to detach, so propagation sets up embolization. Infected venous thrombi (thrombophlebitis) are the source of septic emboli that produce pyemia.",
     L2)

# ---------------------------------------------------------------- embolism
B.concept("path-embolism", "Embolism and pulmonary embolism", [
    "An embolus is a detached intravascular solid, liquid or gaseous mass carried by the blood to a site distant from its origin.",
    "Thromboemboli are the most common type (99%); others: fat, parasitic, air or nitrogen, amniotic fluid, tumor, cholesterol and foreign body emboli.",
    "Pulmonary emboli: 95% originate from deep vein thrombi of the legs; seen in up to 25-30% of DVT patients; 60-80% are small and silent.",
    "Saddle embolus causes sudden death (acute right failure); medium emboli give hemorrhage in a normal lung or infarction in a congested lung; small repeated emboli give pulmonary hypertension and cor pulmonale.",
], L2)

B.mc("A client on bed rest after surgery suddenly develops dyspnea, and pulmonary embolism is suspected. Which is the most likely source of the embolus?",
     "A thrombus in the deep veins of the legs",
     [("A mural thrombus in the left ventricle", "Left heart thrombi enter the systemic circulation, giving systemic emboli.", "sends left-heart emboli to the lungs"),
      ("An ulcerated atheromatous plaque in the aorta", "Aortic plaques give systemic or cholesterol emboli, not pulmonary emboli."),
      ("Vegetations on the mitral valve", "Mitral vegetations embolize into the systemic arterial circulation.")],
     "A pulmonary embolus starts in a systemic vein and lodges in the pulmonary arteries. In 95% of cases it originates from deep vein thrombi of the legs, and it is seen in up to 25-30% of patients with DVT. Emboli from the left heart or arteries travel instead to systemic organs.",
     L2 + ", slide note (why venous thrombi are most common)", last=True)

B.tf("A nurse teaching about deep vein thrombosis states that about 95% of pulmonary emboli originate from thrombi in the deep veins of the legs.", True,
     "True. In 95% of cases pulmonary emboli originate from deep vein thrombi of the legs, and pulmonary embolism is observed in up to 25-30% of patients with DVT.",
     L2, "This statement is true: 95% of pulmonary emboli come from leg DVT.")

B.match("A nurse reviews the outcomes of pulmonary embolism by embolus size. Match each embolus to its usual outcome.",
        [("Large saddle embolus at the pulmonary bifurcation", "Sudden death from acute right-sided failure"),
         ("Medium embolus in a normal lung", "Pulmonary hemorrhage only"),
         ("Medium embolus in a congested lung", "Pulmonary infarction"),
         ("Small repeated emboli over time", "Pulmonary hypertension and cor pulmonale")],
        [("Clinically silent with no effect ever", "60-80% of emboli are small and silent, but none of these listed emboli is silent.")],
        "The effect of a pulmonary embolus depends on its size and on the lung. 60-80% are small and clinically silent. A large saddle embolus at the bifurcation or in a main pulmonary artery causes sudden death from acute right-sided failure. A medium embolus causes only hemorrhage in a normal lung, but infarction in a congested lung. Small repeated emboli cause pulmonary hypertension and right-sided failure (cor pulmonale).",
        L2,
        row_stems={
            "Large saddle embolus at the pulmonary bifurcation": "A client collapses from a saddle embolus at the pulmonary bifurcation. Which outcome should the nurse anticipate?",
            "Medium embolus in a normal lung": "A client with healthy lungs has a medium-sized pulmonary embolus. Which outcome is expected?",
            "Medium embolus in a congested lung": "A client with heart failure and lung congestion has a medium pulmonary embolus. Which outcome is expected?",
            "Small repeated emboli over time": "A client has had small pulmonary emboli repeatedly for years. Which long-term outcome should the nurse anticipate?",
        })

B.concept("path-systemic-emboli", "Systemic, fat, air and amniotic fluid emboli", [
    "Systemic emboli: 80% from intracardiac thrombi (2/3 left ventricular wall infarcts, 1/3 dilated left atria or vegetations); also aortic aneurysm, ulcerated plaques, paradoxical emboli.",
    "Paradoxical emboli start as venous emboli but pass through an interatrial or interventricular defect into the systemic circulation.",
    "Site of arrest: 75% lower extremities, 10% brain.",
    "Fat embolism: long bone fracture is the most common cause; the syndrome begins 1-3 days after injury with tachypnea, dyspnea, tachycardia, neurologic symptoms, thrombocytopenia and anemia.",
    "Air embolism needs more than 100 cc of air for a pulmonary effect; causes include neck vein injury, chest wall injury, obstetric or laparoscopic procedures, bypass surgery and decompression sickness.",
    "Amniotic fluid embolism: 1 in 40,000 deliveries, mortality 80%; sudden dyspnea, cyanosis, shock, seizures, pulmonary edema and DIC.",
], L2)

B.mc("A client recovering from a large anterior myocardial infarction develops a cold, pulseless leg. Which source of the arterial embolus is most likely?",
     "An intracardiac thrombus over the infarcted left ventricular wall",
     [("A deep vein thrombus of the leg", "Leg vein thrombi travel to the lungs unless they pass through a septal defect.", "sends venous emboli to the systemic circulation"),
      ("A fat embolus from bone marrow", "Fat emboli follow long bone fractures."),
      ("An amniotic fluid embolus", "Amniotic fluid embolism occurs during delivery.")],
     "Systemic emboli travel in the arterial circulation. About 80% arise from intracardiac thrombi, two thirds of which are associated with left ventricular wall infarcts. Others come from aortic aneurysms, ulcerated atheromatous plaques or paradoxical emboli. About 75% lodge in the lower extremities and 10% in the brain.",
     L2)

B.mc("A client with an interatrial septal defect and a known leg DVT suddenly develops stroke symptoms. Which type of embolism best explains this?",
     "Paradoxical embolism",
     [("Pulmonary thromboembolism", "A pulmonary embolus lodges in the lung, not the brain.", "sends a crossed embolus to the lungs"),
      ("Fat embolism", "Fat embolism follows long bone fracture or soft tissue trauma."),
      ("Atheroembolism", "Atheroembolism discharges debris from a ruptured arterial plaque.")],
     "A paradoxical embolus begins as a venous embolus, but instead of reaching the lungs it crosses an interatrial or interventricular defect into the systemic circulation. A leg vein thrombus can therefore reach the brain in a client with a septal defect.",
     L2)

B.mc("Two days after a femoral shaft fracture, a client becomes tachypneic, dyspneic, tachycardic and confused, and labs show thrombocytopenia and anemia. Which condition should the nurse suspect?",
     "Fat embolism syndrome",
     [("Air embolism", "Air embolism follows entry of more than 100 cc of air, as in neck vein or chest wall injury.", "mixes up fat and air emboli"),
      ("Amniotic fluid embolism", "Amniotic fluid embolism occurs during delivery."),
      ("Cholesterol embolism", "Cholesterol emboli come from atheromatous plaques.")],
     "Fat embolism occurs in about 90% of people with severe skeletal injuries, most commonly long bone fractures, but fewer than 10% develop clinical findings. The syndrome begins 1-3 days after injury with tachypnea, dyspnea and tachycardia, neurologic symptoms, and thrombocytopenia and anemia. Fat globules obstruct vessels mechanically and free fatty acids injure endothelium and activate platelets; it is fatal in 5-15%.",
     L2)

B.sata("A nurse reviews situations that carry a risk of air embolism. Which situations apply?",
       ["Injury to large neck veins", "Chest wall injury", "Laparoscopic procedures", "Air trapped in a coronary artery during bypass surgery", "Decompression sickness"],
       [("Fracture of a long bone", "Long bone fracture is the most common cause of FAT embolism.", "mixes up fat and air emboli"),
        ("Tear in the placental membranes", "This lets amniotic fluid enter the maternal circulation: amniotic fluid embolism."),
        ("Rupture of an atheromatous plaque", "Plaque rupture discharges cholesterol debris: atheroembolism.")],
       "Gas bubbles in the circulation coalesce into frothy masses that obstruct flow and cause distal ischemia. Causes include injury to large neck veins, chest wall injury, obstetric or laparoscopic procedures, air trapped in a coronary artery during bypass surgery, and decompression sickness (Caisson disease).",
       L2 + ", slide exercise (decompression sickness)", last=True)

B.tf("A nurse states that more than 100 cc of air is required to have a clinical effect in the pulmonary circulation.", True,
     "True. Air embolism needs more than 100 cc of air to produce a clinical effect in the pulmonary circulation.",
     L2, "This statement is true: more than 100 cc of air is needed.")

B.mc("During delivery, a client suddenly develops severe dyspnea, cyanosis, shock and a seizure, followed by bleeding from IV sites. Which condition should the nurse suspect?",
     "Amniotic fluid embolism",
     [("Fat embolism syndrome", "Fat embolism begins 1-3 days after a long bone fracture.", "mixes up amniotic and fat emboli"),
      ("Pulmonary thromboembolism from a DVT", "PE from DVT does not explain the seizure and DIC at delivery."),
      ("Air embolism from a neck vein injury", "There is no neck vein injury; air embolism needs over 100 cc of air.")],
     "Amniotic fluid or fetal tissue can enter the maternal circulation through a tear in the placental membranes or ruptured uterine veins. It causes sudden severe dyspnea, cyanosis and shock, neurologic impairment (headache, seizures, coma), pulmonary edema and DIC. It is rare (1 in 40,000 deliveries) but has 80% mortality, and 85% of survivors keep a neurologic deficit.",
     L2)

# ---------------------------------------------------------------- rheumatic fever
B.concept("path-arf", "Acute rheumatic fever: pathogenesis and lesions", [
    "ARF is an acute, immunologically mediated, multisystem inflammatory disease a few weeks after group A streptococcal pharyngitis.",
    "It appears 10 days to 6 weeks after pharyngitis, in about 3% of infected patients, most often in children aged 5-15.",
    "Antibodies and CD4+ T cells against streptococcal M proteins cross-react with self antigens in the heart.",
    "Aschoff bodies are pathognomonic: focal necrosis, T lymphocytes and Anitschkow (caterpillar) cells with a slender wavy ribbon of chromatin.",
    "Pancarditis: fibrinous \"bread and butter\" pericarditis, myocarditis, and small vegetations along the lines of closure over fibrinoid necrosis (mitral 65%, aortic 25%).",
], L3)

B.mc("A 14-year-old girl is brought to the physician because of a 1-week history of malaise and chest pain. Three weeks ago, she had a sore throat that resolved without treatment. Her temperature is 38.7°C (101.7°F). Examination shows several subcutaneous nodules on her elbows and wrist bilaterally and a new-onset early systolic murmur best heard at the apex in the left lateral position. An endomyocardial biopsy is most likely to show which of the following?",
     "Fibrinoid necrosis with histiocytic infiltrate",
     [("Coagulative necrosis with neutrophilic infiltrate", "This pattern is not the lesion of rheumatic carditis, which is the Aschoff body (focal necrosis, T lymphocytes and Anitschkow histiocytes).", "expects infarct-type necrosis in ARF"),
      ("Deposits of misfolded protein aggregates", "Misfolded protein deposits are not part of the rheumatic lesion described in ARF."),
      ("Myocardial infiltration with eosinophilic proteins", "Eosinophilic protein infiltration is not part of the rheumatic lesion described in ARF."),
      ("Fibrosis with myofibrillar disarray", "Fibrosis follows healing in chronic disease; myofibrillar disarray is not part of the ARF lesion.")],
     "A sore throat 3 weeks earlier, fever, subcutaneous nodules and a new apical murmur fit acute rheumatic fever. Its pathognomonic microscopic lesion is the Aschoff body, found in all layers of the heart: foci of necrosis with T lymphocytes and Anitschkow cells, which are activated macrophages (cardiac histiocytes). The valve vegetations overlie foci of fibrinoid necrosis. A biopsy therefore shows fibrinoid necrosis with a histiocytic infiltrate. (The slide's word \"endomysial\" is corrected here to endomyocardial.)",
     L3 + ", in-class case", last=True)

B.mc("A 9-year-old boy from Eritrea is admitted to the hospital for lethargy and increased work of breathing. He has had recurrent episodes of fever, shortness of breath, and fatigue over the past 3 years. His pulse is 132/min and blood pressure is 90/66 mm Hg. Pulse oximetry on room air shows an oxygen saturation of 82%. Auscultation of the chest shows coarse crackles in both lungs and a diastolic murmur at the cardiac apex. Despite appropriate lifesaving measures, he dies. A photomicrograph of a section of myocardium obtained at autopsy is shown. Which of the following is the most likely underlying cause of this patient's cardiac disease?",
     "Type II hypersensitivity reaction",
     [("Amastigote infiltration", "Amastigote infiltration means direct parasitic invasion of the myocardium, not the antibody cross-reaction of rheumatic heart disease."),
      ("Exotoxin-mediated myonecrosis", "Rheumatic carditis is not caused by a toxin; it is caused by antibodies and T cells cross-reacting with heart antigens.", "thinks strep toxin damages the heart directly"),
      ("Caseating granulomatous inflammation", "Caseating granulomas are not the lesion of rheumatic heart disease; the Aschoff body is.")],
     "Recurrent febrile episodes, pulmonary congestion and an apical diastolic murmur (mitral stenosis) in a child from an endemic area point to rheumatic heart disease, and the autopsy section shows Aschoff bodies. The disease is immunologically mediated: antibodies and CD4+ T cells raised against streptococcal M proteins cross-react with self antigens in the heart. Antibodies binding tissue antigens activate complement and recruit macrophages, which is a type II (antibody-mediated) hypersensitivity reaction; the slide states the antibody cross-reaction but not the term \"type II\".",
     L3 + ", in-class case", last=True)

B.mc("A group of epidemiologists is studying the rates of cardiac surgeries performed in several Southeast Asian countries compared to the United States. Results show a significant increase in the number of mitral valve replacements performed in Vietnam in adults aged 30–50 years compared to the same age group in the United States. Which of the following public health interventions is most likely to decrease this number?",
     "Prompt antibiotic treatment for bacterial pharyngitis",
     [("Improved access to drug rehabilitation centers", "Drug rehabilitation addresses IV drug use endocarditis, which mainly affects the tricuspid valve.", "links mitral disease to IV drug use"),
      ("Genetic screening program for FBN1 gene mutation", "FBN1 mutation screening is unrelated to rheumatic valve disease, the cause described here."),
      ("Childhood vaccination against Corynebacterium diphtheriae", "Diphtheria vaccination does not prevent group A streptococcal pharyngitis."),
      ("Screening echocardiography for prolapsed anterior mitral valve leaflets", "Screening finds valve disease; it does not prevent rheumatic scarring.")],
     "Mitral valve replacement in young adults in a developing country points to chronic rheumatic heart disease, which follows group A streptococcal pharyngitis by decades. The incidence and mortality of rheumatic fever fell over the past century because of better socioeconomic conditions and rapid diagnosis and treatment of strep pharyngitis. Prompt antibiotic treatment prevents the immune reaction and therefore the valve scarring.",
     L3 + ", in-class case", last=True)

B.mc("A nurse takes the history of a child with suspected acute rheumatic fever. Which history is most consistent with the diagnosis?",
     "An 8-year-old with a sore throat caused by group A streptococci 3 weeks ago",
     [("A 40-year-old with a sore throat 3 weeks ago", "ARF occurs most often in children aged 5-15.", "ignores the age pattern"),
      ("An 8-year-old with a sore throat 2 days ago", "ARF appears 10 days to 6 weeks after the pharyngitis, not within 2 days.", "ignores the latent period"),
      ("An 8-year-old with a group A streptococcal skin infection 6 months ago", "ARF follows streptococcal PHARYNGITIS by 10 days to 6 weeks.")],
     "Acute rheumatic fever appears 10 days to 6 weeks after group A beta-hemolytic streptococcal pharyngitis, develops in about 3% of infected patients and is most common in children aged 5-15. The delay reflects the time needed for antibodies and T cells against streptococcal M proteins to form and cross-react with heart antigens.",
     L3)

B.mc("A pathology report on a child's heart describes macrophages with abundant cytoplasm and a central nucleus whose chromatin forms a slender wavy ribbon. What are these cells?",
     "Anitschkow cells",
     [("Heart failure cells", "Heart failure cells are hemosiderin-laden alveolar macrophages in chronic pulmonary congestion.", "mixes up heart failure cells and Anitschkow cells"),
      ("Foam cells", "Foam cells are lipid-filled cells in atherosclerotic lesions.", "mixes up foam cells and Anitschkow cells"),
      ("T lymphocytes", "T lymphocytes are also in the Aschoff body, but they lack the caterpillar chromatin pattern.")],
     "Anitschkow cells (caterpillar cells) are cardiac histiocytes: macrophages with abundant cytoplasm and central round to oval nuclei whose chromatin condenses into a slender wavy ribbon. Together with focal necrosis and T lymphocytes they form the Aschoff body, the pathognomonic lesion of acute rheumatic fever found in all layers of the heart.",
     L3)

B.mc("A nurse auscultates a pericardial friction rub in a child with acute rheumatic fever. Which pericardial lesion is expected?",
     "Fibrinous \"bread and butter\" pericarditis",
     [("Vegetations along the lines of valve closure", "Vegetations are the lesion of rheumatic ENDOcarditis, on the valves.", "puts valve lesions in the pericardium"),
      ("Brown induration", "Brown induration is fibrosis of the lung in chronic congestion."),
      ("A mural thrombus", "A mural thrombus forms in the left ventricle over an infarct.")],
     "Acute rheumatic fever causes a pancarditis with Aschoff bodies in all layers. In the pericardium it causes fibrinous inflammation, the \"bread and butter\" pericarditis that produces a friction rub. The myocardium shows myocarditis and the valves show small vegetations along the lines of closure.",
     L3)

B.mc("A child's echocardiogram during acute rheumatic fever shows small vegetations along the lines of valve closure. Which valve is most commonly affected?",
     "Mitral valve",
     [("Aortic valve", "The aortic valve is second (25%).", "ranks aortic first"),
      ("Tricuspid valve", "The tricuspid valve is typical of IV drug use endocarditis, not rheumatic fever.", "confuses RHD with IVDU endocarditis"),
      ("Pulmonary valve", "The pulmonary valve is not among the most common sites.")],
     "Rheumatic vegetations are small, lie along the lines of closure and overlie foci of fibrinoid necrosis. They favor the high-pressure valves: mitral (65%) and aortic (25%). Chronic rheumatic heart disease follows the same pattern, with the mitral valve most affected.",
     L3)

B.concept("path-jones", "Jones criteria", [
    "Major: carditis, migratory polyarthritis, Sydenham chorea, erythema marginatum, subcutaneous nodules.",
    "Minor: fever, arthralgia, previous rheumatic fever, raised ESR, CRP or leukocytosis, prolonged PR interval.",
    "Evidence of preceding group A strep: positive throat culture or rapid antigen test, or raised or rising streptococcal antibody titer.",
    "Diagnosis: 2 major, or 1 major and 2 minor, supported by evidence of preceding group A streptococcal infection.",
    "Migratory polyarthritis of large joints is self-limited with no chronic deformities.",
], L3)

B.sata("A nurse reviews a child's findings using the Jones criteria. Which findings are MAJOR criteria?",
       ["Carditis", "Migratory polyarthritis", "Sydenham chorea", "Erythema marginatum", "Subcutaneous nodules"],
       [("Fever", "Fever is a minor criterion.", "mixes up major and minor Jones criteria"),
        ("Arthralgia", "Arthralgia (joint pain without arthritis) is a minor criterion.", "mixes up arthritis and arthralgia"),
        ("Prolonged PR interval", "A prolonged PR interval is a minor criterion.", "mixes up major and minor Jones criteria")],
       "The Jones major criteria are carditis, migratory polyarthritis, Sydenham chorea, erythema marginatum and subcutaneous nodules. The minor criteria are fever, arthralgia, previous rheumatic fever, laboratory evidence of inflammation (ESR, CRP, leukocytosis) and ECG changes (prolonged PR interval).",
       L3)

B.mc("A child has Sydenham chorea, fever and a raised ESR, and the streptococcal antibody titer is elevated. How should the nurse interpret these findings using the Jones criteria?",
     "The criteria are met: 1 major and 2 minor criteria with evidence of preceding strep infection.",
     [("The criteria are not met because 2 major criteria are always required.", "Diagnosis needs 2 major OR 1 major plus 2 minor criteria.", "forgets the 1 major + 2 minor rule"),
      ("The criteria are not met because chorea is a minor criterion.", "Sydenham chorea is a MAJOR criterion.", "mixes up major and minor Jones criteria"),
      ("The criteria are met even without evidence of streptococcal infection.", "The criteria must be supported by evidence of preceding group A strep infection; here the titer supplies it.")],
     "Acute rheumatic fever is diagnosed with 2 major criteria, or 1 major and 2 minor criteria, supported by evidence of a preceding group A streptococcal infection (positive throat culture or rapid antigen test, or a raised or rising antibody titer). Chorea is major; fever and a raised ESR are minor; the elevated titer is the supporting evidence.",
     L3)

B.tf("A nurse tells a family that the migratory polyarthritis of acute rheumatic fever typically leaves chronic joint deformities.", False,
     "False. Migratory (\"fleeting\") polyarthritis of the large joints is self-limited and leaves NO chronic deformities. The lasting damage of rheumatic fever is to the heart valves.",
     L3, "The arthritis is self-limited with no chronic deformities.", "thinks rheumatic arthritis deforms joints")

B.concept("path-rhd", "Chronic rheumatic heart disease and mitral stenosis", [
    "Endocarditis of ARF heals by fibrosis; repeated pharyngeal infections reactivate the disease and scar the valves.",
    "Mitral valve most commonly affected, then aortic; fibrosis of the leaflets leads to stenosis (\"fish mouth\" or \"buttonhole\").",
    "Usually becomes clinically manifest decades after ARF.",
    "Mitral stenosis: left atrial dilatation (with thrombi), chronic pulmonary venous congestion, lung fibrosis, pulmonary hypertension, chronic right-sided failure; the left ventricle is largely unaffected.",
    "Other complications: arrhythmias (especially atrial fibrillation), thromboembolism, infective endocarditis.",
], L3)

B.sata("A client has long-standing rheumatic mitral stenosis. Which consequences should the nurse anticipate?",
       ["Left atrial dilatation with possible thrombi", "Chronic venous congestion of the lungs", "Pulmonary hypertension", "Chronic right-sided heart failure", "Atrial fibrillation"],
       [("Marked left ventricular dilatation", "The left ventricle is largely unaffected by isolated pure mitral stenosis.", "thinks mitral stenosis enlarges the LV")],
       "A fibrotic \"fish mouth\" mitral valve obstructs flow from the left atrium, which dilates and may harbor thrombi that embolize. Back pressure causes chronic pulmonary venous congestion, lung fibrosis, pulmonary hypertension and eventually chronic right-sided failure. Atrial fibrillation, thromboembolism and infective endocarditis complicate it. The left ventricle, upstream of nothing that is blocked, is largely unaffected.",
       L3)

B.tf("A nurse explains that chronic rheumatic heart disease usually becomes clinically manifest decades after the episode of acute rheumatic fever.", True,
     "True. ARF endocarditis heals by fibrosis, repeated infections reactivate it, and the chronic valve scarring usually becomes clinically manifest after decades.",
     L3, "This statement is true: RHD usually appears decades later.")

# ---------------------------------------------------------------- atherosclerosis
B.concept("path-arteriosclerosis", "Arteriosclerosis patterns", [
    "Arteriosclerosis: thickening and loss of elasticity of arterial walls (\"hardening of the arteries\").",
    "Atherosclerosis: the most frequent and important pattern.",
    "Mönckeberg medial sclerosis: calcific deposits in muscular arteries in people older than 50.",
    "Arteriolosclerosis: small arteries and arterioles, with hypertension and diabetes; hyaline (amorphous proteinaceous wall) and hyperplastic (\"onion-skinning\").",
], L4)

B.match("A nurse reviews vessel biopsy reports. Match each pattern of arteriosclerosis to its description.",
        [("Atherosclerosis", "Intimal atheromas that protrude into the lumen"),
         ("Mönckeberg medial sclerosis", "Calcific deposits in muscular arteries after age 50"),
         ("Hyaline arteriolosclerosis", "Arteriolar wall thickened by amorphous proteinaceous material"),
         ("Hyperplastic arteriolosclerosis", "\"Onion-skinning\" of the arteriolar wall")],
        [("Fatty spots of foam cells under 1 mm", "Fatty spots are the earliest lesion OF atherosclerosis, not a separate pattern.")],
        "Arteriosclerosis means thickening and loss of elasticity of arterial walls, in three patterns. Atherosclerosis, the most frequent and important, forms intimal atheromas. Mönckeberg medial sclerosis lays down calcific deposits in muscular arteries of people over 50. Arteriolosclerosis affects small arteries and arterioles in hypertension and diabetes: the hyaline type deposits amorphous protein in the wall, and the hyperplastic type shows onion-skinning that narrows the lumen.",
        L4,
        row_stems={
            "Atherosclerosis": "A biopsy shows intimal atheromas protruding into an artery's lumen. Which pattern of arteriosclerosis is this?",
            "Mönckeberg medial sclerosis": "A 70-year-old client's report describes calcific deposits in the media of muscular arteries. Which pattern is this?",
            "Hyaline arteriolosclerosis": "A diabetic client's renal biopsy shows arterioles thickened by amorphous proteinaceous material. Which pattern is this?",
            "Hyperplastic arteriolosclerosis": "A biopsy from a client with severe hypertension shows onion-skinning of arterioles. Which pattern is this?",
        })

B.tf("A nurse explains that Mönckeberg medial sclerosis mainly affects arterioles in clients with hypertension.", False,
     "False. Mönckeberg medial sclerosis is calcific deposits in MUSCULAR ARTERIES in people older than 50. The pattern that affects small arteries and arterioles in hypertension and diabetes is arteriolosclerosis.",
     L4, "Mönckeberg affects muscular arteries; arteriolosclerosis affects arterioles.", "mixes up Mönckeberg and arteriolosclerosis")

B.concept("path-athero", "Atherosclerosis: risk factors, pathogenesis and plaque", [
    "Atherosclerosis: a chronic inflammatory disease of the arterial wall with intimal atheromas that protrude into the lumen and weaken the media.",
    "Non-modifiable risk factors: increasing age, male gender, family history. Modifiable: hyperlipidemia (LDL), hypertension, cigarette smoking, diabetes mellitus.",
    "Response to injury: chronic endothelial injury, endothelial dysfunction with monocyte adhesion, smooth muscle recruitment and macrophage activation, foam cells, then smooth muscle proliferation and collagen deposition.",
    "Fatty spots (<1 mm, foam cells) are the earliest lesion; fatty streaks (1 cm or longer) are not significantly raised and do not disturb blood flow.",
    "Atheroma: raised intimal patch with a soft yellow lipid core under a firm white fibrous cap; cells, ECM and lipid.",
], L4)

B.sata("A nurse counsels a client about atherosclerosis risk. Which risk factors can the client modify?",
       ["Hypercholesterolemia", "Hypertension", "Cigarette smoking", "Diabetes mellitus"],
       [("Increasing age", "Age is a non-modifiable risk factor.", "thinks non-modifiable factors are modifiable"),
        ("Male gender", "Male gender is a non-modifiable risk factor.", "thinks non-modifiable factors are modifiable"),
        ("Family history", "Genetic abnormalities and family history are non-modifiable.", "thinks non-modifiable factors are modifiable")],
       "Atherosclerosis risk factors are split into non-modifiable (increasing age, male gender, genetic abnormalities and family history) and modifiable (hyperlipidemia, especially hypercholesterolemia with high LDL, hypertension, cigarette smoking and diabetes mellitus). Counseling targets the modifiable ones.",
       L4)

B.order("A nurse explains how an atheroma develops according to the response-to-injury hypothesis. Arrange the steps in order.",
        ["Chronic endothelial injury (hyperlipidemia, hypertension, smoking)", "Endothelial dysfunction with monocyte adhesion and emigration",
         "Smooth muscle recruitment to the intima and macrophage activation", "Macrophages and smooth muscle cells engulf lipid to form foam cells (fatty streak)",
         "Smooth muscle proliferation with collagen and ECM deposition (fibrofatty atheroma)"],
        "The response-to-injury hypothesis sees atherosclerosis as a chronic inflammatory response to endothelial injury. Injury from hyperlipidemia, hypertension, smoking, homocysteine, toxins, viruses or immune reactions makes the endothelium leaky and sticky, so monocytes adhere and migrate in. Smooth muscle cells are recruited into the intima and macrophages activate; both engulf lipid as foam cells, forming a fatty streak. Smooth muscle proliferation and collagen deposition then build the fibrofatty atheroma.",
        L4)

B.mc("A biopsy of a young client's aorta shows flat yellow lesions about 1 cm long made of foam cells that do not narrow the lumen. Which lesion is this?",
     "Fatty streak",
     [("Fatty spot", "Fatty spots are smaller (less than 1 mm) and are the earliest lesion.", "mixes up spots and streaks"),
      ("Atheromatous plaque", "An atheroma is a RAISED patch with a lipid core under a fibrous cap.", "calls any fatty lesion a plaque"),
      ("Mönckeberg medial sclerosis", "Mönckeberg sclerosis is calcification of the media of muscular arteries.")],
     "Atherosclerotic lesions progress from fatty spots (multiple yellow spots under 1 mm made of foam cells) to fatty streaks, where spots coalesce into elongated streaks 1 cm or longer. Streaks contain foam cells and a little extracellular lipid, are not significantly raised and do not disturb blood flow. Atheromas come later.",
     L4)

B.mc("A nurse reviews the gross description of a coronary atheroma. Which description is accurate?",
     "A raised intimal patch with a soft yellow lipid core covered by a firm white fibrous cap",
     [("A flat yellow streak that does not disturb blood flow", "That describes a fatty streak.", "mixes up streaks and plaques"),
      ("Calcific deposits in the media of a muscular artery", "That describes Mönckeberg medial sclerosis."),
      ("A thickened arteriolar wall with onion-skinning", "That describes hyperplastic arteriolosclerosis.")],
     "An atheroma is a raised patch within the intima with a soft, yellow core of lipid covered by a firm, white fibrous cap. Microscopically it has cells (smooth muscle cells, macrophages, other leukocytes), extracellular matrix (collagen, elastic fibers, proteoglycans) and intracellular and extracellular lipid.",
     L4)

B.tf("A nurse states that fatty streaks are not significantly raised and do not disturb blood flow.", True,
     "True. Fatty streaks are elongated streaks 1 cm or longer that are not significantly raised and do not cause any disturbance in blood flow.",
     L4, "This statement is true: fatty streaks are flat and do not disturb flow.")

B.concept("path-athero-complications", "Complications and sites of atherosclerosis", [
    "Common sites: lower abdominal aorta, coronary, popliteal and internal carotid arteries, and the circle of Willis.",
    "Acute plaque changes: rupture, ulceration or erosion (induces thrombosis), and fissure with hemorrhage into the plaque.",
    "Other complications: atheroembolism, aneurysm from weakened media, calcification.",
    "Consequences: ischemic heart disease (coronary), stroke (cerebral), aortic aneurysm (aorta), peripheral vascular disease with gangrene (leg arteries).",
], L4)

B.sata("A nurse reviews where atherosclerosis most often develops. Which sites are common?",
       ["Lower abdominal aorta", "Coronary arteries", "Popliteal arteries", "Internal carotid arteries", "Vessels of the circle of Willis"],
       [("Arterioles of the kidney", "Arterioles are affected by arteriolosclerosis, not atherosclerosis.", "mixes up atherosclerosis and arteriolosclerosis sites"),
        ("Deep veins of the leg", "Leg veins are a site of deep vein thrombosis, not atherosclerosis.")],
       "Atheromas form in large and medium arteries. The common sites listed are the lower abdominal aorta, coronary arteries, popliteal arteries, internal carotid arteries and the vessels of the circle of Willis, which explains the main consequences: ischemic heart disease, stroke, aortic aneurysm and peripheral vascular disease.",
       L4)

B.mc("A client with known coronary atherosclerosis suddenly develops an acute myocardial infarction. Which plaque change most likely triggered the event?",
     "Rupture or erosion of the plaque surface, which induces thrombosis",
     [("Calcification of the atheroma", "Calcification is a chronic change of atheromas, not the acute trigger of thrombosis.", "thinks calcification causes acute events"),
      ("Formation of a new fatty streak", "Fatty streaks are flat early lesions that do not disturb flow."),
      ("Mönckeberg medial sclerosis of the artery", "Mönckeberg sclerosis is medial calcification, a separate pattern.")],
     "Acute plaque changes are rupture, ulceration or erosion of the luminal surface, which induces thrombosis, and fissure with hemorrhage into the plaque, which can expand or rupture it. Plaque rupture can also discharge debris (atheroembolism). Thrombosis on a ruptured coronary plaque is what turns chronic ischemic disease into infarction.",
     L4)

B.match("A nurse explains the clinical consequences of atherosclerosis at different sites. Match each site to its major consequence.",
        [("Coronary arteries", "Ischemic heart disease"),
         ("Cerebral arteries", "Cerebral infarction (stroke)"),
         ("Aorta", "Aortic aneurysm"),
         ("Arteries of the lower extremity", "Peripheral vascular disease with gangrene of the legs")],
        [("Pulmonary infarction", "Pulmonary infarction follows pulmonary embolism, usually from DVT, not atherosclerosis.", "links PE to atherosclerosis")],
        "Where an atheroma narrows or thromboses an artery decides the disease. Coronary atherosclerosis causes ischemic heart disease, cerebral atherosclerosis causes stroke, aortic atherosclerosis weakens the media and causes aneurysms, and atherosclerosis of the limb arteries causes peripheral vascular disease and gangrene.",
        L4,
        row_stems={
            "Coronary arteries": "A client has severe coronary atherosclerosis. Which clinical consequence should the nurse anticipate?",
            "Cerebral arteries": "A client has atherosclerosis of the cerebral arteries. Which consequence is the nurse watching for?",
            "Aorta": "A client has advanced aortic atherosclerosis. Which consequence should the nurse anticipate?",
            "Arteries of the lower extremity": "A client has atherosclerosis of the leg arteries. Which consequence should the nurse anticipate?",
        })

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
