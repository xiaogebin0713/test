from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import re
import json

def analysis(str1):
    str_arg = str1.split("\n")
    flg = 0   # 初始化标识符
    # 参数
    params = {}
    unit = ""
    for line in str_arg:
        if re.match("^\s*#.*", line):
            continue
        line = line.strip()
        # 读取单元
        ret = re.match("^\[([^\[\]]*)\]$", line)
        if ret:
            # 获取到单元的标识符
            unit = ret.group(1)
            params[unit] = []
            flg = 1
            print("unit:", unit)
            continue
            
        if flg == 1 and line is not None:
            # 如果获取到标识符则添加参数到数组
            params[unit].append(line)
    return params


def insert_str(text, containString, insertString):
    """
    containString: 包含的字符串location、server、
    """
    list_text = text.split("\n")
    cut_space_list_text = [i.strip() for i in list_text]
    index = 0
    if containString == "server":
        flg = 0
        flg1 = 0
        for line in list_text:
            if flg == 1:
                flg = 0
                index = index + 1
                continue
            if re.match("server\s*{", line):   # 如果是server\s*{}
                flg1 = 1
            if flg1 == 1:
                if line.strip() == insertString.strip():
                    print("已存在: ", insertString)
                    return text
                    # continue
            if re.match("\s*location.*{\s*", line) and flg1 == 1:
                # index = index + 1
                list_text.insert(index, line[:(len(line) - len(line.lstrip()))] + "%s" % insertString)
                flg1 = 0
                flg = 1
            index = index + 1

    elif containString == "location":
        # print("location.............")
        flg = 0
        flg1 = 0
        for line in list_text:
            
            if flg == 1:
                flg = 0
                index = index + 1
                continue
            if flg1 == 1:
                flg1 = 0
                if line.strip() == insertString.strip():
                    # index = index + 1
                    print("line:", line)
                    print("已存在: ", insertString)
                    return text
            # print(re.match("\s*location\s*/\s*{\s*", line))
            if re.match("\s*location\s*/\s*{\s*", line):   # 如果是server\s*{}
                # print("match location")
                index = index + 1
                list_text.insert(index, "    " + line[:(len(line) - len(line.lstrip()))] + "%s" % insertString)
                flg = 1
                flg1 = 1
                continue
            index = index + 1
    # print('\n'.join(list_text))
    return '\n'.join(list_text)

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
wd = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
wd.implicitly_wait(5)
wd.get('http://localhost:8888/index')
element = wd.find_element_by_id("s1")
s = Select(element)
s.select_by_visible_text("3")


ta1 = wd.find_element_by_id("ta1")
text = ta1.text

comment = wd.find_element_by_id("comment").text
print(comment)
params = analysis(comment)             # 把内容解析成字典


for k, v in params.items():
    for i in v:
        i = i.strip()
        print("i:", i)
        if i != "":
            text = insert_str(text, k, i)

wd.execute_script('document.getElementById("ta1").value = "%s"' % text.replace("\n", "\\n"))
