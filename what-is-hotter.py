import requests
import praw
import random
import os
from dotenv import find_dotenv, load_dotenv

env_path = find_dotenv()

load_dotenv(env_path)

secret = os.getenv("secret")
client_id = os.getenv("client_id")



# weather API

weather_url = "https://api.open-meteo.com/v1/forecast?"

latitude = input("Enter the latitude: ")

longitude = input("Enter the longitude: ")

def get_weather(long, lat):

    url = f"{weather_url}latitude={lat}&longitude={long}&hourly=temperature_2m"
    response = requests.get(url)

    response = response.json()
    list_of_temp = response['hourly']['temperature_2m']
    max_temp = max(list_of_temp)
    avg = sum(list_of_temp) / len(list_of_temp)

    print(f"Highest temp: {max_temp}")

    return max_temp, avg

max_temp, avg = get_weather(longitude, latitude)

# Reddit API

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=secret,
    user_agent="script:what-is-hotter:v1.0 (by /u/Malaficient-Fall-3246)"
)

subreddit = reddit.subreddit("confession")

posts = list(subreddit.hot(limit=5))

post = random.choice(posts)

print("Title:", post.title)
print("Body:", post.selftext)
print("Upvotes:", post.score)

scaled_weather = (max_temp / 40) * 100
scaled_votes = (post.score / 1000) * 100

print(f"Scaled weather: {scaled_weather}")

print(f"Scaled upvotes: {scaled_votes}")

if scaled_weather > scaled_votes:
    print("Looks like the weather is hotter today than a random reddit post!")
elif scaled_votes > scaled_weather:
    print("The reddit post is hotter than the weather, looks like the tea is hot!")
else:
    print("Both of them are equally hot today!")


