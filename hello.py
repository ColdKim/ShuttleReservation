from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def openChrome():
    driver = webdriver.PhantomJS('/workspace/ShuttleReservation/ShuttleReservation/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    time.sleep(1)
    driver.get('https://ysweb.yonsei.ac.kr/ysbus.jsp')
    time.sleep(1)
    driver.find_element_by_id('id').send_keys('2016141088')
    time.sleep(1)
    pwd = driver.find_element_by_id('password')
    pwd.send_keys('s!102618')
    #driver.find_element_by_id('password').send_keys('s!102618')
    time.sleep(1)
    pwd.send_keys(Keys.ENTER)
    #driver.find_element_by_class_name('submit').click()
    time.sleep(1)
    driver.get('https://ysweb.yonsei.ac.kr/busTest/index2.jsp')
    time.sleep(1)
    print(driver.find_element_by_css_selector('span.en').text)
    driver.save_screenshot('1.png')
    
flag = True
while flag :
    ttt = input('Enter when you want to alarm, ex : 1400 -> 2:00 p.m.\n')
    targetTime = {'hour' : int(ttt[:2]), 'minute' : int(ttt[2:])}
    print(targetTime)
    isNotTime = True
    while isNotTime :
        now = datetime.now()
        print('Time is {0} {1} {2}'.format(now.hour+9, now.minute, now.second))
        if targetTime['hour'] == now.hour+9 and targetTime['minute'] == now.minute :
            print('Time is now!!')
            openChrome()
            isNotTime = False
            flag = False
        else :
            print('now wating...')
            time.sleep(5)