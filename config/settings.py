'''
该文件用于设置flask项目的配置参数
'''

SECRET_KEY = '123456'



try:
    from config.localSettings import *
except ImportError:
    pass
