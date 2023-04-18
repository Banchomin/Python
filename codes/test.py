# warning 파일 이름은 절대 selenium으로 만들지 않기

# selenium
from selenium import webdriver

# 선택자 사용시 By 사용
from selenium.webdriver.common.by import By

# key 입력
from selenium.webdriver.common.keys import Keys

# 복붙
import pyperclip

# time.sleep 사용
import time

# -------------------------------------------------

# Chrome driver 사용
driver = webdriver.Chrome()

# naver URL
naver = "https://www.naver.com"

# naver URL로 들어가기
driver.get(naver)
# 1초 쉬기
time.sleep(1)

# -------------------------------------------------

# 로그인 버튼의 XPATH
login_btn = "/html/body/div[2]/div[3]/div[3]/div/div[2]/a"
# XPATH로 요소 찾기
element = driver.find_element(By.XPATH, login_btn)
# 요소 클릭
element.click()

# 1초 쉬기
time.sleep(1)

# -------------------------------------------------

# USER INFO
user_id = "ryusw14"
user_pw = "ryusw14@gmail.pw"

# id input
id_input = "/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[1]/input"
# password input
pw_input = "/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[2]/input"

pyperclip.copy(user_id)
driver.find_element(By.XPATH, id_input).send_keys(Keys.CONTROL, "v")

time.sleep(2)

pyperclip.copy(user_pw)
driver.find_element(By.XPATH, pw_input).send_keys(Keys.CONTROL, "v")

time.sleep(3)
# -------------------------------------------------
