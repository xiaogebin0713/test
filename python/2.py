import matplotlib.pyplot as plt
from datetime import datetime 
from datetime import timedelta
import numpy as np
from time import sleep

def get_times():
    now = datetime.now()
    f4 = now - timedelta(minutes=1)
    f3 = now - timedelta(minutes=2)
    f2 = now - timedelta(minutes=3)
    f1 = now - timedelta(minutes=4)
    return [ i.strftime("%H:%M") for i in [f1, f2, f3, f4] ]


x = get_times()
y = np.random.normal(loc=0, scale=100, size=4)
plt.rcParams['font.sans-serif']=['SimHei']
plt.ion()
while True:
    plt.clf()
    
    # y = [1, 2, 200, 5000]
    # 创建一个画布
    # plt.figure()
    # 创建一条线

    agraphic = plt.subplot(2,1,1)
    agraphic.set_title('子图表标题1')      #添加子标题
    agraphic.set_xlabel('',fontsize=10)   #添加轴标签
    agraphic.set_ylabel('', fontsize=20)
    new_x = get_times()
    # print("new_x:", new_x)
    # print("x:", x)

    # 发生变化的时候
    if x[0] != new_x[0]:
        y = np.random.normal(loc=0, scale=100, size=4)
        x = new_x
        # plt.pause(0.4)
    # else:
        # continue    
    # print(y)
    agraphic.plot(x, y)
    # plt.plot(x, y)

    # 设置标题
    plt.suptitle("测试")
    plt.pause(5)
    sleep(5)

# 展现画布
plt.ioff()
plt.show()