#coding=utf-8
import requests
from selenium import webdriver
import time
from  PIL import Image

# 实例化浏览器
driver = webdriver.Chrome()

# 设置窗口大小
driver.set_window_size(1920,1080)
# 最大化窗口
# driver.maximize_window()

# 发送请求
driver.get('https://www.baidu.com/')

# .page_source是获取网页的全部html
# print(driver.page_source)

# 进行页面截屏
driver.save_screenshot("./baidu.png")


# 网页元素定位,输入关键词并搜索
driver.find_element_by_id('kw').send_keys('Python深度学习 pdf')
driver.find_element_by_id('su').click()
time.sleep(5)

# 当前搜索结果页面的链接
print("current_url: ",driver.current_url)

# 保存搜索结果页面
driver.save_screenshot("./搜索结果.png")

# 保存第一条结果的截图
first_result = driver.find_element_by_id('2')
left = first_result.location['x']
top = first_result.location['y']
right = first_result.location['x'] + first_result.size['width']
bottom = first_result.location['y'] + first_result.size['height']

im = Image.open("./搜索结果.png")
# im = im.crop((left - 5, top - 5, right + 5 , bottom + 5))
im = im.crop((left,top,right,bottom))
im.save('./第一条搜素结果.png')


# driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("*"*100)
# cookies = {i["name"]:i["value"] for i in cookies}
# print(cookies)


# 退出浏览器
driver.quit()


