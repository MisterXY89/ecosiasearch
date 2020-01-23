
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# ========== get vars ========== #
# TOR #
TOR_PASS = os.getenv('TOR_PASS')
