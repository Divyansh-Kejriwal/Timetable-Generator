import random
import json
import constrains

def subject_generator(subject_list):
    r1 = random.choice(subject_list)
    return r1

def teacher_assignment_per_subject(subject, teacher_list):
    for sub, teacher in teacher_list.items():
        if sub == subject:
            return teacher

def print_timetable(timetable):
    for section, schedule in timetable.items():
        print(section)
        for day, period in schedule.items():
            print(day, period)

with open('../data/sample_data.json', "r") as a:
    sample_data = json.load(a)

subjects = sample_data['subjects']

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
periods = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
sections = sample_data['Sections']
teachers = sample_data['Teachers']

timetable_per_section = {}

for i in sections:
    timetable = {}
    timetable_per_section[i] = {}
    for j in days:
        timetable[j] = {}
        for k in periods:
            while True:
                r1 = subject_generator(subjects)
                if constrains.subject_limit(timetable[j],r1, 2):
                    teacher = teacher_assignment_per_subject(r1, teachers)
                    timetable[j][k] = (r1, teacher)

                    break
        timetable_per_section[i][j] = timetable[j]

for day in days:
    for period in periods:
        teacher_seen = set()
        for section in sections:
            subject, teacher = timetable_per_section[section][day][period]
            if teacher in teacher_seen:
                a = subject_generator(subjects)
                timetable_per_section[section][day][period] = (a, teacher_assignment_per_subject(a, teachers))

                if constrains.subject_limit(timetable_per_section[section],a, 2 ):
                    t = teacher_assignment_per_subject(a, teachers)
                    timetable_per_section[section][day][period] = (a, t)
            else:
                teacher_seen.add(teacher)

print_timetable(timetable_per_section)
