import math as m


def dis(p1, p2):
    return m.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2) + pow(p1[2] - p2[2], 2))


def vec(p1, p2):
    d = dis(p1, p2)
    return [(p2[0] - p1[0]) / d, (p2[1] - p1[1]) / d, (p2[2] - p1[2]) / d]


def crea_line_points(p1, p2, num):
    p = []
    interval = dis(p1, p2) / (num + 1)
    v = vec(p1, p2)
    for i in range(num + 1):
        p.append([p1[0] + v[0] * interval * i, p1[1] + v[1] * interval * i, p1[2] + v[2] * interval * i])
    p.append([p2[0], p2[1], p2[2]])
    return p


def crea_plane_points(line1, line2, num):
    p = []
    for i in range(len(line1)):
        temp = crea_line_points(line1[i], line2[i], num)
        for j in range(len(temp)):
            p.append(temp[j])
    return p


def crea_volume_points(plane1, plane2, num):
    p = []
    for i in range(len(plane1)):
        temp = crea_line_points(plane1[i], plane2[i], num)
        for j in range(len(temp)):
            p.append(temp[j])
    return p


p1 = [-0.0615968, -0.12872767, -0.20466079]
p2 = [0.074516684, -0.122140095, -0.24632582]
p4 = [0.0467028, -0.1219704, -0.3371628]
p3 = [-0.08941068, -0.12855798, -0.29549778]

p5 = [-0.05744714, -0.22362597, -0.20610867]
p6 = [0.078666344, -0.2170384, -0.2477737]
p8 = [0.05085246, -0.2168687, -0.3386107]
p7 = [-0.08526102, -0.22345628, -0.29694566]

print(dis(p1, p2))
pl1 = crea_plane_points(crea_line_points(p1, p2, 10), crea_line_points(p3, p4, 10), 10)
pl2 = crea_plane_points(crea_line_points(p5, p6, 10), crea_line_points(p7, p8, 10), 10)
p = crea_volume_points(pl1, pl2, 10)
for i in range(len(p)):
    print(p[i])
