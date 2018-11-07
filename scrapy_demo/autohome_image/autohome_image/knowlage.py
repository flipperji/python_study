import os
# 获取当前文件夹所在的绝对路径
path_current = os.path.dirname(__file__)
#获取当前项目所在绝对路径
path_project = os.path.dirname(path_current)
print(path_project)
