"""
=================================
Author: 吴萍
Time: 2021/10/29 下午5:28
Project: touzi_yaml

=================================

"""
'''
封装日志:
1、创建收集器
2、设置日志输出格式
3、设置输出渠道
4、将输出格式绑定到输出渠道中
5、将输出渠道加到收集器中
'''
import logging
import os
from Common.handle_conf import HandleConf
from Common.filepath import conf_path,out_put
# filename = os.path.join(conf_path, "log.ini")
# conf=HandleConf(filename)
# class Handel_logger(logging.Logger):
#
#     def __init__(self, filename=None):
#         '''
#         先设置收集器，读取日志级别
#         :param filename: 输出渠道--文件
#         '''
#         #设置收集器
#         log_name=conf.get("log","log_name")
#         # 设置日志级别
#         log_level = conf.get("log", "log_level")
#         super().__init__(log_name,log_level)
#
#         #设置输出格式：
#         fmt=' %(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d： %(message)s'
#         formatter=logging.Formatter(fmt)
#         # 设置输出渠道---控制台
#         console = logging.StreamHandler()
#         #将日志格式绑定到输出渠道中
#         console.setFormatter(formatter)
#         #将输出渠道添加到日志收集器中
#         self.addHandler(console)
#         #判断是否要将日志输出到日志文件
#         if filename:
#             # 设置输出渠道---控制台
#             output_file = logging.FileHandler(filename,encoding="utf-8")
#             output_file.setFormatter(formatter)
#             self.addHandler(output_file)
# if conf.getboolean("log","file_ok"):
#     filename=os.path.join(out_put,conf.get("log","log_name"))
# else:
#     filename=None
# logger=Handel_logger(filename)
# if __name__ == '__main__':
#     logger.info("test_register的测试日志！")
