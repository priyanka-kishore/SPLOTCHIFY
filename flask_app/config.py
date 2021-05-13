import os

# Stores all configuration values
SECRET_KEY = b'\x020;yr\x91\x11\xbe"\x9d\xc1\x14\x91\xadf\xec'
MONGODB_HOST = "mongodb://localhost:27017/splotchify"

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ.get("MAIL_SENDER")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_SENDER")