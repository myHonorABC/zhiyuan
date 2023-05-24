from flask import Flask

from flask import Flask
from codes.bluePrint.loginUrl import loginUrl
from codes.bluePrint.index import indexUrl
from codes.tools.urlTool import RegConverter


app = Flask(__name__)

app.config.from_object('config.settings')

app.secret_key = app.config['SECRET_KEY']  # 设置 secret key 来使用 session

app.url_map.converters['regex'] = RegConverter   # 自定义路由使用正则表达式匹配路由函数的入参

app.register_blueprint(indexUrl)
app.register_blueprint(loginUrl)
