from datetime import date


def cap_day(string):
    # split the actual date
    act_date = str(date.today()).split("-")
    # concatinate the month and the day
    act_day = act_date[1] + act_date[2]
    # check if day is bigger than CAPS LOCK DAY
    if int(act_day) > int("0822"):
        return string.upper()

    if string.isupper():
        string = string.lower()

    return string.capitalize()


print(cap_day("CAPS"))
print(cap_day("lower"))
print(cap_day("Mid"))
