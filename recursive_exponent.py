
def x_toThePower_n(x, n):
	''' Calculates the n_th power of x using recursion. 
		Running time: O(log(n))
		Inputs
			x: integer 
			n: integer
		Output
			integer (if n > 0) or float(if n < 0)
	'''
    if n == 1:
        return x
    if n == -1:
        return 1/x
    elif n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        temp_f = f(x, n/2)
        return temp_f * temp_f
    elif n > 0 and n % 2 != 0:
        temp_f = f(x, (n-1)/2)
        return temp_f * temp_f * x
    elif n < 0 and n % 2 == 0:
        temp_f_neg = f(x, -1*n/2)
        return 1 / (temp_f_neg * temp_f_neg)
    else:
        temp_f_neg_odd = f(x, (-1*n-1)/2)
        return 1 / (temp_f_neg_odd * temp_f_neg_odd * x)