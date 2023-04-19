from selenium import webdriver
import time
import os
#from selenium.webdriver.chrome.options import Options

#options = Options()
#options.binary_location= '/workspace/test1/chrome/Application/chrome.exe'

#print("================dr started")
#os.environ['PATH'] += "/workspace/test1/chromedriver.exe"
#dr = webdriver.Chrome('path/chromedriver_win32/chromedriver.exe', chrome_options = options)
#dr.set_window_size(414, 800) #브라우저 크기 414*800으로 고정
#dr.get('https://lms.kau.ac.kr/login.php') #LMS 접속
dr = webdriver.Chrome("C:/windows/chromedriver.exe")
dr.set_window_size(414, 800)  # 브라우저 크기 414*800으로 고정
dr.get('https://lms.kau.ac.kr/login.php')  # LMS 접속
time.sleep(1)  # 반초 대기
#time.sleep(1)
print("================dr closed")
dr.close()