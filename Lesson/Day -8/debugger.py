#pdb debugger

# import pdb
def multiplication(a,b):
    answer = a * b
    return answer 
breakpoint()
# pdb.set_trace()
x = input("Enter first Number : ")
y = input("Enter second Number : ")
mul = multiplication(x,y)
print(mul)
