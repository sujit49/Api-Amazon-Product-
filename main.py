from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?crid=2XVC11P6R6FEG&dib=eyJ2IjoiMSJ9.JCyn2nZZp1sOG9u3pnBnukIPry2sbigHOVAW_O_7ys2-0MwA5zNvaOrYYGeTxhUP7cyCW4HHRXlfXi6q0S03lxPuIau6Euk_xufh2-4jkojsYmKA7cBiXPZOwmeVCn3mmga_R6Gf9pby58g1jeyVBRX3AS5UhI_8cmzD4aQI1mEXifBU3rOLqkGJaNo-wMGQefgeOBxCxyGRm0ddW_DsUaiNyWSFjZwrT1Kt3OWQzEw.b8wmBW6o0SUsDatnFkQK6Rxh8MMmYMkogJZmvoy7C3M&dib_tag=se&keywords=instant+pot+duo+plus+9-in-1&qid=1722186000&sprefix=instant+pot+duo+plus+%2Caps%2C284&sr=8-1")

#price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents =driver.find_element(By.CLASS_NAME,value = "a-price-fraction")
#print(f"The price is{price_dollars.text}.{price_cents.text}")

#search_bar = driver.find_element(By.NAME , value="q")
#print(search_bar.get_attribute("placeholder"))
#button = driver.find_element(By.ID , value="submit")
#print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value="documentation-widget a ")

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

tier_1 =driver.find_elements(By.CLASS_NAME,value="tier-1")

event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
for time in  event_times:
    print(time.text)

driver.quit()

