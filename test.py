import os
import sys

print('当前工作路径: ', os.getcwd())
print('导包路径为: ')

for p in sys.path:
    print(p)

