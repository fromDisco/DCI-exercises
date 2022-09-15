import datetime


print("\n------ Task1 & Task2 ------")


def task1(daychange):
    datetime_now = datetime.datetime.now()
    print("# datetime.datetime.now():")
    print(datetime_now)

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
    for i in range(1, 13):

        payday_object = datetime.datetime(act_year, month = i, day = 25)
        
        date_format = "%d %B %Y"
        payday = payday_object.strftime(date_format)

        message = f"Hello , your rent of 30.000 Euros is due on {payday}!"
        print(message)


chosen_year = 2022
print(task3(chosen_year))