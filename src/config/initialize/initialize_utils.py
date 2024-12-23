import os


def log_initialize():
    """
    执行日志文件夹的初始化
    :return: pass
    """
    # 设置日志文件夹路径
    log_folder = "./logs"
    # 检查日志文件夹是否存在，如果不存在则创建
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)


def initialize_trigger():
    """
    执行服务的初始化
    :return: pass
    """
    log_initialize()
