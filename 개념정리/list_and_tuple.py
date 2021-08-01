#1 따로따로 생성한 리스트, 튜플의 동일성 판단
lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]

print(lst1 == lst2) # True
print(lst1 is lst2) # False ➞ 리스트는 이뮤터불(고정된 값x)이니까 False

lst1 = (1,2,3,4,5)
lst2 = (1,2,3,4,5)

print(lst1 == lst2) # True
print(lst1 is lst2) # True ➞ 튜플은 뮤터불(고정된 값o) 이니까 True
