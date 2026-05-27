class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

class Subject:
    def __init__(self, name, max_periods):
        self.name = name
        self.max_period = max_periods

class SchoolClass:
    def __init__(self, class_name, sections, subjects, vocational_subjects, periods_per_day, working_day ):
        self.class_name = class_name
        self.sections = sections
        self.subjects = subjects
        self.vocational_subjects = vocational_subjects
        self.periods_per_day = periods_per_day
        self.working_day = working_day

class Section:
    def __init__(self, class_name, subjects, teachers):
        self.class_name = class_name
        self.subjects = subjects
        self.teachers = teachers

class Period:
    def __init__(self, period_number, start_time, end_time):
        self.period_number = period_number
        self.start_time = start_time
        self.end_time = end_time

class Timetable:
    def __init__(self, section, schedule):
        self.section = section
        self.schedule = schedule