import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).parent
load_dotenv(basedir / '.env')

class Config(object):
    # Dev only so browser doesnt cache for CSS
    SEND_FILE_MAX_AGE_DEFAULT = 0
