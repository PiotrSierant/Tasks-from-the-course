from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('Kurs dla zaawansowanych - LAB\chromedriver.exe')
browser.get('https://strefakursow.pl/')

elem = browser.find_element_by_name("search_course[name]")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(10)

browser.close()