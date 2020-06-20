# Require the Bot module from instabot package
from instabot import Bot

# Create an instance of Bot
bot = Bot()

# Login to your account by typing in username and password
bot.login(username='username', password='password')

# Image path
image = "./images/insta.JPG"
# Post Caption
text = "This is a test post using instagram automator application"

# Upload the image as in your filepath, along with necessary caption 
bot.upload_photo(image ,caption=text)
