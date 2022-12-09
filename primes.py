"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(n):
    
  if(n==1 or n==0):
    return False

  for i in range(2,n):

    if(n%i==0):
      return False
    
  return True




def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError('cant work with 0 or below')
    list = []
    counter = 0


    while(len(list) < number_of_primes):
        if(isPrime(counter)):
            list.append(counter)
                        
        counter= counter+1
    return list

