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
            return math.atan2((ap.y - self.y), (ap.x - self.x))
        except ZeroDivisionError:
            print(1)


class PointInfo:
    def __init__(self, num, points):
        self.num = num
        self.points = points
        self.points_info = {}
        for i in range(num):
            a = self.__add_info(self.points[i])
            self.points_info[self.points[i]] = a

    def __add_info(self, p):
        points_info = {}
        for i in range(self.num):
            if p != self.points[i]:
                points_info[self.points[i]] = [math.sqrt(p.cal_dis_2(self.points[i])), p.cal_tan_angle(self.points[i])]
        return points_info

    def show_info(self):
        for i in range(num):
            info = self.points_info[final_points[i]]
            print("(%d, %d)" % (final_points[i].x, final_points[i].y))
            for a in info.keys():
                print("[(%d, %d)" % (a.x, a.y), info[a][0], '%.2f' % (info[a][1]) + ']', end=' ')
                # print(b, tan[b])
            print()

    '''def show_info(self, p):
        info = self.points_info[p]
        print("(%d, %d)" % (p.x, p.y))
        for a in info.keys():
            print("[(%d, %d)" % (a.x, a.y), info[a][0], str(info[a][1]) + ']', end=' ')
            # print(b, tan[b])
        print()'''


def have_nei(p, p_i, tan, dis, err_t, err_d):
    flag = False
    info = p_i.points_info[p]
    for a in info.keys():
        if dis < a[0] + err_d < dis:
            if tan < a[1] + err_t < tan:
                flag = True
    return flag


e_r = 10
num = 20
final_points = []
for i in range(num):
    final_points.append(Point(random.randrange(50), random.randrange(50)))
    plt.plot(final_points[i].x, final_points[i].y, 'ro')
    # final_points.append([nx[i], ny[i]])

for i in range(num):
    plt.annotate("%d(%.1f, %.1f)" % (i, final_points[i].x, final_points[i].y),
                 xy=(final_points[i].x, final_points[i].y))

'''x = np.linspace(p1.x, p2.x, 10)
y = (p1.cal_tan_angle(p2)) * (x - p1.x) + p1.x
plt.plot(x, y, 'o')'''
# plt.plot([p1.x, p2.x], [p1.y, p2.y], color='b')
# plt.scatter([p1.x, p1.y], [p2.x, p2.y], color='b')
p_i = PointInfo(num, final_points)
'''for i in range(num):
    p_i.show_info(final_points[i])'''
#p_i.show_info()

num_p = input('0-19: ')
r_o = Point(final_points[int(num_p)].x, final_points[int(num_p)].y)
angle = random.uniform(-math.pi, math.pi)
rr = random.randrange(e_r)
r_o.x += rr * math.sin(angle)
r_o.y += rr * math.cos(angle)
plt.plot(r_o.x, r_o.y, 'bo')
plt.plot([final_points[int(num_p)].x, r_o.x], [final_points[int(num_p)].y, r_o.y], color='b')
x = np.arange(r_o.x - e_r, r_o.x + e_r, 0.1)
y = np.arange(r_o.y - e_r, r_o.y + e_r, 0.1)
x, y = np.meshgrid(x, y)
plt.contour(x, y, (x - r_o.x) ** 2 + (y - r_o.y) ** 2, [e_r ** 2])  # x**2 + y**2 = 9 的圆形

sum = 0
test_points = []
for i in range(num):
    p = final_points[i]
    if pow(p.x - r_o.x, 2) + pow(p.y - r_o.y, 2) <= pow(e_r, 2):
        test_points.append(p)
        print(p.x, p.y)
        sum += 1
print(sum)
info = p_i.points_info[final_points[int(num_p)]]
j = 2
while j >= 0:
    n = input('0-19: ')
    n_p = final_points[int(n)]
    o_p = final_points[int(num_p)]
    k = info[n_p]
    x = r_o.x + k[0] * math.cos(k[1])
    y = r_o.y + k[0] * math.sin(k[1])
    plt.plot(x, y, 'bo')
    plt.plot([x, n_p.x], [y, n_p.y], 'b')
    j -= 1
plt.axis('scaled')

plt.show()