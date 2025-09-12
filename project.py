test_dict={'codingal': 3, 'is': 2,'best': 4, 'for': 3,'coding': 2}
print("The original dictionary:  "+ str(test_dict))
K=int(input("Enter the number to check its frequency in the test dictionary:  "))
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print(f"Frequency of K is:   "+str(res))