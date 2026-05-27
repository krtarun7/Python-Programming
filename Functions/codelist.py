# Define a list of names and print them
list=["tarun","kumar","suman","sumanth","tarun kumar"]
def print_list(lst):
    for item in lst:
        print(item,end=" ")
print_list(list)
print() # for new line


# convert the  usd  to inr value
usd_value=int(input("Enter the amount in USD: "))
def converter(usd_value):
    inr_value=usd_value*82.5
    print(usd_value,"USD is equal to",inr_value,"INR")
    
converter(usd_value)