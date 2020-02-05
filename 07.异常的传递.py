
# # try嵌套
# try:
#     try:
#         open("qqq.txt", "r")
#         # 没有捕获异常，但是最终还是会打印
#     finally:
#         print("最终")
# # 里面没有捕获异常，但是外面可以捕获
# except:
#     print("捕获异常")

# def fun1():
#     print(num)
#     print("1")
# def fun2():
#     fun1()
#     print("2")
# def fun3():
#     fun2()
#     print("3")
# # 可以直接在最后捕获异常
# try:
#     fun3()
# except:
#     print("异常")


def fun1():
    # 直接在可能出现的异常下捕获
    try:
        print(num)
    except:
        print("异常")

def fun2():
    fun1()

def fun3():
    fun2()

fun3()