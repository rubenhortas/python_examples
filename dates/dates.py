#!/usr/bin/env python3

from datetime import datetime, time, date, MINYEAR, MAXYEAR


# noinspection PyShadowingNames
def _get_delorean_date_format(date_: date) -> str:
    return datetime.strftime(date_, "'%b %d %Y %H:%M'").upper()


def _get_delorean_time_format(time_: time) -> str:
    return time.strftime(time_, "'%H:%M'")


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
    diff_hours, remainder = divmod(diff.seconds, 3600)  # 3600 = 60min * 60sec
    diff_minutes, diff_seconds = divmod(remainder, 60)

    print(f"- Hi, Doc! Today is {_get_delorean_date_format(now)}. What are the minimum and maximum years for the Delorean?")
    # return: - Hi, Doc! Today is 'OCT 18 2023 20:59'. What are the minimum and maximum years for the Delorean?

    print(f"- We can travel anywhere between {MINYEAR}AC and {MAXYEAR}AC")
    # return: - We can travel anywhere between 1AC and 9999AC

    print(f"- We could go to {_get_delorean_date_format(first_dest)}!")
    # return:  We could go to 'OCT 26 1985 09:00'!

    print(f"- We could also go to {_get_delorean_date_format(second_dest_date)}... But we need a time, what about {_get_delorean_time_format(second_dest_time)}?")
    # return: - We could also go to 'OCT 21 2015 00:00'... But we need a time, what about '07:28'?

    print(f"- I was thinking about go to {_get_delorean_date_format(third_dest)}. What are the difference with {_get_delorean_date_format(second_dest)}")
    # return: - I was thinking about go to 'NOV 12 1955 06:38'. What are the difference with 'OCT 21 2015 07:28'

    print(f"- We would be traveling {diff.seconds} seconds! {diff.days} days! {diff_years} years, {diff_months} months, {diff_days} days, {diff_hours} hours and {diff_seconds} seconds!")
    # return: - We would be traveling 80880 seconds! 10951 days! 30 years, 0 months, 1 days, 22 hours and 0 seconds!
