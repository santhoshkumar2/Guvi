for row in range(5,0,-1):
	for column in range(5,0,-1):
		if row+column<=6:
			print (column,end="\t")
		else:
			print (end="\t")
		print (column ,end=" ")
	print ("\t")
