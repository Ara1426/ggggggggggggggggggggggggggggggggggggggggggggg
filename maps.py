m1=[1,2,3]
m2=[2,5,68]
resalt=map(lambda x,y:x+y,m1,m2)
print(list(resalt))

nums = [1, 2, 3, 4, 5]

def sq(n):

    return n*n

square = list(map(sq, nums))

print("Square of numbers in list")

print(square)