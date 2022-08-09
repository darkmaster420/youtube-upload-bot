from pyrogram import Client

from .config import Config
from bot import SESSION_NAME, BOT_TOKEN, API_ID, API_HASH

class UtubeBot(Client):
    def __init__(self):
        super().__init__(
            session_name = Config.SESSION_NAME, 
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID, 
            api_hash = Config.API_HASH,
            plugins = dict(
                root="bot.plugins"
            ), 
            workers = 6
        )
        self.DOWNLOAD_WORKERS = 6
        self.counter = 0
        self.download_controller = {}
