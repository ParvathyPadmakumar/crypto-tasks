
def evenFibSum(limit) :
	
	ef1 = 2
	ef2 = 8
	sm=10
	
	
	while (ef2 <= limit) :

		ef3 = 4 * ef2 + ef1

		if (ef3 > limit) :
			break

		ef1 = ef2
		ef2 = ef3
		sm = sm + ef2
	
	return sm

limit = 4000000
print(evenFibSum(limit))

