import xlrd
import csv
import numpy as np

# ---求出目标行行号
def GetRow(ds) :
    i = 0 ; num = 0
    while num == 0:
        if ds.row_values(i)[1] == '':
            if ds.row_values(i+1)[1] != "":
                num = 1
        i = i + 1
    row = i
    return row

# ---超孔压
PorData = xlrd.open_workbook('C:\\Abaqus\\temp\\POR.xls')  # 读入文件
ds = PorData.sheet_by_index(0)
PorNum = [[] for _ in range(ds.nrows)]                     # 生成多个空表
for i in range(ds.nrows):
    PorNum[i] = (ds.row_values(i))
    del PorNum[i][0:2]
PxNum = np.arange(-21.6, 25.2, 1.2).tolist()               # 横坐标
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(PxNum)                                  # 1 *39
    f_csv.writerows(PorNum)                                # 12*39

# ---地表沉降
U3Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U30.xls')   # 读入文件
ds = U3Data.sheet_by_index(0)
rowNum = GetRow(ds)
U3Num = [[] for _ in range(23)]                            # 生成多个空表
for i in range(23):
    U3Num[i] = (ds.row_values(rowNum+i))
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(U3Num)                                 # 23*40

# ---水平位移
U20Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U20.xls')  # 读入文件
U21Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U21.xls')  # 读入文件
U22Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U22.xls')  # 读入文件
U23Data = xlrd.open_workbook('C:\\Abaqus\\temp\\U23.xls')  # 读入文件
ds1 = U20Data.sheet_by_index(0)
ds2 = U21Data.sheet_by_index(0)
ds3 = U22Data.sheet_by_index(0)
ds4 = U23Data.sheet_by_index(0)
U2yNum = [[] for _ in range(26)]
for i in range(26):
    U2yNum[i] = ds1.row_values(1+i)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(U2yNum)                                        # 26*40

U2yNum = [[] for _ in range(25)]
for i in range(25):
    U2yNum[i] = ds2.row_values(1+i)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(U2yNum)                                        # 25*40

U2yNum = [[] for _ in range(23)]
for i in range(23):
    U2yNum[i] = ds3.row_values(1+i)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(U2yNum)                                        # 23*40

U2yNum = [[] for _ in range(17)]
for i in range(17):
    U2yNum[i] = ds4.row_values(1+i)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(U2yNum)                                        # 17*40

# ---扰动分析
SSDz1 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV70.xls')   # 读入文件
SSDz2 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV71.xls')   # 读入文件
SSDy1 = xlrd.open_workbook('C:\\Abaqus\\temp\\SDV7Y0.xls')  # 读入文件
ds1 = SSDz1.sheet_by_index(0)
ds2 = SSDz2.sheet_by_index(0)
ds3 = SSDy1.sheet_by_index(0)

rowNum = GetRow(ds1)
yNum = [[] for _ in range(16)]
for i in range(16):
    yNum[i] = ds1.row_values(i+rowNum)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(yNum)                                          # 16*40

rowNum = GetRow(ds2)
yNum = [[] for _ in range(11)]
for i in range(11):
    yNum[i] = ds2.row_values(i+rowNum)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(yNum)                                          # 11*40

rowNum = GetRow(ds3)
yNum = [[] for _ in range(17)]
for i in range(17):
    yNum[i] = ds3.row_values(i+rowNum)
with open('C:\\Abaqus\\temp\\ContainDat.csv', 'a', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(yNum)                                         # 17*4
