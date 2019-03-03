from selenium import webdriver
qspider=webdriver.Chrome(executable_path="G:/Downloads/New folder/chromedriver/chromedriver.exe")
qspider.get("https://www.facebook.com/")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("email").send_keys("rinimukkathu@gmail.com")
qspider.find_element_by_name("pass").send_keys("rinipaul")
qspider.find_element_by_id("u_0_8").click()