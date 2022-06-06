


#### 전체 컨셉 = 예외 처리 (만들기)

# 한자리 전용 계산기

# try:
#     print("한자리 나누기 전용계산기 입니다.")
#     nums1=int(input("첫번째 숫자는 ?"))
#     nums2=int(input("두번째 숫자는 ?"))

#     if nums1>=10 or nums2>=10:
#         raise ValueError

#     print(" {} / {} ={}".format(nums1,nums2,int(nums1/nums2)))
# except ValueError:
#     print("두자리 전용 계산기 입니다. 어느 자리중 이상있습니다.")
    
    
    
    
#### 전체 컨셉 = 사용자 정의 예외 처리

# 위에서 사용한 한자리 전용 계산기를 재탕하기

# class TwonumberErr(Exception):
#     def __init__(self, msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# try:
#     print("한자리 나누기 전용계산기 입니다.")
#     nums1=int(input("첫번째 숫자는 ?"))
#     nums2=int(input("두번째 숫자는 ?"))

#     if nums1>=10 or nums2>=10:
#         raise TwonumberErr("입력값 : {}, {}".format(nums1,nums2))
#     print(" {} / {} ={}".format(nums1,nums2,int(nums1/nums2)))
# except ValueError:
#     print("두자리 전용 계산기 입니다. 어느 자리중 이상있습니다.")
# except TwonumberErr as twoerr:            #위에서 정의한 사용자 정의 예외 처리 클래스
#     print("에러가 발생하였습니다 한자리 숫자만 입력하세요")
#     print(twoerr)



#### 전체 컨셉 = final

# 위에서 사용한 한자리 전용 계산기를 재탕하기

class TwonumberErr(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print("한자리 나누기 전용계산기 입니다.")
    nums1=int(input("첫번째 숫자는 ?"))
    nums2=int(input("두번째 숫자는 ?"))

    if nums1>=10 or nums2>=10:
        raise TwonumberErr("입력값 : {}, {}".format(nums1,nums2))
    print(" {} / {} ={}".format(nums1,nums2,int(nums1/nums2)))
except ValueError:
    print("두자리 전용 계산기 입니다. 어느 자리중 이상있습니다.")
except TwonumberErr as twoerr:            #위에서 정의한 사용자 정의 예외 처리 클래스
    print("에러가 발생하였습니다 한자리 숫자만 입력하세요")
    print(twoerr)
finally:
    print("계산기 사용을 마치겠습니다.")