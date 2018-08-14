def greedy_sorting(P):
	approx_reversal_distance = 0
	
	print(P)
	
	for k in range(len(P)):
		if P[k] != k+1:
			i = find(P, k, k+1)
			P = reversal(P, k, i)
			approx_reversal_distance += 1
			
			print(P)
			
			if P[k] < 0:
				P[k] = -P[k]
				approx_reversal_distance += 1
				
				print(P)
				
	return approx_reversal_distance