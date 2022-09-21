# import datetime
import datetime 

def main():
    user_input = "26 08 1978 05:03"
    user_object = datetime.datetime.strptime(user_input, "%d %m %Y %H:%M")
    print("user_object: ", user_object)

    now_time = datetime.datetime.now()
    print("now_time_object: ", now_time)

    print("\n# Nowtime - Userbirthday:")
    time_passed = now_time - user_object

    print("# time_passed: ", time_passed)
    print("\n# type(now_time - user_object)")
    print(type(now_time - user_object))

    days_passed = time_passed.days
    print("\n# days_passed", days_passed)
    years_passed = int(days_passed / 365)
    print("\n# years_passed:", int(years_passed))
    
    days_rest_after_years = int(days_passed % 365)
    print("\n# days_rest_after_years:", days_rest_after_years)

    weeks_passed = int(days_rest_after_years / 7)
    print("\n# weeks_passed:", weeks_passed)

    days_rest_after_weeks = days_rest_after_years % weeks_passed
    print("\n# days_rest_after_weeks:", days_rest_after_weeks)


    print(f"\nYou spend {years_passed} years, {weeks_passed} weeks and {days_rest_after_weeks} days on this planet.\nIf your are not an astronaut.")




if __name__ == "__main__":
    main()