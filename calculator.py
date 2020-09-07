# Python calculator (*/+- -only)

a, operand, b = (input().rstrip() for i in range(0,3))
#Check our data
if operand not in ('*', '/', '+', '-'):
    print("Error: {} is wrong operand".format(operand))
    exit()
elif operand == '/' and b == '0':
    print("Error: you can`t divide by zero")
    exit()

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Error: data can`t be converted to int. Check them")
    exit()

#Calculate
#(Sure, I google more fancy version instead four "if"
# This one was taken from first request "python variable as operand" -
# https://stackoverflow.com/questions/2983139/assign-operator-to-variable-in-python)

result = eval(str(a)+operand+str(b))
print(result)

