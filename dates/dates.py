#!/usr/bin/env python3

from datetime import datetime, time, date, MINYEAR, MAXYEAR


# noinspection PyShadowingNames
def _get_delorean_date_format(date):
    return datetime.strftime(date, '"%b %d %Y %H:%M"').upper()


def _get_delorean_time_format(time_):
    return time.strftime(time_, '"%H:%M"')


if __name__ == '__main__':
    now = datetime.now()
    first_dest = datetime(1985, 10, 26, 9, 00)
    second_dest_date = date(2015, 10, 21)
    second_dest_time = time(7, 28)
    second_dest = datetime(2015, 10, 21, 7, 28)
    third_dest = datetime(1955, 11, 12, 6, 38)
    diff = second_dest - first_dest  # diff is a timedelta instance
    diff_years, remainder = divmod(diff.days, 365)
    diff_months, diff_days = divmod(remainder, 12)
    diff_hours, remainder = divmod(diff.seconds, 3600)  # 60*60
    diff_minutes, diff_seconds = divmod(remainder, 60)

    print(f"- Hi, Doc! Today is {_get_delorean_date_format(now)}. What are the minimum and maximum years for the Delorean?")
    print(f"- We can travel anywhere between {MINYEAR}AC and {MAXYEAR}AC")
    print(f"- We could go to {_get_delorean_date_format(first_dest)}!")
    print(f"- We could also go to {_get_delorean_date_format(second_dest_date)}... But we need a time, what about {_get_delorean_time_format(second_dest_time)}?")
    print(f"- I was thinking about go to {_get_delorean_date_format(third_dest)}. What are the difference with {_get_delorean_date_format(second_dest)}")
    print(f"- We would be traveling {diff.seconds} seconds! {diff.days} days! {diff_years} years, {diff_months} months, {diff_days} days, {diff_hours} hours and {diff_seconds} seconds!")
