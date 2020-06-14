import matplotlib.pyplot as plt
from datetime import datetime 
from datetime import timedelta
import numpy as np
from time import sleep
import time


plt.rcParams['font.sans-serif']=['SimHei']

# y = [1, 2, 200, 5000]
# 创建一个画布
# plt.figure()
# 创建一条线

x = []
y = []

with open("data.txt", "r", encoding="utf-8") as f1:
    for line in f1.readlines()[-4:]:
        # 分割line
        line = line.strip().split()
        x1 = time.strftime("%H:%M", time.localtime(float(line[0])))
        y1 = int(line[1])                 # 把字符串转换为整数
        x.append(x1)
        y.append(y1)

# x = [ i.strftime("%H:%M") for i in [date1, date2, date3, date4]]
# y = [10, 0, 20, 97]
agraphic = plt.subplot(2,1,1)
agraphic.set_title('子图表标题1')      #添加子标题
agraphic.set_xlabel('',fontsize=10)   #添加轴标签
agraphic.set_ylabel('', fontsize=20)
# print("new_x:", new_x)
# print("x:", x)

# 发生变化的时候
# else:
    # continue    
# print(y)
print("x:", x)
print("y:", y)
agraphic.plot(x, y)
# plt.plot(x, y)



# 展现画布
plt.show()