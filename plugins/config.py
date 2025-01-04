import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7885458993:AAGcrfHkaQ2TSsUoOGAzpi5Sjox48nU0BCw")
    
    API_ID = int(os.environ.get("API_ID", "21894814"))
    
    API_HASH = os.environ.get("API_HASH", "4366bdf6ed33089c363df8e4d7b9a1b5")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = ""
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "HTTP_PROXY")
    
    OUO_IO_API_KEY = "OUO_IO_API_KEY"
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "UploadLinkToFile"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ndjdn6062:QrBljgOpVLbSBeSr@cluster0.f0a88.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFile")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002367641884"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "1002367641884")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5071005351"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Ariana_leech_bot")
                                  
