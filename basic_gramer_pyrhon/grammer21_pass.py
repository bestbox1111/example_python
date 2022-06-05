

#### 전체 컨셉은 pass

# def game_start():
#     print("게임을 시작하지")
    
# def game_over():
#     pass            #그냥 지나치기

# game_start()
# game_over()




#### 전체 컨셉 = super


# class Unit:
#     def __init__(self, name, hp):       #__init__   생성자라고함.객체나 클래스생성될때.
#         self.name=name
#         self.hp=hp
        
# #건물

# class Building(Unit):
#     def __init__(self, name, hp,location):
#         Unit.__init__(self, name,hp,0)  
#         # super().__init__(name, hp)        #위 Unit과 동일하지만(self인자는 빼야함.)
#         self.location =location             #하지만 super는 다중상속사용때 문제 발생 
        
        
        
# 다중상속 관련 super 예제

class Unit:
    def __init__(self):
        print("Unit생성자")
        
class Flyable:
    def __init__(self) :
        print("Flable생성자")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
        
        
class FlyableUnit(Flyable ,Unit):
    def __init__(self):
        super().__init__()   
        
        
class FlyableUnit(Flyable ,Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)   
#드랍쉽

dropship = FlyableUnit()        #드랍쉽을 만든다고 가정했을시에  flyableunit의 두개의 인자중 먼저 들어간 인자만 적용되게 된다.
                                # 따라서 55라인의 57~58 같이 부모의 초기화를 두개다 시켜줘야 함.
    