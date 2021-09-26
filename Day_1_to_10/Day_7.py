# factorial function
def fact(n):
  return n * fact(n - 1) if n != 0 else 1


#checking if prime number
def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
        return True 
