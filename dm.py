# Require the Bot module from instabot package
from instabot import Bot

# Create an instance of Bot
bot = Bot()

# Login to your account by typing in username and password
bot.login(username='viivek_uvv', password='realmadridRONALDOINSTA007')

# User ID to share post
user = ""
# Image path
message = "Hey! This is a txt sent from InstaBot Automator"

# Send the message as in the filepath to the required user's Insta ID
bot.send_messages(message, user)
