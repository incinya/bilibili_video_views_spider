from firefox_driver import FirefoxDriver
from utils.bili_pool import BiliPool

ip = BiliPool().pool

FirefoxDriver().play_loop(ip)
