try:
    # 文件不存在
    open("haha3.txt", "r")

# try中代码发生异常，执行except中代码
except Exception:
    print("捕获异常")

# try中代码没有发生异常，执行else中代码
else:
    print("无异常")

# 无论try中的代码是否发生异常，finally都会执行
finally:
    print("最终")