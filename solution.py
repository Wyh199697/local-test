import random
import matplotlib.pyplot as plt
import math
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cal_dis_2(self, ap):
        return pow(self.x - ap.x, 2) + pow(self.y - ap.y, 2)

    def cal_tan_angle(self, ap):
        return math.tan((ap.y - self.y) / (ap.x - self.x))


class point_info:
    def __init__(self, num, points):
        self.num = num
        self.points = points
        self.dis_info = {}
        self.tan_info = {}
        for i in range(num):
            a, b = self.__add_info(self.points[i])
            self.dis_info[self.points[i]] = a
            self.tan_info[self.points[i]] = b

    def __add_info(self, p):
        dis_info = []
        tan_info = []
        return dis_info, tan_info

num = 10
final_points = []
for i in range(num):
    final_points.append(Point(random.randrange(num), random.randrange(num)))
    plt.plot(final_points[i].x, final_points[i].y, 'ro')
    # final_points.append([nx[i], ny[i]])

for i in range(num):
    plt.annotate("%d(%.1f, %.1f)" % (i, final_points[i].x, final_points[i].y), xy=(final_points[i].x, final_points[i].y))

p1 = final_points[5]
p2 = final_points[6]
'''x = np.linspace(p1.x, p2.x, 10)
y = (p1.cal_tan_angle(p2)) * (x - p1.x) + p1.x
plt.plot(x, y, 'o')'''
plt.plot([p1.x, p2.x], [p1.y, p2.y], color='b')
#plt.scatter([p1.x, p1.y], [p2.x, p2.y], color='b')
plt.show()
print(p1.cal_tan_angle(p2))