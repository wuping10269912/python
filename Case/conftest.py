"""
=================================
Author: 吴萍
Time: 2021/10/29 下午9:46
Project: touzi_yaml

=================================

"""
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import pytest
from Common.replace_data import EnvData,EnvData_del
from loguru import logger
@pytest.fixture(scope="class")
def init():
    logger.info("开始执行测试项目")
    yield
    logger.info("环境变量：{}".format(EnvData.__dict__))
    logger.info("=========================测试项目执行完毕=========================")
# @pytest.fixture(scope="function")
# def delete_register_user():
#     """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
#     del_sql = base_data["init_sql"]["delete_register_user"]
#     db.execute_db(del_sql)
#     logger.info("注册用户操作：清理用户--准备注册新用户")
#     logger.info("执行前置SQL：{}".format(del_sql))
#     yield # 用于唤醒 teardown 操作
#     db.execute_db(del_sql)
#     logger.info("注册用户操作：删除注册的用户")
#     logger.info("执行后置SQL：{}".format(del_sql))