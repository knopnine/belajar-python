def l100kmtompg(liters):
    mpg = 378541.1784 / (liters * 1609.344)
    return mpg

def mpgtol100km(miles):
    l100km = (378.5411784) / (miles * 1.609344)
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))