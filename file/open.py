#这个玩意用做打开文件和创建文件
print("============文件操作=============")
print("1.读文件")
print("2.写文件")
print("3.创建文件")
print("4.退出")
a = input("请输入：")
while a == a:
    if a == "1":
        b = input("请输入路径(绝对路径)：")
        file = open(b,'r')
        file.close()
    elif a == "2":
        c = input("请输入你想写入的内容")
        file.write(c,w)
        file.close()
    elif a == "3":
        print("请输入文件名后面要带.txt")
        c =int("请输入：")
        file = open('c','w')
        file.close()
    elif a == "4":
        print("退出。。。")
    else:
        print("你tm输的什么？")
        a = input("请重新输入：")
        continue