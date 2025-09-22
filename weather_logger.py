import requests
import datetime

API_KEY = "aa70e339f0cdd410fd20e0863475266c"
CITY = "Vancouver"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
       temp = data['main']['temp']
       humidity = data['main']['humidity']
       return temp, humidity
    else:
       print("Error fetching data:", data.get("message", "Unknown Error"))
       return None, None

def log_weather(temp, humidity):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("weather_log.csv", "a") as f:
        f.write(f"{now},{temp},{humidity}\n")
    print(f"[{now}] City = {CITY}, Logged: Temp = {temp}°C, Humidity = {humidity}%")

def main():
    temp, humidity = fetch_weather()
    if temp is not None:
        log_weather(temp, humidity)

if __name__== "__main__":
    main()
