import math
import random
from sklearn.linear_model import LinearRegression
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

SIM_topo_H1 = 0
SIM_dir_theta1 = 0
SIM_dist_b_a_1 = 0

def tan_a_b(orin_tan, angle):
    return (orin_tan + math.tan(angle)) / (1 - orin_tan * math.tan(angle))

def cal(size = 10):
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    final_points = []
    for i in range(size):
        nx.append(random.randrange(10))
        ny.append(random.randrange(10))
        final_points.append([nx[i], ny[i]])
    print(final_points)


    #final_points = [[76, 86], [498, 336], [149, 479], [114, 63], [54, 286], [382, 450], [10, 255], [412, 193], [367, 147], [202, 454], [142, 2], [1, 6], [99, 407], [466, 404], [185, 385], [466, 422], [172, 324], [257, 70], [364, 157], [371, 296], [53, 253], [358, 207], [271, 242], [191, 282], [321, 392]]
    final_points = [[6, 2], [8, 3], [7, 4], [5, 8], [6, 5], [3, 2], [8, 7], [2, 2], [0, 6], [4, 8]]
    xx = np.array(np.array(final_points)[:,0]).reshape(-1, 1)
    yy = np.array(np.array(final_points)[:,1])
    #PCA
    model = LinearRegression()
    model.fit(xx, yy)
    #print(model.coef_)
    #print(model.intercept_)
    vor = Voronoi(final_points)
    voronoi_plot_2d(vor,show_points=True,show_vertices=False,line_colors='red',
                    line_width=1,line_alpha=1,point_size=0.1)


    points_arr = np.array(final_points)
    tri = Delaunay(points_arr)
    plt.triplot(points_arr[:, 0], points_arr[:, 1], tri.simplices.copy())
    plt.plot(points_arr[:, 0], points_arr[:, 1], 'o')


    points_neighbor_vertices = tri.vertex_neighbor_vertices
    #plt.plot(b[:,0], b[:,1], 'o')
    '''print(b[1][b[0][0]:b[0][0+1]])
    for i in range(len(b[1][b[0][0]:b[0][0+1]])):
        print(a[b[1][b[0][0]:b[0][0+1]][i]])
        plt.plot(a[b[1][b[0][0]:b[0][0+1]][i]][0], a[b[1][b[0][0]:b[0][0+1]][i]][1], 'o')
    print(a[0][0], a[1][1])'''
    #print(final_points)


    neighbor_num = {}
    #print('asd', type(a[0,0]))
    neigh_num = 0
    for i in range(size):
        neighbor_num[(int(points_arr[i][0]), int(points_arr[i][1]))] = len(points_neighbor_vertices[1][points_neighbor_vertices[0][i]:points_neighbor_vertices[0][i + 1]])
        neigh_num += len(points_neighbor_vertices[1][points_neighbor_vertices[0][i]:points_neighbor_vertices[0][i + 1]])
    SIM_topo_H1 = neigh_num / size
    #print(neigh)
    center_x = 0
    center_y = 0
    for i in range(size):
        center_x += points_arr[i][0]
        center_y += points_arr[i][1]
    center_y /= size
    center_x /= size
    trans_points = []
    for i in range(size):
        trans_points.append([final_points[i][0] - center_x, final_points[i][1] - center_y])
    #print(trans_ponit)
    #print(trans_ponit)
    #pow_sum = sum(pow(trans_ponit[:][0], 2)) - sum(pow(trans_ponit[:][1], 2))
    #print(pow_sum)
    #cheng_sum = sum(trans_ponit[:][0]*trans_ponit[:][1])
    '''temp1 = 0
    temp2 = 0
    for i in range(size):
        temp1 += trans_points[i][0] * trans_points[i][1]
        temp2 += (pow(trans_points[i][0], 2) - pow(trans_points[i][1], 2))
    
    angle = math.atan((temp2 + math.sqrt(pow(temp2, 2) + 4 * pow(temp1, 2))) / (2 * temp1))
    x = np.linspace(-10, 10, 10)
    y = (model.coef_) * (x - center_x) + center_y'''
    theta = math.atan(model.coef_)
    SIM_dir_theta1 = theta
    #plt.plot(x, y, 'o')
    #print(angle / (3.1415926*2) * 360)
    plt.plot(center_x, center_y, 'o')
    temp_da = 0
    temp_db = 0
    for i in range(size):
        temp_da += pow(trans_points[i][0] * math.cos(theta) - trans_points[i][1] * math.sin(-theta), 2)
        temp_db += pow(trans_points[i][0] * math.sin(-theta) + trans_points[i][1] * math.cos(theta), 2)
    da = math.sqrt(temp_da)
    db = math.sqrt(temp_db)
    SIM_dist_b_a_1 = db / da
    #print('dxdy', dx, dy)
    ell1 = Ellipse(xy = (center_x, center_y), width = da, height = db, angle =math.atan(model.coef_) / math.pi * 180, facecolor='yellow', alpha=0.3)
    #print('theta', math.atan(model.coef_) / math.pi * 180)
    #print('asd', theta)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.add_patch(ell1)
    x, y = center_x, center_y
    ax.plot(x, y, 'ro')
    ax.triplot(points_arr[:, 0], points_arr[:, 1], tri.simplices.copy())
    ax.plot(points_arr[:, 0], points_arr[:, 1], 'o')
    x = np.linspace(0, 10, 20)
    y = (model.coef_) * (x - center_x) + center_y
    ax.plot(x, y, 'o')
    plt.axis('scaled')
    #plt.plot(xx, model.predict(xx), 'o')

    #plt.axis('square')
    #plt.xlim(0, 500)
    #plt.ylim(0, 500)
    plt.show()

N1 = 10
cal(N1)