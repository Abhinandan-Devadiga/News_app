import requests

query = input("What type of news you are interested..")

api = ""

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-03&sortBy=popularity&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1 ,article["title"],article["url"])
    print("\n********************************************\n")
