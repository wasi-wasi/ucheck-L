##Install selenium
#type "pip install selenium" in the shell if you don't have selenium installed already

from selenium import webdriver
import time

from getpass import getpass

uTorID = input('Enter your uTorid:')
password = getpass()

##Download Chrome driver
#Download link "https://chromedriver.chromium.org/downloads"
#Make sure that the version of Chrome driver you download is the same as the version of Google Chrome you are using
#After downloading, unzip it and put it in any directory
#Change the PATH variable to the directory you put Chrome driver in.
#If you are a Firefox user, repeat the steps with Firefox driver


PATH = r"Enter the path to Chrome Driver here" #Make sure you change the directory here

driver = webdriver.Chrome(PATH)

driver.get("https://ucheck.utoronto.ca")
time.sleep(2)

input_username = driver.find_element_by_id('username')
input_password = driver.find_element_by_id('password')



##Enter your uTorID
input_username.clear()
input_username.send_keys(uTorID) #replace the <uTORid> with your uTORid, make sure they are in quotations
time.sleep(1)


##Enter your password
input_password.clear()
input_password.send_keys(password)#replace the <Password> with your password, make sure they are in quotations
time.sleep(1)

##If you're using pyzo, just "Ctrl+E" at this point
#Didn't want to implement input functions cause waste of time just change your credentials once and save the file and then just run the .py file everytime.

#If you did do save it, just know that anyone that can open this file can access your uTORid and Password. Only way to avoid that is to not save the file, manually change your password and utorid everysingle time and execute the file

#Currently built for desktops and laptops only probably will make a mobile version soon

#Works for windows at least, no idea about macs and linux, but it should work just fine.

submit_credentials = driver.find_element_by_name("_eventId_proceed")
submit_credentials.click()
time.sleep(2)

start_self_assessment = driver.find_element_by_css_selector('.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-fullWidth').click()
time.sleep(1)

Option_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[6]/div/div/div/div/div/div/div/div/fieldset/label[2]/span')
Option_1.click()
time.sleep(0.4)


Option_2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[8]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_2.click()
time.sleep(0.6)

Option_3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[10]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_3.click()
time.sleep(0.5)

Option_4 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[12]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_4.click()
time.sleep(0.5)

Option_5 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[14]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_5.click()
time.sleep(0.5)

Option_6 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[16]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_6.click()
time.sleep(0.5)

Option_7 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[18]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_7.click()
time.sleep(0.5)

Option_8 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[20]/div/div/div/div/div/div/div/div/fieldset/label[1]/span')
Option_8.click()
time.sleep(0.5)

submit_form = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/div/button/span[1]').click()

time.sleep(5)

driver.close()