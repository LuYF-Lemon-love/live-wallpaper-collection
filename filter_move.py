# @Created_Time     : 2024/08/04
# @Created_Author   : luyanfeng
# @Updated_Time     : 2024/08/04
# @Updated_Author   : luyanfeng
# @File             : filter_move.py
# @desc             : filter live wallpapers by 50 MB and move to baidu directory
# @src_data         : None
# @dest_data        : None

import os
import shutil
import logging
from logging import Logger

# 日志器，将日志打印到日志文件中
logger: Logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(levelname)s:%(module)s:%(funcName)s:%(asctime)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    filename="filter_move.log",
    filemode='a',
    encoding='utf-8',
)

def filter_move(
        src_dir: str,
        dist_dir: str
) -> None:

    """
    从src_dir目录中筛选出大于50MB的.mp4文件，并移动到dist_dir目录中。
    
    Args:
        src_dir (str): 源目录路径。
        dist_dir (str): 目标目录路径。
    
    Returns:
        None
    """

    # 初始化一个空列表，用于存储需要移动的文件路径
    move_files: list = []

    # 遍历源目录及其子目录中的文件
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # 判断文件是否以.mp4结尾
            if file.endswith('.mp4'):
                # 拼接文件完整路径
                file_path: str = os.path.join(root, file)
                # 获取文件大小（单位：MB）
                size: int = os.stat(file_path).st_size / 1024 / 1024
                # 判断文件大小是否大于50MB
                if size > 50:
                    # 如果文件大小大于50MB，则记录日志并添加到移动文件列表中
                    logger.info(f'{file_path} is too large, size: {size} MB')
                    move_files.append(file_path)
                    # 将文件移动到目标目录
                    shutil.move(file_path, dist_dir)

    # 记录日志，显示移动的文件数量及目标目录
    logger.info(f'move {len(move_files)} files to {dist_dir}')

if __name__ == '__main__':
    src_dir: str = './wallpapers/'
    dist_dir: str = './baidu/'
    filter_move(src_dir, dist_dir)