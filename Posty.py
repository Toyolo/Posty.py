from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

user = []
pswrd = []
post = []
maxLengthList = 1

#login =

def wait(x):
    time.sleep(x)

def getPostInput():
    while len(post) < maxLengthList:
        item = input("what would you like to say?")
        post.append(item)

def getUser():
    while len(user) < maxLengthList:
        item = input("Email:")
        user.append(item)

def getPswrd():
    while len(pswrd) < maxLengthList:
        item = input("Password:")
        user.append(item)

getUser()

wait(3)

getPswrd()

wait(3)

getInput()

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

driver.get('https://www.facebook.com')
#this will locate the login parameters and log me in
emailBox = driver.find_element_by_xpath('//*[@id="email"]')
emailBox.send_keys(user)

wait(3)

passBox = driver.find_element_by_xpath('//*[@id="pass"]')
passBox.send_keys(pswrd)

login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()


wait(15)

textbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea')

wait(8)

textbox.send_keys(post)

wait(10)

postBut = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button').click()


wait(5)

driver.quit()
