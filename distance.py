import csv
import numpy as np
import math as ma
import matplotlib.pyplot as plt
from scipy import integrate



q = float(0.25) #0.25
r = float(0.01) #0.01
p = float(0.01) #0.01
x = float(0)
m = float(0.0) #0.1加速度均值
n = float(0.000) #0.05加速度标准差
v_n = 0.0000 #0.0001速度标准差
win_size = 25
avg_size = 100
v_pre = float(0)
a_pre = float(0)
pos = float(0)
win_a = [0 for i in range(0, win_size)]
vel = [0 for i in range(0, win_size)]
delta_t = [0 for i in range(0, win_size)]
avg_arr = [0 for i in range(0, avg_size-1)]
avg_arr2 = []
delta = float(0.02)
const_delta = 0
avg = 0
filt = 0 and avg == 0
row = [0 for i in range(0,5)]

birth_data = []
filter_a = []

birth_data = []
with open('C:\\Users\\1\\Desktop\\dataset\\2020-05-30 21_29_57.csv') as csvfile:
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
filter_a = [0 for i in range(0, len(birth_data))]
#cmp = [[float(x) for x in row] for row in birth_data]

def init_colors():
    return ['blue', 'red', 'green', 'black', 'blue', 'purple', 'green', 'green','blanchedalmond','deeppink']


count = 0
sum = 0

while count != avg_size:
    sum += birth_data[count][0]
    count += 1

sum /= avg_size
avg_arr.append(sum)

for i in range(avg_size, len(birth_data)):
    avg_arr.append(avg_arr[i-1] + (birth_data[i][0] - birth_data[i-avg_size][0])/avg_size)

count = 0
sum = 0
temp_avg = 0

for i in range(0, len(birth_data)):
    temp_avg = (temp_avg*count + birth_data[i][0])/(count+1)
    count += 1
    if (i+1) % 100 == 0 or i == (len(birth_data)-1):
        count = 0
        for j in range(0, i%100+1):
            avg_arr2.append(temp_avg)




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
        temp, = plt.plot(X, Y, linewidth=0.5, color=color, label=birth_header[j])
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
    #plt.show()
    '''if save_png_name is not None:
        plt.savefig(save_png_name)'''


'''for i in range(0, len(birth_data)):
    x = x
    p = p
    k = (p * (p + r))
    x = x + k * float((birth_data[i][0] - x))
    p = (1 - k) * p + q
    filter_a[i] = x
    birth_data[i][1] = x'''


count = 0
j = 0

win_a = [0 for i in range(0, win_size)]
b = 0

for k in range(0,3):
    win_a = [0 for i in range(0, win_size)]
    v_pre = 0
    a_pre = 0
    pos = 0
    for j in range(0, len(filter_a)):
        if count != win_size:
            if avg == 1:
                win_a[count] = avg_arr[j]
            else:
                win_a[count] = filter_a[j] if filt == 1 else birth_data[j][1+k]
            delta_t[count] = delta if const_delta == 1 else birth_data[j][0]
            #print(str(j) + ":" + str(win_a[count]))
            count += 1
        else:
            g = np.mean(win_a)
            s = np.std(win_a)
            if g < m and s < n:
                win_a = [0 for i in range(0, win_size)]
                for i in range(j-win_size, j):
                    birth_data[i][1+k] = 0
            else:
                for i in range(j-win_size, j):
                    birth_data[i][1+k] = win_a[i - j + win_size]

            vel[0] = v_pre + a_pre * delta_t[0]
            for i in range(1, win_size):
                vel[i] = vel[i-1] + (win_a[i-1] * delta_t[i])
            v_s = np.std(vel)
            if v_s < v_n:
                vel = [0 for i in range(0, win_size)]
                for i in range(j - win_size, j):
                    birth_data[i][4+k] = 0
            else:
                for i in range(j - win_size, j):
                    birth_data[i][4+k] = vel[i - j + win_size]
            pos += v_pre*delta_t[0]
            birth_data[j - win_size][7+k] = pos
            for i in range(1, win_size):
                pos += vel[i-1] * delta_t[i]
                birth_data[j-win_size+i][7+k] = pos
                flag = 0

            v_pre = vel[win_size - 1]
            a_pre = win_a[win_size - 1]
            if avg == 1:
                win_a[0] = avg_arr[j]
            else:
                win_a[0] = filter_a[j] if filt == 1 else birth_data[j][1+k]
            delta_t[0] = delta if const_delta == 1 else birth_data[j][0]
            count = 1
#print(str(pos*100) + "cm")
'''for i in range(0, len(birth_data) - win_size):
    if (ma.isclose(birth_data[i][2], avg_arr[i])):
        a = 1
    else:
        a = 1
        print(i, birth_data[i][2], avg_arr[i])'''


'''vel = []
for j in range(0, len(avg_arr)):
    x = [i * delta for i in range(0, j)]
    y = [avg_arr[i] for i in range(0, j)]
    v = integrate.trapz(y, x)
    vel.append(v)
    # print(v)

x = [i * delta for i in range(0, len(avg_arr))]
# y = [birth_data[i][3] for i in range(0, len(birth_data))]
pos = integrate.trapz(vel, x)
print(pos * 100)'''
print('x: ' + str(birth_data[len(birth_data) - 100][7]*100) + "cm")
print('y: ' + str(birth_data[len(birth_data) - 100][8]*100) + "cm")
print('z: ' + str(birth_data[len(birth_data) - 100][9]*100) + "cm")
show_graph(birth_data, "x", init_colors(), 0)
show_graph(birth_data, "y", init_colors(), 1)
show_graph(birth_data, "z", init_colors(), 2)

