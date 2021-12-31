"""
=================================
Author: 吴萍
Time: 2021/10/29 下午3:30
Project: touzi_yaml

=================================

"""
'''
获取各个文件路径
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import os
#获取工程路径
pro=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#路径拼接
#获取配置文件路径
conf_path=os.path.join(pro,"Conf")

out_put=os.path.join(pro,"OutPut")