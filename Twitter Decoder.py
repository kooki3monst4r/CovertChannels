import tweepy
import json



# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# api is the main tweepy class we're going to use to make this work
api = tweepy.API(auth)

# Check to make sure we can authenticate before we begin. Prevents ya boi from trying to do this without an internet connection
try:
    api.verify_credentials()
    print("I'm in...")
except:
    print("You didn't say the magic word!")

# # Pulls the last 20 tweets from the timeline
# timeline = api.home_timeline()
#
# # This is the exit condition. We will continue going through the loop until we find the EOF delimiter.
# EOF = False
#
# while not EOF:
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # # Authenticate
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.
    # stream.filter(track=['@channingtatum'])
