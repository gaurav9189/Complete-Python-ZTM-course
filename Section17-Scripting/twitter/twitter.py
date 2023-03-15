import os
import tweepy
import time
# Using v1 of tweepy with OAuth1 user context
auth = tweepy.OAuth1UserHandler(
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret']
)
# v1 of tweepy using API
api = tweepy.API(auth)


def search_users(name, screen_name):
    users = api.search_users(name)
    for i in users:
        if i.name == name and i.screen_name == screen_name:
            print(f'ID for {name} is {i.id}')
            # andrei, screen_andrei = i.id, i.screen_name
            api.create_friendship(user_id=i.id, screen_name=i.screen_name)
            print(f"You have now followed {name}")
            return i.id


found = search_users('Sundar Pichai', 'sundarpichai')
# if found:
#     followers = api.get_followers(user_id=found, count=100, cursor=-1)
#     # print(followers)
#     # print(followers[1])
# followers_100 = (list(map(lambda x: x.screen_name, followers[0])))
if found:
    try:
        for i in tweepy.Cursor(api.get_followers, user_id=found, count=100).items():
            print(i.name)
            # print("now sleeping")
            time.sleep(1)
    except tweepy.errors.TooManyRequests as er:
        print(f'Rate limit exceeded, sleeping longer: {er}')
        time.sleep(100)
