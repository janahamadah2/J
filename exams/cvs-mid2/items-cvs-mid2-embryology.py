from _authoring import Bank

B = Bank("Embryology")
L = "Embryology L3 slides (aortic arches)"

B.concept("emb-arches", "Formation and derivatives of the aortic arches", [
    "At the 4th week two primitive aortae appear, each with a ventral aorta, a dorsal aorta and a connecting segment; the ventral aortae fuse into the aortic sac with right and left horns.",
    "1st arch: disappears, remnant forms the maxillary arteries. 2nd arch: disappears, remnant forms the stapedial arteries. 5th arch: disappears completely.",
    "3rd arch: proximal parts form the common carotid arteries; distal parts join the dorsal aorta to form the internal carotid arteries. The external carotid is a new bud from the junction.",
    "Left 4th arch: part of the arch of the aorta between the left common carotid and left subclavian. Right 4th arch: proximal part of the right subclavian artery.",
    "6th arch: left proximal forms the left pulmonary artery and left distal forms the ductus arteriosus; right proximal forms the right pulmonary artery and right distal degenerates.",
], L)

B.mc("A nurse reviews the embryology of a child's head arteries. Which artery develops from the remaining part of the 1st aortic arch?",
     "Maxillary artery",
     [("Stapedial artery", "The stapedial artery is the remnant of the 2nd arch.", "mixes up the 1st and 2nd arches"),
      ("Common carotid artery", "The common carotid comes from the proximal part of the 3rd arch."),
      ("External carotid artery", "The external carotid is a new bud from the junction of the common and internal carotids.")],
     "The first two arch vessels largely disappear. The remaining part of the 1st arch forms the maxillary arteries and the remaining part of the 2nd arch forms the stapedial arteries. The 3rd arch gives the carotids, the 4th the aortic arch and right subclavian, and the 6th the pulmonary arteries and ductus arteriosus.",
     L)

B.match("A nurse reviews which adult vessels come from each aortic arch. Match each arch to its derivative.",
        [("3rd arch (proximal parts)", "Common carotid arteries"),
         ("Left 4th arch", "Arch of the aorta between the left common carotid and left subclavian"),
         ("Right 4th arch", "Proximal part of the right subclavian artery"),
         ("Left 6th arch (distal part)", "Ductus arteriosus")],
        [("Disappears completely", "The 5th arch vessel disappears completely.", "thinks the 5th arch persists")],
        "The 3rd arches form the common carotids (proximal parts) and, with the dorsal aorta, the internal carotids. The left 4th arch forms the part of the aortic arch between the left common carotid and left subclavian arteries, and the right 4th arch forms the proximal right subclavian. The 5th arch disappears. The left 6th arch forms the left pulmonary artery (proximal) and the ductus arteriosus (distal).",
        L,
        row_stems={
            "3rd arch (proximal parts)": "A nurse reviews the 3rd aortic arch. What do its proximal parts form?",
            "Left 4th arch": "A child has an anomaly of the left 4th aortic arch. Which adult vessel segment develops from it?",
            "Right 4th arch": "A nurse explains the right 4th aortic arch. Which adult vessel does it form?",
            "Left 6th arch (distal part)": "A newborn has a patent vessel formed from the distal left 6th arch. Which vessel is it?",
        })

B.mc("A student nurse asks what happens to the 5th aortic arch vessel. Which response is accurate?",
     "It disappears completely.",
     [("It forms the stapedial artery.", "The stapedial artery comes from the 2nd arch.", "mixes up the 2nd and 5th arches"),
      ("It forms the ductus arteriosus.", "The ductus arteriosus comes from the distal left 6th arch.", "mixes up the 5th and 6th arches"),
      ("It forms the right pulmonary artery.", "The right pulmonary artery comes from the proximal right 6th arch.")],
     "Of the six pairs of aortic arch vessels, the 1st and 2nd leave small remnants (maxillary and stapedial arteries), the 3rd, 4th and 6th form major vessels, and the 5th disappears completely.",
     L)

