from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'D://dev//elab'} #Set Directory 
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path="D:\\dev\\chromedriver.exe") #Set your Chromedriver path
driver.get("http://care.srmuniv.ac.in/ktrcseada/")
driver.find_element_by_id("username").send_keys("REG NO") #Type your Reg no " 
driver.find_element_by_id("password").send_keys("Password") #Type your password
driver.find_element_by_id("button").click()
time.sleep(1)
driver.find_element_by_css_selector("div.card-content.white-text").click()
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.get("http://care.srmuniv.ac.in/ktrcseada/login/student/code/daa/daa.code.php?id=1&value=0")
question="http://care.srmuniv.ac.in/ktrcseada/login/student/code/daa/daa.code.php?id"
rep="http://care.srmuniv.ac.in/ktrcseada/login/student/code/getReport.php"
delay=10
for i in range(0,100):
    
    first=i
    driver.get("http://care.srmuniv.ac.in/ktrcseada/login/student/code/daa/daa.code.php?id=1&value=%(first)d" %{"first":first})
    time.sleep(2)
    

    try:
        driver.find_element_by_xpath('//*[@id="evaluateButton"]').click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,'printMsg')))
        driver.get(rep)
        
        
        
    except TimeoutException:
        print("Not Done",i)
        
        
        
        
        
        







     
       

                
                
    


