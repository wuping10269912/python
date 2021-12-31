"""
=================================
Author: 吴萍
Time: 2021/10/29 下午3:06
Project: touzi_yaml

=================================

"""
'''
读取yaml中的测试用例
'''
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
import yaml
class HandleYaml:

    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        with open(self.filename,mode='r', encoding='utf-8') as fs:
            # 避免报警告：yaml.FullLoader，load是将字符串转换为字典类型
            data = yaml.load(fs, Loader=yaml.FullLoader)
            return data
    def write_yaml(self,data,name):
        '''
        向yaml文件写入
        :param data: 要写入的数据
        :return:
        '''
        with open(self.filename,"w",encoding="utf-8") as fs:
            #写入的数据
            data={name:data}
            #允许写入中文：allow_unicode=True
            yaml.dump(data,stream=fs,allow_unicode=True)

if __name__ == '__main__':
    import os
    from Common.filepath import conf_path
    filename=os.path.join(conf_path,"register.yaml")
    rc=HandleYaml(filename)
    case=rc.read_yaml()
    print(case)

