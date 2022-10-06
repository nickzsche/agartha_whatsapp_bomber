import chromedriver_autoinstaller
import sqlite3
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from PyQt5.QtCore import *
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")
time.sleep(25)
name = "Test 3"
number = 50
searchbox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
searchbox.click()
searchbox.send_keys(name)
time.sleep(3)
user = driver.find_element_by_class_name('_3vPI2')
#user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
try:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('p3_M1')
    msg = ("1")
    for i in range(number):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
except:
    user.click()
    time.sleep(0.5)
    msg_box = driver.find_element_by_class_name('p3_M1')
    msg = ("2")
    for i in range(number):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
time.sleep(300)
driver.close()
