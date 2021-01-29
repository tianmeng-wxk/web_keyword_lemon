from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from options.chrome_options import Options
from time import sleep
import requests
from log.log import Logger

def open_browser(browser_type):
    try:
        if browser_type == 'CHR':
            global driver
            driver = webdriver.Chrome(options=Options().options_conf())
        else:
            driver = getattr(webdriver, browser_type)()
    except Exception as e:
        driver = webdriver.Chrome()
    return driver

def close_browser():
    driver.close()


def visit(url):
    driver.get(url)

def find_element(loc_type,loc_ex):
    return driver.find_element(loc_type, loc_ex)
    #return WebDriverWait(driver,10,0.5).until(lambda x:x.find_element(loc_type,loc_ex))

def input(loc_type,loc_ex,txt):
    find_element(loc_type,loc_ex).send_keys(txt)

def click(loc_type,loc_ex):

    find_element(loc_type, loc_ex).click()
    try:
        find_element("xpath",'//*[text()="验证码错误"]')
    except:
        pass
    else:
        # index = 1
        # Logger().log().debug("验证码识别失败，第{}次重试".format(index))
        find_element("xpath", '//*[@id="codeimage"]').click()
        find_element("id", 'captcha_normal').clear()
        i = ivercode()
        find_element("xpath", '//*[@id="captcha_normal"]').send_keys(i)
        find_element(loc_type, loc_ex).click()
        # index = index + 1




def wait(time):
    driver.implicitly_wait(time)

def sleeps(time):
    sleep(int(time))

def assert_text(loc_type, loc_ex, expect):
    try:
        reality = find_element(loc_type,loc_ex).text
        assert reality == expect
        Logger().log().info("流程正确，断言成功！")
        return True
    except Exception as e:
        Logger().log().info("流程正确，断言失败！失败信息：{}".format(e))
        return False

def ivercode():

        ele = driver.find_element_by_id("codeimage")
        ele.screenshot("../vercode_img/verify.png")
        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
        data = {
            'user': 'wuqingfqng',
            'pass2': '6e8ebd2e301f3d5331e1e230ff3f3ca5',#密碼：wuqing&fqng
            "softid": "904357",
            "codetype": "1902"
        }
        userfile = open("../vercode_img/verify.png", "rb").read()
        userfile = {"userfile": ("../vercode_img/verify.png", userfile)}
        res = requests.post("http://upload.chaojiying.net/Upload/Processing.php",data=data, files=userfile, headers=headers)
        res = res.json()
        vercode = res["pic_str"]
        vercode = vercode[:3]
        return vercode








def verify(value):
    assert value in driver.page_source#验证当前页面中是否含有value




