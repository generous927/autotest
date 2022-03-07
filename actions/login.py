from selenium import webdriver




def login(driver,username,pwd):

    # driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
    # 打开网址
    # driver.get('http://121.42.15.146:9090/mtx/')
    # 点击登录并进入登录页面
    driver.find_element_by_link_text('登录').click()
    # 输入用户名
    driver.find_element_by_name('accounts').send_keys(username)
    # 输入密码
    driver.find_element_by_name('pwd').send_keys(pwd)
    # 点击登录按钮,class如果包含了空格，需要使用空格分隔的一部分进行定位
    driver.find_element_by_class_name('btn-loading-example').click()
if __name__=='__main__':
    driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
    #打开网址
    driver.get('http://121.42.15.146:9090/mtx/')


# login(driver,"shamotest1",'123456')