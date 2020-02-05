"""
    try:
        执行可能发生的异常代码01
        执行可能发生的异常代码02
    except (错误类型1,错误类型2...):
        如果发生异常执行的代码01
        如果发生异常执行的代码02
"""
# 多个异常不写多个错误类型的话，只捕获填的那个错误类型异常
try:
    open("haha.txt", "r")
    print(num)
except (FileNotFoundError, NameError):
    print("捕获异常")