B.mc("A nurse explains the origin of a client's external carotid artery. How does the external carotid artery develop?",
     "As a new bud from the junction between the common and internal carotid arteries",
     [("From the distal part of the 3rd arch", "The distal 3rd arch joins the dorsal aorta to form the internal carotid.", "mixes up internal and external carotid origins"),
      ("From the remaining part of the 1st arch", "The 1st arch remnant forms the maxillary artery."),
      ("From the right horn of the aortic sac", "The right horn forms the brachiocephalic artery.")],
     "The 3rd arch's proximal parts form the common carotid arteries and its distal parts join the dorsal aorta to form the internal carotids. The external carotid artery is not an arch derivative: it arises as a newly formed bud from the junction between the common and internal carotid arteries.",
     L + ", slide note (N.B.)", last=True)

B.mc("During surgery to ligate a patent ductus arteriosus, which nerve should the nurse know is at risk because it hooks around the ductus?",
     "Left recurrent laryngeal nerve",
     [("Right recurrent laryngeal nerve", "The right recurrent laryngeal nerve hooks around the proximal right subclavian artery.", "mixes up the right and left recurrent laryngeal nerves"),
      ("Phrenic nerve", "The phrenic nerve is not described as hooking around any aortic arch derivative."),
      ("Vagus nerve trunk", "The nerves that hook around the arches are the recurrent laryngeal branches, not the vagal trunk.")],
     "The recurrent laryngeal nerves supply the 6th pharyngeal arches and hook around the 6th aortic arches. On the left, the distal 6th arch persists as the ductus arteriosus, so the left recurrent laryngeal nerve hooks around the ductus. On the right, the distal 6th arch degenerates, so the right nerve moves up and hooks around the proximal right subclavian artery (from the 4th arch).",
     L + ", slide note (N.B.)", last=True)

B.tf("A nurse states that the distal part of the right 6th aortic arch degenerates.", True,
     "True. On the right, the proximal 6th arch forms the right pulmonary artery and the distal part degenerates; on the left, the distal part persists as the ductus arteriosus.",
     L, "This statement is true: the distal right 6th arch degenerates.")

B.tf("A nurse states that the 5th aortic arch vessel disappears completely.", True,
     "True. The 5th arch vessel disappears completely; only the 1st and 2nd arches leave small remnants (maxillary and stapedial arteries) among those that regress.",
     L, "This statement is true: the 5th arch disappears completely.")

B.tf("A nurse states that the 2nd aortic arch persists as the maxillary artery.", False,
     "False. The remaining part of the 2nd arch forms the STAPEDIAL artery; the maxillary artery comes from the remaining part of the 1st arch.",
     L, "The 2nd arch gives the stapedial artery; the 1st gives the maxillary.", "mixes up the 1st and 2nd arches")

B.concept("emb-sac-dorsal", "Aortic sac, dorsal aorta and the origin of the great arteries", [
    "Aortic sac: arch of the aorta proximal to the brachiocephalic artery. Left horn: arch between the brachiocephalic and left common carotid. Right horn: brachiocephalic artery.",
    "Right dorsal aorta: cranial to the 3rd arch forms the distal internal carotid; at the 7th intersegmental artery forms the distal right subclavian; the rest degenerates.",
    "Left dorsal aorta: at the 7th intersegmental artery forms the subclavian; between the 4th and 6th arches forms the distal arch of the aorta; caudal to the 6th arch forms the descending thoracic and abdominal aorta.",
    "Arch of the aorta from proximal to distal: aortic sac, left horn, left 4th arch, left dorsal aorta between the 4th and 6th arches.",
], L)

B.order("A nurse traces the embryological origin of the arch of the aorta. Arrange its parts from proximal to distal by origin.",
        ["Aortic sac (up to the brachiocephalic artery)", "Left horn of the aortic sac (between brachiocephalic and left common carotid)",
         "Left 4th aortic arch (between left common carotid and left subclavian)", "Left dorsal aorta between the 4th and 6th arches (distal arch)"],
        "The arch of the aorta is built from four sources in sequence: the aortic sac forms the part proximal to the brachiocephalic artery, the left horn of the sac forms the part between the brachiocephalic and left common carotid, the left 4th arch forms the part between the left common carotid and left subclavian, and the left dorsal aorta between the 4th and 6th arches forms the distal part.",
        L, last=False)

