# 规则是test_开头
import time
from selenium import webdriver

from actions.login import login


def test_login():
    # 调用你的测试业务，传入测试数据，实现测试
    # 测试数据是不存在的用户名和一个正常的密码
    driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
    #打开网址
    driver.get('http://121.42.15.146:9090/mtx/')
    login(driver,'sdffddfff','123456')
    # 如何判断结果，断言
    # 判断页面内容里是否包含了“账号不存在”这几个字
    # 如果存在成功，不存在失败
    time.sleep(1) # 等待1秒
    page_source = driver.page_source # 表示获取页面所以源码内容
    assert '登录' in page_source

