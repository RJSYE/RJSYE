userid = str(input("회원가입 아이디 입력해라"))
userid2 = str()
command = str()
rank = int()
ban = str()
if userid or userid2 == "admin" :
    rank = 3
if userid or userid2 == "moderator" :
    rank = 2
if userid or userid2 == "vip" :
    rank =1
if userid or userid2 == "banned" :
    rank = -1
    
else :
    rank = 0
if rank > 1 :
    print("환영합니다  " + userid + "관리자 님")
    command = str(input())
if rank > 2 :
    print("owner mod")
    command = str(input())
if rank == -1 :
    print("응너밴 ㅅㄱ")
else :
    print("환영합니다 : " + userid or userid2)
    a = int(input("숫자를 입력하세요"))
    b=int(input("두번째 숫자를 입력해라"))
    c=int(input("세번째나 입력해"))
    larg=str()
    if a > b and c :
        larg=a
    if b > a and c :
        larg=b
    else :
        larg=c
    print(larg)
    
        
    
if command == "resister" :
    userid2 = str(input("관리자 권한으로 새로운 계정을 개설합니다 id : "))
if command == "ban" and rank > 2 :
    ban = str(input("밴대상의 아이디를 입력하세요 :"))
if str(ban) == str(userid) :
    userid = str("banned")
if str(ban) == str(userid2) :
    userid2 = str("banned")
    