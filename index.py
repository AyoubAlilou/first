import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Initialize the Chrome WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
# Navigate to YouTube
driver.get("https://www.youtube.com/")
driver.maximize_window()
# Locate the search bar and enter the search query
# Partie login
username_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "pass")
# Entrer le nom d'utilisateur et le mot de passe
username_input.send_keys("ayoubsniper2@yahoo.fr")
password_input.send_keys("kjkszpj2021839     ")
# Attendre un court instant (facultatif)
time.sleep(2)
#Entrééé
password_input.send_keys(Keys.RETURN)
# Trouver l'élément du bouton par son ID, son nom, sa classe ou tout autre attribut approprié
button_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div/div[2]")# Cliquer sur le bouton
button_element.click()
# Wait for search results to load
wait = WebDriverWait(driver, 10)
first_video_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#video-title')))
first_video_link.click()
# Close the browser after a brief delay (you can remove this if not needed)
# import time
time.sleep(5)  # Wait for 5 seconds
driver.quit()
