"""
=================================
Author: 吴萍
Time: 2021/10/29 下午4:37
Project: touzi_yaml

=================================

"""
'''
封装headers,url,requests请求方式
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import os
import requests
from Common.handle_conf import HandleConf
from Common.filepath import conf_path
from loguru import logger
confpath=os.path.join(conf_path,"data.ini")
hc=HandleConf(confpath)

def __url(url):
    url=hc.get("server","url")+url
    return url
def __header(token=None):
    header = {"X-Lemonban-Media-Type": "lemonban.v2"}
    if token:
        header["Authorization"] = "Bearer {}".format(token)  # token是动态值
    return header
def send_request(method,url,data,token=None):
    url=__url(url)
    header=__header(token)
    logger.info('开始发起请求：')
    logger.info("请求头为:{}".format(header))
    logger.info("请求地址为:{}".format(url))
    logger.info("请求数据为:{}".format(data))
    try:
        if method=="POST":
            res=requests.post(url,json=data,headers=header)
        elif method=="GET":
            res = requests.get(url, params=data, headers=header)
        elif method=="PATCH":
            res = requests.patch(url, json=data, headers=header)
        elif method=="PUT":
            '''
                    封装put方法，uri是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
                    :param uri: 访问路由
                    :param params: 传递参数，string类型，默认为None
                    :return: 此次访问的response
            '''
            if data is not None:
                # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
                # 返回request的Response结果，类型为requests的Response类型
                res=requests.put(url,json=data,headers=header)
            else:
                # 如果无参数，访问方式如下
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.put(url)
        elif method=="DELETE":
            '''
                封装delete方法，uri是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
                :param uri: 访问路由
                :param params: 传递参数，string类型，默认为None
                :return: 此次访问的response
            '''
            if data is not None:
                # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
                # 返回request的Response结果，类型为requests的Response类型
                res=requests.delete(url,data=data,headers=header)
            else:
                # 如果无参数，访问方式如下
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.delete(url,headers=header)
    except Exception as e:
        logger.info("无效的请求方式，get/post/put/delete,请查找原因！！！")
        logger.exception("错误为{}".format(e))
        raise e
    else:
        logger.info("响应数据为{}".format(res.status_code))
        return res


if __name__ == '__main__':
    login_url = "member/login"
    login_datas = {
        "mobile_phone": "17811111111",
        "pwd": "123456789"
    }
    res=send_request('POST',login_url,login_datas)
    # print(res.json())