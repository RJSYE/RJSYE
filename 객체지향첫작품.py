class cat():
    age = 1
    speed = 1
    name=""
    saying = ""
    def set_info(self,name,speed):
        self.name = name
        self.speed = speed

    def hello(self):
        print("%s%s"%(cat.name,cat.saying))
    def get_info(self) :
        
        if cat.speed > 2 and cat.speed < 6 :
            print("속도는 조금빠르다")
        elif cat.speed > 5 :
            print("속도가 꽤나 빠르다.")
        else :
            print("속도가 제법느리다.")
        print(self.name,self.speed)
    
cat = cat()
cat.saying = "meow"
cat.set_info("ggam",8)
cat.hello()
cat.get_info()
