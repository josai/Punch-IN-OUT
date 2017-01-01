import os
from punchoutclasses import *
import sys


def program():
    """Runs the entire script start to finish."""
    settings = ALL_SETTINGS()
    in_building = get_list(settings.live_file_path, settings.active_list, 9999)
    count = 0
    while True:
        try:
            clear_console_screen()
            print_logs(in_building, settings)
            person = input_prompt(in_building, settings)
            in_building = update_lists(settings, person)
            count = count + 1
            #  Changes the mode back to default
            if count >= 8:
                settings.mode = 0
                count = 0
        except SystemExit:
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass


def get_list(a_path, a_list, max_length):
    """Returns a list of objects for each occupant in the building. As well
    as displays current list in the consol."""
    full_file_name = a_path + a_list
    text_file = open(full_file_name, "r")
    info = text_file.readlines()
    text_file.close()
    info.reverse()
    index = 0
    people = []
    for i in info:
        i = i.split()
        i = [i[2], i[3], i[4], i[1], i[0]]
        person = check()
        person.import_info(i)
        people.append(person)
        if index >= max_length:
            break
        index = index + 1
    people.reverse()
    return people


def clear_console_screen():
    """Clears console window of all text."""
    os.system('cls')


def print_logs(some_logs, settings):
    num_people = ("0" + str(len(some_logs)))[-2:]
    if settings.mode == 1:
        settings.generate_current_path()
        some_logs = get_list(settings.current_path, settings.file_name, 25)
    else:
        some_logs = some_logs[:25]
    top_field = (normalize_string("DATE", 0, 11) +
                 normalize_string("TIME", 0, 13) +
                 normalize_string("NAME", 0, 16) +
                 normalize_string("SURNAME", 0, 24) +
                 normalize_string("CHECKED", 0, 10)
                 )
    print_spaces(2)
    print normalize_string(top_field, 4, 72)
    print normalize_string(("-" * 72), 4, 72)
    for log in some_logs:
        print normalize_string(create_log_string(log), 4, 72)
    print normalize_string(("-" * 72), 4, 72)
    print normalize_string((num_people + " TOTAL IN"), 59, 16)
    print normalize_string(("-" * 72), 4, 72)
    print_spaces(2)


def normalize_string(a_string, int_space, max_length):
    """Define string length, makes sure a string is always within a maximum
    number of characters"""
    if int_space > 0:
        int_space = " " * int_space
    else:
        int_space = ""
    extra_space = (" " * max_length)
    return int_space + (a_string + extra_space)[:max_length]


def print_spaces(num):
    count = 0
    while count < num:
        print ""
        count = count + 1


def input_prompt(in_building, settings):
    """Controls the user input insuring that it is always valid. Otherwise it
    just continues to prompt the user for a valid answer."""
    valid_inputs = ["IN", "OUT"]
    print_spaces(1)
    error = normalize_string("ERROR: Last input was invalid...", 4, 72)
    mode_changed = normalize_string("MODE CHANGED", 4, 72)
    report = error
    while True:
        an_input = raw_input("    SCAN ID CARD: ")
        an_input = an_input.upper()
        if "MODE" == an_input:
            settings.change_mode()
            report = mode_changed
        elif "EXIT" == an_input:
            sys.exit()
        elif " " in an_input:
            an_input = an_input.split()
            an_input.reverse()
            if an_input[0] in valid_inputs:
                an_input = check_surname(an_input)
                person = check()
                person.import_info(an_input)
                return person
        clear_console_screen()
        print_logs(in_building, settings)
        print report
        report = error


def check_surname(a_name):
    """Checks the surname as well as rearranges the inputs for a proper
    import."""
    if len(a_name) < 3:
        a_name = [a_name[1], "(NO-SURNAME)", a_name[0]]
    else:
        a_name = [a_name[2], a_name[1], a_name[0]]
    return a_name


def update_lists(settings, a_log):
    path = settings.live_file_path
    active_file = settings.active_list
    log = create_log_string(a_log)
    settings.generate_current_path()
    save_data(settings.current_path, settings.file_name, [log], "a")
    building_occupants = get_list(path, active_file, 999999)
    building_occupants = update_live(building_occupants, a_log, settings)
    return building_occupants


def create_log_string(a_person):
    """Returns a normalized string from the "check" classe for printing in the
    console or for saving in a text file."""
    normal_string = (normalize_string(str(a_person.datetime)[:19], 0, 24) +
                     normalize_string(a_person.first_name, 0, 16) +
                     normalize_string(a_person.last_name, 0, 24) +
                     normalize_string(a_person.mark, 0, 7)
                     )
    return normal_string


def update_live(occupants, new_log, settings):
    """Updates the live list"""
    sett = settings
    list_for_file = []
    for person in occupants:
        person.update(sett)
        if person.full_name == new_log.full_name:
            occupants.remove(person)
            break
        elif person.time_in >= sett.expiration:
            occupants.remove(person)
            log_string = create_log_string(person)
            save_data(sett.current_path, sett.file_name, [log_string], "a")
    if new_log.mark == "IN":
        occupants.append(new_log)
    for i in occupants:
        new = create_log_string(i)
        list_for_file.append(new)
    save_data(sett.live_file_path, sett.active_list, list_for_file, "w")
    save_data(sett.backup_file_path, sett.active_list, list_for_file, "w")
    return occupants


def save_data(file_path, file_name, some_data, mode):
    """Saves data in folder and creates a new subfolder if it doesn't exist"""
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    full_file_name = file_path + file_name
    text_file = open(full_file_name, mode)
    for i in some_data:
        text_file.write(i)
        text_file.write("\n")
    text_file.close()


program()
