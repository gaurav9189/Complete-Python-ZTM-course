import tweepy
import os
import time

# Using v2 of tweepy with OAuth1 user context
client = tweepy.Client(
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret']
)
# I had to set user_auth to False as it was failing otherwise!
# This script helps in following the list of followers your influencers follow!
# To-Do: Make a retry function to help resume once the exceptions are handled
#        Check the following list and only follow the ones not followed

my_id = client.get_me().data.id
my_followers = [myfollows.id for myfollows in client.get_users_following(
    my_id, user_auth=True).data]


def search_users(username):
    users = client.get_users(usernames=username, user_auth=True)
    for i in users.data:
        if i.username in username:
            print(f'ID for {i.name} is {i.id}')
            client.follow_user(target_user_id=i.id, user_auth=True)
            print(f"You are now following the great {i.name}")
            return i.id


def followers_of_influencers(influencer_id):
    page = tweepy.Paginator(client.get_users_following,
                            influencer_id, user_auth=True)
    return paginate(page)


def paginate(page):
    for data in page:
        for user in data.data:
            # print(user.name)
            follow = following(user.id, user.name)
            time.sleep(1)
            if not follow:
                print('breaking the loop')
                break
            # print(f'Now following {user.name}')
        # print('Followed from this page')


def following(userid, username):
    try:
        if userid not in my_followers:
            print(f'Added follower for your influencer: {username}')
            client.follow_user(target_user_id=userid, user_auth=True)
            return 1
        else:
            print(f'Already following {username}')
            return 1

    except tweepy.errors.TooManyRequests as er:
        print(f'Things are getting escalated!, slow down {er}')
        time.sleep(20)
        return 0


if __name__ == '__main__':

    influencer_id = search_users('sundarpichai')
    followers_of_influencers(influencer_id)
