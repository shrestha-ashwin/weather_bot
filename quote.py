import requests

URL = "https://zenquotes.io/api/today"

def get_quote():
    try:
      res = requests.get(URL)

      res.raise_for_status()

      refined_data = res.json()[0]

      quote = refined_data['q']
      author = refined_data['a']

    except Exception as e:
        print("Error: ", e)
        raise

    return quote, author

print(get_quote())

