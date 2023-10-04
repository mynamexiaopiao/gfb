import math

from selenium import webdriver
from lxml import etree
import time
from matplotlib import pyplot as plt
class getString:
    def __init__(self, BV):
        self.BV = BV

    #获取播放量
    def get(self):
        #隐藏窗口
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        #创建
        driver = webdriver.Chrome(options=option)

        driver.get(f"https://www.bilibili.com/video/{self.BV}")

        selector = etree.HTML(driver.page_source)
        #字符串处理
        links = selector.xpath('//*[@id="viewbox_report"]/div/div/span[1]/text()')
        lin = " ".join(links)
        lind = lin.replace('\n',"").replace(" ", "")
        if '万' in lind:
            end_lind = int(float(lind[:-1])*10000)
            return end_lind
        else:
            return int(lind)


#time为秒
def view_list_get(the_time,times):
    view_list = []
    for i in range(times):
        print(f"开始获取第{i+1}次播放量")
        num = getString("BV1vw411i7Cb").get()
        view_list.append(num)
        time.sleep(the_time)
    return view_list

def view_list_linechart(view_list,tim,ti):
    r = range(tim,(ti+1)*tim,tim)
    plt.plot( r,view_list)

    plt.show()




