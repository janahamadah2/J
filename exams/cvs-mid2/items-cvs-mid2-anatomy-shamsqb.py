"""Shams Practices CVS MID-2 QB (past papers 2022-2025 + two unknown sets): Anatomy.

Only the questions NOT already in items-cvs-mid2-anatomy-shams.py live here; the 18
repeats are tagged with their papers in that file (PAPERS). Wording, options and key
are as printed; typos fixed only. Limb vessels are not in the uploaded Mid 2 slides.
"""
from _authoring import Bank

B = Bank("Anatomy")
NS = "Shams Practices QB, %s; not in your uploaded Mid 2 slides (answer from the bank's key)"

B.concept("anat-limb-vessels", "Upper and lower limb vessels (past papers)", [
    "The subclavian artery becomes the axillary artery at the outer border of the 1st rib.",
    "Axillary artery: the anterior circumflex humeral artery is one of its branches; the lateral thoracic artery comes from its 2nd part.",
    "The deep palmar arch is formed mainly by the radial artery, joined by the deep branch of the ulnar artery; the superficial palmar arch is formed mainly by the ulnar artery.",
    "The dorsalis pedis artery is the continuation of the anterior tibial artery.",
    "The cephalic vein drains into the axillary vein; the lesser (small) saphenous vein drains into the popliteal vein; blood tests are drawn from the median cubital vein.",
], "Shams Practices QB (past papers); not in your uploaded slides")

B.keyed("The deep palmar arch is formed by",
        ["Brachial artery", "Axillary artery", "Posterior interosseous artery", "Radial artery"], "d",
        "The deep palmar arch is formed mainly by the terminal part of the radial artery, completed by the deep branch of the ulnar artery. The superficial arch is the ulnar artery's arch. This limb-vessel topic is not in your uploaded Mid 2 slides; the answer follows the bank's key.",
        {"a": "The brachial artery is the artery of the arm; it divides into the radial and ulnar arteries at the elbow.",
         "b": "The axillary artery is the continuation of the subclavian artery in the axilla.",
         "c": "The posterior interosseous artery runs in the back of the forearm."},
        NS % "2024 May Q62")

B.keyed("The anterior circumflex humeral branch is a branch of",
        ["Axillary artery", "Radial artery", "Ulnar artery", "Common carotid artery"], "a",
        "The anterior and posterior circumflex humeral arteries are branches of the axillary artery, which continues the subclavian artery beyond the outer border of the 1st rib. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "The radial artery is a forearm branch of the brachial artery.",
         "c": "The ulnar artery is a forearm branch of the brachial artery.",
         "d": "The common carotid artery ends at the upper border of the thyroid cartilage by dividing into the external and internal carotids."},
        NS % "2024 May Q63")

B.keyed("Which of the following is from the 2nd part of axillary artery?",
        ["Superior thoracic artery", "Lateral thoracic artery", "Subscapular artery", "Posterior circumflex humeral artery"], "b",
        "Like the subclavian, the axillary artery is divided into three parts by a muscle crossing in front of it (pectoralis minor). The 2nd part gives the thoraco-acromial and lateral thoracic arteries. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The superior thoracic artery comes from the 1st part of the axillary artery.",
         "c": "The subscapular artery comes from the 3rd part of the axillary artery.",
         "d": "The posterior circumflex humeral artery comes from the 3rd part of the axillary artery."},
        NS % "2024 May Q65", labels={"a": "mixes up the parts of the axillary artery", "c": "mixes up the parts of the axillary artery", "d": "mixes up the parts of the axillary artery"})

B.keyed("Which of the following arteries forms the superficial palmar arch?",
        ["Anterior interosseous artery", "Posterior interosseous artery", "Profunda brachii artery", "Ulnar artery"], "d",
        "The superficial palmar arch is formed mainly by the ulnar artery; the deep arch mainly by the radial artery. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The anterior interosseous artery runs on the front of the interosseous membrane in the forearm.",
         "b": "The posterior interosseous artery runs in the back of the forearm.",
         "c": "The profunda brachii artery is the deep artery of the arm."},
        NS % "2024 May Q66", labels={"a": "mixes up the palmar arches"})

