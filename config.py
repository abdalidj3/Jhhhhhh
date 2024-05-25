import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7066213924:AAGhUa9xJpV_CF9voi2OnwY9CwkyyoPRe88")

    APP_ID = int(os.environ.get("APP_ID", 25612365))

    API_HASH = os.environ.get("API_HASH", "983959cac2c32428b55d7c929a146b80")
