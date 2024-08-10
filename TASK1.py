from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()
try:
    
    driver.get("https://dev--taupe-pithivier-3c339a.netlify.app/")

    # Create new account 
    username="rp_test"+str(random.randint(1,100000))
    print("username: " + username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-header/header/ul/li[3]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))).send_keys(username+"@gmail.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Create the article
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-header/header/ul/li[4]")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-header/header/ul/li[2]"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Article Title']"))).send_keys("test"+str(random.randint(1,100000)))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder=\"What's this article about\"]"))).send_keys("test")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea[placeholder='Write your article (in markdown)']"))).send_keys("test")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder='Enter tags']"))).send_keys("test")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/app-new-article/app-article-form/form/button"))).click()
    
    # Comment on the article
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Write a comment...']"))).send_keys("test comment")
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-article-detail/div[4]/div/app-comment-form/div/div[2]/button"))).click()

    # Edit the article
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-article-detail/div[3]/div/div[2]/button[1]"))).click()
    content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Write your article (in markdown)']")))
    time.sleep(1)
    content.clear()
    time.sleep(1)
    content.send_keys("test edit")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Set the article as favorite
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-header/header/ul/li[4]"))).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-profile/div[2]/div/app-profile-article-list/app-article-list/app-article/div/div[1]/button"))).click()
finally:
    # Close the browser
    driver.quit()
