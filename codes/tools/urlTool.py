from werkzeug.routing import BaseConverter


'''
正则表达式路由类，使用正则表达式匹配路由函数传入参数。

使用实例：

app.url_map.converters['regex'] = RegConverter  # 自定义路由使用正则表达式匹配路由函数的入参

# 使用正则表达式匹配路由函数入参，匹配规则为：'\d+'
@app.route('/index/<regex('\d+'):x1>')
def index(x1):
    print(x1)
    return render_template('index.html)

'''
class RegConverter(BaseConverter):
    def __init__(self, map, regex):
        super().__init__(map)
        self.regex = regex

    def to_python(self, value):
        return value
