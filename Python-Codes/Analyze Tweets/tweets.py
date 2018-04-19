from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

consumer_key = 	'EIpX5D2FDpsEzJPyxu2sxtf06'
consumer_secret = '8iA5K12xzLook3XY6JPBTfhFZgyB3KMb9NZB0ET75nEQPJ6NXm'
access_token = '757584924-HaTPG64QoUgH2V262IbD2pmUZN4lB39CCKgX6IHg'
access_secret = 'sfeXIwiwnc28YMatWCgzbXmXHlGgTqTHczMqpBGs8hI9m'

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    stream.filter(track=['h1b', 'Opt', 'F1'])
