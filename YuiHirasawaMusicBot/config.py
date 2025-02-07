from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
MONGODB_URI = os.environ.get("MONGODB_URI")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CapitalLondonRadio")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "yuir")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "CapitalLondonRadio")
PROJECT_NAME = getenv("PROJECT_NAME", "Yui v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Yeagerist-Music-Streamer-Bot-V3/YuiHirasawaMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
