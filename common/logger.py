# 标准python日志配置代码
import logging

def get_logger(name="SauceDemoTest"):
    # 创造一个日志收集器
    logger = logging.getLogger(name)
    # 设置最低能被记录的日志级别（INFO及以上都会被记录）
    logger.setLevel(logging.INFO)
    # 防止日志重复打印的陷阱规避
    if not logger.handlers:
        # 创建一个控制台输出渠道
        console_handler = logging.StreamHandler()
        # 定义高端的日志输出格式[时间]-[级别]-具体的日志信息
        formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')
        console_handler.setFormatter(formatter)
        # 将输出渠道绑定在收集器上
        logger.addHandler(console_handler)
    return logger
# 实例化一个供全局使用的logger对象
log = get_logger()