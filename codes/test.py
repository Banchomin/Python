# warning 파일 이름은 절대 selenium으로 만들지 않기

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

naver = "https://www.naver.com"

driver.get(naver)
time.sleep(2)


time.sleep(10)

# # 3초 동안 쉬기(멈추기)
# time.sleep(3)

# # 웹 브라우저 종료
# driver.quit()
