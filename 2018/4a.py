import operator
import re
from datetime import datetime
from collections import defaultdict


class Timestamp:
    def __init__(self, line, reg):
        res = reg.match(line)
        groups = res.group(1, 2, 3, 4, 5, 6)
        year, month, day, hour, minute, msg = groups
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)
        self.d = datetime(year, month, day, hour, minute)
        self.msg = msg

    def __lt__(self, other):
        return self.d < other.d


with open("4.txt") as f:
    lines = f.readlines()
    reg = re.compile("\[(\d*)-(\d*)-(\d*) (\d*):(\d*)\] (.*)\n")
    ts = list(map(lambda x: Timestamp(x, reg), lines))
    ts.sort()

    # Current guard
    guard = 0

    # Every guards needs a dictionary that will contain another dictionary that
    # will contain values from zero to 59

    # {id_guard: {minute: number_of_minutes}}
    guard_sleep = defaultdict(lambda: defaultdict(int))
    guard_tot_sleep = defaultdict(int)
    # when guard fell asleep
    fell_asleep_min = 0

    for t in ts:
        # falls asleep
        if "fa" in t.msg:
            fell_asleep_min = t.d.minute
        # wakes up
        elif "w" in t.msg:
            guard_tot_sleep[guard] += t.d.minute - fell_asleep_min
            for i in range(fell_asleep_min, t.d.minute):
                guard_sleep[guard][i] += 1
        else:
            spl = t.msg.split()
            num = int(spl[1][1:])
            # print(num)
            guard = num

    maximum = 0
    max_min = 0

    max_guard = max(guard_tot_sleep.items(), key=operator.itemgetter(1))[0]

    for minute, num in guard_sleep[max_guard].items():
        if num > maximum:
            maximum = num
            max_min = minute

    print(max_guard * max_min)
