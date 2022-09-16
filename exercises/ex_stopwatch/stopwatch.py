import time


def stopwatch():
    # take snapshot of actual time
    start_time = time.time()
    # readable time
    readable_start = time.ctime()

    print("\nstart time (unix):", start_time)
    print(time.ctime())

    # spend some time between snapshots. Ask user for input
    user = input("Waste Time. Type something: ")

    # take snapshot after user input
    end_time = time.time()
    # readable time
    readable_end = time.ctime()
    print("\nend time (unix):", end_time)
    print(readable_end)

    # substract start_time from end_time to get seconds passed between snapshots
    time_passed = end_time - start_time
    print("Passed time in seconds:", time_passed)



stopwatch()