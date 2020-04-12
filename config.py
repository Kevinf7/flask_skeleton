import os
from dotenv import load_dotenv
from pathlib import Path

# handy to have - makes referencing files on local system each
basedir = Path(__file__).parent
# loads .env
load_dotenv(basedir / '.env')

class Config(object):
    # Used by Flask and extensions like WTF to prevent CSRFsed by Flask and WTF extension
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random string'

    # Dev only so browser doesnt cache for CSS
    SEND_FILE_MAX_AGE_DEFAULT = 0
