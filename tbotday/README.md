TBot day source code
====
This directory contains source code of the simple bot developed in TBot day. There must be a `.env` file containing your bot token and your Unsplash app id. An example `.env` file is available as `.env.example`.

Prerequisties
----
You need the following packages to start the bot:
* python 3.5
* python-telegram-bot
* requests
* python-dotenv  

You can install dependency packages by running:
```bash
pip3 install python-telegram-bot requests python-dotenv
```
(If you are a windows user, use `pip` instead of `pip3`.)

Usage
----
In order to run the bot, clone or download the source code, go to the bot directory and simply run:
```bash
python3 bot.py
```
(If you are a windows user, use `python` instead of `python3`.)

Bot token
----
In order to implement a Telegram bot, you have to talk to [BotFather](https://telegram.me/BotFather) Telegram bot, and persuade him to give you a bot token :) then you have to put this token in your `.env` file.

Unsplash app id
----
In addition to the bot token, you have to register to Unsplash and get an app id by creating an app. For more information, refer to the [Unsplash docs](https://unsplash.com/documentation). After that, you have to put this app id in your `.env` file. This app id is used in `Authorization` header of the requests to the Unsplash api to give you the permission to use the api.

#### A note about Unsplash api
By default, Unsplash only provides 50 api requests per hour. So be careful, and don't overuse the api! (You can increase that rate limit to 5K per hour. Just refer to the Unsplash docs and follow the instructions.)
