import math

def binomial_distribution(n, p, k):
    q = 1 - p
    return math.comb(n, k) * (p ** k) * (q ** (n - k))

def poisson_distribution(lmbda, k):
    return (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)

n, p, k = 10, 0.5, 3
binomial_prob = binomial_distribution(n, p, k)
print(f"Binomial probability: {binomial_prob}")

lmbda, k = 2, 4
poisson_prob = poisson_distribution(lmbda, k)
print(f"Poisson probability: {poisson_prob}")
