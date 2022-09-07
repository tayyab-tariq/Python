from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def complaints():
    sms = "Hi, How Are You Doing"   #   Enter your Message Here
    time.sleep(2)
    grp_name ="Tayyab"          #   Enter Your Group/Contact Name Here
    try:
        box_search = WebDriverWait(driver,20).until(lambda driver: driver.find_element(By.XPATH, '//button[@data-testid="icon-search-morph"]'))   # Tries to find element for 20 seconds     
        box_search.click()
        box_search.send_keys(Keys.CONTROL + 'a')
        box_search.send_keys(grp_name)
        time.sleep(1)
        box_search.send_keys(Keys.ENTER)
        time.sleep(1)

        try:
            group = driver.find_element(By.XPATH, '//span[@title="{}"]'.format(grp_name))
            group.click()

            text_box = driver.find_element(By.CLASS_NAME, 'p3_M1')
            text_box.send_keys(sms)

            send_btn = driver.find_element(By.XPATH, '//button[@data-testid = "compose-btn-send"]')
            send_btn.click()

        except Exception as err:
            print(f"Unable To Post Message On Whatsapp: {err}")
    except:
        print("Unable to Load Web Page or Label Not Found")

options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
try:
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)          #   Wait For Page to Load
    count = int(input("Enter No. of Messages: "))       #   Only Input If you are Logged In. You can also implement your own logic.
    for i in range(count):
        complaints()
    print("Ending Execution")
except Exception as error:
    print(error)

