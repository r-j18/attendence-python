import logic 
import rw
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("subject")
    parser.add_argument("command")
    args = parser.parse_args()

    subject_list = []
    try:
        subject_list = rw.read()
    except ValueError as e:
        print(e)
        return
    except TypeError as f:
        print(f)
        return
    except KeyError:
        print("Typoooo")
        return

    
    try:
        if(args.command == "present"):
            print(logic.mark_p(subject_list, args.subject))

        elif(args.command == "absent"):
            print(logic.mark_a(subject_list, args.subject))

        elif(args.command == "show"):
            print(logic.show_perc(subject_list, args.subject))

        elif(args.command == "add"):
            subject_list = logic.add_subject(subject_list, args.subject)
            print("Subject added")

        elif(args.command == "rem"):
            subject_list = logic.rem_subject(subject_list, args.subject)
            print("Subject removed")

        else:
            print("Opps looks like a typo")

        try:
            rw.write(subject_list)
        except:
            print("Failed to save")
    except ValueError as e:
        print(e)
    

