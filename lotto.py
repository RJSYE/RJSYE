import random

money = 5000000000000

def buy(n, money2):
    global money
    money1 = money2
    already = [[]]
    lottery = random.sample(range(1, 46), 6)
    bonus = random.choice(range(1, 46))  # 보너스 번호는 하나만 필요하므로 random.choice를 사용합니다.
    n = int(n)
    five = 0
    four = 0
    for _ in range(n):

        num = random.sample(range(1, 46), 6)
        if num in already[0] :
            while num in already[0] :
                num = random.sampe(range(1,46),6)
                break
        
        count = len(set(num) & set(lottery))
        bonus_count = 1 if bonus in num else 0

        if count == 3:
            five += 1
        if count == 4:
            four += 1
        if count == 5:
            print("축하합니다 3등입니다!")
            money += 5000000
        if count == 5 and bonus_count == 1:
            print("축하합니다! 2등입니다!")
            money += 20000000
        if count == 6:
            print("[[[ 축하합니다 1등입니다! ]]] \n\n\n")
            money += 2000000000
        already.append(num)
        
    print("축하합니다! %s개의 5등이있어요." %five)
    print("축하합니다! %s개의 4등이있어요." %four)
    money += (five * 5000 + four * 50000)
    earn = money - money1
    print("총 당첨금 : %s" % earn)

a = int(input("복권 구매수량입력"))
money = money - a*1000
if money >= a*1000 :
    buy(a, money)
