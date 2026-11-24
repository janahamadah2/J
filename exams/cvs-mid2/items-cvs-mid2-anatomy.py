from _authoring import Bank

B = Bank("Anatomy")
L4 = "Anatomy L4 slides"
L5 = "Anatomy L5 slides"

# ---------------------------------------------------------------- L4 heart
B.concept("anat-coronary", "Coronary arteries: origin, course and territories", [
    "Right coronary artery: from the right (anterior) aortic sinus; left coronary artery: from the left (anterior) aortic sinus.",
    "LAD runs in the anterior interventricular groove and supplies the sternocostal surface of both ventricles, the anterior 2/3 of the interventricular septum and the A-V bundle.",
    "The posterior interventricular artery (PDA) runs in the posterior interventricular groove and supplies the diaphragmatic surface of both ventricles and the posterior 1/3 of the septum.",
    "Circumflex (LCx): branches to the left atrium and to the left ventricle, including the left (obtuse) marginal artery.",
    "Artery to the SA node: RCA 65%, circumflex 35%. Artery to the AV node: RCA 80%, circumflex 20%.",
], L4)

B.mc("A 68-year-old man suffering from recurrent angina underwent a coronary angiogram. It reveals 90% stenosis of the left anterior descending (LAD) artery. Based on this finding, which portion of the heart is most likely susceptible to ischemic damage?",
     "Anterior two thirds of interventricular septum",
     [("Posterior one third of interventricular septum", "The posterior 1/3 of the septum is supplied by the posterior interventricular (descending) artery, not the LAD.", "mixes up LAD and PDA septal territory"),
      ("Atrioventricular (AV) node", "The artery to the AV node comes from the RCA (80%) or the circumflex (20%), not the LAD.", "thinks LAD supplies the AV node"),
      ("Diaphragmatic surface of left ventricle", "The diaphragmatic surface of both ventricles is supplied by the posterior interventricular artery (and in co-dominance a circumflex branch).", "mixes up sternocostal and diaphragmatic surfaces"),
      ("Right atrium", "The right atrium gets atrial branches of the right coronary artery.")],
     "The LAD (anterior interventricular artery) is one of the two terminal branches of the short left main coronary artery. It runs in the anterior interventricular groove with the great cardiac vein, so the muscle it feeds lies on the front of the heart: the sternocostal surface of both ventricles, the anterior two thirds of the interventricular septum and the A-V bundle. A 90% LAD stenosis therefore puts the anterior septum at risk. The posterior third of the septum and the diaphragmatic surface depend on the posterior interventricular artery instead.",
     L4 + ", in-class case", last=True)

B.mc("A client's angiogram shows a blocked posterior interventricular (descending) artery. Which region should the nurse anticipate is at greatest risk of ischemia?",
     "Posterior one third of the interventricular septum",
     [("Anterior two thirds of the interventricular septum", "The anterior 2/3 of the septum is LAD territory.", "mixes up LAD and PDA septal territory"),
      ("Sternocostal surface of both ventricles", "The sternocostal surface of both ventricles is supplied by the LAD.", "mixes up sternocostal and diaphragmatic surfaces"),
      ("Left atrium", "The left atrium receives branches of the circumflex artery."),
      ("Infundibulum of the right ventricle", "The infundibulum is supplied by the right conus artery, an early RCA branch.")],
     "The posterior interventricular (descending) artery runs in the posterior interventricular groove together with the middle cardiac vein. It supplies the diaphragmatic surface of both ventricles and the posterior one third of the interventricular septum. The septum is therefore shared: the front two thirds belong to the LAD and the back third to the PDA, so a PDA block threatens the posterior septum.",
     L4)

B.sata("A client has a sudden occlusion of the proximal right coronary artery. Which structures should the nurse recognize may lose their arterial supply?",
       ["SA node", "AV node", "Right ventricle via the acute (right) marginal branch", "Posterior one third of the interventricular septum"],
       [("Anterior two thirds of the interventricular septum", "The anterior 2/3 of the septum is supplied by the LAD.", "thinks RCA supplies the anterior septum"),
        ("Left ventricle via the obtuse (left) marginal branch", "The obtuse (left) marginal artery is a branch of the circumflex, a branch of the left coronary.", "mixes up acute and obtuse marginal")],
     "The RCA arises from the right aortic sinus and runs in the coronary groove, first between the right atrium and right ventricle and then posteriorly. Along the way it gives the artery to the SA node (65% of people), the artery to the AV node (80%), ventricular branches and the acute (right) marginal artery to the right ventricle, and it ends as the posterior interventricular artery that supplies the posterior third of the septum. A proximal occlusion can therefore starve all of these.",
     L4)

