from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from bs4 import BeautifulSoup
geckodriverpath = "C:/PUT/THE/PATH/TO/YOUR/GECKODRIVER"


email = input('Enter your email or username: ')
password = input('Enter your password: ')


browser = webdriver.Firefox(executable_path=geckodriverpath)
browser.get('https://instagram.com')
sleep(2)
email2 = browser.find_element_by_name('username')
pass2 = browser.find_element_by_name('password')
email2.send_keys(email)
sleep(1)
pass2.send_keys(password)
pass2.send_keys(Keys.RETURN)
print("Logging in..")
twofa = input("Enter your 2FA Code (if you dont have one leave blank): ")
if twofa != "":
    vericode = browser.find_element_by_name('verificationCode')
    vericode.send_keys(twofa)
    vericode.send_keys(Keys.RETURN)
elif twofa == "":
    print("Not entering 2fa code, continuing!")
sleep(15)
succsucc = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
succsucc.click()
searchstring = input("What do you want to search for?: ")
succsucctucc = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
succsucctucc.send_keys(searchstring)
sleep(4)
succsucctucc.send_keys(Keys.RETURN)
succsucctucc.send_keys(Keys.RETURN)
succsucctucc.send_keys(Keys.RETURN)
succsucctucc.send_keys(Keys.RETURN)

URL = "https://instagram.com/" + searchstring

def scrape(username):
    r = requests.get(URL)
    s = BeautifulSoup(r.text, "lxml")

    tag = s.find("meta", attrs = {"name": "description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text

usernametosucc = searchstring
data = scrape(usernametosucc)
print(data)
