import argparse

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()

# 添加参数定义
parser.add_argument("--arg1", help="argument 1")
parser.add_argument("--arg2", help="argument 2")
parser.add_argument("--arg3", help="argument 3")

# 解析参数
args = parser.parse_args()

# 打印参数
print("arg1:", args.arg1)
print("arg2:", args.arg2)
print("arg3:", args.arg3)

'''
python 高阶知识/Learn_argparse.py \
--arg2 1 \
--arg1 2 \
--arg3 3000
    
'''
