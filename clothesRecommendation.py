def cloth_recommender(weather: dict) -> str:

    temp = weather["temp"]
    wind = weather.get("wind", 0)

    if temp < 5:
        outfit = "thick warm jacket, sweater, and long pants"
    elif temp < 10:
        outfit = "warm jacket or hoodie with long pants"
    elif temp < 16:
        outfit = "light jacket or hoodie with long pants"
    elif temp < 22:
        outfit = "long-sleeve top or light jacket with pants"
    elif temp < 28:
        outfit = "t-shirt or light clothes, comfortable pants"
    else:
        outfit = "very light clothes like a t-shirt and breathable pants or shorts"

    wind_note = ""
    if wind >= 6:
        wind_note = " It’s also windy, so make sure your outer layer is enough."
    elif wind >= 3 and temp < 18:
        wind_note = " There’s a bit of wind, so don’t skip a layer."

    return f"Wear a {outfit}.{wind_note}"
