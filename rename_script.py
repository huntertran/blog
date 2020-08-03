from os import listdir
from os import rename
from os.path import isfile, join
import datetime

blog_path = './source/_posts/'

def is_file_name_start_with_date(filename):
    year = filename[0:4]
    month = filename[4:6]
    day = filename[6:8]
    if str.isnumeric(year) and str.isnumeric(month):
        return True
    else:
        return False

def rename_file(filename):
    is_renaming = False
    date_string = ''
    with open(blog_path + filename, 'r', encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('date: '):
                is_renaming = not is_file_name_start_with_date(filename)
                date = datetime.datetime.fromisoformat(
                    str.strip(line.split(': ')[1]))
                month_string = ''
                day_string = ''

                if date.month < 10:
                    month_string = "0" + str(date.month)
                else:
                    month_string = str(date.month)

                if date.day < 10:
                    day_string = "0" + str(date.day)
                else:
                    day_string = str(date.day)

                date_string = str(date.year) + month_string + day_string
                break
    if is_renaming:
        rename(blog_path + filename, blog_path + date_string + "-" + filename)

onlyfiles = [f for f in listdir(blog_path) if isfile(join(blog_path, f))]

for filename in onlyfiles:
    rename_file(filename)
