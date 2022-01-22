from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Kurs dla zaawansowanych - LAB\chromedriver.exe')
driver.set_page_load_timeout(30)
driver.get('https://www.facebook.com')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file('./Facebook.png')
driver.find_element_by_id('email').send_keys('Proko.Piotr@gmail.com')
driver.find_element_by_name('pass').send_keys('LVLak8oJVu')
driver.find_element_by_id('u_0_j_N4').click()
driver.get_screenshot_as_file('./Facebook2.png')
driver.quit()