import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def chrome_driver():
    
    current_directory = os.getcwd()
    path_to_driver = os.path.join(current_directory, 'chromedriver.exe')

    service = Service(path_to_driver)

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-notifications')
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False) 
    #options.add_argument("--headless")
    
    #options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

    driver = webdriver.Chrome(service=service, options=options)

    return driver   