
import math
import matplotlib.pyplot as plt

n =1
x = []
logn = []
nlogn = []
N = []
n2 = []
n3 = []
o2n = []

def Log(n):
	while n<=10:
		x.append(n)
		print(math.log(n))
		logn.append(math.log(n))
		print(n*math.log(n))
		nlogn.append(n*math.log(n))
		print(n)
		N.append(n)
		print(n**2)
		n2.append(n**2)
		print(n**3)
		n3.append(n**3)
		print(2**n)
		o2n.append(2**n)
		n+=1

	plt.plot(x,logn)
	plt.plot(x,nlogn)
	plt.plot(x,N)
	plt.plot(x,n2)
	plt.plot(x,n3)
	plt.plot(x,o2n)
	plt.ylabel('log value')
	plt.xlabel('number of entries')
	plt.title('log')
	plt.show()

Log(n)
