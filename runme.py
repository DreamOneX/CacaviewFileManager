#化学垃圾文件资源管理器v1.0
print("欢迎使用化学文件资源管理器，键入数字以开始：")
print("1.基本文件操作")
print("2.目录操作")
print("3.高级文件操作")
a = input("输入前面的数字，输入0退出:")
import os
while a == a:
    if a == "1":
        print("============基本操作=============")
        print("1.打开，写入，创建文件")
        print("0.返回")
        b = input("请输入：")
        while b == b:
            if b == "1":
                os.system("python file/open.py")
                print()#不知道怎么写
                break
            elif b == "0":
                print("退出。。。")
                break
            else :
                print("错误，重输")
                continue
        #这里打算做点东西
        break
    elif a == "2":
        print("还没开始做呢")
        #同上
        break
    elif a == "3":
        print("还没开始做呢")
        #同上
        break
    elif a == "0":
        print("退出程序")
        break
    else:
        print("错误，请重输")
        a = input("请重新输入：")
        continue