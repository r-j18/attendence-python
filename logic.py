from classes import Subject

def find_subject(subjects, target ):
    for s in subjects:
        if s.name.lower() == target.lower():
            return s
    return None

def mark_p(subjects, subject):
    found = find_subject(subjects, subject)
    if found is None:
        raise ValueError("Subject not found")
    found.mark_present()
    return found.percentage()

def mark_a(subjects, subject):
    found = find_subject(subjects, subject)
    if found is None:
        raise ValueError("Subject not found")   
    found.mark_absent()
    return found.percentage()

def show_perc(subjects, subject):
    found = find_subject(subjects, subject)
    if found is None:
        raise ValueError("Subject not found")   
    return found.percentage()

def add_subject(subjects, new_sub, new_pre = 0, new_ab = 0):
    if find_subject(subjects,new_sub) is None:
        new = Subject(new_sub, new_pre, new_ab)
        new_subjects = subjects.copy()
        new_subjects.append(new)
        return new_subjects
    raise ValueError("Subject Already Exists")

def rem_subject(subjects, to_rem):
    found = find_subject(subjects, to_rem)
    if  found is not None:
        new_subjects = subjects.copy()
        new_subjects.remove(found)
        return new_subjects
    raise ValueError("Subject not found")