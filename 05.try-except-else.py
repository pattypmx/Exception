try:
    # 文件已存在
    open("haha.txt", "w")

# try中代码发生异常，执行except中代码
except Exception:
    print("捕获异常")

# try中代码没有发生异常，执行else中代码
else:
    print("无异常")