import tweepy

auth = tweepy.OAuthHandler("BsWQFvspc62hthS5gXqdm6GO2","ch2QXuvRMcEeMDvphmE892JeMh9OmsymuOjMmKkriUfNtqv7le")
auth.set_access_token("27445586-PrUeoJpoqygd4F4M8OOWaPx2No0poCaFoHN6YdI6g","rle1z1LqzMWyIigzjUXkhTjqkYpI0lPjQeF0ZRnkLsPgI")

twitter_api = tweepy.API(auth)

healthy_tweets = twitter_api.user_timeline(
    id = "FoodRev"
)

for tweet in healthy_tweets:
    print tweet.user.name + ":" + tweet.text + "\n"

# healthy_tweets =  twitter_api.search("healthy", rpp=10)
# print healthy_tweets
