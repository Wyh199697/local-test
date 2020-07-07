import csv
import numpy as np
import math as ma
import matplotlib.pyplot as plt
from scipy import integrate
birth_data = []
with open('C:\\Users\\1\\Desktop\\dataset\\AccelerationExplorer-2020-6-21-11-22-50.csv') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    birth_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        birth_data.append(row)

birth_header.append('v')
birth_header.append('pos')
pre = [float(0) for i in row]

for i in range(len(birth_data)):
    if len(birth_data[i]) < 4 or birth_data[i][1] == '':
        t = birth_data[i][0]
        birth_data[i] = [float(x) for x in pre]
        birth_data[i][0] = float(t)
    else:
        birth_data[i] = [float(x) for x in birth_data[i]]
    pre = birth_data[i]

def init_colors():
    return ['blue', 'red', 'green', 'black', 'pink', 'purple', 'gray', 'yellow']

def show_graph(data, save_png_name=None, colors=None):
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
    for j in range(1, 6):
        if j == 2 or j == 4 or j == 5:
            for i in range(0, len(data)):
                color = colors[j]
                X.append(i)
                Y.append(data[i][j])
            temp, = plt.plot(X, Y, linewidth=0.5, color=color, label='')
            plts.append(temp)
            X = []
            Y = []
    labels.append(birth_header[1])
    labels.append(birth_header[4])
    labels.append(birth_header[5])
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

#birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式
vel = []
y = []
x = []
for j in range(0, len(birth_data)):
    x = [birth_data[i][0] for i in range(0, j)]
    y = [birth_data[i][2] for i in range(0, j)]
    v = integrate.trapz(y, x)
    vel.append(v)
    birth_data[j].append(v)
    # print(v)

# y = [birth_data[i][3] for i in range(0, len(birth_data))]
pos = []
for j in range(0, len(birth_data)):
    x = [birth_data[i][0] for i in range(0, j)]
    y = [vel[i] for i in range(0, j)]
    pos = integrate.trapz(y, x)
    vel.append(v)
    birth_data[j].append(pos)

print(str(pos*100) + "cm")
show_graph(birth_data,"asas", init_colors())
