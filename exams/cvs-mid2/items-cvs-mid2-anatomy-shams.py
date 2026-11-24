"""Shams Practices | CVS MID-2 | Anatomy (uploaded question bank).

All 18 questions kept with their own options and answer key; only typos fixed
(marked in comments). Each joins an existing Anatomy concept card. The source
tag "Shams Practices" puts them in the last pass.
"""
from _authoring import Bank

B = Bank("Anatomy")
H = "Shams Practices, Blood Supply of the Heart, key slide %d; Anatomy L4 slides"
N = "Shams Practices, Blood Supply of the Head and Neck, key slide %d; Anatomy L5 slides"
LIMB = "%s is not one of the head, neck or heart vessels taught in this block; it is a limb vessel, so it cannot be the answer."

# ---------------------------------------------------------------- Blood supply of the heart
B.join("anat-surface")
B.mc("Where is the anatomical surface projection of the tricuspid valve?",
     "Behind the midline of the sternum at the level of the fourth intercostal space",
     [("At the second intercostal space on the right midclavicular line", "No heart valve is marked here; the four valves all lie behind the sternum between the left 3rd costal cartilage and the left 4th intercostal space.", "places a valve away from the sternum"),
      ("Behind the midpoint of the left clavicle", "No heart valve is marked behind the clavicle; the highest valve, the pulmonary, is behind the left 3rd costal cartilage.", "places a valve away from the sternum"),
      ("At the sixth intercostal space on the left midaxillary line", "This lies outside the heart's outline; the lowest point on the left is the apex at the left 5th intercostal space, 3.5 inches from the midline.")],
     "The valves lie in a diagonal line behind the sternum, remembered as PAMT from top to bottom: pulmonary behind the left 3rd costal cartilage, aortic opposite the left 3rd intercostal space, mitral opposite the left 4th costal cartilage, and tricuspid opposite the left 4th intercostal space behind the midline of the sternum. The tricuspid is the lowest and the most medial.",
     H % 17, last=True)

B.join("anat-coronary")
B.mc("In a right-dominant heart, which artery arises from the right coronary artery and runs in the posterior interventricular groove?",
     "Posterior descending artery (PDA)",
     [("Left anterior descending artery (LAD)", "The LAD is a branch of the left coronary artery and runs in the ANTERIOR interventricular groove.", "mixes up LAD and PDA"),
      ("Left circumflex artery", "The circumflex is a branch of the left coronary artery; in left dominance it gives the PDA, but it does not arise from the RCA.", "mixes up right and left dominance"),
      ("First diagonal artery", "A diagonal artery is not described on your slides; it is not the vessel in the posterior interventricular groove.")],
     "The right coronary artery runs in the coronary groove and ends as the posterior interventricular (posterior descending) artery, which runs in the posterior interventricular groove with the middle cardiac vein. It supplies the diaphragmatic surface of both ventricles and the posterior 1/3 of the septum. In right dominance this PDA is a large branch of the RCA.",
     H % 8, last=True)

B.join("anat-cardiac-veins")
# typo fixed: "from the Poster inter-ventricular groove content ?"
B.mc("Which of the following is a content of the posterior interventricular groove?",
     "Middle cardiac vein",
     [("Great cardiac vein", "The great cardiac vein runs in the ANTERIOR interventricular groove with the LAD.", "mixes up great and middle cardiac veins"),
      ("Small cardiac vein", "The small cardiac vein is a tributary of the coronary sinus, but it does not run in the posterior interventricular groove."),
      ("Anterior cardiac vein", "Anterior cardiac veins arise from the right ventricle and end in the anterior wall of the right atrium.")],
     "Each interventricular groove carries an artery and a vein. The anterior groove has the LAD with the great cardiac vein; the posterior groove has the posterior interventricular artery with the middle cardiac vein. Both veins drain into the coronary sinus.",
     H % 8, last=True)

B.join("anat-coronary")
B.mc("The posterior surface of the heart supplied by ?",
     "Posterior interventricular artery",
     [("Radial artery", LIMB % "The radial artery"),
      ("Superior thyroid artery", "The superior thyroid artery is the first branch of the external carotid in the neck; it does not supply the heart."),
      ("Posterior interosseous artery", LIMB % "The posterior interosseous artery")],
     "The posterior (diaphragmatic) surface of both ventricles is supplied by the posterior interventricular artery, which runs in the posterior interventricular groove and also supplies the posterior 1/3 of the interventricular septum. The front of the heart (sternocostal surface) belongs to the LAD.",
     H % 8, last=True)

B.join("anat-cardiac-veins")
B.mc("Vein in the posterior interventricular groove ?",
     "Middle cardiac vein",
     [("Great cardiac vein", "The great cardiac vein runs in the ANTERIOR interventricular groove with the LAD.", "mixes up great and middle cardiac veins"),
      ("Anterior cardiac vein", "Anterior cardiac veins arise from the right ventricle and end in the anterior wall of the right atrium."),
      ("Small cardiac vein", "The small cardiac vein drains into the coronary sinus, but it is not the vein of the posterior interventricular groove.")],
     "The middle cardiac vein runs in the posterior interventricular groove alongside the posterior interventricular artery and drains into the coronary sinus. Its partner in the anterior groove is the great cardiac vein. Note: this question tests the same fact as the earlier \"content of the posterior interventricular groove\" question; both are kept as uploaded.",
     H % 8, last=True)

