import pymysql
import threading
from dbutils.pooled_db import PooledDB
from config.configManager import db_host, db_password, db_port, db_user
from config.configManager import maxconnections, mincached, blocking, ping, database


class SqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,      # 使用链接数据库的模块。
            maxconnections=maxconnections,     # 链接池允许的最大连接数，0 或 NONE 表示不限制链接数。
            mincached=mincached,           # 初始化时，链接池中至少创建的链接，0 表示不创建。
            blocking=blocking,        # 链接池中如果没有可用链接后，是否阻塞等待。True：等待；False：不等待。
            ping=ping,               # ping mysql 服务器，检查是否服务可用。
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=database,
            charset='utf8'
        )
        self.local = threading.local()  # threading local 用于存放 conn 与 cursor

    def open(self):
        '''建立数据库链接'''
        conn = self.pool.connection()
        cursor = conn.cursor()
        return conn, cursor
    
    def close(self, cursor, conn):
        '''关闭数据库链接'''
        cursor.close()
        conn.close()

    def fetchall(self, sql, *args):
        '''获取所有数据'''
        conn,cursor = self.open()
        cursor.execute(sql,args)
        result = cursor.fetchall()
        self.close(conn,cursor)
        return result
    
    def fetchone(self, sql, *args):
        '''获取单条数据'''
        conn,cursor = self.open()
        cursor.execute(sql,args)
        result = cursor.fetchone()
        self.close(conn,cursor)
        return result

    def __enter__(self):
        '''上下文入口函数：将conn与cursor数据放入local数据列表中，同时返回cursor'''
        conn, cusor = self.open()
        rv = getattr(self.local,'stack',None)
        if not rv:
            self.local.stack = [(conn,cusor),]
        else:
            rv.append((conn,cusor))
            self.local.stack = rv
        return cusor
    
    def __exit__(self):
        '''上下文出口函数：退出上下文后关闭conn与cursor'''
        rv = getattr(self.local,'stack',None)
        if not rv:
            return
        conn,cursor = self.local.stack.pop()
        self.close(conn,cursor)


db = SqlHelper()


# if __name__ == '__main__':
#     '''实现上下文的嵌套，查询当前用户和所有表的信息'''
#     with db as cursor1:
#         cursor1.execute('SELECT USER(), CURRENT_USER()')
#         print(cursor1.fetchall())
#         with db as cursor2:
#             cursor2.execute('SHOW TABLES')
#             print(cursor2.fetchall())
