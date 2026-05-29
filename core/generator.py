import random
import json
import constrains


def subject_generator(subject_list):
    return random.choice(subject_list)

def teacher_assignment_per_subject(subject, teacher_list):
    return teacher_list[subject]

def generate_timetable():
    timetable_per_section = {}

    for section in sections:
        timetable = {}
        timetable_per_section[section] = {}

        for day in days:
            timetable[day] = {}

            for period in periods:
                while True:
                    subject = subject_generator(subjects)

                    if constrains.subject_limit(
                        timetable[day],
                        subject,
                        2
                    ):
                        teacher = teacher_assignment_per_subject(
                            subject,
                            teachers
                        )

                        timetable[day][period] = (
                            subject,
                            teacher
                        )
                        break

            timetable_per_section[section][day] = timetable[day]

    return timetable_per_section


def resolve_teacher_conflicts(timetable_per_section):
    conflict_counter = 0

    for day in days:
        for period in periods:

            teacher_seen = set()

            for section in sections:

                subject, teacher = timetable_per_section[
                    section
                ][day][period]

                if teacher in teacher_seen:

                    conflict_counter += 1

                    while True:

                        new_subject = subject_generator(subjects)

                        new_teacher = teacher_assignment_per_subject(
                            new_subject,
                            teachers
                        )

                        if (
                            constrains.subject_limit(
                                timetable_per_section[section][day],
                                new_subject,
                                2
                            )
                            and
                            new_teacher not in teacher_seen
                        ):

                            timetable_per_section[section][day][period] = (
                                new_subject,
                                new_teacher
                            )

                            teacher_seen.add(new_teacher)
                            conflict_counter -= 1
                            break

                else:
                    teacher_seen.add(teacher)

    print(f"Conflict counter: {conflict_counter}")


def print_timetable(timetable):
    for section, schedule in timetable.items():

        print(f"\n{'=' * 50}")
        print(section)
        print(f"{'=' * 50}")

        for day, period_data in schedule.items():
            print(day, period_data)


with open("../data/sample_data.json", "r") as file:
    sample_data = json.load(file)


subjects = sample_data["subjects"]

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

periods = ["P1","P2","P3","P4","P5","P6","P7","P8"]

sections = sample_data["Sections"]
teachers = sample_data["Teachers"]


timetable_per_section = generate_timetable()

resolve_teacher_conflicts(timetable_per_section)

print_timetable(timetable_per_section)