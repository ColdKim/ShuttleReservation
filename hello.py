from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def isRightInput(ttt):
	if len(ttt) != 4 :
		return False
	if not ('00' <= ttt[:2] and '23' >= ttt[:2]):
		return False
	if not ('00' <= ttt[:2] and '59' >= ttt[2:]):
		return False
	return True

while True :
	ttt = input('Enter when you want to alarm, ex : 1400 -> 2:00 p.m.\n')
	if isRightInput(ttt):
		targetTime = {'hour' : int(ttt[:2]), 'minute' : int(ttt[2:])}
		break
while True :
	ttt = input('Enter when you want to Sinchon -> International, ex : 1400 -> 2:00 p.m.\nIf you do not want, enter "x"\n')
	if ttt == 'x':
		sinchon = 'nope'
		break
	if isRightInput(ttt):
		sinchon = {'hour' : ttt[:2], 'minute' : ttt[2:]}
		break
while True :
	ttt = input('Enter when you want to International -> Sinchon, ex : 1400 -> 2:00 p.m.\nIf you do not want, enter "x"\n')
	if ttt == 'x':
		international = 'nope'
		break
	if isRightInput(ttt):
		international = {'hour' : ttt[:2], 'minute' : ttt[2:]}
		break

print('\n'+'-' * 10)
print('At {0}:{1}, program will reserve for you'.format(targetTime['hour'], targetTime['minute']))
if sinchon != 'nope' :
	print('Sinchon -> International {0}:{1}'.format(sinchon['hour'], sinchon['minute']))
if international != 'nope' :
	print('International -> Sinchon {0}:{1}'.format(international['hour'], international['minute']))
print('-' * 10 + '\n')



def login(driver):
	driver.get('https://ysweb.yonsei.ac.kr/ysbus.jsp')
	driver.find_element_by_id('id').send_keys('2016141088')
	pwd = driver.find_element_by_id('password')
	pwd.send_keys('s!102618')
	pwd.send_keys(Keys.ENTER)
	#driver.find_element_by_id('password').send_keys('s!102618')
	#driver.find_element_by_class_name('submit').click()
	driver.get('https://ysweb.yonsei.ac.kr/busTest/index2.jsp')

def selectDate(driver):
	driver.find_elements_by_css_selector('select#selectedDate option')[-1].click()

def reserve(driver, reserveTime, startingPoint):
	ls = driver.find_elements_by_css_selector('ul.ty2 li')
	if startingPoint == 'sinchon':
		ls[0].find_element_by_tag_name('a').click()
	else:
		ls[1].find_element_by_tag_name('a').click()

	trList = driver.find_elements_by_css_selector('table.display tbody tr')
	for tr in trList :
		#print(tr.find_element_by_tag_name('td').text[:5])
		tdList = tr.find_elements_by_tag_name('td')
		startTime = tdList[0].text[:5]
		if startTime[:2] == reserveTime['hour'] and startTime[3:] == reserveTime['minute'] :
			#print(tdList[3].text)
			tdList[4].find_elements_by_tag_name('option')[1].click()
			try :
				tdList[5].find_element_by_tag_name('a').click()
				print('Starting from '+startingPoint+' bus is reserved!')
			except :
				print('Starting from '+startingPoint+' bus is full booked... T^T')
			break

isNotTime = True
while isNotTime :
	now = datetime.now()
	print('Time is {0} {1} {2}'.format((now.hour+9)%24, now.minute, now.second))
	if targetTime['hour'] == (now.hour+9)%24 and targetTime['minute'] == now.minute :
		print('Time is now!!')
		driver = webdriver.PhantomJS('/workspace/ShuttleReservation/ShuttleReservation/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
		login(driver)
		selectDate(driver)
		if sinchon != 'nope':
			reserve(driver, sinchon, 'sinchon')
		if international != 'nope':
			reserve(driver, international, 'international')
		driver.save_screenshot('1.png')
		isNotTime = False
	else :
		print('now wating...')
		time.sleep(5)