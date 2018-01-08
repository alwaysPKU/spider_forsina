import os

def mkdir(path):
    """
    创建并且返回路径
    :param path: 
    :return: 
    """
    if not os.path.exists(path):
        return os.mkdir(path)
    else:
        return path
