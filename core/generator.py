import random
import json
import constrains

with open('../data/sample_data.json', "r") as a:
    sample_data = json.load(a)

subjects = sample_data['subjects']

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
periods = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]

timetable = {}

for i in days:
    timetable[i] = {}
    for j in periods:
        while True:
            r1 = random.choice(subjects)
            if constrains.subject_limit(timetable[i],r1, 2):
                timetable[i][j] = r1
                break

for i in timetable.items():
    print(i)
