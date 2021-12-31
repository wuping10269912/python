"""
=================================
Author: 吴萍
Time: 2021/10/29 下午4:52
Project: touzi_yaml

=================================

"""
'''
连接数据库：
步骤：连接数据库：host,port,username,password,databases,charset,cursorclass
     建立游标
     获取数据
     关闭数据库
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import pymysql
import os
from Common.filepath import conf_path
from Common.handle_conf import HandleConf
conf_path=os.path.join(conf_path,"mysql.ini")
hc=HandleConf(conf_path)
mysql_path=os.path.join(conf_path,"mysql.ini")
class HandelDB:

    def __init__(self):
        '''
        如果项目中有不同的库，不要读取配置文件，需要进行参数化处理。
        '''
        self.conn=pymysql.connect(
            host=hc.get("mysql","host"),
            port=int(hc.get("mysql","port")),
            user=hc.get("mysql","user"),
            password=hc.get("mysql","password"),
            database=hc.get("mysql","database"),
            charset=hc.get("mysql","charset"),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur= self.conn.cursor()
    def count(self,sql):
        #更新数据库
        self.conn.commit()
        #执行sql语句
        count=self.cur.execute(sql)
        return count
    def get_one_data(self,sql):
        # 更新数据库
        self.conn.commit()
        # 执行sql语句
        self.cur.execute(sql)
        return self.cur.fetchone()
    def get_all_data(self,sql):
        # 更新数据库
        self.conn.commit()
        # 执行sql语句
        self.cur.execute(sql)
        return self.cur.fetchall()

    # 更新数据库
    def update(self, sql):
        '''
            对数据库进行增删改操作，如果出错，则进行异常处理
            :return:
        '''
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()  # 发生错误时回滚
            raise

    # 关闭数据库连接
    def close(self):
        self.cur.close()
        self.conn.close()
if __name__ == '__main__':
    db = HandelDB()
    sql = 'select * from member where mobile_phone="17866666666"'
    # 发起一个注册请求
    from Common.handle_request import send_requests
    case = {
        "method": "POST",
        "url": "member/register",
        "request_data": {"mobile_phone": "17866666666", "pwd": "123456789", "type": 1, "reg_name": "可爱"}
    }
    response = send_requests(case["method"], case["url"], case["request_data"])  # 接口
    print("响应结果：", response.json())
    # 查询注册的手机号码
    count = db.get_one_data(sql)
    print("获取到的结果为：", count)