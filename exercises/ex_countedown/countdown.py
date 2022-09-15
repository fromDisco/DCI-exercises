import time
import os


def countdown():
    os.system("clear")
    delay = int(input("How long do you want to sleep? "))

    begin_time = time.time()
    readable_begin = time.ctime()

    # go up {x} lines
    UP1 = f"\x1B[{1}A"
    UP2 = f"\x1B[{2}A"
    UP3 = f"\x1B[{3}A"

    # add some line breaks to give UP3 some space
    print("\n\n\n")
    
    for i in range(delay, -1, -1):
        # two \n (line breaks) and the linebreak of the print => 3 * \n
        # so UP3 is required that lines get overwritten
        print(f"{UP3}{i}\n\nStart time: {begin_time}")
        time.sleep(1)

    end_time = time.time()
    readable_end = time.ctime()

    # print("\nStart time:", readable_begin)
    print("End time:", readable_end)

    time_passed = end_time - begin_time
    print("\nElapsed time:", time_passed)


countdown()