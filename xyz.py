import csv
import numpy as np
import math as ma
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import axes3d


birth_data = []
with open('C:\\Users\\70894\\Desktop\\dataset\\2020-05-25 17_56_18.csv') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    birth_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        birth_data.append(row)
birth_header.append('v_x')
birth_header.append('v_y')
birth_header.append('v_z')
birth_header.append('pos_x')
birth_header.append('pos_y')
birth_header.append('pos_z')
for i in range(len(birth_data)):
    birth_data[i] = [float(x) for x in birth_data[i]]
    for j in range(6):
        birth_data[i].append(0)
#birth_data = [[float(x) for x in row] for row in birth_data]

def init_colors():
    return ['blue', 'red', 'green', 'black', 'blue', 'purple', 'green', 'green','blanchedalmond','deeppink']

def show_graph(data, save_png_name=None, colors=None, offset=0):
    """
    绘制折线图
    :param data: 数据格式：{label:{X:Y}, label:{X:Y}...}
    :param save_png_name:保存的图片的名字
    :param colors: 颜色列表
    :return:
        None
    """
    # 解决中文显示乱码的问题，不用中文就不需要设置了
    # my_font = font_manager.FontProperties(fname="/自己补充路径/IOS8.ttf")

    if colors is None:
        colors = init_colors()
    plt.figure(dpi=512, figsize=(14, 6))
    plts = []
    labels = []
    X = []
    Y = []
    for j in range(1+offset, 8 + offset, 3):
        for i in range(0, len(data)):
            color = colors[j-offset]
            X.append(i)
            Y.append(data[i][j])
        temp, = plt.plot(X, Y, linewidth=0.5, color=color, label='')
        plts.append(temp)
        X = []
        Y = []
    for i in range(1+offset, 8+offset,3):
        labels.append(birth_header[i])
    #labels.append("avg_a")
    plts.append(plt.plot([i for i in range(0, len(data))], [0 for i in range(0, len(data))], linewidth=1, color="black"))
    #plts.append(plt.plot([i for i in range(0, len(data))], avg_arr, linewidth=0.5, color="purple"))
    #plts.append(plt.plot([i for i in range(0, len(data))], avg_arr2, linewidth=0.5, color="red"))
    plt.legend(handles=plts, labels=labels)
    if save_png_name is not None:
        plt.savefig(save_png_name)
    plt.show()
    '''if save_png_name is not None:
        plt.savefig(save_png_name)'''




for k in range(3):
    vel = []
    y = []
    for j in range(0, len(birth_data)):
        x = [0 for i in range(j+1)]
        x[0] = birth_data[0][0]
        for i in range(1, j+1):
            x[i] = x[i-1] + birth_data[i][0]
        y = [birth_data[i][k+1] for i in range(0, j+1)]
        v = integrate.trapz(y, x)
        vel.append(v)
        birth_data[j][4+k] = v
        # print(v)

    # y = [birth_data[i][3] for i in range(0, len(birth_data))]
    pos = []
    for j in range(0, len(birth_data)):
        x = [0 for i in range(j + 1)]
        x[0] = birth_data[0][0]
        for i in range(1, j + 1):
            x[i] = x[i - 1] + birth_data[i][0]
        y = [vel[i] for i in range(0, j+1)]
        pos = integrate.trapz(y, x)
        birth_data[j][7+k] = pos

print('x: ' + str(birth_data[len(birth_data) - 1][7]*100) + "cm")
print('y: ' + str(birth_data[len(birth_data) - 1][8]*100) + "cm")
print('z: ' + str(birth_data[len(birth_data) - 1][9]*100) + "cm")
show_graph(birth_data,"x", init_colors(), 0)
show_graph(birth_data,"y", init_colors(), 1)
show_graph(birth_data,"z", init_colors(), 2)