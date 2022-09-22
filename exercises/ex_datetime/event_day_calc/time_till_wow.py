import datetime
import time
import os

def main():
    nadias_arrival = "07-10-2022 22:09"
    arrival_object = create_time_object(nadias_arrival)
    while True:
        os.system("clear")
        remaining_time = time_till_wow(arrival_object)
        print("\n" + remaining_time)
        time.sleep(1)


def time_till_wow(date):
    # create datetime object with actual time
    actual_date = datetime.datetime.now()

    # create timedelta object with difference between event and actual_date
    timedelta_object = (date - actual_date)

    # get remaining days
    rest_days = timedelta_object.days
    print("\nrest_days:", rest_days)

    # get the remaining minutes too.
    timedelta_minus_days = timedelta_object - datetime.timedelta(days = rest_days)
    print("\ntimedelta_minus_days ", timedelta_minus_days)
    rest_total_seconds = timedelta_minus_days.seconds
    print("rest_total_seconds:", rest_total_seconds)
    rest_hours = int(rest_total_seconds / (60 * 60))
    print("rest_hours:",rest_hours)

    timedelta_minus_hours = timedelta_minus_days - datetime.timedelta(hours = rest_hours)
    print("\ntimedelta_minus_hours:", timedelta_minus_hours)
    rest_minutes = int(timedelta_minus_hours.seconds / 60)
    print("rest_minutes", rest_minutes)

    timedelta_minus_minutes = timedelta_minus_hours - datetime.timedelta(minutes = rest_minutes)
    print("\ntimedelta_minus_minutes:", timedelta_minus_minutes)
    rest_seconds = timedelta_minus_minutes.seconds
    print("rest_seconds", rest_seconds)

    return f"We will meet in {rest_days} days, {rest_hours} hours, {rest_minutes} minutes and {rest_seconds} seconds."


def create_time_object(event):
    pattern = "%d-%m-%Y %H:%M"
    return datetime.datetime.strptime(event, pattern)



if __name__ == "__main__":
    print(main())