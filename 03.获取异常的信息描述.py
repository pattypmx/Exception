
"""
try:
        执行可能发生的异常代码
    except 错误类型 as e：
        可获得临时变量e
"""
try:
    open("haha.txt", "r")
except FileNotFoundError as e:
    print("捕获异常", e)

"""
    try:
        执行可能发生的异常代码
    except (错误类型1,错误类型2) as e：
        可获得临时变量e
"""


try:
    open("haha.txt", "r")
    print(num)
except (FileNotFoundError, NameError) as e:
    print(e)
