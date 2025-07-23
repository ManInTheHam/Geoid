import argparse
import pyfiglet
from simple_chalk import chalk
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API key for WeatherAPI.com
# Base URL for WeatherAPI.com current weather endpoint
API_KEY = os.getenv("API_KEYY")
BASE_URL = os.getenv("BASE_URLL")

# Check if API_KEY and BASE_URL were loaded successfully
if not API_KEY:
    print(chalk.red("Error: API_KEYY not found in .env or environment variables. Please check your .env file and its location."))
    exit()
if not BASE_URL:
    print(chalk.red("Error: BASE_URLL not found in .env or environment variables. Please check your .env file and its location."))
    exit()

# Construct Api url with query parameters
parser = argparse.ArgumentParser(description ="Check weather for the different country/city")
parser.add_argument("country", help = "The country/city to check the weather for")
args = parser.parse_args()

url = f"{BASE_URL}?key={API_KEY}&q={args.country}"

response = requests.get(url)

if response.status_code != 200:
    print(chalk.red(f"Error: Unable to retrieve weather information. Status Code: {response.status_code}"))
    print(chalk.red(f"API Response: {response.text}"))
    exit()

data = response.json()

temperature = data["current"]["temp_c"]
feels_like = data["current"]["feelslike_c"]
description = data["current"]["condition"]["text"]
city = data["location"]["name"]
country = data["location"]["country"]


# Construct the output
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"Condition: {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print the output
print(chalk.green(output))
