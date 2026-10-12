import json
from classes import Subject

DATA_PATH = "data/data.json"

def read():

    try :
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    
    subject_list = []
    for sub in data:
        instance = Subject(sub["name"], sub['present'], sub["absent"])
        subject_list.append(instance)

    return subject_list

def write(subject_list):

    data = []
    for instance in subject_list:
        sub_class = {"name": instance.name, "present": instance.present, "absent": instance.absent}
        data.append(sub_class)

    with open(DATA_PATH, "w") as f:
        json.dump(data, f)

