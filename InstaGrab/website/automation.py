from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

class Auto:

    # Config. du navigateur
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Auto.chrome_options)

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/')

        cookiesBt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')))
        cookiesBt.click()

        usernameField = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))
        usernameField.send_keys(username)

        passwordField = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')))
        passwordField.send_keys(password)
        passwordField.send_keys(Keys.RETURN)
    

        try:
            notificationsBt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
            notificationsBt.click()
        except:
            pass

    def quit(self):
        self.driver.quit()

    def getCookies(self):
        return self.driver.get_cookies()
    
    def loadCookies(self, cookies):
        self.driver.get('http://www.instagram.com')
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def isLogged(self):
        self.driver.get('http://www.instagram.com')
        try:
            usernameField = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))
            return False
        except:
            return True

    def refresh(self):
        self.driver.refresh()
        try:
            notificationsBt = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
            notificationsBt.click()
        except:
            pass

    def getUsernames(self, fromAccount):
        cookies = [{'domain': '.instagram.com', 'httpOnly': True, 'name': 'rur', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"CLN\\0548497208868\\0541745200412:01f7596e257ac8f23370b508d67397c4806607896c0f2fd0828322c1fb2b5542ba4eee92"'}, {'domain': '.instagram.com', 'expiry': 1714269271, 'httpOnly': True, 'name': 'shbts', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"1713664412\\0548497208868\\0541745200412:01f7b50b76fedd1df90e643d3d1442b80b77558ad1d2cb003fc57548c972e80795c31c4a"'}, {'domain': '.instagram.com', 'expiry': 1721440471, 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8497208868'}, {'domain': '.instagram.com', 'expiry': 1745200468, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8497208868%3A7P1podmLJz0H17%3A25%3AAYfAlYsi8SZOZia9ucDVMjevXy-NeLNlnsidpeRSZQ'}, {'domain': '.instagram.com', 'expiry': 1748224468, 'httpOnly': False, 'name': 'mid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'ZiRxlgALAAFNaQKNLbKcyToksYod'}, {'domain': '.instagram.com', 'expiry': 1745114071, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'irvAoRU3MQwHUhVCQz7rm29b9GH0Js7N'}, {'domain': '.instagram.com', 'expiry': 1714269271, 'httpOnly': True, 'name': 'shbid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"15180\\0548497208868\\0541745200412:01f73ddb8c97b33f3d519de3b33c1554c27b380cb073452599f427e3f2f23602ecab75e9"'}, {'domain': '.instagram.com', 'expiry': 1748224471, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'mXEkZoDQUH4n2B2rYDN2k5Cb'}, {'domain': '.instagram.com', 'expiry': 1745200468, 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '02ED7C9E-AED0-46A2-96AE-4138D7DD8379'}]
        self.loadCookies(cookies)
        self.driver.get(f'https://www.instagram.com/{fromAccount}/followers')
        followerSpans = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/*/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/*/div/div/div/div[2]/div/div/div/div/div/a/div/div/span')))
        return [element.text for element in followerSpans]
    
    def sendMessage(self, message, usernames):
        self.driver.get('https://www.instagram.com/direct/inbox/')
        try:
            notificationsBt = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
            notificationsBt.click()
        except:
            pass

        for usr in usernames:
            #self.driver.get('https://www.instagram.com/direct/inbox/')
            newMsg = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div')))
            newMsg.click()
            uNameField = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))
            uNameField.send_keys(usr)
            firstUsr = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input')))
            firstUsr.click()
            chatBtn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
            chatBtn.click()
            msgField = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')))
            msgField.send_keys(message)
            sendBtn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')))
            sendBtn.click()

# cookies = [{'domain': '.instagram.com', 'httpOnly': True, 'name': 'rur', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"CLN\\0548497208868\\0541745200412:01f7596e257ac8f23370b508d67397c4806607896c0f2fd0828322c1fb2b5542ba4eee92"'}, {'domain': '.instagram.com', 'expiry': 1714269271, 'httpOnly': True, 'name': 'shbts', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"1713664412\\0548497208868\\0541745200412:01f7b50b76fedd1df90e643d3d1442b80b77558ad1d2cb003fc57548c972e80795c31c4a"'}, {'domain': '.instagram.com', 'expiry': 1721440471, 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8497208868'}, {'domain': '.instagram.com', 'expiry': 1745200468, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8497208868%3A7P1podmLJz0H17%3A25%3AAYfAlYsi8SZOZia9ucDVMjevXy-NeLNlnsidpeRSZQ'}, {'domain': '.instagram.com', 'expiry': 1748224468, 'httpOnly': False, 'name': 'mid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'ZiRxlgALAAFNaQKNLbKcyToksYod'}, {'domain': '.instagram.com', 'expiry': 1745114071, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'irvAoRU3MQwHUhVCQz7rm29b9GH0Js7N'}, {'domain': '.instagram.com', 'expiry': 1714269271, 'httpOnly': True, 'name': 'shbid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"15180\\0548497208868\\0541745200412:01f73ddb8c97b33f3d519de3b33c1554c27b380cb073452599f427e3f2f23602ecab75e9"'}, {'domain': '.instagram.com', 'expiry': 1748224471, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'mXEkZoDQUH4n2B2rYDN2k5Cb'}, {'domain': '.instagram.com', 'expiry': 1745200468, 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '02ED7C9E-AED0-46A2-96AE-4138D7DD8379'}]

# auto2 = Auto()
# auto2.loadCookies(cookies)

# auto2.sendMessage('hello', ['adham.es'])

# try:
#     # Keep the program running until manually terminated
#     while True:
#         time.sleep(1)  # You can adjust the sleep duration if needed
# except:
#     # If Ctrl+C is pressed, close the WebDriver session
#     auto2.driver.quit()
