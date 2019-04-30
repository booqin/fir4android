# -*- coding:utf-8 -*-
# Create by BoQin on 2018/12/06
import os

import time

import zipfile

import sys


def print_file(input_path):
    """
    对目录进行深度优先遍历
    :param input_path:
    :param result:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            print_file(input_path + '/' + file)
        else:
            print(input_path + '/' + file)


if __name__ == '__main__':
    """
    将jenkins上的备份文件解压到指定目录
    """

    """
    {PATH, PATCH_SOURCE_PATH, PATCH_TARGET_PATH}
    """
    file = zipfile.ZipFile(sys.argv[1]+"/bakApk.zip")
    file.extractall(sys.argv[2])
    file.close()
    print_file(sys.argv[2])