B.join("anat-coronary")
B.mc("Lateral infarct (lateral wall of the Lt. ventricle):",
     "Circumflex branch of the left coronary",
     [("Right marginal branch of the right coronary artery", "The right (acute) marginal branch supplies the RIGHT ventricle.", "mixes up acute and obtuse marginal"),
      ("Posterior interventricular artery", "The posterior interventricular artery supplies the diaphragmatic surface and the posterior 1/3 of the septum.", "mixes up lateral and posterior walls"),
      ("Conus branch of the right coronary artery", "The right conus branch supplies the infundibulum of the right ventricle.")],
     "The circumflex branch of the left coronary artery gives branches to the left atrium and to the left ventricle, including the left (obtuse) marginal artery along the lateral wall. Occlusion of the circumflex therefore causes a lateral infarct of the left ventricle. Note: the stem was a phrase with an unclosed bracket; the question asks which artery is blocked in a lateral wall infarct.",
     H % 10, last=True)

# ---------------------------------------------------------------- Blood supply of the head and neck
B.join("anat-facial-veins")
B.mc("The anterior division of the retromandibular vein joins the facial vein. Into which vein does the resulting common facial vein usually drain?",
     "Internal jugular vein (IJV)",
     [("Axillary vein", LIMB % "The axillary vein"),
      ("Azygos vein", "The azygos vein is not part of the head and neck drainage on your slides; the common facial vein drains into the IJV."),
      ("Femoral vein", LIMB % "The femoral vein")],
     "The anterior facial vein joins the anterior division of the retromandibular vein to form the common facial vein, which drains into the internal jugular vein. The common facial vein is one of the IJV's tributaries, with the pharyngeal, lingual, superior thyroid and middle thyroid veins.",
     N % 14, last=True)

B.mc("Union of Anterior facial vein & anterior part of posterior facial vein will form?",
     "Common facial vein",
     [("External jugular vein", "The external jugular vein forms from the POSTERIOR division of the posterior facial (retromandibular) vein and the posterior auricular vein.", "mixes up anterior and posterior divisions"),
      ("Anterior jugular vein", "The anterior jugular vein is a tributary of the external jugular vein, not formed by the facial veins."),
      ("Vertebral vein", "The vertebral vein is not formed by the facial veins.")],
     "The posterior facial vein is another name for the retromandibular vein. At the lower pole of the parotid it divides: its anterior part joins the anterior facial vein to form the common facial vein (which drains into the IJV), and its posterior part joins the posterior auricular vein to form the external jugular vein.",
     N % 14, last=True)

B.join("anat-subclavian")
# typo fixed: "supra scapular" -> "suprascapular"
B.mc("Branch of 1st part of subclavian artery, runs dorsally to the suprascapular notch?",
     "Thyrocervical trunk",
     [("Vertebral artery", "The vertebral artery is also a 1st-part branch, but it does not give the suprascapular artery.", "mixes up first-part branches"),
      ("Internal thoracic artery", "The internal thoracic artery is also a 1st-part branch, but it does not give the suprascapular artery.", "mixes up first-part branches"),
      ("Axillary artery", "The axillary artery is the continuation of the subclavian beyond the outer border of the 1st rib, not a branch of its 1st part.")],
     "The first part of the subclavian artery, medial to scalenus anterior, gives the vertebral artery, the internal thoracic artery and the thyrocervical trunk. The thyrocervical trunk divides into the inferior thyroid, transverse cervical and suprascapular arteries, and it is through its suprascapular branch that it reaches the suprascapular notch. Note: strictly, the artery that runs to the notch is the suprascapular artery; the key answer is the 1st-part branch that gives it.",
     N % 10, last=True)

B.join("anat-carotid")
B.mc("An artery which is medial to IJV, originate from aortic arch, and terminate in the thyroid cartilage ?",
     "Common carotid artery",
     [("Left subclavian artery", "The left subclavian also arises from the arch of the aorta, but it arches laterally in the root of the neck and ends at the outer border of the 1st rib.", "mixes up carotid and subclavian"),
      ("Left vertebral artery", "The vertebral artery is a branch of the 1st part of the subclavian artery."),
      ("Left superior thyroid artery", "The superior thyroid artery is the first branch of the external carotid artery.")],
     "The left common carotid artery arises from the arch of the aorta (the right from the brachiocephalic artery). It ascends inside the carotid sheath, related medially to the trachea and larynx and laterally to the IJV, and ends at the upper border of the thyroid cartilage (C3-4) by dividing into the external and internal carotids.",
     N % 4, last=True)

