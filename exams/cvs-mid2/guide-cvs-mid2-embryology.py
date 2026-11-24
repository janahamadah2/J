"""Mastery Study Guide part: Embryology.

SECTIONS: one section per concept, in lecture order. "key" holds the Key ideas box;
every fact on a linked concept card must appear in its section (build-guide checks).
PROSE fills mechanism, priority actions, patient example, trap, memory trick and
tap-to-reveal blanks ([[answer]])."""

SECTIONS = [
    {"id": "emb-arches", "unit": "Embryology", "title": "Formation and derivatives of the aortic arches", "source": "Embryology L3 slides (aortic arches)",
     "key": [
         "At the 4th week two primitive aortae appear, each with a ventral aorta, a dorsal aorta and a connecting segment; the ventral aortae fuse into the aortic sac with right and left horns.",
         "1st arch: disappears, remnant forms the maxillary arteries. 2nd arch: disappears, remnant forms the stapedial arteries. 5th arch: disappears completely.",
         "3rd arch: proximal parts form the common carotid arteries; distal parts join the dorsal aorta to form the internal carotid arteries. The external carotid is a new bud from the junction.",
         "Left 4th arch: part of the arch of the aorta between the left common carotid and left subclavian. Right 4th arch: proximal part of the right subclavian artery.",
         "6th arch: left proximal forms the left pulmonary artery and left distal forms the ductus arteriosus; right proximal forms the right pulmonary artery and right distal degenerates.",
     ]},
    {"id": "emb-sac-dorsal", "unit": "Embryology", "title": "Aortic sac, dorsal aorta and the origin of the great arteries", "source": "Embryology L3 slides (aortic arches)",
     "key": [
         "Aortic sac: arch of the aorta proximal to the brachiocephalic artery. Left horn: arch between the brachiocephalic and left common carotid. Right horn: brachiocephalic artery.",
         "Right dorsal aorta: cranial to the 3rd arch forms the distal internal carotid; at the 7th intersegmental artery forms the distal right subclavian; the rest degenerates.",
         "Left dorsal aorta: at the 7th intersegmental artery forms the subclavian; between the 4th and 6th arches forms the distal arch of the aorta; caudal to the 6th arch forms the descending thoracic and abdominal aorta.",
         "Arch of the aorta from proximal to distal: aortic sac, left horn, left 4th arch, left dorsal aorta between the 4th and 6th arches.",
     ]},
    {"id": "emb-anomalies", "unit": "Embryology", "title": "Anomalies of the aortic arches", "source": "Embryology L3 slides (aortic arches)",
     "key": [
         "Patent ductus arteriosus: a patent duct between the left pulmonary artery and the arch of the aorta; associated with aortic stenosis, pulmonary stenosis and Fallot's tetralogy.",
         "Right arch of aorta: develops from the right dorsal aorta and right 4th arch.",
         "Double arch of aorta: persistence of the distal right dorsal aorta; a vascular ring around the trachea (dyspnea) and esophagus (dysphagia).",
         "Coarctation: constriction of the aorta distal to the left subclavian. Postductal: distal to the ductus, ductus usually closed. Preductal: proximal to the ductus, ductus open.",
     ]},
    {"id": "emb-veins", "unit": "Embryology", "title": "Development of the veins", "source": "Embryology L3 slides (aortic arches)",
     "key": [
         "At the 5th week each horn of the sinus venosus receives the umbilical, vitelline and common cardinal veins.",
         "Vitelline veins form the portal and superior mesenteric veins. After birth the ductus venosus becomes the ligamentum venosum and the left umbilical vein the ligamentum teres.",
         "Right common cardinal vein: SVC inside the pericardium. Left common cardinal vein: oblique vein of the left atrium.",
         "Right anterior cardinal: SVC outside the pericardium, right brachiocephalic and right internal jugular veins. Left anterior cardinal: left superior intercostal, left brachiocephalic and left internal jugular veins.",
         "Posterior cardinal veins: IVC, common iliac, suprarenal, testicular or ovarian, and renal veins.",
     ]},
]
PROSE = {
"emb-arches": dict(
    mechanism="In the 4th week, paired aortic arch vessels link the aortic sac to the dorsal aortae. Some disappear and others are remodeled into the adult great arteries; the recurrent laryngeal nerves hook around the 6th arches, so their adult course depends on which arch segments survive.",
    actions=["Memorize arch by arch: 1 maxillary, 2 stapedial, 3 carotids, 4 aortic arch (left) and right subclavian (right), 5 none, 6 pulmonary arteries and ductus.",
             "Protect the left recurrent laryngeal nerve during ductus surgery."],
    example="During PDA ligation, the left recurrent laryngeal nerve is at risk because it hooks around the ductus.",
    trap="Mixing up the 1st (maxillary) and 2nd (stapedial) arch remnants.",
    trick="1-2 small leftovers, 3 Carotid (C is the 3rd letter), 4 Systemic (aorta, subclavian), 5 gone, 6 Pulmonary.",
    blanks=["The right recurrent laryngeal nerve hooks around the proximal part of the right [[subclavian]] artery.",
            "The distal part of the left 6th arch forms the [[ductus arteriosus]]."]),
"emb-sac-dorsal": dict(
    mechanism="The aortic sac, its horns and the dorsal aortae each contribute a segment to the adult vessels. Reading the arch of the aorta from proximal to distal walks through sac, left horn, left 4th arch and left dorsal aorta.",
    actions=["Answer origin questions by locating the segment first: brachiocephalic = right horn; left subclavian = 7th intersegmental artery; right subclavian = right 4th arch + right dorsal aorta at the 7th intersegmental."],
    example="A review sheet asks for the origin of the brachiocephalic artery: the right horn of the aortic sac.",
    trap="Giving the common carotid to the right horn.",
    trick="Right horn = brachiocephalic; left horn = the bit of arch next to it.",
    blanks=["The common dorsal aorta forms the abdominal aorta and the [[median sacral]] artery."]),
"emb-anomalies": dict(
    mechanism="Each anomaly is a normal step that failed: the ductus did not close (PDA), the right side persisted instead of the left (right arch), both persisted (double arch, a ring), or a segment narrowed (coarctation).",
    actions=["Suspect a double arch in an infant with dyspnea and dysphagia.",
             "Classify coarctation by where it sits relative to the ductus."],
    example="An infant with stridor and feeding difficulty has a vascular ring: double aortic arch.",
    trap="Mixing up right arch (one arch on the wrong side) with double arch (two arches).",
    trick="PRE-ductal: before the duct, duct oPEN.",
    blanks=["A patent ductus connects the left pulmonary artery to the [[arch of the aorta]]."]),
"emb-veins": dict(
    mechanism="At the 5th week three pairs of veins (umbilical, vitelline, cardinal) drain into the sinus venosus. Vitelline veins build the gut's venous drainage, umbilical veins become ligaments after birth, and the cardinal veins become the systemic veins.",
    actions=["Sort derivatives by vein: vitelline = portal and SMV; anterior cardinal = upper body; posterior cardinal = IVC and lower body veins."],
    example="A nurse traces the ligamentum teres back to the obliterated left umbilical vein.",
    trap="Giving the IVC to the vitelline veins.",
    trick="Vitelline = Viscera; Anterior cardinal = Above; Posterior cardinal = below.",
    blanks=["The cardinal veins are the main venous drainage of the [[fetus]]."]),
}
for _s in SECTIONS:
    _s.update(PROSE[_s["id"]])
