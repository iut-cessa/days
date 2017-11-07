import telegram
import os
import requests
import urllib.request as urllib2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv, find_dotenv


# This function sends a request to one of the Unsplash api endpoints
# and returns the response as a dictionary
def unsplash_api_request(endpoint):
    UNSPLASH_API_BASE_URL = 'https://api.unsplash.com'
    app_id = get_env('UNSPLASH_APP_ID')  # UNSPLASH_APP_ID is defined in .env
    # Send api request and add `Authorization` to the request header
    # so that Unsplash knows you have permission to use the api
    api_response = requests.get(
        '{}{}'.format(UNSPLASH_API_BASE_URL, endpoint),
        headers={'Authorization': 'Client-ID {}'.format(app_id)}
    )
    return api_response.json()


# This function returns the value of an environmental variable `envvar_name`
def get_env(envvar_name):
    return os.environ.get(envvar_name)


# This fuction replies the the URL of a random image and the image itself
# to the user
def random(bot, update):
    # This inner fuction return the URL of a random image
    def get_random_image_url():
        # indexes `urls` and `full` are used based on api response structure
        return unsplash_api_request('/photos/random')['urls']['full']

    update.message.reply_text(
        'OK. Wait some seconds while we fetch the image for you.'
    )
    random_image_url = get_random_image_url()
    # Download the image on the disk as a file named `img`
    urllib2.urlretrieve(random_image_url, 'img')

    # Show `>>> sending a photo` chat action to the user
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=telegram.ChatAction.UPLOAD_PHOTO
    )
    # Unsplash images are messy in size (about 2-10 MB each),
    # so override the default small timeout for sending the image
    # with an enough large timeout
    update.message.reply_document(open('img', 'rb'), timeout=300)
    update.message.reply_text(random_image_url)


# This function just replies the message `A reply!` whenever called
def test(bot, update):
    update.message.reply_text('A reply!')


def main():
    bot_token = get_env('BOT_TOKEN')  # BOT_TOKEN is defined in .env

    # Make an Updater to fetch all updates from Telegram servers
    updater = Updater(bot_token)

    # Get the Updater's Dispatcher to handle messages and commands
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CommandHandler('random', random))

    # Start the bot by making the Updater listen for updates
    updater.start_polling()

    # Use this line so that whenever you press Ctrl+C, your bot stops working
    updater.idle()

# Run these only if this is the main python module,
# i.e. it is run using `python bot.py`, other than
# being imported in another python module
if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()
