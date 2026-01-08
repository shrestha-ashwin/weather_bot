import requests
import os
import json

api_key = os.getenv("API_KEY")
latitude = "27.713"
longitude = "85.345"
units = "metric"
STATE_FILE = "state.json"
degree_symbol = "\N{DEGREE SIGN}"

def get_weather_data():

    if not api_key:
        raise RuntimeError("api key missing. add to env")

    open_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units={units}"

    response = requests.get(open_weather_url)

    response.raise_for_status()

    json_data = response.json()
    return json_data



def extract_weather_data():

    try:
        data = get_weather_data()
    except requests.RequestException as e:
        print("Error: ", e)
        raise

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    wind = data["wind"]["speed"]

    weather_data = {
        "temp": temperature,
        "description": weather_description,
        "feels_like": feels_like,
        "wind": wind
    }

    return weather_data


def load_previous_state():
    if not os.path.exists(STATE_FILE):
        return None

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error reading file: ", e)
        return None



def save_state(today_temp, day):
    state = {
        "last_temp": today_temp,
        "day" : day
    }

    with open(STATE_FILE, "w") as f:
        json.dump(state, f)



def get_next_day(previous_state):
    if not previous_state:
        return 1

    day = previous_state.get("day")

    if not isinstance(day, int) or day < 1:
        return 1

    return day + 1



def build_comparison_message(today_temp, yesterday_temp):
    if yesterday_temp is None:
        return "No previous temperature data — starting from today!"

    difference = today_temp - yesterday_temp
    abs_diff = abs(difference)

    if abs_diff < 0.5:
        return "Today's weather feels about the same as yesterday."

    if difference > 0:
        temp = "warmer"
    else:
        temp = "colder"

    diff_display = round(abs_diff, 1)

    return f"Today's weather is {temp} by {diff_display}{degree_symbol} compared to yesterday."




def get_weather_summary():
    weather_data = extract_weather_data()
    today_temp = weather_data["temp"]

    previous_state = load_previous_state()
    if previous_state is not None:
        yesterday_temp = previous_state.get("last_temp")
    else:
        yesterday_temp = None

    day = get_next_day(previous_state)

    comparison_msg = build_comparison_message(today_temp, yesterday_temp)

    save_state(today_temp, day)

    summary = weather_data.copy()
    summary["day"] = day
    summary["weather_comparison_msg"] = comparison_msg

    return summary









