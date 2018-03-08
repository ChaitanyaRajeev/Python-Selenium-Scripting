from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
#Edit the Email Id and Replace it with your email id
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys("Email")
#Edit Password and replace it with Password
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys("Password")
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
#Edit the range till the number of times you wanted to tweet
for i in range(1,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get("https://twitter.com")
    #in the send keys Write the Content you want to tweet.
    #Kidly note Do not remove i. Same tweet cannot be tweeted again 
    driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').send_keys("#TweetDiscription",i)
    driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').click()
    

