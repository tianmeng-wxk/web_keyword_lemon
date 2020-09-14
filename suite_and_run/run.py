import pytest,os,time
from common.common import send_mail,send_email
from config.config import case,report_path

if __name__ == '__main__':
    #pytest.main()

    #生成pytest-html报告
    report_path = report_path
    report_file = report_path+"{}_pytest_html.html".format(time.strftime("%Y-%m-%d  %H-%M-%S",time.localtime()))
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        pass
    pytest.main(["-s", "-v", "../test_case/test_cases.py", "--html="+report_file])
    #-k "关键字" -q 返回简化的控制台 --maxfail=2两次失败就停止 -n=2多线程，命令行中无=  --reruns=5，命令行中无=
    #--reruns-delay=10命令行中无=
    send_email(case)

    #生成allure报告
    # import os
    # pytest.main(['-s','../test_case/test_cases.py', '--alluredir', '../report/html_xml'])#生成alure缓存文件
    # os.system('allure generate --clean ../report/html_xml -o ../report/allure_html')
    # send_mail('../report/allure_html/index.html')
    # os.system('allure serve ../report/allure_xml')