L = [1]*10001
L[0]=L[1]=0
for i in range(2,10001):
	if L[i] == 1:
		j=i*2
		while j<=10000:
			L[j] = 0
			j += i
	else:
		continue
n = 0

while n!=-1:
	n = int(input())
	if L[n] == 1:
		print(str(n)+" is a prime number.")
	else:
		print(str(n)+" is a not prime number.")
print("System terminated!")    