import os,configparser
base_path = os.getcwd()


#存放用例的路径
case_path = os.path.join(base_path,"../cases/")

#需要运行的用例
case = os.path.join(case_path,'login.xlsx')


#生成的报告路径
report_path = os.path.join(case_path,'../report/')


#发送邮件配置
test_config_file = os.path.join(base_path, '../config', 'config.ini')
rc = configparser.ConfigParser()
rc.read(test_config_file, encoding='utf-8')
host = rc.get('email', 'host')
port = rc.get('email', 'port')
sender = rc.get('email', 'sender')
password = rc.get('email', 'password')
receiver = rc.get('email', 'receiver')
