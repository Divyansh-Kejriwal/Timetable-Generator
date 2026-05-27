import random
import json

with open('../data/sample_data.json', "r") as a:
    sample_data = json.load(a)

subjects = sample_data['subjects']

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["P1", "P2", "P3", "P4", "P5"]

timetable = {}

for i in days:
    timetable[i] = {}
    for j in periods:
      r1 = random.choice(subjects)
      Count =0
      for subject in timetable[i].values():
          if subject == r1:
              Count += 1
      if Count >= 2:
          r1 = random.choice(subjects)
      else:
          timetable[i][j] = r1
for i in timetable.items():
    print(i)
