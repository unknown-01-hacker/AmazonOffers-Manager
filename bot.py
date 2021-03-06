from AmazonBot.config import API_HASH, API_ID, WORKERS_NUM, SESSION_NAME, BOT_TOKEN, PLUGINS_ROOT, LOGGING_CONFIG, DB_PATH
import logging
from pyrogram import Client
from AmazonBot.database import dbcreator
import AmazonBot.config
from AmazonBot.scheduler import scheduler_thread as scheduler
from threading import Thread


logging.basicConfig(datefmt=LOGGING_CONFIG[0], level=LOGGING_CONFIG[2], format=LOGGING_CONFIG[1])

try:
    BOT = Client(api_hash=API_HASH,
                 api_id=API_ID,
                 session_name=SESSION_NAME,
                 workers=WORKERS_NUM,
                 bot_token=BOT_TOKEN,
                 plugins=dict(root=PLUGINS_ROOT))
except Exception as error:
    logging.error(f"Something went wrong while instantiating the client! -> {error}")
    exit(error)

if __name__ == "__main__":
    dbcreator.create_database(DB_PATH)
    scheduler_thread = Thread(target=scheduler, args=tuple())
    BOT.start()
    scheduler_thread.start()
