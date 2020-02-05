# Exception为所有异常的父类，不需要确定是哪种错误类型，即可全部捕获

try:
    open("haha.txt", "r")
except Exception:
    print("捕获异常")

try:
    open("haha.txt", "r")
except Exception as e:
    print("捕获异常", e)