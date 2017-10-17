#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from datetime import datetime

from fund import test

x, y = test.get_xy()


print(x[0], y[0])
print(x[1], y[1])
print(x[2], y[1])


def my_formatter_fun(x, p):
    try:
        dt = datetime.utcfromtimestamp(x / 1000)
        return dt.strftime('%Y-%m-%d')
    except:
        return ''



# x = [0, 1,2,3,4,5]
# y = [0, 1,2,5,4,5]
plt.figure(figsize=(9, 4))
plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('money1')
plt.axis([x[0], x[len(x) - 1], 0, 2])
ax = plt.subplot(111)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(my_formatter_fun))
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
    print('label')

axes = plt.subplot(111)
axes.set_title('xxxx')
# for xxx in axes.xaxis.get_ticklabels():
#     print(xxx)
#     break

print(axes.xaxis)
plt.show()
plt.savefig('easyplot.jpg')
