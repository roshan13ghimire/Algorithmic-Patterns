#Bottom_Up_Approach (Tabulation)
def fib(n):
    if n == 0 or n == 1:
        return n
    tab = [0] * (n + 1)
    tab[1] = 1
    for i in range(2,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]
print(fib(6))