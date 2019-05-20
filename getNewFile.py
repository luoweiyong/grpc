#! usr/bin/env python3
#-*- coding:utf-8 -*-
import os
#获取最新文件
def getNewFile(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回
    lists = os.listdir(test_dir)
    print(lists)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    print("排序后:")
    print(lists)
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir,lists[-1])
    return file_path
file = getNewFile(r'D:\test_prj\test_image')
print(file)
