def print_list(lst,index=0):
    if(index ==len(list)):
        return
    print(lst[index])
    print_list(lst,index+1)
    
list=["mango","banana","grapes","orange","watermelon"]
print_list(list)