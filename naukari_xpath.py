from selenium import webdriver
qspider=webdriver.Chrome(executable_path="G:/Downloads/New folder/chromedriver/chromedriver.exe")
qspider.get("https://my.naukri.com/account/createaccount?othersrcp=16201&err=1")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_xpath("//button[contains(text(),'Fresher')]").click()
qspider.find_element_by_xpath("//input[@name='fname']").send_keys("Rini Paul")
qspider.find_element_by_xpath("//input[@id='email']").send_keys("rinimukkathu@gmail.com")
qspider.find_element_by_xpath("//input[@name='password']").send_keys("rinimukkathu123*")
qspider.find_element_by_xpath("//input[@name='number']").send_keys("8547359559")
# qspider.find_element_by_xpath("//select[@id='day']").send_keys("14")
# qspider.find_element_by_xpath("//select[@id='month']").send_keys("Feb")
# qspider.find_element_by_xpath("//select[@title='Year']").send_keys("1992")
# qspider.find_element_by_xpath("//input[@id='u_0_9']").click()
# qspider.find_element_by_xpath("//button[@name='websubmit']").click()

