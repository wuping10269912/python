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
from Common.handle_yaml import HandleYaml
from Common.handle_conf import conf
from Common.filepath import conf_path
from Common.replace_data import replace_case_by_regular,expre_data_response,EnvData
filename=os.path.join(conf_path,"invest.yaml")
yaml=HandleYaml(filename)
cases=yaml.read_yaml()
file = os.path.join(conf_path, "data.ini")
filename=os.path.join(conf_path,"touzi.yaml")
yaml_touzi=HandleYaml(filename)
touzi_cases=yaml_touzi.read_yaml()




@allure.step("步骤1 ==>> 管理员审核项目")
def step_1():
    logger.info("步骤1 ==>> 管理员审核项目")


@allure.step("步骤1 ==>> 普通用户进行投资")
def step_2(username):
    logger.info("步骤1 ==>> 普通用户进行投资")

@allure.epic("测试项目")
@allure.feature("投资模块")
@pytest.mark.usefixtures("init")
class Test_Invest:
    '''管理员审核项目'''

    @pytest.mark.sign
    @allure.story("用例--管理员审核项目")
    @allure.description("该用例是针对管理员用户接口的测试")
    @allure.issue("https://blog.csdn.net/ping233", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://blog.csdn.net/ping233", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.parametrize("case",cases)
    def test_loan_audit(self,case):
        logger.info("***********************开始执行{}{}测试用例***********************".format(case["id"],case["title"]))
        step_1()
        #先替换不需要关联的数据--参数化的数据
        replace_case_by_regular(case)
        if hasattr(EnvData,"admin_token"):
            conf.write_admintoken_conf(file,EnvData.admin_token)
            res = send_request(case["method"],case["url"],json.loads(case["request_data"]),token=conf.get("case_data","admin_token"))
        else:
            res = send_request(case["method"], case["url"], json.loads(case["request_data"]))
        try:
            if case["expre_data"]:
                expre_data_response(case["expre_data"],res.json())
                logger.info("环境变量：{}".format(EnvData.__dict__))
            else:
                print("not exist")
        except Exception as e:
            logger.info("该用例没有expre_data字段")
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

    @pytest.mark.sign
    @allure.story("用例--普通用户投资项目")
    @allure.description("该用例是针对普通用户接口的测试")
    @allure.issue("https://blog.csdn.net/ping233", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://blog.csdn.net/ping233", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.parametrize("case", touzi_cases)
    def test_invest(self, case):
        logger.info("***********************开始执行{}{}测试用例***********************".format(case["id"], case["title"]))
        # 先替换不需要关联的数据--参数化的数据
        replace_case_by_regular(case)
        if hasattr(EnvData, "token"):
            conf.write_usertoken_conf(file, EnvData.token)
            res = send_request(case["method"], case["url"], json.loads(case["request_data"]),
                               token=conf.get("case_data", "token"))
        else:
            res = send_request(case["method"], case["url"], json.loads(case["request_data"]))
        try:
            if case["expre_data"]:
                expre_data_response(case["expre_data"], res.json())
                logger.info("环境变量：{}".format(EnvData.__dict__))
            else:
                print("not exist")
        except Exception as e:
            logger.info("该用例没有expre_data字段")
        expect = json.loads(case["expect"])
        logger.info("期望结果为{}".format(expect))
        logger.info("响应结果为:{}".format(res.json()))
        if expect:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["msg"] == expect["msg"]

            except Exception as e:
                logger.info("断言失败")
                raise
            return res

