"""
=================================
Author: 吴萍
Time: 2021/10/30 下午12:30
Project: touzi_yaml

=================================

"""
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import pytest

# from loguru import logger
from Common.filepath import out_put
# logger.add(os.path.join(out_put,"loggers.log"))
# pytest.main(["-s",
#              "-v",
#              "-m","sign",
#              "--html=pyreports.html",
#              "--alluredir=allure_dir",
#              "--reruns","2","--reruns-delay","5"])

pytest.main(["-s",
             "-v",
             "-m","sign",
             "--alluredir=allure_dir"])