B.mc("A client with angina asks where the coronary arteries begin. Which response by the nurse is accurate?",
     "The right coronary artery arises from the right aortic sinus, just above the right cusp of the aortic valve.",
     [("The right coronary artery arises from the posterior aortic sinus.", "The posterior aortic sinus lies above the posterior cusp and gives no coronary artery.", "thinks a coronary arises from the posterior sinus"),
      ("The left coronary artery arises from the pulmonary trunk.", "The left coronary artery only runs between the pulmonary trunk and the left auricle; it arises from the left aortic sinus.", "confuses the LCA's course with its origin"),
      ("Both coronary arteries arise from the arch of the aorta.", "The arch gives the brachiocephalic, left common carotid and left subclavian arteries; the coronaries arise from sinuses of the ascending aorta.")],
     "The ascending aorta has three sinuses just above the cusps of the aortic valve: right, left and posterior. The right coronary artery arises from the right (anterior) aortic sinus and the left coronary artery from the left (anterior) aortic sinus. The posterior sinus gives no coronary branch.",
     L4)

B.mc("A client develops complete heart block after a coronary occlusion. The nurse knows the artery to the AV node most often arises from which vessel?",
     "Right coronary artery",
     [("Circumflex artery", "The circumflex gives the artery to the AV node in only about 20% of people.", "reverses the AV-node percentages"),
      ("Left anterior descending artery", "The LAD supplies the A-V bundle, not the AV node itself.", "thinks LAD supplies the AV node"),
      ("Left (obtuse) marginal artery", "The obtuse marginal is a circumflex branch to the left ventricle.")],
     "The AV node sits in the conduction path between atria and ventricles, so losing its blood supply can block conduction. The artery to the AV node comes from the right coronary artery in about 80% of people and from the circumflex in about 20%. The LAD supplies the A-V bundle further down the conducting system.",
     L4)

B.mc("A nursing student describes the blood supply of the SA node. Which statement by the student is accurate?",
     "It arises from the right coronary artery in about 65% of people and from the circumflex in about 35%.",
     [("It arises from the circumflex in about 65% of people and from the right coronary in about 35%.", "The percentages are reversed: the RCA supplies the SA node in about 65%.", "reverses the SA-node percentages"),
      ("It always arises from the left anterior descending artery.", "The LAD supplies the sternocostal surface, anterior 2/3 of the septum and the A-V bundle, not the SA node."),
      ("It arises from the right conus artery.", "The right conus artery goes to the infundibulum of the right ventricle.")],
     "The SA node artery is a branch of the right coronary artery in about 65% of people and of the circumflex branch of the left coronary in about 35%. Knowing the percentages helps predict which occlusion can disturb the pacemaker.",
     L4)

B.tf("A nurse states that the LAD supplies the A-V bundle as well as the anterior two thirds of the interventricular septum.", True,
     "The anterior interventricular artery (LAD) supplies the sternocostal surface of both ventricles, the anterior 2/3 of the interventricular septum and the A-V bundle.",
     L4, "This statement is true: the A-V bundle is listed among the LAD's territories.")

B.concept("anat-dominance", "Coronary dominance", [
    "Co-dominance (balanced) 70%: the right coronary has the posterior interventricular branch and the circumflex has a branch to the diaphragmatic surface of the left ventricle.",
    "Right dominance (15%): the posterior interventricular artery is a large branch.",
    "Left dominance (15%): the posterior interventricular artery is a large branch of the circumflex coronary.",
], L4)

