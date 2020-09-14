class Options:
    def options_conf(self):
        from selenium import webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        #options.add_argument("--headless")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #隐身模式
        #options.add_argument('incognito')
        #利用缓存免登录
        #options.add_argument(r'--user-data-dir=C:\Users\王雄开\AppData\Local\Google\Chrome\User Data')
        #去掉密码管理弹窗
        # prefs = {"": ""}
        # prefs["credentials_enable_service"]=False
        # prefs["profile.password_manager_enabled"]=False
        # options.add_experimental_option("prefs",prefs)
        return options