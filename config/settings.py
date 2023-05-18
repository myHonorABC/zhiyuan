
HOST = '127.0.0.2'
PORT = 5000
SECRET_KEY = '123456'

try:
    from config.dbSettings import *
except ImportError:
    pass
