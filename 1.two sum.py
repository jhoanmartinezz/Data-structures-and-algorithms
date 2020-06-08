'#---------Double for loop---------------------'
'#Time complexity is O(n^2)'
'# Space complexity is O(1)'

#
# def twoSum(data, target):
#     for k in range(len(data)-1):
#         for i in range(k+1, len(data)):
#             if data[k] + data[i] == target:
#                 print("becouse index", data.index(data[k]), "plus index", data.index(data[i]), "equals to ", target)
#                 return [data[k], data[i]]
#     return []
#
# #
# array = [54,34,67,8,62]
# print(twoSum(array,70))
# print(twoSum(data, target))


'#---------------Hash Table------------------------'
'#Time complexity O(n)'
'#Space complexity O(n)'

def twoSum(datos, target):
    numeros = {}
    for k in range(len(datos)):
        y = target - datos[k]
        if y in numeros:
            #print("indices:", datos.index(y), datos.index(datos[k]))
            return [y, datos[k]]
        else:
            numeros[datos[k]] = True
    return []

array = [54,34,67,8,62]
print(twoSum(array,15))