B.blanks("A nurse completes an embryology review sheet. The brachiocephalic artery arises from the {1}; the left subclavian artery arises from the left dorsal aorta at the {2}; and the proximal part of the right subclavian artery arises from the {3}.",
         [("right horn of the aortic sac", [("left horn of the aortic sac", "The left horn forms the part of the arch between the brachiocephalic and left common carotid.", "mixes up right and left horns"),
                                            ("3rd aortic arch", "The 3rd arch forms the common and internal carotid arteries.")]),
          ("attachment of the 7th intersegmental artery", [("junction of the 3rd and 4th arches", "The left dorsal aorta between the 3rd and 4th arches disappears.", "places the subclavian at the 3rd-4th segment"),
                                                          ("region caudal to the 6th arch", "Caudal to the 6th arch, the left dorsal aorta forms the descending thoracic and abdominal aorta.")]),
          ("right 4th aortic arch", [("left 4th aortic arch", "The left 4th arch forms part of the arch of the aorta.", "mixes up right and left 4th arches"),
                                     ("right 6th aortic arch", "The right 6th arch forms the right pulmonary artery; its distal part degenerates.")])],
         "The slide's fill-in questions ask for these origins. The brachiocephalic artery comes from the right horn of the aortic sac. The internal carotids come from the distal 3rd arches plus the dorsal aorta cranial to the 3rd arch. The left subclavian forms from the left dorsal aorta at the attachment of the 7th intersegmental artery. The right subclavian has two parts: proximal from the right 4th arch and distal from the right dorsal aorta at the 7th intersegmental artery.",
         L + ", slide exercise (??? slide)", last=True)

B.tf("A nurse states that the left horn of the aortic sac forms the part of the aortic arch between the brachiocephalic and left common carotid arteries.", True,
     "True. The aortic sac forms the arch proximal to the brachiocephalic artery, the left horn forms the part between the brachiocephalic and left common carotid, and the right horn forms the brachiocephalic artery.",
     L, "This statement is true: the left horn forms that segment of the arch.")

B.tf("A nurse states that the right horn of the aortic sac forms the right common carotid artery.", False,
     "False. The right horn of the aortic sac forms the BRACHIOCEPHALIC artery. The common carotid arteries come from the proximal parts of the 3rd arches.",
     L, "The right horn forms the brachiocephalic artery.", "mixes up brachiocephalic and carotid origins")

B.mc("A nurse reviews the fate of the left dorsal aorta caudal to the 6th arch. Which adult vessels does this segment form?",
     "The descending thoracic and abdominal aorta",
     [("The distal part of the arch of the aorta", "The distal arch comes from the left dorsal aorta BETWEEN the 4th and 6th arches.", "shifts the dorsal aorta segments"),
      ("The left subclavian artery", "The left subclavian forms at the attachment of the 7th intersegmental artery."),
      ("The distal internal carotid artery", "The distal internal carotid comes from the dorsal aorta cranial to the 3rd arch.")],
     "Each segment of the left dorsal aorta has its own fate: cranial to the 3rd arch it forms the distal internal carotid, between the 3rd and 4th arches it disappears, at the 7th intersegmental artery it forms the subclavian, between the 4th and 6th arches it forms the distal arch, and caudal to the 6th arch it forms the descending thoracic and abdominal aorta. The common dorsal aorta forms the abdominal aorta and median sacral artery.",
     L)

B.concept("emb-anomalies", "Anomalies of the aortic arches", [
    "Patent ductus arteriosus: a patent duct between the left pulmonary artery and the arch of the aorta; associated with aortic stenosis, pulmonary stenosis and Fallot's tetralogy.",
    "Right arch of aorta: develops from the right dorsal aorta and right 4th arch.",
    "Double arch of aorta: persistence of the distal right dorsal aorta; a vascular ring around the trachea (dyspnea) and esophagus (dysphagia).",
    "Coarctation: constriction of the aorta distal to the left subclavian. Postductal: distal to the ductus, ductus usually closed. Preductal: proximal to the ductus, ductus open.",
], L)

