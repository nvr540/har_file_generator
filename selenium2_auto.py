from browsermobproxy import Server
import json
import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to BrowserMob Proxy
bmp_path = 'C:/Users/Moumita/Desktop/sorder_project/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat'
server = Server(bmp_path)
server.start()
proxy = server.create_proxy()
print(f"Proxy started on port: {proxy.port}")

# Start a new HAR capture
proxy.new_har("clay-email-finder")

# Automatically download and install the correct ChromeDriver
chromedriver_path = chromedriver_autoinstaller.install()

# Set up Chrome options to capture network traffic
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument(f'--proxy-server={proxy.proxy}')

# Provide the path to your ChromeDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get('https://clay-email-finder.netlify.app')
wait = WebDriverWait(driver, 10)

# Interact with the website
try:
    name = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="fullName"]'))
    )
    name.send_keys("nivrita")
except Exception as e:
    print(f"Error finding 'fullName' input: {e}")

try:
    domain = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="domain"]'))
    )
    domain.send_keys("google.com")
except Exception as e:
    print(f"Error finding 'domain' input: {e}")

try:
    button = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, 'button'))
    )
    button.click()
except Exception as e:
    print(f"Error finding button: {e}")

# Give some time for the requests to complete
time.sleep(10)

# Extract HAR data
try:
    har_data = proxy.har
    if har_data:
        pprint.pprint(har_data)
        with open("network_traffic.json", "w") as har_file:
            json.dump(har_data, har_file)
    else:
        print("No HAR data captured.")
except Exception as e:
    print(f"Error capturing HAR data: {e}")

driver.quit()
server.stop()
