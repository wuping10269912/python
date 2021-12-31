"""
=================================
Author: 吴萍
Time: 2021/10/29 下午9:44
Project: touzi_yaml

=================================

"""
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import pytest
import allure
import os
import json
from Common.handle_request import send_request
from loguru import logger
from Common.handle_yaml import HandleYaml
from Common.filepath import conf_path
from Common.replace_data import replace_case_by_regular
filename=os.path.join(conf_path,"login.yaml")
yaml=HandleYaml(filename)
cases=yaml.read_yaml()
@pytest.mark.sign
@allure.epic("测试项目")
@allure.feature("登录模块")
@pytest.mark.usefixtures("init")
class Test_Login:
    @pytest.mark.parametrize("case",cases)
    def test_login(self,case):
        logger.info("开始执行{}{}测试用例".format((),case["id"],case["title"]))
        replace_case_by_regular(case)
        res=send_request(case["method"],case["url"],json.loads(case["request_data"]))
        expect=json.loads(case["expect"])
        logger.info("期望结果为{}".format(expect))
        logger.info("响应结果为:{}".format(res.json()))
        logger.info("用例通过！")
        if expect:
            try:
                assert res.json()["code"]==expect["code"]
            except Exception as e:
                logger.info("断言失败")
                raise
            return res