B.mc("A client's angiography report reads \"left dominant circulation.\" Which interpretation by the nurse is correct?",
     "The posterior interventricular artery is a large branch of the circumflex artery.",
     [("The posterior interventricular artery is a large branch of the right coronary artery.", "That describes right dominance.", "mixes up right and left dominance"),
      ("The RCA gives the posterior interventricular branch and the circumflex sends a branch to the diaphragmatic left ventricle.", "That describes co-dominance (balanced circulation).", "mixes up co-dominance and left dominance"),
      ("The circumflex supplies the SA node in every client.", "The circumflex supplies the SA node in only about 35% of people, whatever the dominance.")],
     "Dominance is named by which artery gives the posterior interventricular artery. In left dominance (15% on the slide) the posterior interventricular artery is a large branch of the circumflex; in right dominance (15%) it is a large branch of the right coronary; in co-dominance (70%) the RCA gives it and the circumflex also reaches the diaphragmatic surface of the left ventricle. Note: the slide gives co-dominance as the most common pattern (70%); many textbooks give right dominance as the most common instead, so check which figure your instructor expects.",
     L4)

B.concept("anat-cardiac-veins", "Venous drainage of the heart", [
    "Coronary sinus: lies between the left atrium and the diaphragmatic surface and ends in the posterior wall of the right atrium.",
    "Tributaries of the coronary sinus: great, middle and small cardiac veins, posterior vein of the left ventricle and oblique vein of the left atrium.",
    "Anterior cardiac veins arise from the right ventricle and end in the anterior wall of the right atrium.",
    "Venae cordis minimi drain directly into the cardiac chambers, especially on the right side.",
    "The great cardiac vein runs with the LAD in the anterior interventricular groove; the middle cardiac vein runs with the posterior interventricular artery.",
], L4)

B.match("While reviewing a cardiac venogram with a client, the nurse identifies where each vein runs or ends. Match each vein to its location.",
        [("Great cardiac vein", "Anterior interventricular groove, with the LAD"),
         ("Middle cardiac vein", "Posterior interventricular groove, with the posterior interventricular artery"),
         ("Coronary sinus", "Posterior wall of the right atrium"),
         ("Anterior cardiac veins", "Anterior wall of the right atrium")],
        [("Directly into all four chambers", "This is how the venae cordis minimi drain, not any of the named veins.", "confuses named veins with venae cordis minimi")],
        "The heart drains by three routes. Most blood collects into the coronary sinus, which lies between the left atrium and the diaphragmatic surface and ends in the posterior wall of the right atrium; its tributaries include the great cardiac vein (with the LAD in the anterior groove) and the middle cardiac vein (with the PDA in the posterior groove). The 2-3 anterior cardiac veins of the right ventricle end in the anterior wall of the right atrium, and the venae cordis minimi open directly into the chambers. Note: one slide says 3-4 anterior cardiac veins and another says 2-3.",
        L4 + ", slide exercise",
        row_stems={
            "Great cardiac vein": "During cardiac surgery the nurse watches the surgeon trace the vein that accompanies the LAD. In which location does the great cardiac vein run?",
            "Middle cardiac vein": "A client's venogram highlights the middle cardiac vein. Where should the nurse expect this vein to run?",
            "Coronary sinus": "A nurse explains to a client where the heart's main venous channel empties. Where does the coronary sinus end?",
            "Anterior cardiac veins": "A nurse reviews the small veins draining the right ventricle. Where do the anterior cardiac veins end?",
        }, last=True)

B.tf("A nurse explains to a client that the coronary sinus empties into the posterior wall of the left atrium.", False,
     "False. The coronary sinus lies between the left atrium and the diaphragmatic surface of the heart, but it terminates in the posterior wall of the RIGHT atrium, like the rest of the systemic venous return.",
     L4, "The coronary sinus ends in the right atrium, not the left.", "thinks coronary sinus drains into left atrium")

B.sata("A client's coronary sinus is being cannulated for a procedure. Which veins should the nurse recognize as tributaries that drain into it?",
       ["Great cardiac vein", "Middle cardiac vein", "Small cardiac vein", "Oblique vein of the left atrium"],
       [("Anterior cardiac veins", "Anterior cardiac veins bypass the coronary sinus and end directly in the anterior wall of the right atrium.", "thinks anterior cardiac veins join the coronary sinus"),
        ("Venae cordis minimi", "Venae cordis minimi drain directly into the cardiac chambers.")],
       "The coronary sinus collects five tributaries: the great, middle and small cardiac veins, the posterior vein of the left ventricle and the oblique vein of the left atrium. The anterior cardiac veins and the venae cordis minimi do not join it; they drain straight into the right atrium or the chambers.",
       L4)

