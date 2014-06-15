hrs = raw_input("Enter Hours:")
h = float(hrs)

rph = raw_input("Rate Per Hours:")
r = float(rph)

if h >= 40:
	overtime_pay = r * 1.5
	overtime_hours = h - 40

	pay = (40 * r) + (overtime_hours * overtime_pay)
else:
	pay = h * r

print pay