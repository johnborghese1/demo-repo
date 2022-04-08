# Selects how big a numbers is
from tracemalloc import stop


x = input('select a number')
200
x=int(x)
if x > 100:
    print(x, 'is too big ')
    stop
elif x < 5:
    print( x, 'is too small ')
    stop
else:
    print( 'the number is in the range')




