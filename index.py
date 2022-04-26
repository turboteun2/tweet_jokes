import tweepy
import time
import random
import secret

client = tweepy.Client(
   consumer_key=secret.CONSUMER_KEY,
   consumer_secret=secret.CONSUMER_SECRET,
   access_token=secret.ACCESS_TOKEN,
   access_token_secret=secret.ACCESS_TOKEN_SECRET
)

def tweet():
   # All testaments that are available in the bible directory
   jokeFiles = ["one", "two", "deck"]
   # Get a random testament
   jokeFile = jokeFiles[random.randrange(len(jokeFiles))]

   def getFileLength():
      file_length = open("jokes/"+jokeFile+".txt", 'r')
      lines_file = 0
      with file_length as f:
         for _ in f:
            lines_file += 1
      return lines_file

   file = open("jokes/"+jokeFile+".txt", 'r')
   rand_quote_num = random.randrange(int(getFileLength()))
   quote_num = 0

   with file as f:
      for line in f:
         if int(quote_num) == int(rand_quote_num): quote = line
         quote_num += 1

   status = client.create_tweet(text=quote+"\n"+"\n"+"#funny"+"\n"+"#jokeoftheday"+"\n"+"#joke")
   print(status)

while True:
   tweet()
   time.sleep(3600)
