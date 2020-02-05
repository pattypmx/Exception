"""
    try:
        执行可能发生的异常代码
    except 错误类型：
        如果发生异常执行的代码
"""
try:
    open("test.txt", "r")
except FileNotFoundError:
    print("发生异常")
