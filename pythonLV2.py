userids = ["R_JSYE","admin"]
bans = ["kohl"]
passwords = ["mau3","mau4"]
banranks = []
ranks = [1,2]
plrid = str()
plrrank = int()
for i in range(10):
    guest = str(input("환영합니다 로그인을 원하시면 1 / 회원가입을 원하시면 2를 입력해주세요"))
    if guest == "2":
        id = str(input("아이디를 입력하세요 : "))
        log = str(input("비밀번호를 입력하세요 : "))
        if id not in userids:
            userids.append(id)
            ind = userids.index(id)
            passwords.insert(ind,log)
            ranks.insert(ind,0)
            plrid = id
            plrrank = 0
            print("회원가입 성공! id : %s password : %s"%(id,log))
    elif guest == "1":
        id1 = str(input("로그인할 아이디를 입력하세요 : "))
        if id1 in userids:
            ind2 = userids.index(id1)
            log2 = str(input("비밀번호를 입력하세요 : "))
            if log2 == str(passwords[ind2]):
                print("로그인 성공!")
                plrid = id1
                plrrank = ranks[ind2]
            else:
                print("비밀번호가 틀렸습니다!")
                break
        else:
            print("아이디가 틀렸습니다! 남은시도 : %s"%i)
    if plrrank >= 0 and plrrank < 1:
        print("환영합니다 유저님! 잘노세요!")
        ind1 = userids.index(plrid)
        e = str(input("1 + 1 = ?"))
        if e == "2":
            print("정답을 맞추셨습니다! 보상으로 유저님의 랭크가 0.1이올랐습니다! 다음문제를 맞추시오")
            ranks[ind1] = ranks[ind1] + 0.1
            plrrank = plrrank + 0.1
            e2 = str(input("2*2*3 = ?"))
            if e2 == "12":
                print("정답을 맞추셨습니다! 보상으로 유저님의 랭크가 0.1이올랐습니다! 다음문제를 맞추시오")
                ranks[ind1] = ranks[ind1] + 0.1
                plrrank = plrrank + 0.1
                e3 = str(input("a+a+b+b = 16 , b+b = 10 이라면 a 는 무엇인가요 ? :"))
                if e3 == "3":
                    print("정답! 귀하의 랭크가 0.8더오르셨어요!")
                    ranks[ind1] = ranks[ind1] + 0.8
                    plrrank = plrrank + 0.8
    elif plrrank >= 1 and plrrank < 2:
        command = str(input("환영합니다 부관리자님 커맨드를 입력해주세요 : "))
        if command == "ban":
            banner = str(input("밴할 유저를 적어주세요"))
            if banner in userids and banner != plrid:
                ind3 = userids.index(banner)
                if ranks[ind3] < plrrank:
                    pop = userids.pop(ind3)
                    bans.insert(ind3,pop)
                    pop2 = ranks.pop(ind3)
                    banranks.insert(ind3,pop2)
                    print("%s의 계정이 성공적으로 정지되었습니다."%banner)
                else:
                    print("밴대상의 랭크가 귀하보다 높습니다.")
            else:
                print("대상의 계정이 발견되지않았습니다." if banner not in userids else "스스로를 밴할수없습니다.")
        elif command == "unban":
            unban = str(input("밴을풀 대상을 적어주세요 :"))
            if unban in bans:
                ind4 = bans.index(unban)
                un = bans.pop(ind4)
                userids.insert(ind4,un)
                un2 = banranks.pop(ind4)
                ranks.insert(ind4,un2)
                print("성공적으로 언밴되었습니다!")
