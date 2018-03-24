from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'D://dev//elab'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path="D:\\dev\\chromedriver.exe")
driver.get("http://care.srmuniv.ac.in/ktrcsejava1/") #if you belong to Java2 replace 1 with 2
driver.find_element_by_id("username").send_keys("Reg no") #Type your Reg no in between " "
driver.find_element_by_id("password").send_keys("password") #Enter your pass in between " "
driver.find_element_by_id("button").click()
time.sleep(1)
driver.find_element_by_css_selector("div.card-content.white-text").click()
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.get("http://care.srmuniv.ac.in/ktrcsejava1/login/student/question.php") #if you belong to Java2 replace 1 with 2
question="http://care.srmuniv.ac.in/ktrcsejava1/login/student/code/java/java.code.php?id" #if you belong to Java2 replace 1 with 2
rep="http://care.srmuniv.ac.in/ktrcsejava1/login/student/code/getReport.php" #if you belong to Java2 replace 1 with 2
delay=10
for i in range(0,100):
    
    first=i
    driver.get("http://care.srmuniv.ac.in/ktrcsejava1/login/student/code/java/java.code.php?id=1&value=%(first)d" %{"first":first}) #if you belong to Java2 replace 1 with 2
    time.sleep(2)
    
    
    k='//*[@id="printMsg"]'

    try:
        driver.find_element_by_xpath('//*[@id="evaluateButton"]').click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,'printMsg')))
        driver.get(rep)
        
        
        
    except TimeoutException:
        print("Reorts Printed",i)
        
        
        
        
        
        







     
       

                
                
    


