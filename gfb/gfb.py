import math

from selenium import webdriver
from lxml import etree
import time
from matplotlib import pyplot as plt
class getString:
    def __init__(self, BV,way):
        self.BV = BV
        self.way = way

    def ifw(self,l):
        if '万' in l:
            end_lind = int(float(l[:-1]) * 10000)
            return end_lind
        else:
            return int(l)

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
        if self.way == "view":
            links = selector.xpath('//*[@id="viewbox_report"]/div/div/span[1]/text()')
            lin = " ".join(links)
            lind = lin.replace('\n',"").replace(" ", "")
            return self.ifw(lind)
        elif self.way == "like":
            links1 = selector.xpath('//*[@id="arc_toolbar_report"]/div[1]/div[1]/div/span/text()')
            link1 = " ".join(links1)
            return self.ifw(link1)
        elif self.way == "coin":
            links2 = selector.xpath('//*[@id="arc_toolbar_report"]/div[1]/div[2]/div/span/text()')
            link2 = " ".join(links2)
            return self.ifw(link2)
        elif self.way == "collect":
            links3 = selector.xpath('//*[@id="arc_toolbar_report"]/div[1]/div[3]/div/span/text()')
            link3 = " ".join(links3)
            return self.ifw(link3)
        elif self.way == "share":
            links4 = selector.xpath('//*[@id="share-btn-outer"]/div/span/text()')
            link4 = " ".join(links4)
            return self.ifw(link4)

#time为秒
    def view_list_get(self,the_time,times):
        view_list = []
        for i in range(times):
            print(f"开始第{i+1}次获取")
            num = getString(self.BV,self.way).get()
            view_list.append(num)
            time.sleep(the_time)
        return view_list



def view_list_linechart(view_list,tim,ti):
    r = range(tim,(ti+1)*tim,tim)
    plt.plot( r,view_list)

    plt.show()


def gethot():
        #隐藏窗口
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
        #创建
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.bilibili.com/v/popular/rank/all")
    selector = etree.HTML(driver.page_source)
    #100热榜名称
    ul = selector.xpath('//*[@class="info"]/a/text()')
    #100热榜作者
    ull = selector.xpath('//*[@class="data-box up-name"]/text()')
    for i in range(99):
        ull[i]= " ".join(ull[i]).replace('\n',"").replace(" ", "")
    lul = dict(zip(ull,ul))
    return lul






