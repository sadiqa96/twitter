from flask import Flask, render_template, request
import tweepy
import os

port = int(os.getenv("PORT", 5000))
app = Flask("Twitter")
#
# with open("credentials.txt", "r") as file:
#     consumer_key = file.readline().split()[2]
#     consumer_secret = file.readline().split()[2]
#     access_token = file.readline().split()[2]
#     access_token_secret = file.readline().split()[2]

consumer_key = os.getenv("consumer_key", None)
consumer_secret = os.getenv("consumer_secret", None)
access_token = os.getenv("access_token", None)
access_token_secret = os.getenv("access_token_secret", None)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/timeline", methods=["GET"])
def timeline():
    tweets_from_timeline = api.home_timeline()
    return render_template("main.html", tweets_from_timeline=tweets_from_timeline)
    #for tweet in tweets_from_timeline:
        #print tweep.text

@app.route("/tweet", methods=["POST"])
def tweet():
    text = request.form['Tweet']
    post_tweet = api.update_status(text)
    response = "Your tweet was sent: {}".format(text)
    return render_template("main.html", response=response)
#text = raw_input("What would you like to Tweet?")

app.run(port=port, debug=True)
