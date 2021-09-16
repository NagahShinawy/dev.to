from datetime import date
import os
from calendar import monthrange


CMD = os.getcwd()
DATE_FORMAT = "%Y-%m-%d"
FIRST_DAY = 1

today = date.today()
current_month = today.month
current_year = today.year


def get_month_days(year, month):
    return monthrange(year, month)


def create_day_dir(day):
    dirname = f"{day}-{current_month}-{current_year}"
    destination = os.path.join(CMD, dirname)
    if not os.path.isdir(destination):
        os.makedirs(destination)


def main():
    _, last_day = get_month_days(year=current_year, month=current_month)
    for day in range(FIRST_DAY, last_day + 1):
        create_day_dir(day)


if __name__ == '__main__':
    main()

