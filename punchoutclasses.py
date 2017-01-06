from datetime import *


class ALL_SETTINGS(object):
    """Determines the settings for this session."""
    def __init__(self):
        all_settings = import_settings()
        self.main_file_path = remove_underscore(all_settings[9][0])
        self.live_file_path = remove_underscore(all_settings[11][0])
        self.backup_file_path = remove_underscore(all_settings[13][0])
        self.file_ext = remove_underscore(all_settings[15][0])
        self.expiration = int(remove_underscore(all_settings[17][0]))
        self.active_list = "LIVE LIST" + self.file_ext
        self.mode = 0

    def generate_current_path(self):
        """Always updates the current file name and path to current date.
        returns as a string."""
        now = datetime.now()
        self.file_name = str(now)[:10] + self.file_ext
        t = now.ctime().upper()
        month = t[4:7]
        year = t[-4:]
        b = ('\ ')[0]
        self.current_path = self.main_file_path + year + b + month + b

    def change_mode(self):
        if self.mode == 0:
            self.mode = 1
        else:
            self.mode = 0


class check(object):
    """Creates an in/out log for a personal."""
    def __init__(self):
        self.mark = ""
        self.time_in = 0

    def import_info(self, info):
        """Imports the name and other data into the object. If there is no time
        stamp it creates one from the current time."""
        self.mark = info[2]
        self.first_name = info[0]
        self.last_name = info[1]
        self.full_name = self.first_name + " " + self.last_name
        if len(info) > 3:
            self.datetime = info[4] + " " + info[3]
        else:
            self.update_time()

    def update(self, settings):
        """Updates the mark in the live list to expired if passed expiration
        date."""
        self.time_in = calculate_hours_beteween(self.datetime, datetime.now())
        if self.time_in >= (settings.expiration / 2):
            self.mark = "EXPIRED"
    
    def update_time(self):
        self.datetime = datetime.today()


def import_settings():
    text_file_data = read_file("SETTINGS.txt")
    settings_info = []
    for line in text_file_data:
        line = line.split()
        line.reverse()
        settings_info.append(line)
    return settings_info


def read_file(a_file_name):
    text_file = open(a_file_name, "r")
    text_data = text_file.readlines()
    text_file.close()
    return text_data


def remove_underscore(a_string):
    return a_string.replace("_", " ")


def calculate_hours_beteween(before_date, after_date):
    """Returns number of hours between two dates."""
    d1 = str_numbers_2_list(before_date)
    d2 = str_numbers_2_list(after_date)
    date_1 = datetime(d1[0], d1[1], d1[2], 0, 0, 0,)
    date_2 = datetime(d2[0], d2[1], d2[2], 0, 0, 0)
    days_between = ((date_2 - date_1).days)
    hours_between = ((d2[3] - d1[3]))
    total = (days_between * 24) + hours_between
    return total


def str_numbers_2_list(a_string):
    """Returns a list of intgers seperated by the NON-digit characters
    from the input string."""
    a_string = str(a_string) + " "
    new_string = ""
    new_list = []
    for c in a_string:
        if c.isdigit() is True:
            new_string = new_string + c
        elif len(new_string) >= 1:
            new_list.append(int(new_string))
            new_string = ""
    return new_list
