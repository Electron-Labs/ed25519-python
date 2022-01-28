def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def diophantine(a, b, c):
  (d,x,y) = egcd(a,b)
  assert c % d == 0
  t = c//d
  x1 = x*t
  y1 = y*t
  assert a*x1 + b*y1 == c
  return (x1,y1)
  # return (x, y) such that a * x + b * y = c

#print(diophantine(8,16,24))

def inv(a,p):
    (d,x,y) = egcd(a,p)
    assert d==1
    (x1,y1) = diophantine(a,p,1)
    if x1<0:
        x1 = p + x1
    assert (a*x1)%p == 1
    return x1

def a_power_n(a,n,p): # n is large
  if n==1:
    return a
  if n%2 == 0:
    return ((a_power_n(a,n//2,p))**2)%p
  elif n%2==1:
    return ((a_power_n(a,(n-1)//2,p))**2 * a )%p

def fermat_inv(a,p):
  apminus2 = a_power_n(a,p-2,p)
  a_inv = apminus2%p
  assert ((a%p)*a_inv)%p == 1
  return a_inv

def test_fermat_inv():
  primes = [3,5,7,11,13,17,19]

  for p in primes:
      print("Prime = "+ str(p))
      for a in range(1,p):
          print("a = "+ str(a) + ", inv = "+str(fermat_inv(a,p)))

def test_inv():
  primes = [3,5,7,11,13,17,19]

  for p in primes:
      print("Prime = "+ str(p))
      for a in range(1,p):
          print("a = "+ str(a) + ", inv = "+str(inv(a,p)))
