"""
=================================
Author: 吴萍
Time: 2021/10/30 下午4:43
Project: touzi_yaml

=================================

"""
'''
充值测试用例
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import pytest
import os
import json
import allure
from Common.handle_request import send_request
from loguru import logger
from Common.handle_db import HandelDB
from Common.handle_yaml import HandleYaml
from Common.handle_conf import HandleConf
from Common.filepath import conf_path
from Common.replace_data import replace_case_by_regular,expre_data_response,EnvData
filename=os.path.join(conf_path,"recharge.yaml")
yaml=HandleYaml(filename)
cases=yaml.read_yaml()
tokenfile=os.path.join(conf_path,"data.ini")
hc=HandleConf(tokenfile)
db=HandelDB()

@allure.epic("测试项目")
@allure.feature("充值模块")
@pytest.mark.usefixtures("init")
class Test_Recharge:
    @pytest.mark.parametrize("case",cases)
    def test_recharge(self,case):
        logger.info("***********************开始执行{}{}测试用例***********************".format(case["id"],case["title"]))
        replace_case_by_regular(case)
        # if hasattr(EnvData,"member_id"):
        #     replace_case_by_regular(case)
        if hasattr(EnvData,"token"):
            res = send_request(case["method"],case["url"],json.loads(case["request_data"]),token=EnvData.token)
        else:
            res = send_request(case["method"], case["url"], json.loads(case["request_data"]))
        try:
            if case.get("expre_data"):
                expre_data_response(case["expre_data"],res.json())
                logger.info("环境变量：{}".format(EnvData.__dict__))

            else:
                print("not exist")

        except Exception as e:
            logger.info("该用例没有expre_data字段")
        try:
            if case.get("sql"):
                amount = db.get_one_data(case["sql"])
                logger.info("充值后的余额为{}".format(amount))
        except Exception as e:
            logger.info("该用例没有sql字段")
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

