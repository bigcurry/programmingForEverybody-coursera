def computepay(h,r):
    h = float(h)
    r = float(r)

    if h >= 40:
    	overtime_pay = r * 1.5
    	overtime_hours = h - 40
    	pay = (40 * r) + (overtime_hours * overtime_pay)

    else:
    	pay = h * r

    return pay

hrs = raw_input("Enter Hours: ")
rate = raw_input("Rate of Pay: ")

p = computepay(hrs, rate)

print p