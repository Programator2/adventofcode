"""
I'm using this script to download input for newest challenge exactly at 6am CET.
It is stored as {day}.txt.
For older challenges see `get_data()` from `advent-of-code-data` package.
"""
import datetime
from time import sleep
from aocd import get_data
import aocd
import sys

DAY = datetime.date.today().day
YEAR = 2023
FILENAME = f"{DAY}.txt"

print(f"Preparing to download {FILENAME}")
print("Waiting for 6am")

while datetime.datetime.now().hour < 6:
    print(".", end="")
    sleep(1)

print("It's 6am")

sleep_time = 1

while True:
    try:
        print("Trying to get data")
        data = get_data(day=DAY, year=YEAR)
    except aocd.exceptions.AocdError:
        sleep_time *= 2
        if sleep_time > 64:
            sleep_time = 64
        print(f"Sleeping for {sleep_time} seconds")
        sleep(sleep_time)
        continue
    break

with open(FILENAME, "w", encoding="utf8") as f:
    f.write(data)

print(f"Data stored as {FILENAME}")
