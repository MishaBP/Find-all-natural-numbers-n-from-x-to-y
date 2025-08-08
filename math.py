import math
from get_dividers import ged_dividers

x_from,x_to,degree = int(input()),int(input()),int(input())
for i in range(x_from,x_to+1):
	# print(f'{i=}{i**degree=} {math.prod(ged_dividers(i))=}')
	if i**degree == math.prod(ged_dividers(i)):

		print(f'{i=}  ,i^{degree}={i**degree}  , {(ged_dividers(i))=}' )
	i += 1

	