B.mc("A newborn has a continuous connection between the left pulmonary artery and the arch of the aorta. Which associated conditions should the nurse watch for?",
     "Aortic stenosis, pulmonary stenosis or Fallot's tetralogy",
     [("A vascular ring around the trachea and esophagus", "A vascular ring is the feature of a double aortic arch.", "mixes up PDA and double arch"),
      ("Constriction of the aorta distal to the left subclavian", "That is coarctation of the aorta, a different anomaly."),
      ("Persistence of the distal right dorsal aorta", "That is the cause of a double aortic arch.")],
     "Patent ductus arteriosus means the ductus, formed from the distal left 6th arch, stays open, leaving a duct between the left pulmonary artery and the arch of the aorta. It is associated with other congenital heart disease such as aortic stenosis, pulmonary stenosis and Fallot's tetralogy.",
     L)

B.mc("An infant has noisy breathing and difficulty swallowing feeds, and imaging shows a vascular ring around the trachea and esophagus. Which anomaly should the nurse suspect?",
     "Double arch of the aorta",
     [("Right arch of the aorta", "A right arch forms from the right dorsal aorta and right 4th arch; a ring needs both arches to persist.", "mixes up right arch and double arch"),
      ("Patent ductus arteriosus", "PDA is an open duct between the left pulmonary artery and the aortic arch."),
      ("Coarctation of the aorta", "Coarctation is a constriction of the aorta distal to the left subclavian.")],
     "A double aortic arch results from persistence of the distal part of the right dorsal aorta, so a second arch joins the left one. The two arches form a vascular ring around the trachea, causing dyspnea, and the esophagus, causing dysphagia.",
     L)

B.mc("A client's imaging shows a right-sided arch of the aorta. Which developmental cause should the nurse identify?",
     "The arch developed from the right dorsal aorta and the right 4th aortic arch.",
     [("The distal right dorsal aorta persisted alongside a normal left arch.", "Persistence of the distal right dorsal aorta with the left arch gives a DOUBLE arch.", "mixes up right arch and double arch"),
      ("The ductus arteriosus failed to close.", "A ductus that fails to close is a patent ductus arteriosus."),
      ("The 5th arch persisted.", "The 5th arch vessel normally disappears completely and is not given as a cause of any listed anomaly.")],
     "Normally the left 4th arch and left dorsal aorta form the arch of the aorta. In a right arch of the aorta, the arch instead develops from the right dorsal aorta and the right 4th aortic arch vessel.",
     L)

B.mc("A client's imaging shows a constriction of the aorta proximal to the entrance of the ductus arteriosus, with the ductus still open. How should this coarctation be classified?",
     "Preductal coarctation",
     [("Postductal coarctation", "Postductal coarctation lies DISTAL to the ductus, which is usually closed.", "mixes up preductal and postductal"),
      ("Double arch of the aorta", "A double arch is a vascular ring, not a constriction."),
      ("Patent ductus arteriosus alone", "The ductus is open here, but the defining lesion is the constriction proximal to it.")],
     "Coarctation is a constriction of the aorta distal to the origin of the left subclavian artery. In the preductal type the constriction is proximal to the entrance of the ductus arteriosus and the ductus stays open. In the postductal type the constriction is distal to the ductus, which is usually closed. Note: the slide labels preductal as \"Adult\" and postductal as \"fetal\" (and notes the closed duct as fatal); many references label them the other way round (preductal as infantile, postductal as adult), so check which label your instructor expects.",
     L)

B.tf("A nurse states that coarctation of the aorta is a constriction proximal to the origin of the left subclavian artery.", False,
     "False. Coarctation of the aorta is a constriction DISTAL to the origin of the left subclavian artery, either before (preductal) or after (postductal) the entrance of the ductus arteriosus.",
     L, "Coarctation lies distal to the left subclavian origin.", "places coarctation proximal to the left subclavian")

