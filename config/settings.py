'''
该文件用于设置flask项目的配置参数
'''


HOST = '127.0.0.1'
PORT = 5000
SECRET_KEY = '123456'

DB_HOST = '192.168.2.2'



try:
    from config.localSettings import *
except ImportError:
    pass
