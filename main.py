import datetime

from openWeather import get_weather_summary
from clothesRecommendation import cloth_recommender
from emailHandler import send_email
from quote import get_quote

degree = "\N{DEGREE SIGN}"

def build_email(weather: dict) -> str:
    today = datetime.date.today()
    temp = weather["temp"]
    description = weather["description"]
    feels_like = weather["feels_like"]
    wind = weather["wind"]
    comparison_msg = weather["weather_comparison_msg"]
    quote, author = get_quote()

    messages = [
        f"Good morning! 🌤️",
        f"Today is {today}.",
        f"",
        f"Weather in Kathmandu:",
        f"– {temp:.1f}{degree}C (feels like {feels_like:.1f}{degree}C)",
        f"– {description}, wind: {wind:.1f} m/s",
        "",
        f"{comparison_msg}",
        "",
        f"Cloth recommendation: {cloth_recommender(weather)}",
        "",
        "",
        f'"{quote}"',
        f"– {author}",
        "",
        "",
        "",
        "With care,",
        "Ashwin",
    ]

    return "\n".join(messages)


def main():
    weather = get_weather_summary()
    body = build_email(weather)
    day_counter = weather["day"]
    subject = f"Weather Report, Day #{day_counter}"

    send_email(subject, body)


if __name__ == "__main__":
    main()

