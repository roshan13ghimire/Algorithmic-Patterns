#Top_Down_Approach (Memoization)
def fib(n,memo = None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        return n
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
print(fib(7))