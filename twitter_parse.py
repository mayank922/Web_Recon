import tweepy
import requests
#bearer_token= "AAAAAAAAAAAAAAAAAAAAAPkbnQEAAAAAT9IOYMBuaIFJXt4Sa2I0zs5cRdU%3DsD0UErsBhiBCjyYMMrQv6vyKgUwupB3PeAz8kkpBhJxm4OhRJu"


consumer_key= 'J7pL9EHflvF1hyXi6mMGhaJG7'

consumer_secret='auK9iV5HeABiKIDtgZnsOF0JCpRtekAb9P2dBd2afIrIy2Ffuh'

access_token ='1267397307076468737-iyvcfc5JzSQRNq2cjw64Xr6sG6Iw46'

access_token_secret= '3s300UxoGkRxJfl0AWnpCA0cck9dTYQKNHXB9zivqiC0a'


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

print(api.verify_credentials().screen_name)

for follower in tweepy.Cursor(api.get_followers).items():
    print(follower)