B.concept("emb-veins", "Development of the veins", [
    "At the 5th week each horn of the sinus venosus receives the umbilical, vitelline and common cardinal veins.",
    "Vitelline veins form the portal and superior mesenteric veins. After birth the ductus venosus becomes the ligamentum venosum and the left umbilical vein the ligamentum teres.",
    "Right common cardinal vein: SVC inside the pericardium. Left common cardinal vein: oblique vein of the left atrium.",
    "Right anterior cardinal: SVC outside the pericardium, right brachiocephalic and right internal jugular veins. Left anterior cardinal: left superior intercostal, left brachiocephalic and left internal jugular veins.",
    "Posterior cardinal veins: IVC, common iliac, suprarenal, testicular or ovarian, and renal veins.",
], L)

B.fill("A nurse reviews the timeline of vascular development. The veins that drain into the horns of the sinus venosus develop at the ____ week.",
       "5th",
       [("4th", "The 4th week is when the two primitive aortae (arterial system) appear.", "mixes up arterial and venous timing"),
        ("8th", "The 8th week is not the time given for venous development.")],
       "The arterial system starts at the 4th week, when the two primitive aortae appear. The veins develop at the 5th week, when each horn of the sinus venosus receives an umbilical, a vitelline and a common cardinal vein.",
       L)

B.tf("A nurse states that the vitelline veins form the inferior vena cava.", False,
     "False. The vitelline veins form the portal and superior mesenteric veins. The inferior vena cava develops from the posterior cardinal veins.",
     L, "Vitelline veins form the portal and superior mesenteric veins; the IVC is posterior cardinal.", "mixes up vitelline and cardinal derivatives")

B.tf("A nurse states that the inferior vena cava develops from the posterior cardinal veins.", True,
     "True. The posterior cardinal veins give the inferior vena cava, the common iliac, suprarenal, testicular or ovarian and renal veins.",
     L, "This statement is true: the IVC is a posterior cardinal derivative.")

B.match("A nurse reviews the fate of the embryonic veins. Match each embryonic vein to its adult derivative.",
        [("Vitelline veins", "Portal and superior mesenteric veins"),
         ("Ductus venosus (after birth)", "Ligamentum venosum"),
         ("Left umbilical vein (after birth)", "Ligamentum teres"),
         ("Left common cardinal vein", "Oblique vein of the left atrium")],
        [("Inferior vena cava", "The IVC comes from the posterior cardinal veins.", "mixes up cardinal vein derivatives")],
        "Vitelline veins form the portal and superior mesenteric veins. After birth the ductus venosus closes to form the ligamentum venosum and the obliterated left umbilical vein forms the ligamentum teres. The common cardinal veins differ by side: the right forms the SVC inside the pericardium and the left forms the oblique vein of the left atrium.",
        L,
        row_stems={
            "Vitelline veins": "A nurse reviews the vitelline veins. Which adult veins do they form?",
            "Ductus venosus (after birth)": "After birth the ductus venosus closes. Which adult structure does it form?",
            "Left umbilical vein (after birth)": "After birth the left umbilical vein is obliterated. Which adult structure does it form?",
            "Left common cardinal vein": "A nurse traces the left common cardinal vein. Which adult vein does it form?",
        })

B.sata("A nurse reviews the derivatives of the posterior cardinal veins. Which adult veins develop from them?",
       ["Inferior vena cava", "Common iliac veins", "Renal veins", "Testicular or ovarian veins", "Suprarenal veins"],
       [("Portal vein", "The portal vein comes from the vitelline veins.", "mixes up vitelline and cardinal derivatives"),
        ("Left brachiocephalic vein", "The left brachiocephalic vein comes from the left ANTERIOR cardinal vein.", "mixes up anterior and posterior cardinal veins"),
        ("Right internal jugular vein", "The right internal jugular comes from the right ANTERIOR cardinal vein.", "mixes up anterior and posterior cardinal veins")],
       "The cardinal veins are the main venous drainage of the fetus. The anterior cardinals drain the upper body and form the SVC (outside the pericardium), the brachiocephalic and internal jugular veins and the left superior intercostal vein. The posterior cardinals drain the lower body and form the IVC, common iliac, suprarenal, testicular or ovarian and renal veins.",
       L)

ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC = B.export()