B.concept("anat-surface", "Surface anatomy of the heart and valves", [
    "Point A: lower border of the left 2nd costal cartilage, 0.5 inch from the sternum; point B: upper border of the right 3rd costal cartilage, 0.5 inch from the sternum.",
    "Point C: right 6th costal cartilage, 0.5 inch from the sternum; point D: left 5th intercostal space, 3.5 inches from the midline.",
    "Borders: upper A-B, right B-C, lower C-D, left D-A.",
    "Valves (PAMT): pulmonary behind the left 3rd costal cartilage; aortic opposite the left 3rd intercostal space; mitral opposite the left 4th costal cartilage; tricuspid opposite the left 4th intercostal space behind the midline of the sternum.",
], L4)

B.blanks("Before a cardiac exam, a nurse marks the outline of a client's heart on the chest wall. Point A lies at the lower border of the left {1} costal cartilage, point B at the upper border of the right {2} costal cartilage, and point D, the apex, lies in the left {3}, 3.5 inches from the midline.",
         [("2nd", [("3rd", "The left 3rd costal cartilage is where the pulmonary valve lies, not point A.", "puts point A one level too low"),
                   ("4th", "The left 4th costal cartilage marks the mitral valve.")]),
          ("3rd", [("2nd", "The 2nd costal cartilage is point A on the LEFT side.", "swaps the levels of points A and B"),
                   ("6th", "The right 6th costal cartilage is point C, the lower end of the right border.")]),
          ("5th intercostal space", [("4th intercostal space", "The left 4th intercostal space marks the tricuspid valve.", "places the apex one space too high"),
                                     ("6th costal cartilage", "The 6th costal cartilage is point C, on the right.")])],
         "Four points outline the heart: A (lower border of the left 2nd costal cartilage, 0.5 inch from the sternum), B (upper border of the right 3rd costal cartilage, 0.5 inch from the sternum), C (right 6th costal cartilage, 0.5 inch from the sternum) and D (left 5th intercostal space, 3.5 inches from the midline). Joining them gives the borders: upper A-B, right B-C, lower C-D and left D-A.",
         L4)

B.mc("A nurse is marking the right border of a client's heart on the chest wall. Between which two points should the line be drawn?",
     "From the right 3rd costal cartilage (B) to the right 6th costal cartilage (C)",
     [("From the left 2nd costal cartilage (A) to the right 3rd costal cartilage (B)", "A-B is the upper border.", "mixes up upper and right borders"),
      ("From the right 6th costal cartilage (C) to the left 5th intercostal space (D)", "C-D is the lower border."),
      ("From the left 5th intercostal space (D) to the left 2nd costal cartilage (A)", "D-A is the left border."),
      ("From the left 3rd costal cartilage to point C", "This line marks the coronary groove, not a border.")],
     "The borders are named by joining the four surface points in order: upper border A-B, right border B-C, lower border C-D and left border D-A. The right border therefore runs from the upper border of the right 3rd costal cartilage down to the right 6th costal cartilage, 0.5 inch from the sternum. The coronary groove is a separate line from the left 3rd costal cartilage to point C.",
     L4)

B.mc("A nurse places the stethoscope to locate the surface marking of a client's mitral valve. Where is the mitral valve located?",
     "Opposite the left 4th costal cartilage, behind the left half of the sternum",
     [("Behind the left 3rd costal cartilage at its junction with the sternum", "That is the surface marking of the pulmonary valve.", "mixes up mitral and pulmonary valve markings"),
      ("Opposite the left 3rd intercostal space, behind the left margin of the sternum", "That is the surface marking of the aortic valve.", "mixes up mitral and aortic valve markings"),
      ("Opposite the left 4th intercostal space, behind the midline of the sternum", "That is the surface marking of the tricuspid valve.", "mixes up mitral and tricuspid valve markings"),
      ("Left 5th intercostal space, 3.5 inches from the midline", "That is point D, the apex of the heart, not a valve.")],
     "The valves lie in a diagonal line behind the sternum, from high on the left to low in the middle, remembered as PAMT. Pulmonary: behind the left 3rd costal cartilage at its junction with the sternum. Aortic: opposite the left 3rd intercostal space. Mitral: opposite the left 4th costal cartilage behind the left half of the sternum. Tricuspid: opposite the left 4th intercostal space behind the midline of the sternum.",
     L4)

