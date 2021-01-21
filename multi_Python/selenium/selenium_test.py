from selenium import webdriver

path = "C:\\Users\\bumjh\\Desktop\\Study\\multi_Python\\Pandas\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://github.com/login")
print(driver.title)

search_box = driver.find_element_by_id("login_field")
search_box.send_keys("bumjh0121@gmail.com")
search_box = driver.find_element_by_id("password")
search_box.send_keys("wlsgus0121!")

search_box.submit()

profile = driver.find_element_by_xpath("/html/body/div[1]/header/div[4]/a")
driver.get(profile.get_attribute('href'))
