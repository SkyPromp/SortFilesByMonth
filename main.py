import os
import datetime

path = "../DCIM/"  # Input folder
destination = "Ordered Pictures"  # Output folder
folders = os.listdir(destination)

files = os.listdir(path)
total = len(files)
dates = [[filename, os.path.getmtime(path+filename)] for filename in files]
dates = [[filename, datetime.datetime.fromtimestamp(date)] for filename, date in dates]
dates = [[filename, f"{date.year} {date.month}"] for filename, date in dates]

# print(dates)
index = 0
for filename, date in dates:
    index += 1
    print(f"{index}/{total} : {filename}")
    if date not in folders:
        folders.append(date)
        os.mkdir(f"{destination}{date}")

    os.rename(path + filename, f"{destination}/{date}/{filename}")
