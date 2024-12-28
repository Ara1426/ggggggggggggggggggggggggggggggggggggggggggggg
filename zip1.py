s1={10,20,30,40,50}
s2={'a','c','b','d','m'}
s3=list(zip(s1,s2))
print(s3)

l1=[1,2,3,4,5,6,7,8]
l2=[10,20,30,40,50,60,70,80]
for x,y in zip(l1,l2[::-1]):
    print(x,y)

stocks = ['reliance', 'infosys', 'tcs']

prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,

prices in zip(stocks, prices)}

print('\n{}'.format(new_dict))