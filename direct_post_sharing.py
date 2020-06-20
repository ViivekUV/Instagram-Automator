# Require the Bot module from instabot package
from instabot import Bot

# Create an instance of Bot
bot = Bot()

# Login to your account by typing in username and password
bot.login(username='username', password='password')

# User ID to share post
user = "username to share post"
# Image path
image = "./images/insta.jpg"

# Send the image as in the filepath to the required user's Insta ID
bot.send_photo(user, image)
