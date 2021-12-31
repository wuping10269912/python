"""
=================================
Author: 吴萍
Time: 2021/10/29 下午10:04
Project: touzi_yaml

=================================

"""
'''
对用例里面的参数化进行替换---正则表达式
'''
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #获取当前绝对路径
filePath = os.path.split(curPath)[0] #获取当前目录的上一级目录路径，将文件名和路径切割，然后只取路径
sys.path.append(curPath.split('xxxx')[0])#以xxxx来分割，且只取第一个，并把它追加到python系统模块中
rootPath = curPath.split('xxxx')[0]+"xxxx"#按xxxx分割后，取第一个后，在接上xxxx
sys.path.append(filePath)#sys.path是python的搜索模块的路径集
sys.path.append(rootPath)

import os

import re
import json

import jsonpath
from Common.random_data import get_newphone_writeconf
from Common.filepath import conf_path
from Common.handle_conf import HandleConf
from loguru import logger
filename=os.path.join(conf_path,"data.ini")
hc=HandleConf(filename)
class EnvData():
    pass
def EnvData_del():
    value=dict(EnvData.__dict__.items())
    for key,value in value.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData,value)
def expre_data_response(extract_exprs,response_dict):
    """
       根据jsonpath提取表达式，从响应结果当中，提取数据并设置为环境变量EnvData类的类属性，作为全局变量使用。
       :param extract_exprs: 从excel当中读取出来的，提取表达式的字符串。
       :param response_dict: http请求之后的响应结果。
       :return:Nonoe
       """
    # 将提取表达式转换成字典
    extract_dict = eval(extract_exprs) #yaml文件中已经是字典类无需再转换，但是excel需要转换
    # 遍历字典，key作为全局变量名，value是jsonpath提取表达式。
    for key, value in extract_dict.items():
        # 提取
        res = str(jsonpath.jsonpath(response_dict, value)[0])

        # 设置环境变量
        logger.info("设置环境变量：key:{},value:{}".format(key, res))
        setattr(EnvData, key, res)
        # hc.set("case_data", "admin_token", res)
        # # hc.set("case_data", "token", res)
        # hc.write(open(filename, "w"))
        # hc.writeconf(filename, res)


def replace_case_by_regular(case):
    '''
    对excel中，读取出来的整条测试用例做全部替换，包括url,request_data,check_sql，expect
    :param case:
    :return:
    '''
    # #方法一：
    # #把case的请求的数据类型：字典转换为字符串
    # case_str=json.dumps(case)
    # #生成新的请求数据，替换，调用replace_data_regular的函数
    # new_case=replace_data_regular(case_str)
    # #把替换的字符串，再转为字典
    # case_dict=json.loads(new_case)
    # return case_dict
    for key,value in case.items():#对元组进行拆包
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_data_regular(value)
        else:
            value=json.dumps(value)
            case[key] = replace_data_regular(value)
    logger.info("正则表达式替换完成之后的请求数据为{}".format(case))
    logger.info("环境变量为:{}".format(EnvData.__dict__))
    return case

'''
用正则表达式替换
'''
def replace_data_regular(data):
    '''
    在excel中查找以#开头，以#结尾的字符串，如果找到则替换，如果没有找到则返回空列表
    :param data:
    :return:
    '''
    # if data is isinstance(data,dict):
    #     data=json.dumps(data)
    res=re.findall("#(.*?)#",data)#如果没有找到，返回空列表
    # res = re.compile(r"#(.*?)#")#正则匹配
        #标识符对应的值，来自：1、配置文件 2 环境变量
    if res:
        for item in res:#item是字符串
            try:
                value=hc.get("case_data",item)
            except:
                try:
                    value=getattr(EnvData,item)
                except AttributeError:
                    continue
            data=data.replace("#{}#".format(item),value)
                # data=data.replace("${}".format(item),value)
        #print('==========',data)
    return data

if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://192.168.0.104:7080/token/redis/token",
        "request_data": '{"mobile_phone": "#register_mobile_phone#","pwd": "#pwd#","type": 1,"reg_name": "小橘子"}'
    }
    res=replace_case_by_regular(case)
    print(res)