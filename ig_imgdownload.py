from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
from datetime import datetime


PATH = 'C:/Users/Kyrie-PC/Desktop/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')

#先等待username.password name出現
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

#XPATH抓登入的位置
login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')

#清空對話框,以防有預設文字
username.clear()
password.clear()
#輸入帳號密碼
username.send_keys('你的帳號')
password.send_keys('你的密碼')
#按下確認
login.click()

#登入之後一樣等待收尋欄位

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

#定義關鍵字
keyword = '#dog'
#輸入關鍵字
search.send_keys(keyword)
#停一秒
time.sleep(1)
#回車鍵
search.send_keys(Keys.RETURN)
#停一秒
time.sleep(1)
#回車鍵
search.send_keys(Keys.RETURN)

#登入之後等待IMG CLASS
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aagt"))
)

#JS把進度條往下拉(不拉的話只有32張照片) 可以多跑幾次多一些照片
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

#定義IMGS的CLASS NAME
imgs = driver.find_elements(By.CLASS_NAME,'_aagt')

#下載路徑+時間戳
path = os.path.join(keyword) + '_' + datetime.now().strftime("%Y%m%d_%H%M%S")

#建立路徑
os.mkdir(path)

count = 0
for img in imgs:
    #第一個參數是路徑,第二參數是名稱
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    #print(img.get_attribute('src'))
    #wget抓圖片src存到save_as裡面
    wget.download(img.get_attribute('src'), save_as)
    count += 1