B.keyed("Which artery joins the deep branch of the ulnar artery to form the deep palmar arch?",
        ["Profunda brachii artery", "Radial Artery", "Superior thoracic artery", "Posterior circumflex humeral artery"], "b",
        "The radial artery forms the deep palmar arch and is completed by the deep branch of the ulnar artery. Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem lightly reworded from \"artery joins deep branch of ulnar artery to form Deep Palmar Arch\".)",
        {"a": "The profunda brachii artery is the deep artery of the arm.",
         "c": "The superior thoracic artery is a branch of the 1st part of the axillary artery.",
         "d": "The posterior circumflex humeral artery is a branch of the 3rd part of the axillary artery."},
        NS % "Unknown-1 Q138")

B.keyed("Blood for a blood test is usually drawn from:",
        ["Hepatic portal vein", "Pulmonary vein", "Median cubital vein", "Great cardiac vein"], "c",
        "Routine venipuncture uses the median cubital vein in front of the elbow, which links the cephalic and basilic veins. Not in your uploaded Mid 2 slides; answer from the bank's key. (Stem fixed from \"drain blood test from :\".)",
        {"a": "The hepatic portal vein carries blood from the gut to the liver and is not reachable for a blood test.",
         "b": "The pulmonary veins carry oxygenated blood from the lungs to the left atrium.",
         "d": "The great cardiac vein runs in the anterior interventricular groove with the LAD."},
        NS % "Unknown-1 Q139")

B.keyed("Ulnar and which artery join to form palmar arch?",
        ["Brachial artery", "Radial Artery", "Axillary artery", "Profunda brachii artery"], "b",
        "The palmar arches are formed by the two forearm arteries, radial and ulnar: superficial arch mainly ulnar, deep arch mainly radial. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The brachial artery divides into the radial and ulnar arteries at the elbow; it does not reach the hand.",
         "c": "The axillary artery is in the axilla, far above the hand.",
         "d": "The profunda brachii artery is the deep artery of the arm."},
        NS % "Unknown-2 Q159")

B.keyed("Dorsalis pedis is continuation of?",
        ["Posterior tibial artery", "Fibular artery", "Medial plantar artery", "Anterior Tibial"], "d",
        "The anterior tibial artery runs down the front of the leg and becomes the dorsalis pedis artery in front of the ankle. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The posterior tibial artery ends behind the medial malleolus by dividing into the plantar arteries.",
         "b": "The fibular (peroneal) artery is a branch of the posterior tibial artery.",
         "c": "The medial plantar artery is a terminal branch of the posterior tibial artery in the sole."},
        NS % "Unknown-2 Q160")

B.keyed("Cephalic vein drains to which vein?",
        ["Axillary vein", "Popliteal vein", "Internal jugular vein", "Great saphenous vein"], "a",
        "The cephalic vein runs up the lateral side of the arm and drains into the axillary vein. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"b": "The popliteal vein is behind the knee; it receives the lesser saphenous vein.",
         "c": "The internal jugular vein drains the head and neck and joins the subclavian vein.",
         "d": "The great saphenous vein is a superficial vein of the lower limb."},
        NS % "Unknown-2 Q161")

B.keyed("Lesser saphenous vein drains to which vein?",
        ["Axillary vein", "Internal jugular vein", "Popliteal vein", "Brachiocephalic vein"], "c",
        "The lesser (small) saphenous vein runs up the back of the leg and drains into the popliteal vein behind the knee. Not in your uploaded Mid 2 slides; answer from the bank's key.",
        {"a": "The axillary vein receives the cephalic vein from the upper limb.",
         "b": "The internal jugular vein drains the head and neck.",
         "d": "The brachiocephalic vein is formed by the internal jugular and subclavian veins."},
        NS % "Unknown-2 Q162")

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
