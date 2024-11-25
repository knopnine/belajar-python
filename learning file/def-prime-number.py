def isPrime(num):
    if num < 2: return False
    for i in range (2,  int(num ** 0.5)+1):
        if num%i == 0: return False
    return True

for i in range(50):
    if isPrime(i): print(i,  end=' ')