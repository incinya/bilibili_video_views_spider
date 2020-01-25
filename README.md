## driver国内镜像
http://npm.taobao.org/mirrors/chromedriver/

## bilibili_video_views_spider
自动播放视频，配合换ip等可以刷点播放量

#### 运行主目录的 main.py 看看效果 若不行试试pull1.0稳定版

若要实现伪造多个高匿ip访问
spider代理池是必要的 https://github.com/incinya/proxies
即proxies文件夹，它是基于redis的，使用它可能要改下redis配置

## redis配置，在proxies.memory.conf.py
DB = 2
PASSWORD = 123456
HOST = '10.168.1.245'
PORT = 6379

#### 修改根目录下的conf.py把视频地址，up主空间改成自己的就可以了

#### test文件测试ip变化

####提升selenium速度
driver.get()这个操作，改成不阻塞的

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(executable_path='chromedriver.exe')

