import datetime


print("\n------ Task1 & Task2 ------")


def task1(daychange):
    datetime_now = datetime.datetime.now()
    print("# datetime.datetime.now():")
    print(datetime_now)

    # just datetime.timedelta() gives back the object of da
    datetime_timetravel = datetime_now + datetime.timedelta(days = daychange)
    print("# datetime_timetravel:")
    print(datetime_timetravel)
    print("# type(datetime_timetravel)")
    print(type(datetime_timetravel))

    # only extract Year, Month and Day
    output_time_format = "%Y-%m-%d"
    new_time_formated = datetime_timetravel.strftime(output_time_format)
    return new_time_formated


travel_back = -15
print(task1(travel_back))


print("\n------ Task3 ------")


def task3(act_year):
    # get actual payday of every month in the year
    for i in range(1, 13):
        payday_object = datetime.datetime(act_year, month = i, day = 25)
        
        date_format = "%A, %d %B %Y"
        payday = payday_object.strftime(date_format)

        message = f"Hello Bambam, your rent of 30.000 Euros is due on {payday} * 2!"
        print(message)


chosen_year = 1978
print(task3(chosen_year))