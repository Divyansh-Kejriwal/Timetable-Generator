import random
import json
import constrains

with open('../data/sample_data.json', "r") as a:
    sample_data = json.load(a)

subjects = sample_data['subjects']

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
periods = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
sections = ["11A", "11B", "11C"]


timetable_per_section = {}
for i in sections:
    timetable = {}
    timetable_per_section[i] = {}
    for j in days:
        timetable[j] = {}
        for k in periods:
            while True:
                r1 = random.choice(subjects)
                if constrains.subject_limit(timetable[j],r1, 2):
                    timetable[j][k] = r1
                    break
        timetable_per_section[i][j] = timetable[j]


for section, schedule in timetable_per_section.items():
    print(section)
    for day, period in schedule.items():
        print(day, period)
