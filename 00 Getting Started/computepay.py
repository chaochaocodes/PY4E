# Week 6, Chapter 4

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay(h,r):   
    xp = 0
    if h > 40:
        reg = h*r
        otp = (h-40)*(0.5*r)
        xp = reg + otp
    else:
    	xp = h*r
    return xp

p = computepay(h,r)
print("Pay", p)