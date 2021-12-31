"""
=================================
Author: 吴萍
Time: 2021/10/30 上午8:43
Project: touzi_yaml

=================================

"""
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
from Common.random_data import get_newphone_writeconf

'''
注册功能的测试用例
1、替换数据，手机号随机生成
2、发送请求
3、断言
'''

import pytest
import os
import json
import allure
import time
from Common.handle_request import send_request
from loguru import logger
from Common.handle_yaml import HandleYaml
from Common.filepath import conf_path
from Common.replace_data import replace_case_by_regular

filename=os.path.join(conf_path,"register.yaml")
yaml=HandleYaml(filename)
cases=yaml.read_yaml()

@allure.epic("测试项目")
@allure.feature("注册模块")
@pytest.mark.usefixtures("init")
class Test_Register:
    @pytest.mark.parametrize("case",cases)
    def test_login(self,case):
        logger.info("***********************开始执行{}{}测试用例***********************".format(case["id"],case["title"]))
        #生成随机手机号
        get_newphone_writeconf()
        time.sleep(5)
        replace_case_by_regular(case)
        res=send_request(case["method"],case["url"],json.loads(case["request_data"]))
        expect=json.loads(case["expect"])
        logger.info("期望结果为{}".format(expect))
        logger.info("响应结果为:{}".format(res.json()))
        if expect:
            try:
                assert res.json()["code"]==expect["code"]
                assert res.json()["msg"] == expect["msg"]
            except Exception as e:
                logger.info("断言失败")
                raise
            return res
