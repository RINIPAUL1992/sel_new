from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(10)
curr_win_id=driver.current_window_handle
print(curr_win_id)
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()

mul_win_id=driver.window_handles
print(mul_win_id)
print(type(mul_win_id))

# driver.switch_to.window(mul_win_id[1])
# driver.find_element_by_id("inputEmail").send_keys("testing")

for id in mul_win_id:
    if (id!=curr_win_id):
        driver.switch_to.window(id)
        driver.find_element_by_id("inputEmail").send_keys("testing")

# driver.close()
driver.quit()
#close