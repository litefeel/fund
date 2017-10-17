import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
now = datetime.now

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()



line,  = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '-')
# line.set_antialiased(True)
# plt.title('set_antialiased True')
# line.set_antialiased(False)
# plt.title('set_antialiased False')
plt.axis([0, 6, 0, 20])
# plt.show()
plt.savefig('{:%Y%m%d%H%M%S}.jpg'.format(now()))

1503936000000
1506740287.674108
print(now().timestamp())