#!/usr/bin/python3

import sys
import datetime

def die(code=1, msg=None):
    "print error message and exit"
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(code)


def writefile(filename, data):
    mode = 'w'
    if isinstance(data, (bytes, bytearray)):
        mode = 'wb'
    with open(filename, mode=mode) as f:
        f.write(data)


def costtime(func):
    start=datetime.datetime.now()
    func()
    end=datetime.datetime.now()
    cost=end-start
    # print(cost.seconds)
    # print(cost.microseconds)
    print(cost.total_seconds())
    return cost.total_seconds()
