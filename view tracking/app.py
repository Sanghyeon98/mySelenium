from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach",True)
chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options)

query="python flask"
search_link = f"https://search.naver.com/search.naver?ssc=tab.cafe.all&sm=tab_jum&query={query}"
driver.get(search_link)
input()