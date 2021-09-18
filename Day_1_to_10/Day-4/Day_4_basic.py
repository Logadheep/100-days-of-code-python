
# multiplication table
n = int(input())
for i in range(10):
    print(n, 'x', i, '=', n * i)
    

# find the sum of the series
#[ 1-X^2/2+X^4/4- .........]

x = int(input())
n=int(input())
s=1
for i in range(1, 1+n):
    s+=((-1)**(i))*float(x**(2*i))/(i*2)
print(s)
