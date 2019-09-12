from datetime import datetime
import time
from selenium import webdriver

def openChrome():
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://ysweb.yonsei.ac.kr/ysbus.jsp')
    time.sleep(1)
    driver.find_element_by_id('id').send_keys('2016141088')
    time.sleep(1)
    driver.find_element_by_id('password').send_keys('s!102618')
    time.sleep(1)
    driver.find_element_by_class_name('submit').click()
    driver.get('https://ysweb.yonsei.ac.kr/busTest/index2.jsp')
    time.sleep(2)

flag = True
while flag :
    ttt = input('Enter when you want to alarm, ex : 1400 -> 2:00 p.m.\n')
    targetTime = {'hour' : int(ttt[:2]), 'minute' : int(ttt[2:])}
    
    isNotTime = True
    while isNotTime :
        now = datetime.now()
        print('Time is {0} {1} {2}'.format(now.hour, now.minute, now.second))
        if targetTime['hour'] == now.hour and targetTime['minute'] == now.minute :
            print('Time is now!!')
            openChrome()
            isNotTime = False
            flag = False
        else :
            print('now wating...')
            time.sleep(5)