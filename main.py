from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# -------------------- IMPORTANT -------------------- #
gd_path = "CHROMEDRIVER LOCATION"
driver = webdriver.Chrome(executable_path=gd_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


# -------------------- STORE FUNCTION -------------------- #
def what_to_buy():
    options = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment', 'buyAlchemy lab', 'buyPortal', 'buyTime machine', 'buyElder Pledge']
    store_prices = []
    store = driver.find_elements(By.CSS_SELECTOR, 'div b')
    my_cookies = driver.find_element(By.ID, "money")
    for i in store[10:18]:
        x = i.text.split()[-1]
        try:
            store_prices.append(int(x))
        except:
            y = int(re.sub(",", "", x))
            store_prices.append(y)

        try:
            money = int(my_cookies.text)
        except:
            a = my_cookies.text
            money = int(re.sub(",", "", a))
    val = 0
    for i in store_prices:
        if money >= i:
            val = i
        pos = store_prices.index(val)
    buy = driver.find_element(By.ID, f"{options[pos]}")
    buy.click()


# -------------------- TIMER FUNCTION -------------------- #
ini = int(time.time())
five_min_counter = 0


def timer():
    global ini
    global five_min_counter
    if ini+5 == int(time.time()):
        ini += 5
        five_min_counter += 1
        what_to_buy()


# -------------------- CLICK FUNCTION -------------------- #
clicker = driver.find_element(By.ID, "cookie")

while True:
    clicker.click()
    timer()
    if five_min_counter == 60:
        break

cps = driver.find_element(By.ID, "cps")
print(f"Your Cookies per Second reached: {cps.text}")
driver.quit()

