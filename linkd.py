from selenium import webdriver
qspider=webdriver.Chrome(executable_path="G:/Downloads/New folder/chromedriver/chromedriver.exe")
qspider.get("https://in.linkedin.com/")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("login-email").send_keys("rinimukkathu@gmail.com")
qspider.find_element_by_name("session_password").send_keys("rinipaul")
qspider.find_element_by_id("login-submit").click()