# Require the Bot module from instabot package
from instabot import Bot

# Create an instance of Bot
bot = Bot()

# Login to your account by typing in username and password
bot.login(username='username', password='password')

# Image path
image = "./images/insta.jpg"

# Upload the story as in your filepath, along with necessary caption 
bot.upload_story_photo(image)
