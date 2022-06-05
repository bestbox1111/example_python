


#### 전체 컨셉은 다중상속


# 일반 유닛에 스피드 추가 및 무브라는 함수도 추가.

class Unit:
    def __init__(self, name, hp, speed):       #__init__   생성자라고함.객체나 클래스생성될때.
        self.name=name
        self.hp=hp
        self.speed=speed
     
    def move(self, location): 
        print("[지상 유닛 이동]")
        print("{} : {} 시 방향으로 이동합니다.[ 속도 : {} ]".format(self.name,location,self.speed))  
        
class AttackUnit(Unit):         #자식의 인자에 상속받고 싶은 부모를 적용
    def __init__(self, name, hp,damage,speed):       #__init__   생성자라고함.객체나 클래스생성될때.
        Unit.__init__(self,name,hp,speed)     # Unit 클래스에서 적용되는 name,hp를 Unit.__init(인자)로 그대로 가져와 사용가능
        self.damage= damage
      
    def attack(self,location):
        print("{} : {}시 방향으로 적군을 공격 합니다.[공격력:{}]".format(self.name,location,self.damage))
        
        
        
    def damaged(self, damage):
        print("{}:{} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{}: 현제 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("현제 캐릭터는 사망했습니다.")
        
        
# 드랍쉽 : 공중유닛 이지만, 공격기능 X. 수송기능만.




 #날수있는 기능이 있는 클래스
class Flyable: 
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self, name, location):
        print("{} : {} 시 방향으로 날아갑니다. [속도: {}]".format(name,location,self.flying_speed))
        
        
        
 #공중 공격 유닛 클래스
class FlyableAttack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self, flying_speed)
        
        
    def move(self, location):
        print("[공중 유닛 이동]")   
        self.fly(self.name, location)
        
        
#발키리 생성: 공중 유닛 생성

# valyrie= FlyableAttack("발키리",200,6,5)
# valyrie.fly(valyrie.name,3)


#벌처 유닛 생성: 지상유닛

valture =AttackUnit("벌처", 80,10,20)
valture.move(11)

#배틀 크루져

battle = FlyableAttack("배틀 크루져",500,100,3) 
# battle.fly("배틀크루져",1)

battle.move(6)