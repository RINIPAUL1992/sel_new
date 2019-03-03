from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[text()='Movies']").click()
driver.find_element_by_xpath("//a[text()='Events']").click()
driver.back()
driver.forward()
driver.refresh()