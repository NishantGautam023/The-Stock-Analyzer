from dotenv import load_dotenv
import os

load_dotenv()


HOST = '127.0.0.1'
PORT = 8848
debug = True
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
