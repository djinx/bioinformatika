def reversal(P, start, stop):
	rev = [-i for i in P[start:stop+1]]
	rev.reverse()
	
	P[start:stop+1] = rev
	
	return P