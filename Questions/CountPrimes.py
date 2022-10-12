class Solution:
    def countPrimes(self, n: int) -> int:
        # Prime number is a number that is greater than one but is only divisible by 1 and itself

        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for multiples_of_i in range(i * i, n, i):
                    isPrime[multiples_of_i] = False

        return sum(isPrime)  # this will return the number of true elements in the array