B.join("anat-subclavian")
B.mc("Which of the following is a branch from the 2nd part of subclavian artery?",
     "Deep cervical artery",
     [("Radial artery", LIMB % "The radial artery"),
      ("Superior thyroid artery", "The superior thyroid artery is a branch of the external carotid artery.", "mixes subclavian and carotid branches"),
      ("Femoral artery", LIMB % "The femoral artery")],
     "The second part of the subclavian artery lies behind scalenus anterior and gives the costocervical trunk, which divides into the superior intercostal and deep cervical arteries. The deep cervical artery is therefore a branch of the 2nd part through the costocervical trunk.",
     N % 11, last=True)

B.join("anat-neck-veins")
B.mc("The brachiocephalic vein is formed by",
     "Subclavian vein and internal jugular vein",
     [("Radial vein and ulnar vein", LIMB % "The radial and ulnar veins"),
      ("Cephalic vein and basilic vein", LIMB % "The cephalic and basilic veins"),
      ("Great saphenous vein and femoral vein", LIMB % "The great saphenous and femoral veins")],
     "The internal jugular vein joins the subclavian vein to form the brachiocephalic vein, and the right and left brachiocephalic veins unite to form the superior vena cava. The subclavian vein itself begins as the continuation of the axillary vein at the outer border of the 1st rib.",
     N % 21, last=True)

B.join("anat-facial-veins")
# "facial vein" here means the posterior facial (retromandibular) vein
B.mc("Posterior branch of facial vein will form ?",
     "External jugular vein",
     [("Anterior jugular vein", "The anterior jugular vein is a tributary of the external jugular vein, not formed by the posterior branch."),
      ("Vertebral vein", "The vertebral vein is not formed by the facial veins."),
      ("Subclavian vein", "The subclavian vein begins as the continuation of the axillary vein; the external jugular drains into it.")],
     "The posterior facial (retromandibular) vein divides at the lower pole of the parotid gland. Its posterior branch joins the posterior auricular vein to form the external jugular vein, which descends superficial to sternomastoid and ends in the subclavian vein. Note: the stem says \"facial vein\"; it means the posterior facial vein, since the anterior facial vein does not divide this way.",
     N % 13, last=True)

B.join("anat-carotid")
B.mc("Artery running in the sheath, medially to IJV, and arising from arch of aorta ?",
     "Left common carotid",
     [("Left vertebral artery", "The vertebral artery is a branch of the 1st part of the subclavian artery and does not run in the carotid sheath."),
      ("Left superior thyroid artery", "The superior thyroid artery is the first branch of the external carotid artery."),
      ("Left axillary artery", "The axillary artery is the continuation of the subclavian artery beyond the 1st rib.")],
     "Only the LEFT common carotid arises directly from the arch of the aorta; the right arises from the brachiocephalic artery behind the sternoclavicular joint. Inside the carotid sheath the common carotid lies medial to the internal jugular vein.",
     N % 4, last=True)

B.mc("Facial artery branch of :",
     "External Carotid Artery",
     [("Internal carotid artery", "The internal carotid artery has no branches in the neck.", "gives the ICA neck branches"),
      ("Subclavian artery", "The subclavian artery's branches are the vertebral, internal thoracic, thyrocervical, costocervical and dorsal scapular arteries.", "mixes subclavian and carotid branches"),
      ("Axillary artery", "The axillary artery is the continuation of the subclavian beyond the 1st rib.")],
     "The external carotid artery gives the superior thyroid, ascending pharyngeal, lingual, facial, occipital and posterior auricular arteries, then ends in the parotid gland as the maxillary and superficial temporal arteries. The internal carotid gives no branches in the neck.",
     N % 6, last=True)

B.join("anat-subclavian")
# typo fixed: "continuous of" -> "continuation of"
B.mc("Axillary Artery is a continuation of :",
     "Subclavian Artery",
     [("Radial artery", LIMB % "The radial artery"),
      ("Ulnar artery", LIMB % "The ulnar artery"),
      ("Femoral artery", LIMB % "The femoral artery")],
     "The subclavian artery arches laterally in the root of the neck and ends at the outer border of the 1st rib by becoming the axillary artery.",
     N % 8, last=True)

B.join("anat-neck-veins")
B.mc("Internal jugular Vein drains into :",
     "Brachiocephalic vein",
     [("Cephalic vein", LIMB % "The cephalic vein"),
      ("Basilic vein", LIMB % "The basilic vein"),
      ("Femoral vein", LIMB % "The femoral vein")],
     "The internal jugular vein begins as the continuation of the sigmoid sinus at the jugular foramen and ends by joining the subclavian vein to form the brachiocephalic vein.",
     N % 20, last=True)

B.join("anat-subclavian")
B.mc("Axillary artery is a continuation of which artery?",
     "Subclavian artery",
     [("Radial artery", LIMB % "The radial artery"),
      ("Ulnar artery", LIMB % "The ulnar artery"),
      ("Femoral artery", LIMB % "The femoral artery")],
     "The subclavian artery becomes the axillary artery at the outer border of the 1st rib. Note: this repeats question 10 of the same set; both are kept as uploaded.",
     N % 8, last=True)

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
