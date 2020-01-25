import json
import re

import requests

SPACE_ID = '10241912'
HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'api.bilibili.com',
    'Origin': 'https://space.bilibili.com',
    'Pragma': 'no-cache',
    'Referer': 'https://space.bilibili.com/10241912/video',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

URL = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp'.format(
    SPACE_ID, '{}')


class BiliPool:
    def __init__(self):
        self.pool = self.get_list()

    @staticmethod
    def get_list():
        count = 1
        urls = []
        while True:
            data = requests.get(URL.format(count), headers=HEADERS)
            content = json.loads(data.content)
            vlist = content.get('data').get('list').get('vlist')
            aid_list = [item.get('aid') for item in vlist]
            if not aid_list:
                return urls
            urls += ['https://www.bilibili.com/video/av' + str(item) for item in aid_list]
            print('播放列表抓取了{}页'.format(count))
            count += 1

    def pop(self):
        """轮盘弹出"""
        res = self.pool.pop(0)
        self.pool.append(res)
        return res

    @staticmethod
    def get_play_times(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        res = requests.get(url, headers=headers)
        re_str = '"viewseo":(\d*)'
        result = re.findall(re_str, res.text)
        times = result[0] if result else None
        return times


if __name__ == '__main__':
    pool = BiliPool()
    times = pool.get_play_times(pool.pop())
    print(times)
