# Program to calculate the sum of first n natural numbers using recursion
def calc_sum(n):
    if n == 0:
        return 0
    else:
        return n + calc_sum(n-1)
sum=calc_sum(5)
print("The sum of first 5 natural numbers is:",sum)