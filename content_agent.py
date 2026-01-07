def generate_weather_report(data):
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    report = (
        f"The current weather in {city} shows {description}. "
        f"The temperature is around {temp}°C with a humidity level of {humidity}%. "
        f"Overall, the weather conditions are moderate and suitable for daily activities."
    )

    return report
