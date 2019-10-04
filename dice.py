import random 
roll = int(input("How Many Rolls? "))

x = 1
a = 0
s = 0
d = 0
f = 0 
g = 0
h = 0


while x <= roll:
	randomNum = random.randint(1, 6)
	
	if randomNum == 1:
		a += 1
	if randomNum == 2:
		s += 1
	if randomNum == 3:
		d += 1
	if randomNum == 4:
		f += 1
	if randomNum == 5:
		g += 1
	if randomNum == 6:
		h += 1
	print("Roll " + str(x) + "=" + str(randomNum))

	x += 1

print("Number of rolls:")
print("1s " + str(a))
print("2s " + str(s))
print("3s " + str(d))
print("4s " + str(f))
print("5s " + str(g))
print("6s " + str(h))


print("Percentages for times rolled:")
print("1s " + str((a/roll) * 100) + "%")
print("2s " + str((s/roll) * 100) + "%")
print("3s " + str((d/roll) * 100) + "%")
print("4s " + str((f/roll) * 100) + "%")
print("5s " + str((g/roll) * 100) + "%")
print("6s " + str((h/roll) * 100) + "%")

