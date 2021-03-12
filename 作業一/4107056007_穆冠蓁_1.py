AList = ["Rick", 27, "aMale", "Mary", 24, "aFemale", "Jane", 22, "aFemale", "Eric", 20, "aMale", "cake", "cake", "salad", "cake"]
BList = []
for i in range(0,4):
	temp = []
	temp.append(AList[i*3])
	temp.append(AList[i*3+1])
	string = AList[i*3+2]
	temp.append(string[1:])
	temp.append(AList[i+12])
	BList.append(temp)
print(BList)