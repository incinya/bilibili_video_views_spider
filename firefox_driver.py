import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import log


class FirefoxDriver:
    def __init__(self, head_less=True):
        opt = webdriver.FirefoxOptions()
        opt.add_argument('--window-size=250,600')  # 窗口大小会有影响.
        if head_less:
            opt.add_argument('--headless')  # 无界面化.
            opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
        self.opt = opt

    def play(self, ip, proxy=None):
        """
        :param proxy: 代理
        :param ip: 播放地址
        :return:
        """
        try:
            if proxy:
                self.opt.add_argument('--proxy-server=%s' % proxy)
            with webdriver.Firefox(options=self.opt) as browser:
                # 打开浏览器
                browser.get(ip)
                path = '''//*[@id="bilibiliPlayer"]//button[@class='bilibili-player-iconfont']'''
                log.info(ip)
                # 等待元素渲染完毕再点击播放按钮
                WebDriverWait(browser, 40).until(lambda arg: browser.find_element_by_xpath(path))
                su = browser.find_element_by_xpath(path)
                su.click()
                time.sleep(40)
        except Exception as e:
            log.error(e)

    def play_list(self, ip_list):
        for ip in ip_list:
            self.play(ip)

    def play_loop(self, ip_list):
        while True:
            self.play_list(ip_list)


if __name__ == '__main__':
    from utils.bili_pool import BiliPool

    ip = BiliPool().pop()
    FirefoxDriver().play(ip)
