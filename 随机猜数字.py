import random

number = random.randint(1, 10)
guess_number = int(input("请输入你猜的数字呗：\n"))
if guess_number == number:
    print("对了")
else:
    if guess_number > number:
        print("猜的有点大")
    else:
        print("猜的有点小了")
    guess_number = int(input("请第二次输入你猜的数字呗：\n"))
    if guess_number == number:
        print("对了")
    else:
        if guess_number > number:
            print("猜的有点大")
        else:
            print("猜的有点小了")
        guess_number = int(input("请第三次输入你猜的数字呗：\n"))
        if guess_number == number:
            print("对了")
        else:
            if guess_number > number:
                print("猜的有点大,gameover")
            else:
                print("猜的有点小了,gameover")

