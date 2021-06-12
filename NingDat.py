# -*- coding: utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
import numpy as np

# ---超孔压
PorData = xlrd.open_workbook('C:\\Abaqus\\temp\\POR.xls')  # 读入文件
ds = PorData.sheet_by_index(0)
PorNum = [[] for _ in range(ds.nrows)]                     # 生成多个空表
for i in range(ds.nrows):
    PorNum[i] = (ds.row_values(i))
    del PorNum[i][0:2]
PxNum = np.arange(-21.6, 25.2, 1.2).tolist()               # 横坐标
fig = plt.figure(num=1, figsize=(16, 10))
ax1 = fig.add_subplot(341)                                 # 画布是分为2x2的区域
ax1.plot(PxNum, PorNum[0])
ax2 = fig.add_subplot(342)
ax2.plot(PxNum, PorNum[1])
ax2.plot(PxNum, PorNum[2])
ax2.plot(PxNum, PorNum[3])
ax2.plot(PxNum, PorNum[4])
ax3 = fig.add_subplot(343)
ax3.plot(PxNum, PorNum[5])
ax3.plot(PxNum, PorNum[6])
ax3.plot(PxNum, PorNum[7])
ax3.plot(PxNum, PorNum[8])
ax4 = fig.add_subplot(344)
ax4.plot(PxNum, PorNum[9])
ax4.plot(PxNum, PorNum[10])
ax4.plot(PxNum, PorNum[11])

# ---地表沉降
U3Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U30.xls')  # 读入文件
ds = U3Data.sheet_by_index(0)
U3y1Num = ds.col_values(1, 27, 49)
U3y2Num = ds.col_values(13, 27, 49)
U3y3Num = ds.col_values(27, 27, 49)
U3y4Num = ds.col_values(38, 27, 49)
U3xNum = ds.col_values(0, 27, 49)
fig = plt.figure(num=1, figsize=(16, 10))
ax5 = fig.add_subplot(345)
ax5.plot(U3xNum, U3y1Num)
ax5.plot(U3xNum, U3y2Num)
ax5.plot(U3xNum, U3y3Num)
ax5.plot(U3xNum, U3y4Num)

# ---水平位移
U20Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U20.xls')  # 读入文件
U21Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U21.xls')  # 读入文件
U22Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U22.xls')  # 读入文件
U23Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U23.xls')  # 读入文件
ds1 = U20Data.sheet_by_index(0)
ds2 = U21Data.sheet_by_index(0)
ds3 = U22Data.sheet_by_index(0)
ds4 = U23Data.sheet_by_index(0)

U2xNum = ds1.col_values(0, 1, 26)
ax6 = fig.add_subplot(349)
U2y1Num = [[] for _ in range(6)]
for i in range(6):
    U2y1Num[i] = ds1.col_values(1+i*7, 1, 26)
    ax6.plot(U2y1Num[i], U2xNum)

U2xNum = ds2.col_values(0, 1, 26)
ax7 = fig.add_subplot(3, 4, 10)
U2y2Num = [[] for _ in range(6)]
for i in range(6):
    U2y2Num[i] = ds2.col_values(1+i*7, 1, 26)
    ax7.plot(U2y2Num[i], U2xNum)

U2xNum = ds3.col_values(0, 1, 23)
ax8 = fig.add_subplot(3, 4, 11)
U2y3Num = [[] for _ in range(6)]
for i in range(6):
    U2y3Num[i] = ds3.col_values(1+i*7, 1, 23)
    ax8.plot(U2y3Num[i], U2xNum)

U2xNum = ds4.col_values(0, 1, 17)
ax9 = fig.add_subplot(3, 4, 12)
U2y4Num = [[] for _ in range(6)]
for i in range(6):
    U2y4Num[i] = ds4.col_values(1+i*7, 1, 17)
    ax9.plot(U2y4Num[i], U2xNum)

# ---扰动分析
SSDz1 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV70.xls')   # 读入文件
SSDz2 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV71.xls')   # 读入文件
SSDy1 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV7Y0.xls')  # 读入文件
ds1 = SSDz1.sheet_by_index(0)
ds2 = SSDz2.sheet_by_index(0)
ds3 = SSDy1.sheet_by_index(0)

xNum = ds1.col_values(0, 20, 36)
ax10 = fig.add_subplot(346)
yNum = [[] for _ in range(6)]
for i in range(6):
    yNum[i] = ds1.col_values(1+i*7, 20, 36)
    ax10.plot(yNum[i], xNum)

xNum = ds2.col_values(0, 21, 32)
ax11 = fig.add_subplot(347)
yNum = [[] for _ in range(6)]
for i in range(6):
    yNum[i] = ds2.col_values(1+i*7, 21, 32)
    ax11.plot(yNum[i], xNum)

xNum = ds3.col_values(0, 23, 40)
ax12 = fig.add_subplot(348)
yNum = [[] for _ in range(6)]
for i in range(6):
    yNum[i] = ds3.col_values(1+i*7, 23, 40)
    ax12.plot(xNum, yNum[i])
plt.show()
