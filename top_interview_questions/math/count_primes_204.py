import math

# its correct but too slow in practice - TLE
class Solution1:
    def countPrimes(self, n: int) -> int:
        res = 0
        nums = [i for i in range(n)]
        
        def isprime(x):
            if x < 2:
                return False
            if x == 2:
                return True

            for i in range(2, math.ceil(math.sqrt(x))+1):
                if x % i == 0:
                    return False

            return True
       
        for i in range(len(nums)):
            if isprime(i):
                # print(i, " is prime, list before filter: ", nums)
                nums = list(filter(lambda x: x % i != 0, nums))
                # print("list after filter: ", nums)

                res += 1

        return res

# use the sieve of erathosthenes - you don't need to check if every number is prime
# just remove any composite number with the current value as a divisor
# all the numbers left are prime 
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0

        if n <= 2:
            return 0
        
        nums = [True]*n
        nums[0] = nums[1] == False

        for i in range(2, len(nums)):
            if nums[i]:
                res += 1
                # sieve out the multipes until the end of n
                for j in range(i**2, n, i):
                    nums[j] = False
        return res

 

s = Solution()
print(s.countPrimes(10))

