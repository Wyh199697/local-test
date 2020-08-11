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
        try:
            if ap.x == self.x:
                return float("inf")
            return math.tan((ap.y - self.y) / (ap.x - self.x))
        except ZeroDivisionError:
            print(1)


class PointInfo:
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
        dis_info = {}
        tan_info = {}
        for i in range(self.num):
            if p != self.points[i]:
                dis_info[self.points[i]] = p.cal_dis_2(self.points[i])
                tan_info[self.points[i]] = p.cal_tan_angle(self.points[i])
        return dis_info, tan_info

    def show_info(self):
        for i in range(num):
            dis = self.dis_info[final_points[i]]
            tan = self.tan_info[final_points[i]]
            print("(%d, %d)" % (final_points[i].x, final_points[i].y))
            for a in dis.keys():
                print("(%d, %d)" % (a.x, a.y), dis[a], end=' ')
                # print(b, tan[b])
            print()
            for b in tan.keys():
                print("(%d, %d)" % (b.x, b.y), tan[b], end=' ')
                # print(b, tan[b])
            print()
    def show_info(self, p):
        dis = self.dis_info[final_points[i]]
        tan = self.tan_info[final_points[i]]
        print("(%d, %d)" % (final_points[i].x, final_points[i].y))
        for a in dis.keys():
            print("[(%d, %d)" % (a.x, a.y), str(dis[a]) + ']', end=' ')
            # print(b, tan[b])
        print()
        for b in tan.keys():
            print("[(%d, %d)" % (b.x, b.y), "%.2f" % tan[b] + ']', end=' ')
            # print(b, tan[b])
        print()

num = 20
final_points = []
for i in range(num):
    final_points.append(Point(random.randrange(num), random.randrange(num)))
    plt.plot(final_points[i].x, final_points[i].y, 'ro')
    # final_points.append([nx[i], ny[i]])

for i in range(num):
    plt.annotate("%d(%.1f, %.1f)" % (i, final_points[i].x, final_points[i].y),
                 xy=(final_points[i].x, final_points[i].y))

p1 = final_points[5]
p2 = final_points[6]
'''x = np.linspace(p1.x, p2.x, 10)
y = (p1.cal_tan_angle(p2)) * (x - p1.x) + p1.x
plt.plot(x, y, 'o')'''
plt.plot([p1.x, p2.x], [p1.y, p2.y], color='b')
# plt.scatter([p1.x, p1.y], [p2.x, p2.y], color='b')
p_i = PointInfo(num, final_points)
for i in range(num):
    p_i.show_info(final_points[i])
plt.show()
print(p1.cal_tan_angle(p2))
