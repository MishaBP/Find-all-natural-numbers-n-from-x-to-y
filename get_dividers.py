# def ged_dividers(n):
# 	dividers = []
# 	x = 1 
# 	while n != x and n > x : бля я множители искал епта
# 		print(f"{n=},{x=}")
# 		if n % x == 0:
# 				dividers.append(x)
# 				n = n / x 
# 		x += 1
# 	else:
# 		dividers.append(x)

# 	#return dividers
# 	print(dividers)
# ged_dividers(int(input()))

def ged_dividers(n):
	dividers = []
	x = n 
	while x != 0 :
		# print(f"{n=},{x=}")
		if n % x == 0:
				if x != 0 : 
					dividers.append(x)
				x -= 1
		else:
			x -= 1
	return(dividers)
	#print(dividers[::-1])
# while True:

# 	ged_dividers(int(input()))
