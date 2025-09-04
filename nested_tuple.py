tuple1=('P','Y', 'T' ,'H','O','N')
print(tuple1)
for i in range(4):
    print(tuple1[i])

print(tuple1[0])
print(tuple1[3])
print(tuple1[-1])

tuple1=tuple1+(9,)
print(tuple1)
tuple2=(50,20,10,20,50)
print(tuple2.count(20))
sl=tuple1[1:4]
print(sl)
sl1=tuple1[:5]
print(sl1)