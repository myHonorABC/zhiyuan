import os
import configparser

# 查找 config.cfg 路径
path = os.path.abspath(os.path.dirname(__file__))
config_file_path = os.path.join(path, 'config.cfg')
# 读取 config.cfg 文件
config = configparser.ConfigParser()
config.read(config_file_path)

# 获取配置文件中的参数
debug = config.getboolean('DEFAULT', 'debug')
console_logger = config.getboolean('DEFAULT', 'console_logger')
file_logger = config.getboolean('DEFAULT', 'file_logger')

# 网络服务配置
host = config.get('WEB_SERVER', 'host')
port = config.getint('WEB_SERVER', 'port')

# 数据库配置
db_host = config.get('DATABASE', 'db_host')
db_port = config.getint('DATABASE', 'db_port')
db_user = config.get('DATABASE', 'db_user')
db_password = config.get('DATABASE', 'db_password')
# 数据库链接池配置
database = config.get('DATABASE', 'database')
maxconnections = config.getint('DATABASE', 'maxconnections')
mincached = config.getint('DATABASE', 'mincached')
blocking = config.getboolean('DATABASE', 'blocking')
ping = config.getint('DATABASE', 'ping')
