import requests

def get_coordinates(city):
    """Получает координаты города через OpenStreetMap"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    response = requests.get(url, params=params, headers={"User-Agent": "my-weather-app"})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    return None, None

def get_weather(city):
    """Получает погоду для введённого города"""
    lat, lon = get_coordinates(city)
    if lat is None:
        print("❌ Город не найден!")
        return
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data.get("current_weather", {})
        temp = weather.get("temperature")
        wind = weather.get("windspeed")
        print(f"Погода в городе {city}:")
        print(f"🌡 Температура: {temp}°C")
        print(f"💨 Ветер: {wind} м/с")
    else:
        print("Ошибка при запросе погоды!")

if __name__ == "__main__":
    city = input("Введите название города: ")
    get_weather(city)
