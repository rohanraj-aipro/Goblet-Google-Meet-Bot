# Made By Hacker--Rohan Raj
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
  
print('''
  ________      ___.   .__          __   
 /  _____/  ____\_ |__ |  |   _____/  |_ 
/   \  ___ /  _ \| __ \|  | _/ __ \   __\
\    \_\  (  <_> ) \_\ \  |_\  ___/|  |  
 \______  /\____/|___  /____/\___  >__|  
        \/           \/          \/      
''')


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('^                                                               ^')
print('^              ###   A Simple Google Meet Bot     ###           ^')
print('^                                                               ^')
print('^                                                               ^')
print('^              ###   Made By :- Hacker-- Rohan Raj ###          ^')
print('^                                                               ^')
print('^                                                               ^')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Some Changes have to be made in the Script')
print('In This Python Script, go to line 82 and type your G-mail address ')
print('In This Python Script, go to line 82 and type your Password ')
print('In This Python Script, go to line 96 and type the Path of your chromedriver ')
print('Example :-  C:\Your_Name\chromedriver.exe')
print('Or Download Chrome Driver Latest Version From Here:-')
print('https://chromedriver.chromium.org/downloads')
def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
  
    # Google Page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)
  
  
def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
  
    # turn off camera
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)
  
  
def joinNow():
    # Join meet
    print(1)
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)
  
  
def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
  
# assign email id and password
mail_address = 'Your GMAIL Please'
password = 'Your Password Please'
  
# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome('D:\Rohan\Python\chromedriver.exe')
  
# login to Google account
Glogin(mail_address, password)
  
# go to google meet
driver.get('https://meet.google.com/htr-onhp-eht')
turnOffMicCam()
# AskToJoin()
joinNow()