#檔名:guess_onetime
import random
num=random.randint(1,10)

ans=input("請輸入數字:")
"""
if ans==1 or ans==2 or ans==3 or \
ans==4 or ans==5 or ans==6 or\
ans==7 or ans==8 or ans==9 or\
ans==10:
    ans = int(ans)
    if num == ans:
        print("恭喜答對")
    else:
        print("錯了ㄏㄏ")
else:
    print("不在範圍")
    
"""
if str.isdigit(ans) == True:
    ans = int(ans)
    if num == ans:
        print("恭喜答對")
    else:
        print("錯了ㄏㄏ")
else:
    print("不是數字")
"""
#挑戰題:如果今天不小心打到英文怎麼辦???