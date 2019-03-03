from selenium import webdriver
qspider=webdriver.Chrome(executable_path="G:/Downloads/New folder/chromedriver/chromedriver.exe")
qspider.get("file:///D:/Onedrive/Desktop/login1.html")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("123").send_keys("admin")
qspider.find_element_by_id("456").send_keys("rini")
qspider.find_element_by_id("789").click()