from datetime import datetime
from datetime import timedelta
import time

# 获取画面的point
def get_point(x, y, max_x_len, max_y_len, startX, endX, startY, endY):
    point_x = max_x_len * (x - startX) / (endX - startX)     # 转换数据中的x的值为画面中的值
    point_y = max_y_len * (y - startY) / (endY - startY)     # 转换数据中的y的值为画面中的值
    return {"x": x, "y": y}


if __name__ == "__main__":
    print(datetime.now().strftime("%Y"))
    # print("test")
    # endDateC = datetime.now()
    # endTime = time.mktime(endDateC.timetuple())
    # print("end time:", endTime)
    # startDateC = endDateC - timedelta(minutes=5)
    # startTime = time.mktime(startDateC.timetuple())
    # print("start time:", startTime)
    # with open("data.txt", "r", encoding="utf-8") as f1:
    #     for line in f1.readlines():
    #         print(line.strip())