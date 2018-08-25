def answer(l):
	# your code here
    list_length = len(l)
    count = 0

    for i in range(1, list_length-1):
    	b = l[i]
    	factors = 0
    	multiples = 0
    	# Go through all factors of b
    	for j in range(0, i):
    		a = l[j]

    		if b%a == 0:
    			factors += 1

    	# Go through all multiples of b
    	for k in range(i+1, list_length):
    		c = l[k]

    		if c%b == 0:
    			multiples += 1

    	# The format of lucky-triple is [factor_of_b, b, multiple_of_b]
    	# Thus, we combine the number of multiples and factors
    	count += multiples*factors


    return count

# if __name__ == "__main__":
# 	l = [1,1,2,2,3]
# 	print(answer(l))
