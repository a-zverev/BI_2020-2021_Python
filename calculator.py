import operator
# Python calculator (*/+-** -only)


a, action, b = (input().rstrip() for i in range(0, 3))
# Check our data
if action not in ('**', '/', '+', '-', '*'):
    print("Error: {} is wrong operator".format(action))
    exit()
elif action == '/' and b == '0':
    print("Error: you can`t divide by zero")
    exit()

try:
    a = float(a)
    b = float(b)
except ValueError:
    print("Error: data can`t be converted to float. Check them")
    exit()

# Calculate
# Still hate idea of five if, so another googled solution
# https://stackoverflow.com/questions/54559395/how-to-store-and-use-mathematical-operators-as-python-variable?noredirect=1&lq=1

operatorLookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}
actionAsFunction = operatorLookup.get(action)
res = actionAsFunction(a, b)
print(res)
