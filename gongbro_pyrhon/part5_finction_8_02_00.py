

## list comprehension 과 lambda 함수의 반복문 사용

letter_l=[]
for letter in 'python':
    letter_l.append(letter)
print(letter_l)     #['p', 'y', 't', 'h', 'o', 'n']출력

letter_l2=[letter for letter in "python"]   #위 반복문을  한줄로 해결.
print(letter_l2)     #['p', 'y', 't', 'h', 'o', 'n']출력

letter_l3=list(map(lambda x: x, "python"))  #위와 동일 맵으로 했을때.
print(letter_l3)      #['p', 'y', 't', 'h', 'o', 'n']출력