from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import keyboard
import pyautogui

words = ""
import keyboard

service = Service('C:/chromedriver/chromedriver.exe')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.typeracer.com/")


keyboard.wait("ctrl+alt")

source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')

span = soup.findAll("span")

for i in span:
    if "unselectable" in str(i):
        words = words + i.text

if not words:
    print("none found")
else:
    time.sleep(1)
    pyautogui.write(words, interval=0.02)


        

