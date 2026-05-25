list1=['ab','bc','ab']
copy_list=list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("palindrome")
else:    
    print("not palindrome")