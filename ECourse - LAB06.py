from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('Kurs dla zaawansowanych - LAB\chromedriver.exe')
driver.get('https://www.udemy.com/')

element = driver.find_elements_by_class_name('udlite-btn udlite-btn-medium udlite-btn-secondary udlite-heading-sm')
print(element)

time.sleep(10)

element2 = driver.find_element_by_id('email--1')
element2.clear()
element2.send_keys('proko.piotr@gmail.com')
time.sleep(10)

element3 = driver.find_element_by_id('id_password')
element2.clear()
element2.send_keys('HomeOne123')

time.sleep(10)