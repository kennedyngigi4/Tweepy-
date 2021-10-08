import datetime
import tweepy

#Twitter Developer auth 
auth = tweepy.OAuthHandler("your consumer_key", "you consumer_secret")
auth.set_access_token('access_token','access_token_secret')

# Construct the API instance with wait limits 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def tweepyGreetings():
    #get the current day where Monday == 0 .... and Sunday == 6
    current_day = datetime.date.today().weekday()

    #get time in hours when to post your greetings to your followers
    post_time = datetime.datetime.now().strftime("%H") == '08'

    if current_day == 0 and post_time:
        greetings = "Good morning Monday!"
    elif current_day == 1 and post_time:
        greetings = "Good morning Tuesday!"
    elif current_day == 2 and post_time:
        greetings = "Good morning Wednesday!"
    elif current_day == 3 and post_time:
        greetings = "Good morning Thursday!"
    elif current_day == 4 and post_time:
        greetings = "Good morning Friday!"
    elif current_day == 5 and post_time:
        greetings = "Good morning Saturday!"
    elif current_day == 6 and post_time:
        greetings = "Good morning Sunday!"
    else:
        greetings = "No match!"

    # print(greetings)
    api.update_status(greetings)


#We now call our function so that it can run greetings daily
tweepyGreetings()