'#-----Time complexcity O(n)------------'
'#-----Space complexcity O(d)-------------'
'#d = death of the array'
'#Classic recursion question, recursion is a function that call itself'

def productSum(array, multiplier=1):
    sum = 0
    for k in range(len(array)):
        if type(array[k]) is list:
            sum = sum + productSum(array[k], multiplier+1)
            print("multi", multiplier)
        else:
            sum = sum + array[k]
            print("sum else=", sum)
    return sum * multiplier

array=[5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))
