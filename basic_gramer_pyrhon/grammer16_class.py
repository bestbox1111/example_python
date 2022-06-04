


#### 전체 컨셉 == class



# 스타크래프트로 예시

# 마린 공격 유닛, 군인,총을 쏨

# name="마린"
# hp=40
# damage=5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력 {}".format(hp, damage))

# print()
# print()
# #탱크
# tank_name="탱크"
# tank_hp=150
# tank_damage=30
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력 {}".format(tank_hp, tank_damage))



# def attack(name, location, damage):
#     print("{} : {} 시방향으로 적군을 공격합니다.[공격력 {}]".format(name,location,damage))
    
    
    
# attack(name,4,damage)
# attack(tank_name,4,tank_damage)

#  탱크와 마린이 하나씩이며는 괜찮지만 수십개의 탱크를 만들게 된다면???
# 다음과 같이 클래스를 이용하여 사용.

class Unit:
    def __init__(self, name, hp, damage):       #__init__   생성자라고함.객체나 클래스생성될때.
        self.name=name
        self.hp=hp
        self.damage= damage
        print("{} 유닛이 생성되었습니다.".format(name))
        print("체력 {}, 공격력 {}".format(hp,damage))
        
        
#위에서 Unit이라는 클래스를 만들어놓고
#아래에서 변수이름만 다르게 하여 Unit의 인자를 그대로 사용하게함
#위에서 .생성한 인자갯수에 맞게 매게변수를 넣어야함. 
marine1=Unit("마린",40,5)
marine2=Unit("마린",40,5)
marine3=Unit("마린",40,5)
marine4=Unit("마린",40,5)
tank1=Unit("탱크",100,50)
tank2=Unit("탱크",100,50)
tank3=Unit("탱크",100,50)
        
        
        
        
#### 전체 컨셉은 = 멤버변수
#클래스내에 선언한 변수
# class Unit:
#     def __init__(self, name, hp, damage):       #__init__   생성자라고함.객체나 클래스생성될때.
#         self.name=name
#         self.hp=hp
#         self.damage= damage
        
        #name,hp,damage
        
        
#레이시를 생성
wrace1= Unit("레이스",40,10)
print("유닛이름 : {} , 공격력 {}".format(wrace1.name, wrace1.damage))   #Unit에서 정의한 멤버변수를 인스턴스.멤버변수 와 같이 사용가능함.
