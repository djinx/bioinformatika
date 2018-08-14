def chromosome_to_cycle(chromosome):

	nodes = [0 for i in range(2*len(chromosome))]

	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0:
			nodes[2*j] = 2*i -1
			nodes[2*j+1] = 2*i
		else:
			nodes[2*j] = -2*i
			nodes[2*j+1] = -2*i-1
			
	return nodes
	
	
def cycle_to_chromosome(nodes):
	
	chromosomes = [0 for i in range(len(nodes)//2)]

	for j in range(len(nodes)//2):
		if nodes[2*j] < nodes[2*j+1]:
			chromosomes[j] = nodes[2*j+1] // 2
		else:
			chromosomes[j] = -nodes[2*j] // 2
			
	return chromosomes
	
	
	
def main():
	print(cycle_to_chromosome(chromosome_to_cycle([1,-2,-3,4,5,-6])))
	
if __name__ == "__main__":
	main()
