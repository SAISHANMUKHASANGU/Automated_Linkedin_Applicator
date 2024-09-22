from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3931156184&distance=25&f_AL=true&geoId=102713980&keywords=python&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")


signin_button=driver.find_element(By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
signin_button.click()

username=driver.find_element(By.ID,value="username")
username.send_keys("sangusaishanmukha@gmail.com")

password=driver.find_element(By.ID,value="password")
password.send_keys("shanu@2003")

signin_button_final=driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin_button_final.click()

apply_button=driver.find_element(By.ID,value='ember56')
apply_button.click()

time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys("8555017639")

next_button = driver.find_element(By.CSS_SELECTOR, value=".artdeco-button")
next_button.click()

discard_button = driver.find_element(By.ID, value="ember429")
discard_button.click()
# I AM DISCARDING IT BECAUSE IT IS JUST FOR TRIAL

driver.quit()
