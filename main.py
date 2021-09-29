# To write gcd(a,b) as a linear combination of a and b using integer combination i.e au + bv = gcd(a,b)=1

"""
Find Help in this location
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
"""
def extendedEuclideanAlgorithm(a,b):
	return 1,1

def main():
	quotients= []
	quotients.append(1)
	print(quotients[0])
	print(extendedEuclideanAlgorithm(73,25))

if __name__== "__main__":
	main()