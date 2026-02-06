import yaml
import os

def read_yaml(file_path):
    """
    读取 YAML 文件
    :param file_path: 文件相对于项目的路径
    :return: 列表或字典
    """
    # 获取当前项目的根目录（这里有个小技巧，先别管，照抄即可，以后解释）
    # 假设我们从 data 目录直接读，这里先简化处理，直接传完整路径
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data