B.order("A nurse reviews the surface markings of the heart valves. Arrange the valves from the highest to the lowest position on the chest wall.",
        ["Pulmonary valve (left 3rd costal cartilage)", "Aortic valve (left 3rd intercostal space)",
         "Mitral valve (left 4th costal cartilage)", "Tricuspid valve (left 4th intercostal space)"],
        "The mnemonic PAMT gives the order from top to bottom: pulmonary behind the left 3rd costal cartilage, aortic opposite the left 3rd intercostal space, mitral opposite the left 4th costal cartilage and tricuspid opposite the left 4th intercostal space. Each valve sits about half a level lower than the one before.",
        L4)

B.concept("anat-pci", "Coronary angiography and PCI", [
    "A catheter is passed retrograde from the radial or femoral artery into the ascending aorta under local anesthesia.",
    "Radiopaque contrast is injected into the orifice of each coronary artery to photograph all segments of each vessel.",
    "A stent may be placed to open vessels narrowed by plaque buildup (atherosclerosis).",
], L4)

B.order("A client is scheduled for percutaneous coronary intervention. Arrange the steps of the procedure in the order they occur.",
        ["Local anesthesia is given", "A catheter is passed retrograde from the radial or femoral artery",
         "The catheter reaches the ascending aorta", "Contrast is injected into the orifice of each coronary artery and photographed",
         "A stent is placed to open the narrowed vessel"],
        "With the client under local anesthesia, a catheter is passed retrograde from the radial or femoral artery directly into the ascending aorta, where the coronary arteries begin. Multiple small doses of radiopaque contrast are injected into the orifice of each coronary artery to photograph every segment. A stent may then be placed to open a vessel narrowed by atherosclerotic plaque.",
        L4)

# ---------------------------------------------------------------- L5 head and neck
B.concept("anat-carotid", "Common, external and internal carotid arteries", [
    "Right common carotid: from the brachiocephalic artery behind the sternoclavicular joint; left common carotid: from the arch of the aorta.",
    "The common carotid ascends in the carotid sheath, related medially to the trachea and larynx and laterally to the IJV, and ends at the upper border of the thyroid cartilage (C3-4).",
    "The external carotid ends in the parotid gland behind the neck of the mandible by dividing into the maxillary and superficial temporal arteries.",
    "External carotid branches: superior thyroid, ascending pharyngeal, lingual, facial, occipital, posterior auricular, superficial temporal and maxillary.",
    "The internal carotid has no branches in the neck; it enters the skull through the carotid canal.",
], L5)

B.mc("A 45-year-old man is in surgery. While seated at the head of the operating table, the anesthesiologist periodically checks the patient's pulse by palpating the artery located anterior to the tragus of the external ear. Which of the following arteries is being utilized to monitor the patient's pulse?",
     "Superficial temporal",
     [("Maxillary", "The maxillary artery is the other terminal branch of the external carotid; it runs deep, not in front of the tragus.", "mixes up the two terminal ECA branches"),
      ("Posterior auricular", "The posterior auricular artery is an external carotid branch that runs behind the ear."),
      ("Facial", "The facial artery is an external carotid branch to the face, not in front of the tragus."),
      ("Internal carotid", "The internal carotid has no branches in the neck and enters the skull through the carotid canal.")],
     "The external carotid artery ends inside the parotid gland behind the neck of the mandible by dividing into the maxillary and superficial temporal arteries. The superficial temporal artery then ascends just in front of the tragus of the ear, where it can be felt, which makes it a convenient pulse for the anesthesiologist at the head of the table.",
     L5 + ", in-class case", last=True)

B.mc("A nurse palpates the carotid pulse and recalls where the common carotid artery divides. At which level does the common carotid artery end?",
     "At the upper border of the thyroid cartilage (C3-C4)",
     [("Behind the sternoclavicular joint", "That is where the right common carotid begins from the brachiocephalic artery.", "confuses origin with termination"),
      ("At the outer border of the first rib", "That is where the subclavian artery becomes the axillary artery."),
      ("Behind the neck of the mandible within the parotid gland", "That is where the external carotid ends.", "confuses common and external carotid termination"),
      ("At the jugular foramen", "That is where the internal jugular vein begins.")],
     "The common carotid arteries arise differently on each side (right from the brachiocephalic artery behind the sternoclavicular joint, left from the arch of the aorta), ascend inside the carotid sheath and end at the upper border of the thyroid cartilage, between C3 and C4, by dividing into the external and internal carotid arteries.",
     L5)

