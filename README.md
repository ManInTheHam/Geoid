Geoid
Geoid is a lightweight, command-line weather application that provides current weather conditions for any specified city, leveraging the WeatherAPI.com service. Get quick, clear weather insights directly in your terminal.

✨ Features
* Current Weather: Displays real-time temperature, "feels like" temperature, humidity, wind speed, and wind direction.

* City Search: Get weather for any city worldwide by providing its name.

* Unit Toggle: Easily switch between Celsius (default) and Fahrenheit for temperature display.

* Clean CLI Output: Formatted with ASCII art for city names and colored text for readability.

* Secure API Key Handling: Utilizes a .env file to securely manage your WeatherAPI.com API key, keeping it out of your main codebase.

🚀 Installation
To get Geoid up and running on your local machine, follow these steps:

Clone the Repository:
`
git clone https://github.com/your-username/Geoid.git
cd Geoid
`
(Replace your-username with your actual GitHub username)

Create a Virtual Environment (Recommended):

`python -m venv venv`
# On Windows:
`.\venv\Scripts\activate`

# On macOS/Linux:
`source venv/bin/activate`

Install Dependencies:
`
pip install -r requirements.txt
`
(You'll need to create a requirements.txt file as described in the next section.)

🔑 API Key Setup
Geoid uses WeatherAPI.com to fetch weather data. You'll need a free API key from their website.

Sign Up for WeatherAPI.com:
Go to https://www.weatherapi.com/ and sign up for a free account to obtain your API key.

Create a .env file:
In the root directory of your Geoid project (the same directory where main.py is located), create a new file named .env (note the leading dot).

Add Your API Key and Base URL to .env:
Open the .env file and add the following lines, replacing YOUR_WEATHERAPI_KEY with your actual key:
`
API_KEYY=YOUR_WEATHERAPI_KEY
BASE_URLL=https://api.weatherapi.com/v1/current.json
`
Important: Ensure there are no spaces around the = signs.

📋 Usage
Once installed and configured, you can run Geoid from your terminal:

# Get weather in Celsius (default)
`python main.py "Pune"`

📦 Dependencies
The project relies on the following Python libraries:

requests: For making HTTP requests to the WeatherAPI.com.

pyfiglet: For generating ASCII art text.

simple-chalk: For adding colors to the terminal output.

python-dotenv: For loading environment variables from the .env file.

You can create a requirements.txt file using:
`
pip freeze > requirements.txt
`
Or manually create it with the following content:

`
requests
pyfiglet
simple-chalk
python-dotenv
`
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
