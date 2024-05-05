from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.naver.com")
time.sleep(3)
css_selector ="#shortcutArea > ul > li:nth-child(4)"
그룹_네비게이션 = driver.find_element(By.CSS_SELECTOR, css_selector)

print(그룹_네비게이션.text)
그룹_네비게이션.click()
input()