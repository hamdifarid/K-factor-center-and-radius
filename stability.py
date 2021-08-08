import math
import cmath

def cal_complex(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp

def calculate_polar(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5, math.degrees(math.acos(a/r) if r != 0 else 0))

def mod(z):
    a = z.real
    b = z.imag
    r = abs(z)
    return ((a**2+b**2)**0.5)

def cal_complexconj(z,y):
    a = z*(math.cos(math.radians(y)))
    b = z*(math.sin(math.radians(y)))
    comp = complex(a,b)
    return comp.conjugate()


s11=float(input('enter r value for s11'))#0.894
s11a=float(input('enter angle value for s11'))#-60.6
s21=float(input('enter r value for s21'))#3.122
s21a=float(input('enter angle value for s21'))#123.6
s12=float(input('enter r value for s12'))#0.020
s12a=float(input('enter angle value for s12'))#62.4
s22=float(input('enter r value for s22'))#0.781
s22a=float(input('enter angle value for s22'))#-27.6

delta=(cal_complex(s11,s11a)*cal_complex(s22,s22a))-(cal_complex(s12,s12a)*cal_complex(s21,s21a))
deltamod = (mod(delta))
k = (1+(deltamod**2)-(s11**2)-(s22**2))/(2*(cal_complex(s12,s12a)*cal_complex(s21,s21a)))                                   
Clnm = (cal_complex(s22,s22a)-(delta)*(cal_complexconj(s11,s11a)))
Cldm = ((s22**2)-deltamod**2)
Rlnm = mod(cal_complex(s12,s12a)*cal_complex(s21,s21a))
Csnm = (cal_complex(s11,s11a)-(delta)*(cal_complexconj(s22,s22a)))
Csdm = ((s11**2)-deltamod**2)
Rsnm = mod(cal_complex(s12,s12a)*cal_complex(s21,s21a))
Rsdm = ((s11**2)-deltamod**2)
        

print('Delta =',deltamod)
print('k =',mod(k))
print('Cl =',calculate_polar(Clnm.conjugate()/Cldm))
print('Rl =',calculate_polar(Rlnm/Cldm))
print('Cs =',calculate_polar(Csnm.conjugate()/Csdm))
print('Rs =',calculate_polar(Rsnm/Csdm)),
if mod(k)<1:
    print('Value of K is less than 1 so potentially unstable')
if mod(k)>1:
    print('Value of K is greater than 1 so uncondtionally stable')
if mod(s11)<1:
    print('the outside of output stability circle is stable reigon')
if mod(s22)<1:
    print("the outside of i/p circle is stable region")
if mod(s11)>1:
    print('the inside of output stability circle is stable reigon')
if mod(s22)>1:
    print("the inside of i/p stability circle is stable region")
