import csv
import numpy as np
import matplotlib.pyplot as plt

csvFile = csv.reader(open('C:\\Abaqus\\temp\\ContainDat.csv', 'r'))      # 创建csv文件
print(csvFile)
for stu in csvFile:
    print(stu)