B.mc("Before an internal jugular cannulation, the nurse reviews the relations of the common carotid artery in the carotid sheath. Which structure lies lateral to the artery?",
     "Internal jugular vein",
     [("Trachea", "The trachea lies medial to the common carotid artery.", "reverses medial and lateral relations"),
      ("Larynx", "The larynx lies medial to the common carotid artery.", "reverses medial and lateral relations"),
      ("Scalenus anterior", "Scalenus anterior is a relation of the subclavian artery, which it divides into three parts.")],
     "Inside the carotid sheath the common carotid artery is related medially to the trachea and larynx and laterally to the internal jugular vein. Knowing that the vein is lateral helps the operator avoid the artery during a jugular puncture.",
     L5)

B.sata("A client needs ligation of the external carotid artery. Which arteries should the nurse recognize arise directly from it?",
       ["Superior thyroid artery", "Lingual artery", "Facial artery", "Occipital artery"],
       [("Inferior thyroid artery", "The inferior thyroid artery is a branch of the thyrocervical trunk of the subclavian artery.", "mixes up superior and inferior thyroid origins"),
        ("Vertebral artery", "The vertebral artery is a branch of the first part of the subclavian artery."),
        ("Transverse cervical artery", "The transverse cervical artery is a branch of the thyrocervical trunk.")],
       "The external carotid gives eight branches: superior thyroid, ascending pharyngeal, lingual, facial, occipital and posterior auricular, then ends as the superficial temporal and maxillary arteries. The inferior thyroid, transverse cervical and vertebral arteries all come from the subclavian system instead.",
       L5)

B.tf("A nurse teaching about cerebral blood supply states that the internal carotid artery gives no branches in the neck.", True,
     "True. The internal carotid artery arises at the upper border of the thyroid cartilage, gives no branches in the neck, enters the cranial cavity through the carotid canal and supplies the brain, eyes, forehead and part of the nose.",
     L5, "This statement is true: the internal carotid has no branches in the neck.")

B.concept("anat-subclavian", "Subclavian artery", [
    "Right subclavian: from the brachiocephalic artery behind the right sternoclavicular joint; left subclavian: from the arch of the aorta.",
    "It ends at the outer border of the 1st rib by becoming the axillary artery.",
    "Scalenus anterior passes anterior to the artery and divides it into 3 parts: medial, behind and lateral to the muscle.",
    "1st part: vertebral, internal thoracic and thyrocervical trunk (inferior thyroid, transverse cervical, suprascapular). 2nd part: costocervical trunk. 3rd part: dorsal scapular (66%).",
], L5)

B.mc("A client is being assessed for compression of the subclavian artery in the root of the neck. Which structure divides this artery into three parts?",
     "Scalenus anterior, which passes anterior to the artery",
     [("Sternomastoid, which the external jugular vein crosses", "The sternomastoid is the muscle the external jugular vein descends over.", "confuses neck muscles"),
      ("The outer border of the first rib", "The outer border of the first rib is where the subclavian ends and becomes the axillary artery.", "confuses termination with the dividing muscle"),
      ("The upper border of the thyroid cartilage", "That level marks the end of the common carotid artery.")],
     "The subclavian artery arches laterally in the root of the neck and ends at the outer border of the first rib as the axillary artery. Scalenus anterior passes in front of it and divides it into three parts: the first part medial to the muscle, the second behind it and the third lateral to it. Each part has its own branches.",
     L5)

B.match("A nurse reviews the branches of the subclavian artery before a neck procedure. Match each artery to the part of the subclavian artery it arises from.",
        [("Vertebral artery", "1st part (medial to scalenus anterior)"),
         ("Costocervical trunk", "2nd part (behind scalenus anterior)"),
         ("Dorsal scapular artery", "3rd part (lateral to scalenus anterior)"),
         ("Internal thoracic artery", "1st part (medial to scalenus anterior)")],
        [("External carotid artery", "The external carotid gives neck branches like the superior thyroid but none of these.", "mixes subclavian and carotid branches")],
        "Scalenus anterior divides the subclavian artery into three parts. The first part (medial) gives the vertebral artery, the internal thoracic artery and the thyrocervical trunk. The second part (behind the muscle) gives the costocervical trunk, which divides into the superior intercostal and deep cervical arteries. The third part (lateral) gives the dorsal scapular artery in about 66% of people.",
        L5,
        row_stems={
            "Vertebral artery": "A client has a vertebral artery injury. From which part of the subclavian artery does the vertebral artery arise?",
            "Costocervical trunk": "A nurse traces the costocervical trunk on a client's angiogram. Which part of the subclavian artery gives this trunk?",
            "Dorsal scapular artery": "A nurse reviews a client's shoulder angiogram showing the dorsal scapular artery. Which part of the subclavian artery gives it?",
            "Internal thoracic artery": "A client is being evaluated for an internal thoracic artery graft. Which part of the subclavian artery gives the internal thoracic artery?",
        })

