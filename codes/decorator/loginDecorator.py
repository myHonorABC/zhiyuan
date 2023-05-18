import functools
from flask import session, render_template


'''该装饰器用于验证用户是否登录'''
def auth(func):
    @functools.wraps(func)
    def innerFunc(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return render_template('login.html')
        return func(*args, **kwargs)
    return innerFunc
