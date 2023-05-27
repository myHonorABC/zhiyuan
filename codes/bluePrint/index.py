from flask import render_template
from flask import Blueprint
from codes.tools.loggerTool import logger, run_logger

indexUrl = Blueprint('indexUrl', __name__)


# index_logger = logger.create_logger(__name__, 'log/index.log')     # 创建 index 蓝图日志


# 创建主页路由和登录逻辑
@indexUrl.route('/', methods=['GET', 'POST'])
def index():
    run_logger.info('Welcome to the index!')
    return render_template('index.html')
