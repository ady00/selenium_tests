from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = './chromedriver'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

url = "https://qvoter.vercel.app/election?election=ef9a120b-07fe-4aff-99a4-701af84ccfae"
driver.get(url)
time.sleep(3) #if you want to wait 3 seconds for the page to load
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())