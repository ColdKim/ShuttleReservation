from selenium import webdriver
import time

driver = webdriver.PhantomJS('/workspace/ShuttleReservation/ShuttleReservation/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
time.sleep(1)
driver.get('http://naver.com')
time.sleep(1)
a = driver.find_element_by_class_name('al_favorite')

print(a.text)