"""
=================================
Author: 吴萍
Time: 2021/10/29 下午4:58
Project: touzi_yaml

=================================

"""
'''
读取.ini配置文件
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import os

from Common.filepath import conf_path

from configparser import ConfigParser
c=ConfigParser()

class HandleConf(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")
    def writeconf(self, filename, value):
        '''

        :param filename: 配置文件路径
        :param value: 配置文件的options的值
        :return:
        '''

        # 添加section
        # conf.add_section("goods_id")
        # 写入options
        conf.set("case_data", "register_mobile_phone", value)
        conf.write(open(filename, "w"))
    def write_admintoken_conf(self, filename, value):
        '''

        :param filename: 配置文件路径
        :param value: 配置文件的options的值
        :return:
        '''

        # 添加section
        # conf.add_section("goods_id")
        # 写入options
        # conf.set("case_data", "register_mobile_phone", value)
        conf.set("case_data", "admin_token", value)
        conf.write(open(filename, "w"))
    def write_usertoken_conf(self, filename, value):
        '''

        :param filename: 配置文件路径
        :param value: 配置文件的options的值
        :return:
        '''

        # 添加section
        # conf.add_section("goods_id")
        # 写入options
        conf.set("case_data", "token", value)
        conf.write(open(filename, "w"))
filename = os.path.join(conf_path, "data.ini")
conf=HandleConf(filename)
if __name__ == '__main__':
    # from Common.random_data import get_newphone
    # phone=get_newphone()
    # p = conf.writeconf(filename, phone)
    # print(p)
    data=conf.read(filename)
    print(data)


