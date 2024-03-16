import random

money = 500000000000
first = 0
def lotto(amount):
    global money, first
    lottery = random.sample(range(1,46),6)
    bonus = random.sample(range(1,46),1)[0]
    count = 0
    loop = 0
    bonus1 = 0
    five = 0
    if amount > 1000:
        lottery = random.sample(range(1,46),5)
        
        count = count + 1
    for _ in range(amount):
        sam = random.sample(range(1,46),6)
        loop += 1

        for num in sam:
            if num in lottery:
                count += 1
            if num == bonus:
                bonus1 += 1

        if count == 6:
            money += 2000000000
            print("당첨을 축하합니다! 1등입니다!")
            first = first + 1
        elif count == 5 and bonus1 == 1:
            money += 30000000
            print("당첨을 축하합니다! 2등입니다!")
        elif count == 5:
            money += 1000000
            print("당첨을 축하합니다! 3등입니다!")
        elif count == 4:
            money += 50000
            print("당첨을 축하합니다! 4등입니다!")
        elif count == 3:
            money += 5000
            five += 1
            if loop == amount:
                print("당첨을 축하합니다! %s 번이 5등입니다!"%five)
    return count

buy = int(input("안녕하세요 호구님 로또복권 몇개를 구입하시겠습니까?"))
price = buy*5000
if money >= price :
    money -= price
    lotto(buy)
    print("%d개의 로또를 구입하셨습니다! 파산하기전에 당첨되길 빌어!" % buy)
    if first > 0:
        print("당첨을 축하합니다! 1등입니다!")
