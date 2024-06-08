from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 8848))
debug = os.getenv('DEBUG', 'False') == 'True'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
