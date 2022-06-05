


#### 전체 컨셉은 상속


# 메딕을 생성 한다고 가정  - 메딕은 공격력이 없음. -의무병임 -

class Unit:
    def __init__(self, name, hp):       #__init__   생성자라고함.객체나 클래스생성될때.
        self.name=name
        self.hp=hp

        
        
class AttackUnit(Unit):         #자식의 인자에 상속받고 싶은 부모를 적용
    def __init__(self, name, hp,damage):       #__init__   생성자라고함.객체나 클래스생성될때.
        Unit.__init__(self,name,hp)     # Unit 클래스에서 적용되는 name,hp를 Unit.__init(인자)로 그대로 가져와 사용가능
        self.damage= damage
      
    def attack(self,location):
        print("{} : {}시 방향으로 적군을 공격 합니다.[공격력:{}]".format(self.name,location,self.damage))
        
        
        
    def damaged(self, damage):
        print("{}:{} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{}: 현제 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("현제 캐릭터는 사망했습니다.")
        
        
        
firebat1=Unit("파이어뱃",50)
firebat1=AttackUnit("파이어뱃",50,20)
firebat1.attack( 11)
firebat1.damaged(20)
firebat1.damaged(20)
firebat1.damaged(20)