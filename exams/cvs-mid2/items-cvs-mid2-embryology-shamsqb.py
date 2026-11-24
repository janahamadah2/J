"""Shams Practices CVS MID-2 QB (past papers): Embryology. Wording, options and key as printed (typos fixed)."""
from _authoring import Bank

B = Bank("Embryology")
SL = "Shams Practices QB, %s; Embryology L3 slides"
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"

B.join("emb-arches")
B.keyed("Which embryonic aortic arch gives rise to the proximal part of the right subclavian artery?",
        ["Left second aortic arch", "Right fourth aortic arch", "Left sixth aortic arch", "Right first aortic arch"], "b",
        "The right 4th aortic arch forms the proximal part of the right subclavian artery; the distal part comes from the right dorsal aorta at the 7th intersegmental artery. The left 4th arch instead forms part of the arch of the aorta.",
        {"a": "The 2nd arch largely disappears; its remnant forms the stapedial artery.",
         "c": "The left 6th arch forms the left pulmonary artery and the ductus arteriosus.",
         "d": "The 1st arch largely disappears; its remnant forms the maxillary artery."},
        SL % "2025 Q11", labels={"c": "mixes up the 4th and 6th arches"})

B.keyed("Which aortic arch vessel gives a part of the arch of aorta?",
        ["Right 1st arch", "Left 4th arch", "Left 2nd arch", "Right 6th arch"], "b",
        "The left 4th aortic arch forms the part of the arch of the aorta between the left common carotid and left subclavian arteries. The rest of the arch comes from the aortic sac, its left horn and the left dorsal aorta.",
        {"a": "The 1st arch leaves only the maxillary artery.",
         "c": "The 2nd arch leaves only the stapedial artery.",
         "d": "The right 6th arch forms the right pulmonary artery; its distal part degenerates."},
        SL % "2024 Nov Q35", labels={"d": "mixes up the 4th and 6th arches"})

B.keyed("Origin of common carotid?",
        ["1st aortic arch", "2nd aortic arch", "3rd aortic arch", "6th aortic arch"], "c",
        "The proximal parts of the 3rd aortic arches form the common carotid arteries; their distal parts join the dorsal aorta to form the internal carotids.",
        {"a": "The 1st arch remnant forms the maxillary artery.",
         "b": "The 2nd arch remnant forms the stapedial artery.",
         "d": "The 6th arch forms the pulmonary arteries and the ductus arteriosus."},
        SL % "2024 May Q72")

B.keyed("The origin of brachiocephalic artery?",
        ["Left horn of the aortic sac", "Right horn of the aortic sac", "Right seventh intersegmental artery", "Left sixth aortic arch"], "b",
        "The right horn of the aortic sac forms the brachiocephalic artery; the left horn forms the part of the aortic arch between the brachiocephalic and left common carotid arteries.",
        {"a": "The left horn forms part of the arch of the aorta.",
         "c": "The right 7th intersegmental artery contributes to the distal right subclavian artery.",
         "d": "The left 6th arch forms the left pulmonary artery and ductus arteriosus."},
        SL % "2023 Q95", labels={"a": "mixes up right and left horns"})

B.keyed("Ductus arteriosus arises from?",
        ["1st arch", "2nd arch", "3rd arch", "6th arch"], "d",
        "The distal part of the left 6th aortic arch forms the ductus arteriosus; its proximal part forms the left pulmonary artery. (Stem fixed from \"( In case ) ductus areriosus from ?\".)",
        {"a": "The 1st arch remnant forms the maxillary artery.",
         "b": "The 2nd arch remnant forms the stapedial artery.",
         "c": "The 3rd arch forms the common and internal carotid arteries."},
        SL % "2023 Q96")

B.join("emb-anomalies")
B.keyed("Patient came with difficulty in swallowing (dysphagia) and breathing (dyspnea); an X-ray shows that the right dorsal aorta is not degenerated. What is the anomaly?",
        ["Patent ductus arteriosus", "Coarctation of the aorta", "Persistent truncus arteriosus", "Double aortic arch"], "d",
        "Persistence of the distal part of the right dorsal aorta gives a second arch, a double aortic arch. The two arches form a vascular ring around the trachea (dyspnea) and esophagus (dysphagia).",
        {"a": "PDA is a duct left open between the left pulmonary artery and the aortic arch.",
         "b": "Coarctation is a constriction of the aorta distal to the left subclavian.",
         "c": "Persistent truncus arteriosus is not among the arch anomalies on your slides; it is a failure of the outflow tract to divide."},
        SL % "2024 Nov Q36")

B.keyed("Case: constriction of the aorta distal to the ductus arteriosus in a fetus. What is it?",
        ["Postductal coarctation", "Preductal coarctation", "Double aortic arch", "Persistent truncus arteriosus"], "a",
        "A constriction distal to the ductus arteriosus is postductal coarctation; on your slide it is labelled \"fetal\", with the ductus usually closed. Note: many references call the postductal type the adult type; the bank and your slide both use \"fetal\".",
        {"b": "Preductal coarctation lies proximal to the entrance of the ductus, which stays open.",
         "c": "A double arch is a vascular ring, not a constriction.",
         "d": "Persistent truncus arteriosus is a failure of the outflow tract to divide, not a constriction."},
        SL % "2024 May Q73", labels={"b": "mixes up preductal and postductal"})

B.concept("emb-past", "Other embryology from past papers", [
    "The septum intermedium forms by fusion of the endocardial cushions and divides the common atrioventricular canal into right and left channels.",
    "After birth the umbilical arteries become the medial umbilical ligaments; the left umbilical vein becomes the ligamentum teres.",
], "Shams Practices QB (past papers); partly in Embryology L3 slides")

B.keyed("Which embryonic vessels give rise to the medial umbilical ligaments after birth?",
        ["Umbilical veins", "Vitelline arteries", "Umbilical arteries", "Cardinal veins"], "c",
        "After birth the umbilical arteries are obliterated and become the medial umbilical ligaments. Your slides cover only the veins: the left umbilical vein becomes the ligamentum teres and the ductus venosus the ligamentum venosum. The artery fact is from the bank's key.",
        {"a": "The left umbilical vein becomes the ligamentum teres.",
         "b": "Vitelline arteries supply the yolk sac and form gut arteries, not the umbilical ligaments.",
         "d": "Cardinal veins form the systemic veins, such as the SVC and IVC."},
        NS % "2025 Q12", labels={"a": "mixes up umbilical arteries and veins"})

B.keyed("Which structure normally forms by fusion of the endocardial cushions to divide the common atrioventricular canal into right and left channels?",
        ["Septum intermedium", "Septum secundum", "Truncus arteriosus", "Sinus venosus"], "a",
        "The endocardial cushions fuse to form the septum intermedium, which divides the common atrioventricular canal into right and left channels. This heart-septation topic is not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "The septum secundum is part of the interatrial septum, beside the foramen ovale.",
         "c": "The truncus arteriosus is the outflow tract that divides into the aorta and pulmonary trunk.",
         "d": "The sinus venosus receives the umbilical, vitelline and common cardinal veins."},
        NS % "2025 Q13")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
