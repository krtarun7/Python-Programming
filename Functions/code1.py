#Two parameters and return value
def calc_sum(a,b):
    return a+b
sum=calc_sum(5,10)
print("The sum is:",sum)

#String parameter and no return value
def print_hello(name):
    print("Hello",name)
print_hello("Tarun kumar")


#No parameter and no return value
def print_hello():
    print("Hello")
output=print_hello()
print(output)