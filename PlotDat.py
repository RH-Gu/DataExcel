import csv
import xlrd
import numpy as np
import matplotlib.pyplot as plt

csvFile = csv.reader(open('C:\\Abaqus\\temp\\ContainDat.csv', 'r'))    # 创建csv文件
ss = []                               # 将整个文件转换为列表
for stu in csvFile:
    stu = list(map(float, stu))
    ss.append(stu)
n = len(ss)//171                      # 读表次数
fig = plt.figure(num=1, figsize=(25, 15))
ax1 = fig.add_subplot(341)            # 画布是分为3x4的区域
ax2 = fig.add_subplot(342)
ax3 = fig.add_subplot(343)
ax4 = fig.add_subplot(344)
ax5 = fig.add_subplot(345)
ax6 = fig.add_subplot(3, 4, 9)
ax7 = fig.add_subplot(3, 4, 10)
ax8 = fig.add_subplot(3, 4, 11)
ax9 = fig.add_subplot(3, 4, 12)
ax10 = fig.add_subplot(346)
ax11 = fig.add_subplot(347)
ax12 = fig.add_subplot(348)

PlotColor = [(254/255,67/255,101/255),(252/255,157/255,154/255),
             (254/255,67/255,101/255),(200/255,200/255,169/255),
             (254/255,67/255,101/255),(137/255,190/255,117/255),
             (254/255,67/255,101/255),(222/255,156/255,83/255),
             (254/255,67/255,101/255),(28/255,120/255,135/255),
             (254/255,67/255,101/255),(28/255,120/255,135/255)]

# ---超孔压
PorData = xlrd.open_workbook('C:\\Abaqus\\temp\\SoilPor.xls')  # 读入文件
ds = PorData.sheet_by_index(0)
PorNum = [[] for _ in range(ds.ncols)]                         # 生成多个空表
SumPor = [[] for _ in range(ds.ncols)]
for i in range(ds.ncols):
    PorNum[i] = list(filter(None, ds.col_values(i)))           # 去除空字符串
    if i <= 24:
        SumPor[i] = sum(PorNum[i][0:6])/6
ax1.plot(PorNum[0], PorNum[1])

ax2.plot(PorNum[2], PorNum[3])
ax2.plot(PorNum[4], PorNum[5])
ax2.plot(PorNum[6], PorNum[7])
ax2.plot(PorNum[8], PorNum[9])

ax3.plot(PorNum[10], PorNum[11])
ax3.plot(PorNum[12], PorNum[13])
ax3.plot(PorNum[14], PorNum[15])
ax3.plot(PorNum[16], PorNum[17])

ax4.plot(PorNum[18], PorNum[19])
ax4.plot(PorNum[20], PorNum[21])
ax4.plot(PorNum[22], PorNum[23])

ax5.plot(PorNum[24], PorNum[25])

ax6.plot(PorNum[26], PorNum[27])
ax7.plot(PorNum[28], PorNum[29])

for i in range(n):
    # 超孔压
    ax1.plot(ss[0+171*i], (np.array(ss[1+171*i])+SumPor[1]).tolist(), color=PlotColor[i])

    ax2.plot(ss[0+171*i], (np.array(ss[2+171*i])+SumPor[3]).tolist(), color=PlotColor[i])
    ax2.plot(ss[0+171*i], (np.array(ss[3+171*i])+SumPor[5]).tolist(), color=PlotColor[i])
    ax2.plot(ss[0+171*i], (np.array(ss[4+171*i])+SumPor[7]).tolist(), color=PlotColor[i])
    ax2.plot(ss[0+171*i], (np.array(ss[5+171*i])+SumPor[9]).tolist(), color=PlotColor[i])

    ax3.plot(ss[0+171*i], (np.array(ss[6+171*i])+SumPor[11]).tolist(), color=PlotColor[i])
    ax3.plot(ss[0+171*i], (np.array(ss[7+171*i])+SumPor[13]).tolist(), color=PlotColor[i])
    ax3.plot(ss[0+171*i], (np.array(ss[8+171*i])+SumPor[15]).tolist(), color=PlotColor[i])
    ax3.plot(ss[0+171*i], (np.array(ss[9+171*i])+SumPor[17]).tolist(), color=PlotColor[i])

    ax4.plot(ss[0+171*i], (np.array(ss[10+171*i])+SumPor[19]).tolist(), color=PlotColor[i])
    ax4.plot(ss[0+171*i], (np.array(ss[11+171*i])+SumPor[21]).tolist(), color=PlotColor[i])
    ax4.plot(ss[0+171*i], (np.array(ss[12+171*i])+SumPor[23]).tolist(), color=PlotColor[i])

    # 地表沉降
    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(5):
        for j in range(13 + 171 * i, 36 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 7 * k])
        ax5.plot(xNum, yNum[k], color=PlotColor[i])

    # 水平位移
    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(5):
        for j in range(36 + 171 * i, 62 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 7 * k])
        ax6.plot(yNum[k], xNum, color=PlotColor[i])

    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(5):
        for j in range(62 + 171 * i, 87 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 7 * k])
        ax7.plot(yNum[k], xNum, color=PlotColor[i])

    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(5):
        for j in range(87 + 171 * i, 110 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 7 * k])
        ax8.plot(yNum[k], xNum, color=PlotColor[i])

    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(5):
        for j in range(111 + 171 * i, 127 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 7 * k])
        ax9.plot(yNum[k], xNum, color=PlotColor[i])

    # 扰动分析
    xNum = []
    yNum = [[] for _ in range(3)]
    for k in range(3):
        for j in range(127 + 171 * i, 143 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 10 * k])
        ax10.plot(yNum[k], xNum, color=PlotColor[i])

    xNum = []
    yNum = [[] for _ in range(3)]
    for k in range(3):
        for j in range(143 + 171 * i, 154 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 10 * k])
        ax11.plot(yNum[k], xNum, color=PlotColor[i])

    xNum = []
    yNum = [[] for _ in range(5)]
    for k in range(3):
        for j in range(154 + 171 * i, 171 + 171 * i):
            if k == 0:
                xNum.append(ss[j][0])
            yNum[k].append(ss[j][1 + 10 * k])
        ax12.plot(xNum, yNum[k], color=PlotColor[i])
plt.show()
