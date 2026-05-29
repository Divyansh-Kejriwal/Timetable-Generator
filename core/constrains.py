def subject_limit(day_schedule, subject, max_limit):
    count = 0
    for sub_tuple in day_schedule.values():
        for sub in sub_tuple:
            if subject == sub:
                count += 1

    if count >= max_limit:
        return False
    else:
        return True
            