B.sata("A client is undergoing thyroid surgery near the thyrocervical trunk. Which arteries should the nurse recognize as branches of this trunk?",
       ["Inferior thyroid artery", "Transverse cervical artery", "Suprascapular artery"],
       [("Superior thyroid artery", "The superior thyroid artery is the first branch of the external carotid.", "mixes up superior and inferior thyroid origins"),
        ("Deep cervical artery", "The deep cervical artery is a branch of the costocervical trunk (2nd part)."),
        ("Superior intercostal artery", "The superior intercostal artery is a branch of the costocervical trunk (2nd part).")],
       "The thyrocervical trunk is one of the three branches of the first part of the subclavian artery. It gives the inferior thyroid, transverse cervical and suprascapular arteries. The costocervical trunk from the second part gives the superior intercostal and deep cervical arteries.",
       L5)

B.concept("anat-facial-veins", "Facial veins and the dangerous area of the face", [
    "Anterior facial vein: formed by the supraorbital and supratrochlear veins at the medial angle of the eye.",
    "Retromandibular (posterior facial) vein: formed by the maxillary and superficial temporal veins inside the parotid gland; divides at the lower pole of the parotid.",
    "Common facial vein: anterior facial vein + anterior division of the retromandibular vein; drains into the IJV.",
    "The deep facial vein connects the anterior facial vein to the pterygoid plexus.",
    "Dangerous area of the face (nose and upper lip): infection can reach the cavernous sinus through the connections of the anterior facial vein.",
], L5)

B.mc("A client squeezed an infected pimple on the upper lip and now has a spreading infection. Which complication should the nurse be most concerned about?",
     "Spread of infection to the cavernous sinus",
     [("Spread of infection to the sigmoid sinus", "The sigmoid sinus continues as the internal jugular vein at the jugular foramen; it is not the route from the dangerous area.", "confuses cavernous and sigmoid sinus"),
      ("Spread of infection to the subclavian vein through the external jugular vein", "The external jugular vein drains into the subclavian vein, but it does not drain the nose and upper lip."),
      ("Spread of infection to the parotid gland through the deep facial vein", "The deep facial vein links the anterior facial vein to the pterygoid plexus, not to the parotid gland.")],
     "The nose and upper lip are the dangerous area of the face. Their blood drains into the anterior facial vein, which connects with the cavernous sinus through the ophthalmic veins and through the deep facial vein and pterygoid plexus. Infection in this area can therefore travel back into the cavernous sinus inside the skull.",
     L5)

B.order("A client has an infected lesion on the upper lip. Arrange the deep venous route by which the infection can reach the cavernous sinus.",
        ["Infected area of the nose and upper lip", "Anterior facial vein", "Deep facial vein", "Pterygoid plexus", "Cavernous sinus"],
        "Infection in the dangerous area drains into the anterior facial vein. The deep facial vein connects the anterior facial vein to the pterygoid plexus of veins, and the plexus communicates with the cavernous sinus, so organisms can travel this deep route into the skull. A second route runs from the anterior facial vein through the ophthalmic veins.",
        L5)

