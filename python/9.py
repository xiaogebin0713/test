import matplotlib.pyplot as plt
# import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from scipy import signal
import np
 
def choose_peek_valleys(peekArg, valleysArg):
    list1 = []
    for i in peekArg:
        for j in range(1, len(valleysArg)-1, 1):
            if i > valleysArg[j] and i < valleysArg[j+1]:
                list1.append([valleysArg[j], i, valleysArg[j+1]])
                break
    return list1

#设置距离
# x =np.array([0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 70, 8, 9, 10])
x = np.array([1595151000, 1595151060, 1595151120, 1595151180, 1595151240, 1595151300, 1595151360, 
    1595151420, 1595151480, 1595151540, 1595151600, 1595151660, 1595151720,1595151780, 1595151840, 
    1595151900, 1595151960,])
 
#设置相似度
y =np.array([0.8579087793827057, 0.8079087793827057, 0.9679087793827057, 0.679087793827057,
    0.5579087793827057, 0.9579087793827057, 0.3079087793827057, 0.3009087793827057,
    0.2579087793827057, 0.2009087793827057, -0.1999087793827057, 0.9579087793827057,
    0.0099087793827057, 0.0079087793827057, 0.0069087793827057, 0.0019087793827057,
    0.0000087793827057])
 
#插值法之后的x轴值，表示从0到10间距为0.5的200个数
xnew =np.arange(1595151000,1595151960, 0.1)
 
#实现函数
func = interpolate.interp1d(x,y,kind='cubic')
 
#利用xnew和func函数生成ynew,xnew数量等于ynew数量
ynew = func(xnew)
 
# 原始折线
plt.plot(x, y, "r", linewidth=1)
 
#平滑处理后曲线
plt.plot(xnew, ynew)
#设置x,y轴代表意思
plt.xlabel("The distance between POI  and user(km)")
plt.ylabel("probability")
#设置标题
plt.title("The content similarity of different distance")
#设置x,y轴的坐标范围
plt.xlim(1595151000, 1595151960, 8)
# plt.ylim(-1,1)

peaks, properties = find_peaks(ynew, prominence=0.8, height=0.6, width=120, distance=2 * 60)
print("properties:", properties)
print(xnew[peaks])
# print(len(xnew))
plt.plot(xnew[peaks], ynew[peaks], "x")
# plt.plot(np.zeros_like(x), "--", color="gray")
plt.plot(xnew[signal.argrelextrema(ynew, np.less)[0]], ynew[signal.argrelextrema(ynew, np.less)], '+', markersize=10)
print(xnew[signal.argrelextrema(ynew, np.less)[0]])

# x = electrocardiogram()[17000:18000]
# print(x)
print(choose_peek_valleys(xnew[peaks], xnew[signal.argrelextrema(ynew, np.less)[0]]))
plt.show()