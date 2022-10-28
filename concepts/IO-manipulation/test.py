import os
import dbm
import pickle
import pathlib

# get path of file. result is an object, not a string.
print(type(pathlib.Path(__file__).parent.resolve()))
print("##################")

db = dbm.open("test", "c")

db["carrot"] = "vitamin b"
db["orange"] = "vitamin c"


print(db["carrot"])

for item in db.keys():
    print(f"{item}: {db[item]}")
    
listing = [1, 3, "haha"]
dumping = pickle.dumps(listing)
print(dumping)
back_dump = pickle.loads(dumping)
print(back_dump)


command = "ls -l"
files = os.popen(command)
print(files.read())

files.close()



db.close()