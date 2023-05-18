from flask import render_template
from flask import Blueprint
from codes.decorator.loginDecorator import auth

indexUrl = Blueprint('indexUrl', __name__)

# 创建主页路由和登录逻辑
@indexUrl.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
