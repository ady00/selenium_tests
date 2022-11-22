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
time.sleep(3) # incrementable
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

temp_song = soup.find_all("div", {"class": "col-8"})

song_array = []

for song in temp_song:
    song_array.append(song.decode_contents().strip()) 

song_array.pop(0)
print(song_array)



temp_votes = soup.find_all("div", {"class": "col-4"})

vote_array = []

for song in temp_votes:
    vote_array.append(song.decode_contents().strip()) 

song_array.pop(0) 
print(song_array)





