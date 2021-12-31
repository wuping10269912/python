"""
=================================
Author: 吴萍
Time: 2021/11/3 上午9:55
Project: touzi_yaml

=================================

"""
import sys
sys.path.append("/var/jenkins_home/touzi_yaml")
from faker import Faker

faker = Faker('zh-CN')
print(faker.providers)



def random_name():
    return faker.name()
def random_address():
    return faker.address()
def random_text():
    return faker.text()
def random_email():
    return faker.email()
def random_phone_number():
    return faker.phone_number()
def random_credit_card():
    return faker.credit_card()
def random_bank():
    return faker.bank()

if __name__ == '__main__':

    name=random_name()
    print(name)
    email=random_email()
    print(email)
    address=random_address()
    print(address)
    phone=random_phone_number()
    print(phone)
