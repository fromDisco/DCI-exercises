import random
import inspect

# argument in Random is seed.
# Gives back specific value every time
drng = random.Random(7)
print(drng.__dict__["gauss_next"])
dice = drng.randrange(1, 7)
print(dice)
