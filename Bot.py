from decouple import config
import logging
from telethon import TelegramClient
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

bot = TelegramClient('SpamBot', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 
