import uuid
from flask import render_template, request, redirect, url_for, session
from flask import Blueprint
from codes.decorator.loginDecorator import auth
from codes.tools.loggerTool import logger, run_logger


loginUrl = Blueprint('loginUrl', __name__)


# 创建登录页路由
@loginUrl.route('/login', methods=['GET', 'POST'])
def login():
    run_logger.info('Welcome to the login!')
    return redirect(url_for('loginUrl.welcome'))
    # return render_template('index.html')

# 创建session
@loginUrl.route('/login/session', methods=['GET','POST'], endpoint='session')
def create_session():
    run_logger.info('Create session.')
    if request.method == 'POST':
        session['user_id'] = str(uuid.uuid4())
        session['username'] = request.form['name']  # 将用户名存储在 session 中
        return redirect(url_for('loginUrl.login'))

# 创建欢迎页路由
@loginUrl.route('/welcome', methods=['GET', 'POST'])
@auth
def welcome():
    run_logger.info('Welcome to the welcome!')
    username = session.get('username')  # 从 session 中获取用户名
    run_logger.info('The login name is %s.' % username)
    if not username:
        run_logger.info('The login name does not exist.')
        return render_template('login.html')  # 如果没有用户名则返回到主页
    return render_template('welcome.html', username=username)

@loginUrl.route('/logout')
def logout():
    # 在这里实现清除用户信息和登出操作。
    # 推荐使用session来存储用户登录信息，通过session.clear()方法清空session。
    run_logger.info('Welcome to the logout!')
    if 'user_id' in session:
        session.clear()
        # run_logger('The user_id in session is clear.')
    return redirect(url_for('loginUrl.login'))

@loginUrl.route('/about')
def about():
    run_logger.info('Welcome to the about!')
    # 定义动态数据
    data = {
        'title': 'My First Flask Application',
        'heading': '志愿报考助手',
        'contents': ['reading', 'sports', 'traveling']
    }
    return render_template('about.html', data=data)
