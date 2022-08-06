from time import sleep

question = ["你认为自己是一个不爱说话的人吗?\nA.不爱说话 B.偶尔不爱说话 C.爱说话 D.非常爱说话",
     "用下面一种动物代表自己的性格.\nA.狗 B.兔 C.猫 D.鸟"]

b = len(question)
c = b

we = 0
Fraction = 0

while we < b:
    
    d = b - c

    print(question[d])

    ans = input()

    if ans == "a" or ans == "A":
        Fraction += 2

    elif ans == "b" or ans == "B":
        Fraction += 3

    elif ans == "c" or ans == "C":
        Fraction += 4

    elif ans == "d" or ans == "D":
        Fraction += 5

    else:
        print("你只能选择ABCD这四个选项")
        continue

    we += 1
    c -= 1

print("你的最终得分是:", Fraction, "分")

sleep(10)