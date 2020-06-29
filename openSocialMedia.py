from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def OpenFacebook(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.facebook.com/login.php")

    search_email = driver.find_element_by_id("email")
    search_email.send_keys(Email)
    search = driver.find_element_by_id("pass")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)


def OpenInstagram(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    #we need to wait the page to exist to click the next link
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,"username"))
        )
    
    search_email = driver.find_element_by_name("username")
    search_email.send_keys(Email)
    search = driver.find_element_by_name("password")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)


def OpenTwitter(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://twitter.com/login")

    search_email = driver.find_element_by_name("session[username_or_email]")
    search_email.send_keys(Email)
    search = driver.find_element_by_name("session[password]")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)


def OpenLinkedin(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.linkedin.com/uas/login")
    #we need to wait the page to exist to click the next link
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"username"))
        )
    search_email = driver.find_element_by_id("username")
    search_email.send_keys(Email)
    search = driver.find_element_by_id("password")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)

def OpenGithub(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://github.com/login")
    
    search_email = driver.find_element_by_id("login_field")
    search_email.send_keys(Email)
    search = driver.find_element_by_id("password")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)

'''
def OpenGmail(Email,Password):
    path ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://accounts.google.com/")
    
    search_email = driver.find_elements_by_id("identifierId")
    search_email.send_keys(Email)
    #we need to wait the page to exist to click the next link
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,"password"))
        )
    search = driver.find_element_by_name("password")
    search.send_keys(Password)
    search.send_keys(Keys.RETURN)'''