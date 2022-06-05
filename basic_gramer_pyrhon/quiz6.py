"""주어진 코드를 활용하여 부동산 프로그램을 작성하시오"""


#출력예제
# 총3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50

#코드

# class house:
#     def __init__(self,location,house_type,deal_type,price,complettion_year):
#         pass
#     def show_detail(self):
#         pass

# class house:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price= price
#         self.completion_year=completion_year
        
        
# class house_show(house):     
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#          house.__init__(self,location,house_type,deal_type,price,completion_year)
    
       
#     def show_detail(self,count):
#         print("{} {} {} {} {}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
#         return count

# print("총 {} 대의 매물이 있습니다.".format(str(house_show.show_detail)))
# hosue1= house_show("강남","아파트","매매","10억","2010년")
# house2= house_show("마포","오피스텔", "전세", "5억", "2007년")
# house3= house_show("송파","빌라","월세", "500/50"," ")
# # house1= house_show("천안","발라","월세", "50"," 2011")

# hosue1.show_detail(3)
# house2.show_detail(3)
# house3.show_detail(3)



class house:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price= price
        self.completion_year=completion_year
            
    def show_detail(self):
        print("{} {} {} {} {}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
     

houses=[]       #houses라는 리스트를 만들어서 각각의 정보를 담는 리스트
house1= house("강남","아파트","매매","10억","2010년")
house2= house("마포","오피스텔", "전세", "5억", "2007년")
house3= house("송파","빌라","월세", "500/50"," ")
# house1= house_show("천안","발라","월세", "50"," 2011")

houses.append(house1)       #빈 리스트에 첫번째 집정보 담고
houses.append(house2)       #두번째 집정보 담고
houses.append(house3)       #세번째 집정보 담고



# print("총 {} 대의 매물이 있습니다.".format(len(houses)))
# house1.show_detail()
# house2.show_detail()
# house3.show_detail()
#위의 문구를 반복문으로


print("총 {} 대의 매물이 있습니다.".format(len(houses)))
for house_info in houses:
    house_info.show_detail()