from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import re

def insert_str(text, containString, insertString):
    """
    containString: 包含的字符串location、server、
    """
    list_text = text.split("\n")
    cut_space_list_text = [i.strip() for i in list_text]
    # print(cut_space_list_text)
    index = 0
    # if insertString in cut_space_list_text:
    #     print("已经存在了")
    #     exit(1)
    if containString == "server":
        flg = 0
        flg1 = 0
        # for line in list_text:
        #     if line.strip() == insertString.strip():
        #         print("fffffffffffff_server")
        #         continue
        for line in list_text:
            # if line.strip() == insertString.strip():
            #     print(line.strip())
            #     print("yes")
            #     index = index + 1
            #     continue
                # continue
            if flg == 1:
                flg = 0
                index = index + 1
                continue
            if re.match("server\s*{", line):   # 如果是server\s*{}
                # print("server.............")
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

# text = insert_str(text, "location", "proxy_pass www.baidu.com;")
text = insert_str(text, "location", "client_max_body_size 1m;")
text = insert_str(text, "location", "client_max_body_size 1m;")
params = [
    'gzip on;',
    'gzip_min_length 2k;',
    'gzip_buffers   4 32k;',
    'gzip_http_version 1.1;',
    'gzip_comp_level 6;',
    'gzip_typestext/plain text/css text/javascriptapplication/json application/javascript application/x-javascriptapplication/xml;',
    'gzip_vary on;',
    'gzip_proxied any;',
]

for p in params:
    text = insert_str(text, "location", p)

wd.execute_script('document.getElementById("ta1").value = "%s"' % text.replace("\n", "\\n"))
# element = wd.find_element_by_css_selector('li a[href="//www.mi.com/p/9289.html"]')
# ac = ActionChains(wd)
# ac.move_to_element(element).perform()
# element = wd.find_element_by_xpath('//span[@class="text"][text()="小米手表"]/../img')
# print(element.get_attribute("outerHTML"))
# ac.click(element).perform()
# selectOption = ["促销 "]
# wd.maximize_window()
# for s in selectOption:
#     checkbox = wd.find_element_by_xpath('//a[contains(., "%s")]' % s)
#     checkbox.click()
#     print(checkbox.get_attribute("outerHTML"))

# pass