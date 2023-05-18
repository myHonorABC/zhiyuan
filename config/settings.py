
HOST = '127.0.0.2'
SECRET_KEY = '123456'

try:
    from config.dbSettings import *
except ImportError:
    pass
