# warning 파일 이름은 절대 selenium으로 만들지 않기

# selenium
from selenium import webdriver

# 선택자 사용시 By 사용
from selenium.webdriver.common.by import By

# key 입력
from selenium.webdriver.common.keys import Keys

# time.sleep 사용
import time

# Chrome driver 사용
driver = webdriver.Chrome()

# naver URL
naver = "https://www.naver.com"

# naver URL로 들어가기
driver.get(naver)
# 2초 쉬기
time.sleep(2)

# 로그인 버튼의 XPATH
login_btn = "/html/body/div[2]/div[3]/div[3]/div/div[2]/a"
# XPATH로 요소 찾기
element = driver.find_element(By.XPATH, login_btn)
# 요소 클릭
element.click()

time.sleep(10)
