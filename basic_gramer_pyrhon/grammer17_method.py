


#### 전체 컨셉은 메소드


class Unit:
    def __init__(self, name, hp, damage):       #__init__   생성자라고함.객체나 클래스생성될때.
        self.name=name
        self.hp=hp
        self.damage= damage
        print("{} 유닛이 생성되었습니다.".format(name))
        print("체력 {}, 공격력 {}".format(hp,damage))
        
        
        
class AttackUnit:
    def __init__(self, name, hp, damage):       #__init__   생성자라고함.객체나 클래스생성될때.
        self.name=name
        self.hp=hp
        self.damage= damage
      
    def attack(self,location):
        print("{} : {}시 방향으로 적군을 공격 합니다.[공격력:{}]".format(self.name,location,self.damage))
        
        
        
    def damaged(self, damage):
        print("{}:{} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{}: 현제 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("현제 캐릭터는 사망했습니다.")
        
        
        
#파이어뱃 만들기
firebat1=Unit("파이어뱃",50,20)
firebat1=AttackUnit("파이어뱃",50,20)
firebat1.attack( 11)
firebat1.damaged(20)
firebat1.damaged(20)
firebat1.damaged(20)