from flask import Flask

from flask import Flask
from codes.bluePrint.loginUrl import loginUrl
from codes.bluePrint.index import indexUrl


app = Flask(__name__)

app.secret_key = '123456'  # 设置 secret key 来使用 session

app.register_blueprint(indexUrl)
app.register_blueprint(loginUrl)
