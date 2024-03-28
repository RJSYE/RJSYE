import math,random
class human:
    def __init__(self):
        money = 0
        items = {1:"bronze",2:"iron",3:"gold"}
        inventory = {"bronze":0,"iron":0,"gold":0}
        lv = 1
        exp = 0
        money = self.money
        inventory = self.inventory
        lv = self.lv
        exp = self.exp
        life = 20
    def add_money(self,sell,earn):
            if sell == "gold":
                  if self.inventory["gold"] >= earn:
                        self.inventory["gold"] -= earn
                        self.money += earn*3
            elif sell == "iron":
                  if self.inventory["iron"] >= earn:
                        self.inventory["iron"] -= earn
                        self.money += earn*2
            elif sell == "bronze":
                    if self.inventory["bronze"] >= earn:
                            self.inventory["bronze"] -= earn
                            self.money += earn
            elif sell == "all":
                    self.money += self.inventory["gold"]*3 + self.inventory["iron"]*2 + self.inventory["bronze"]
                    self.inventory["gold"] = 0
                    self.inventory["iron"] = 0
                    self.inventory["bronze"] = 0
    def add_inventory(self,item):
            if type(item) == list:
                  for i in range(3):
                        if self.inventory[i][0] == item[0]:
                            self.inventory[i][1] += item[1]
                            break
                        
                  
            else:
                    for i in range(3):
                            if item == self.inventory[i][0]:
                                self.inventory[i][1] += 1
    def add_exp(self,exp):
            self.exp += exp
            if self.exp >= 100:
                    self.exp -= 100
                    self.lv += 1
                    print("Level up! You are now level",self.lv)
    def mine(self):
           get = random.randint(-1,self.lv)
           if get > 0 and get < 1:
                self.add_inventory(self.items["bronze"])
                print("브론즈 획득!")
                self.add_exp(10)
           elif get > 1 and get < 3:
                self.add_exp(10)
                self.add_inventory(self.items["iron"])
                print("아이언 획득!")
           elif get > 3 and get < 5:
                self.add_exp(20)
                self.add_inventory(self.items["gold"])
                self.add_exp(30)
                print("골드 획득!")
           elif get > 10:
                 self.add_exp(50)
                 self.add_inventory(["gold",5])
                 print("5골드 획득!")
class goblin_King:
      def __init__(self):
            money = 0
            items = {1:"sword"}
            inventory = {"sword":1}
            lv = 20
            exp = 0
            money = self.money
            inventory = self.inventory
            lv = self.lv
            exp = self.exp
            life = 500
            atk = 50
            defense = 10
            army = 3
            army_life = 10
            army_atk = 5
            army_defense = 1
        def attack(self):
            a = input("Press Enter to attack! or type defence to defend")
            



            
