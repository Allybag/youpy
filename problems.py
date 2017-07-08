def probOne():

	trueNums = [i for i in range(1, 1001) if i % 3 == 0 or i % 5 == 0]
	solution = sum(trueNums)
	return solution