B.blanks("A nurse reviews the venous anatomy of the parotid region. The retromandibular vein forms inside the {1} by the union of the maxillary vein and the {2} vein; its posterior branch then joins the {3} vein to form the external jugular vein.",
         [("parotid gland", [("submandibular gland", "The retromandibular vein forms inside the parotid gland, not the submandibular gland."),
                             ("cavernous sinus", "The cavernous sinus is inside the skull and receives the ophthalmic veins.")]),
          ("superficial temporal", [("supraorbital", "The supraorbital vein joins the supratrochlear vein to form the anterior facial vein.", "mixes up anterior facial and retromandibular formation"),
                                    ("lingual", "The lingual vein is a tributary of the internal jugular vein.")]),
          ("posterior auricular", [("anterior facial", "The anterior facial vein joins the ANTERIOR branch to form the common facial vein.", "mixes up anterior and posterior divisions"),
                                   ("transverse cervical", "The transverse cervical vein is a tributary of the external jugular vein.")])],
         "The retromandibular (posterior facial) vein is formed inside the parotid gland by the maxillary and superficial temporal veins. At the lower pole of the parotid it divides: the posterior branch joins the posterior auricular vein to form the external jugular vein, and the anterior branch joins the anterior facial vein to form the common facial vein, which drains into the IJV.",
         L5)

B.concept("anat-neck-veins", "Jugular, subclavian and brachiocephalic veins", [
    "External jugular vein: formed by the posterior division of the retromandibular vein and the posterior auricular vein; descends superficial to sternomastoid; ends in the subclavian vein.",
    "External jugular tributaries: transverse cervical, suprascapular and anterior jugular veins.",
    "Internal jugular vein: begins as the continuation of the sigmoid sinus at the jugular foramen; joins the subclavian vein to form the brachiocephalic vein.",
    "Internal jugular tributaries: pharyngeal, common facial, lingual, superior thyroid and middle thyroid veins.",
    "Right and left brachiocephalic veins unite to form the SVC.",
], L5)

B.mc("A nurse notices a distended vein crossing superficial to a client's sternomastoid muscle. Which veins unite to form this vein?",
     "The posterior division of the retromandibular vein and the posterior auricular vein",
     [("The supraorbital and supratrochlear veins", "These form the anterior facial vein at the medial angle of the eye.", "mixes up formation of the facial veins"),
      ("The maxillary and superficial temporal veins", "These form the retromandibular vein inside the parotid gland.", "mixes up formation of the facial veins"),
      ("The anterior facial vein and the anterior division of the retromandibular vein", "These form the common facial vein, which drains into the IJV.", "mixes up anterior and posterior divisions"),
      ("The internal jugular and subclavian veins", "These form the brachiocephalic vein.")],
     "The vein running superficial to sternomastoid is the external jugular vein. It forms from the posterior division of the retromandibular vein and the posterior auricular vein, descends over sternomastoid and ends in the subclavian vein. Its tributaries are the transverse cervical, suprascapular and anterior jugular veins.",
     L5 + ", slide exercise", last=True)

B.sata("A client has an internal jugular central line. Which veins should the nurse recognize as tributaries of the internal jugular vein?",
       ["Common facial vein", "Lingual vein", "Superior thyroid vein", "Middle thyroid vein", "Pharyngeal vein"],
       [("Transverse cervical vein", "The transverse cervical vein drains into the external jugular vein.", "mixes up IJV and EJV tributaries"),
        ("Suprascapular vein", "The suprascapular vein drains into the external jugular vein.", "mixes up IJV and EJV tributaries"),
        ("Anterior jugular vein", "The anterior jugular vein drains into the external jugular vein.", "mixes up IJV and EJV tributaries")],
       "The internal jugular vein begins as the continuation of the sigmoid sinus at the jugular foramen and receives the pharyngeal, common facial, lingual, superior thyroid and middle thyroid veins before joining the subclavian vein. The transverse cervical, suprascapular and anterior jugular veins belong to the external jugular vein.",
       L5)

B.tf("A nurse states that the external jugular vein ends by draining into the internal jugular vein.", False,
     "False. The external jugular vein descends superficial to sternomastoid and ends in the SUBCLAVIAN vein; the subclavian vein then joins the internal jugular vein to form the brachiocephalic vein.",
     L5, "The external jugular vein ends in the subclavian vein, not the internal jugular vein.", "thinks EJV drains into IJV")

B.order("A nurse traces the venous drainage from a client's face to the heart. Arrange the veins in the order blood passes through them.",
        ["Anterior facial vein", "Common facial vein", "Internal jugular vein", "Brachiocephalic vein", "Superior vena cava"],
        "The anterior facial vein joins the anterior division of the retromandibular vein to form the common facial vein, which drains into the internal jugular vein. The internal jugular joins the subclavian vein to form the brachiocephalic vein, and the right and left brachiocephalic veins unite to form the superior vena cava.",
        L5)

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
