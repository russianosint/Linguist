import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMIN_IDS = list(os.getenv('ADMIN_IDS'))