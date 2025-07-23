# 🌍 Geoid

**Geoid** is a lightweight, command-line weather application that provides current weather conditions for any specified city, leveraging the [WeatherAPI.com](https://www.weatherapi.com/) service. Get quick, clear weather insights directly in your terminal.

---

## ✨ Features

- **Current Weather**: Displays real-time temperature, "feels like" temperature, humidity, wind speed, and wind direction.
- **City Search**: Get weather for any city worldwide by providing its name.
- **Unit Toggle**: Easily switch between Celsius (default) and Fahrenheit for temperature display.
- **Clean CLI Output**: Formatted with ASCII art for city names and colored text for readability.
- **Secure API Key Handling**: Utilizes a `.env` file to securely manage your WeatherAPI.com API key, keeping it out of your main codebase.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Geoid.git
cd Geoid
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

### 1. Get an API Key

- **Go to [WeatherAPI.com](https://www.weatherapi.com/)

- **Sign up and get your free API key

### 2. Create a .env File
In the root directory of your project (same as `main.py`), create a `.env` file with the following content:

```env
API_KEYY=YOUR_WEATHERAPI_KEY
BASE_URLL=https://api.weatherapi.com/v1/current.json
```

---

## 📋 Usage
Once installed and configured, you can run Geoid from your terminal:
```bash
# Get weather in Celsius (default)
python main.py "Pune"

# Get weather in Fahrenheit
python main.py "New York" --fahrenheit

# Or using single-letter flag
python main.py "London" -f
```
---

## 📦 Dependencies
Geoid uses the following Python libraries:

- `requests`: For making HTTP requests

- `pyfiglet`: For generating ASCII art

- `simple-chalk`: For colored terminal text

- `python-dotenv`: For loading environment variables

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to:
- Open an issue
- Submit a pull request
