#!/usr/bin/env python3
from collections import namedtuple
from functools import partial

Slot = namedtuple("Slot", ["do", "start", "to", "place", "subject"])

def add_event(slot, day):
    return {"subject": slot.subject, "start date": day, "end date": day, "start time": slot.start,
            "end time": slot.to, "location": slot.place}
def add_do(tt, do, day):
    return [add_event(s, day) for s in filter(lambda s: s.do == do, tt)]


comp_org = partial(Slot, subject="Computer Organization", place="TP205")
lab_comp_org = partial(Slot, subject="[Lab] Computer Organization", place="TP003")
maths = partial(Slot, subject="Maths", place="TP205")
dsa = partial(Slot,subject="Data Structures and Algorithms", place="TP205")
lab_dsa = partial(Slot, subject="[Lab] Data Structures and Algorithms", place="TP017")
ood = partial(Slot,subject="Object Oriented Design", place="TP205")
lab_ood = partial(Slot,subject="[Lab] Object Oriented Design", place="TP1515")
mgmt = partial(Slot,subject="Management Principles", place="TP205")
sskills = partial(Slot,subject="Social Skills", place="TP205")
ade = partial(Slot,subject="Analog and Digital Electronics", place="TP205")
lab_ade = partial(Slot,subject="[Lab] Analog and Digital Electronics", place="TP017")
bio = partial(Slot,subject="Biology", place="TP205")

tt = [
    lab_comp_org(do=1, start="8:00",to="9:40"),
    maths(do=1, start="12:30", to="14:15"),
    dsa(do=1, start="14:20",to="16:05"),
    ood(do=1, start="16:05",to="16:55"),

    mgmt(do=2, start="8:00", to="9:40"),
    ood(do=2, start="9:45", to="11:30"),
    maths(do=2, start="11:35", to="12:25"),
    lab_ade(do=2, start="13:25", to="15:10"),

    lab_dsa(do=3, start="8:00", to="9:45"),
    ade(do=3, start="12:30", to="14:15"),
    maths(do=3,start="14:20",to="15:10"),
    comp_org(3, "15:15", "16:05"),
    sskills(3, "16:05", "16:55"),

    comp_org(4, "8:00", "9:40"),
    sskills(4, "9:45", "10:35"),

    lab_ood(5, "8:00", "9:40"),
    bio(5, "12:30", "14:15"),
    ade(5, "14:20", "15:10"),
    dsa(5, "15:15", "16:05"),
    comp_org(5, "16:05", "16:55")
]
