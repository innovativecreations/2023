
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.ae/dp/B0079070NY")

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text

ratings = driver.find_element(By.ID, "acrCustomerReviewText").text

print(f"Price: {price}")
print(f"Ratings: {ratings}")
