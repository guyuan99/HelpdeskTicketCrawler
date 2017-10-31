from selenium import webdriver

chrome_path= r"D:\Simple Python Crawler\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver = webdriver.PhantomJS(chrome_path)
driver.get("http://indyhelpdesk:8080/HomePage.do")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("yuangu")
password.send_keys("asd123!@#")

driver.find_element_by_xpath('//*[@id="loginFormDiv"]/form/table/tbody/tr[6]/td[2]/table/tbody/tr/td[3]/input').click()
driver.find_element_by_xpath('//*[@id="Requests"]').click()

posts=driver.find_elements_by_css_selector("a[rel='uitooltip-track']")
for post in posts:
	print(post.text+"\n")
