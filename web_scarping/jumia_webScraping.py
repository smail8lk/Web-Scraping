from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the Jumia page with massive clearance offers
driver.get('https://www.jumia.ma/mlp-destockage-massif/#catalog-listing')

# Allow the page to load fully
time.sleep(5)

# Find the offer elements
offers = driver.find_elements("css selector", ".info")  # Adjust the selector based on the page structure

# Prepare data storage list
data = []

# Loop through each offer and extract the required information
for offer in offers:
    # Extract title (assuming it's in an h3 tag with the class 'name')
    title = offer.find_element("css selector", "h3.name").text

    # Extract price (adjust selector if needed, assumes class 'prc' for price)
    price = offer.find_element("css selector", ".prc").text

    # For this example, the end of the offer is not explicitly mentioned, so use a placeholder
    end_of_offer = "Not mentioned"

    # Append extracted data to the list, classified as Title, Price, and End of Offer
    data.append({"Title of the Offer": title, "Price": price, "End of Offer": end_of_offer})

# Close the browser after scraping
driver.quit()

# Define the Desktop path for saving the CSV file
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the CSV file name with full path on the Desktop
filename = os.path.join(desktop_path, "jumia_offers.csv")

# Write data to CSV file, ensuring proper classification of the columns
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    # Define the column headers for the CSV
    writer = csv.DictWriter(file, fieldnames=["Title of the Offer", "Price", "End of Offer"])
    
    writer.writeheader()  # Write the header row with classified columns
    writer.writerows(data)  # Write the rows of collected data to the file

# Print confirmation message
print(f"Data saved successfully to {filename}")
