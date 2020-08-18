import random

ans = random.randint(1,20)
i = 0

while i<5:
    guess = int(input('請在1~20間猜一個數字(只能猜五次):'))
    if guess>20 or guess<0:
        print('輸入錯誤，請重新輸入!!!')
        i = i +1
    else:
        if guess > ans:
            if i == 4:
                print("抱歉，你已經猜五次了")
                break
            else:
                print('小一點')
                i =i+ 1
        elif guess < ans:
            if i == 4:
                print("抱歉，你已經猜五次了")
                break
            else:
                print('大一點')
                i =i+ 1
        else:
            print('Bingo!!!')
            i =i+ 1
            print('你猜了'+str(i)+'次就答對了')
            break