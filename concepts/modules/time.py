import time
import os
import sys

print("Here we go:")
time.sleep(2)
os.system("clear")
print("Your system drive is being deleted right in the moment.")
print("To stop the process type: 'sdlkfj39sd3s0df§kj3sdf3jsdk!f2928DGBKAeid=??'")

# go up {x} lines
UP2 = f"\x1B[{2}A"
# insert two lines, so that first UP2 isn't overwriting previous lines
print("\n\n")

for i in range(1,11):
    text_line = f"Format process progress: {i * 10}% of 100%"
    progress_line = f"{'#' * i * 3} {'-' * (30 - i * 3)}"
    # go back two lines and overwrite
    # if lines would be shorter than the lines they overwrite, the rest would be visible
    print(f"{UP2}{text_line}\n{progress_line}")
    time.sleep(1)


print("your system wants to say bye:")
for char in "Bye!":
    print(char, end = "")
    time.sleep(.5)

print()