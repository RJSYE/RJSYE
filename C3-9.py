
userid = str(input("아이디를 입력해 계정을 생성하세요 : "))
rank = int()

userid2 = str("R_JSYE")
rank2 = int()
if userid == "admin" :
    rank = 3
elif userid == "mod" :
    rank =2
elif userid == "vip" :
    rank = 1
elif userid == "banned" :
    rank = -1
else :
    rank = 0
if rank == 1 :
    print("환영해요 vip")
elif rank == 2 :
    print("환영해요 모더레이더")
elif rank == 3 :
    print("환영해요 관리자")
elif rank == -1 :
    print("당신은 밴되었음으로 기능이 제한되었씁니다.씁.")
else :
    print("환영합니다 유저님!")
if rank > 1 :
    command = str(input("커맨드를 입력해주세요 : "))
    if command == "ban" :
        ban = str(input("밴할 대상의 아이디를 적어주세요 : "))
        if ban == userid :
            userid = "banned"
        if ban == userid2 :
            userid2 = "banned"
    elif command == "resister" :
        ac = str(input("생성할 계정의 아이디를 입력해주세요 : "))
        userid2 = ac
if userid2 == "admin" :
    rank2 = 3
elif userid2 == "mod" :
    rank2 = 2
elif userid2 == "vip":
    rank2 = 1
elif userid2 == "banned":
    rank2 = -1
else :
    rank2 = 0
if rank2 == -1 :
    print("당신은 밴되었으니 환영안해줘요")
elif rank2 == 1 :
    print("환영합니다 vip!")
elif rank2 == 2 :
    print("환영합니다 모더레이더터!")
elif rank2 == 3 :
    print("환영합니다 관리자투!")
else :
    print("환영합니다 유저투!")
 
if str(ban) == str(userid) :
    userid = str("banned")
if str(ban) == str(userid2) :
    userid2 = str("banned")
    
