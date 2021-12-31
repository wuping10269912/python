"""
=================================
Author: 吴萍
Time: 2021/10/29 下午4:42
Project: touzi_yaml

=================================

"""
'''
随机生成手机号
1、前三位是固定的，从列表phone中取值，value=len(phone)-1
2、生成后8位 用for 
3、后八位的数范围是0-9随机生成 random.randint()
4、前三位与后八位拼接
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import random
import os

from Common.handle_conf import HandleConf
from Common.filepath import conf_path
from Common.handle_db import HandelDB
from Common.data_random_faker import random_phone_number

db=HandelDB()


# p=[130,131,132,134,135,136,137,138,139,145,147,150,151,152,155,156,157,158,159,182,183,185,186,187,188]
# def __phone():
#     index=random.randint(0,len(p)-1)
#     phone=str(p[index])
#     for i in range(0,8):#生成后8位
#         phone+=str(random.randint(0,9))#生成0-9随机数
#     # print(phone)
#     return phone

#未注册的手机号
def get_newphone():
    #连接数据库
    while True:
        #1、生成手机号
        #phone = __phone()
        phone=random_phone_number()
        #2、校验数据库是否存在，存在则重新生成
        try:
            count=db.count('select * from futureloan.member where mobile_phone="{}"'.format(phone))
            if count == 0:#手机号码没有在数据库查到，表示未注册的手机号
                # print('账号未注册')
                db.close()
            return phone
        except:
            print('手机号生成有误')
            raise


def get_newphone_writeconf():
    filename = os.path.join(conf_path, "data.ini")
    hc = HandleConf(filename)
    p = hc.writeconf(filename, phone)
    print(p)


phone=get_newphone()
print(phone)
if __name__ == '__main__':
    p=get_newphone_writeconf()
    print(p)
