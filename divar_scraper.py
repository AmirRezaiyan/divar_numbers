import time
import json
import os
import random
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

COOKIES_FILE = "divar_cookies.json"

def setup_driver():
    try:
        print("Starting Chrome browser...")
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.set_page_load_timeout(30)
        print("Browser opened successfully.")
        return driver
    except Exception as e:
        print(f"Error opening browser: {e}")
        raise

def save_cookies(driver):
    with open(COOKIES_FILE, 'w') as f:
        json.dump(driver.get_cookies(), f, indent=4)
    print("Cookies saved.")

def load_cookies(driver):
    if not os.path.exists(COOKIES_FILE):
        return False
    driver.get("https://divar.ir")
    time.sleep(3)
    with open(COOKIES_FILE, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return True

def manual_login(driver):
    print("\nPlease log into your Divar account:")
    print("1. Enter your phone number and verification code.")
    print("2. Select your city.")
    print("3. After successful login, press Enter here.")
    input("Press Enter when done...")
    
    save_cookies(driver)
    driver.get("https://divar.ir")
    time.sleep(2)
    return True

def click_element_silent(driver, by, selector, timeout=10, description="element"):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, selector)))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(random.uniform(0.5, 1))
        ActionChains(driver).move_to_element(element).click().perform()
        print(f"   Clicked on {description}.")
        return True
    except:
        print(f"   Failed to click on {description}.")
        return False

def extract_phone_number(driver, link):
    driver.get(link)
    time.sleep(random.uniform(3, 5))

    if not click_element_silent(driver, By.CSS_SELECTOR, "button.kt-button.kt-button--primary.post-actions__get-contact", timeout=10, description="contact info button"):
        return "Contact info button not found"

    time.sleep(random.uniform(2, 3))

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='کپی کردن شمارهٔ موبایل']"))
        )
    except:
        return "Copy button not found (phone number is probably hidden)"

    copy_clicked = False
    for attempt in range(3):
        if click_element_silent(driver, By.CSS_SELECTOR, "button[aria-label='کپی کردن شمارهٔ موبایل']", timeout=5, description="copy button"):
            copy_clicked = True
            break
        time.sleep(1)
    if not copy_clicked:
        return "Could not click copy button after retries"

    time.sleep(random.uniform(1, 2))
    phone_number = pyperclip.paste().strip()
    return phone_number if phone_number else "Clipboard empty"

def main():
    print("Divar Scraper")
    print("-" * 40)
    
    print("\nFirst, log into your Divar account from 'My Divar' section.")
    input("Press Enter after login to continue...")
    
    driver = setup_driver()
    
    try:
        driver.get("https://divar.ir")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Divar page loaded.")
    except Exception as e:
        print(f"Failed to load page: {e}")
        print("Check your internet connection.")
        driver.quit()
        return
    
    if not load_cookies(driver):
        manual_login(driver)
    else:
        print("Logged in with saved session.")
    
    print("\nEnter ad links (one per line). Press Enter twice to finish.\n")
    links = []
    while True:
        line = input().strip()
        if not line:
            break
        if "divar.ir/v/" in line:
            links.append(line)
        else:
            print("Invalid link format")
    
    if not links:
        print("No links provided.")
        driver.quit()
        return
    
    results = []
    for i, link in enumerate(links, 1):
        print(f"\nProcessing ({i}/{len(links)})...")
        phone = extract_phone_number(driver, link)
        print(f"   Phone: {phone}")
        results.append((link, phone))
        if i < len(links):
            delay = random.uniform(8, 12)
            print(f"Waiting {delay:.1f} seconds before next...")
            time.sleep(delay)
    
    driver.quit()
    
    with open("results.txt", "w", encoding="utf-8") as f:
        for link, phone in results:
            f.write(f"Link: {link}\nPhone: {phone}\n{'-'*50}\n")
    
    print(f"\nComplete! Saved {len(results)} results to results.txt")

if __name__ == "__main__":
    main()