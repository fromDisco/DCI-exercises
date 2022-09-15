import datetime


datetime_now = datetime.datetime.now()
print("\n# datetime_now:")
print(datetime_now)

print("\n------ Task1 ------")
print("# print year: datetime_now.year")
datetime_now_year = datetime_now.year
print(datetime_now_year)

print("\n------ Task2 ------")
print("# week day: datetime_now.weekday()")
some_date = datetime_now.weekday()
print(some_date)

print("\n------ Task3 ------")
print("is it a leap year?")


def leap(year):
    is_it = "no"

    if year % 400 == 0 and year % 4 == 0:
        is_it = "a" 
    elif year % 4 == 0 and not year % 100 == 0:
        is_it = "a"
            
    return f"{year} is {is_it} leap year"
    
    
print(leap(2000))
print(leap(1900))
print(leap(2016))



print("\n------ Task4 ------")


def convert_date(user_date):
    time_format = "%b %d %Y %I:%M%p"

    return datetime.datetime.strptime(user_date, time_format)


# user_input = input("Please enter Date: (Month Day Year Hour:Minute)")
user_input = "Feb 14 2021 8:30AM"
print(convert_date(user_input))