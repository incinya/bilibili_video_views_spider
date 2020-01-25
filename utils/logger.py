import logging  # 引入logging模块
import os
import time

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def logger(path='', encoding='utf-8', level='INFO', is_file=False):
    logging.basicConfig(level=level)  # 设置日志级别
    # 第一步，创建一个logger
    _logger = logging.getLogger()
    _logger.setLevel(level)  # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    if is_file:
        rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        log_path = os.path.join(os.getcwd(), path)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        logfile = os.path.join(log_path, rq + '.log')
        fh = logging.FileHandler(logfile, mode='a', encoding=encoding)
        fh.setLevel(level)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        _logger.addHandler(fh)

    return logging


log = logger(encoding='utf-8', path='log')
