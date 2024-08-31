p = float(input('enter payment = '))
t = float(input('enter given time = '))
r = float(input('enter rate of intrest = '))
SI = (p*t*r)/100
TA = p+SI
print('%0.2f is simple intrest\n%0.2f is total amount' %(SI,TA))