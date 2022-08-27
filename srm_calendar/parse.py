#!/usr/bin/env python3
import csv
import math
import pandas as pd
from datetime import datetime
import srm_calendar.sched as sched

tables = pd.read_html("calendar.html")
# breakpoint()
semsched = tables[1]
months = len(semsched.columns)

mn_sched = list()
for i,m in enumerate(range(0, months, 5)):
    # this_m = semsched.iloc[:,m:(m+4)]
    # this_m.rename(columns={this_m.columns[0]: "dt", this_m.columns[1]: "dow", this_m.columns[3]: "do"})
    mn_sched.append(semsched.iloc[:,m:(m+4)])

# print(mn_sched[0])
with open("events.csv","w", newline="") as eventsfile:
    fieldnames = ["subject", "start date", "end date", "start time", "end time", "location"]
    writer = csv.DictWriter(eventsfile, fieldnames)
    writer.writeheader()

    for month in range(len(mn_sched)):
    # for month in range(1):
        for _,day in mn_sched[month].iterrows():
            if math.isnan(day[0]):
                continue
            if day[3] == "-":
                continue
            fday = datetime.date(datetime.strptime(f"{int(day[0])} {mn_sched[month].columns[2]}", "%d %b '%y")).isoformat()
            do = day[3]
            # breakpoint()
            writer.writerows(sched.add_do(sched.tt, int(do), fday))
