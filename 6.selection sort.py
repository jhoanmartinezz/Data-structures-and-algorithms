'#-----Time complexcity O(n^2)------------'
'#-----Space complexcity O(1)-------------'

# def selectionSort(array):
#     actualIndex = 0
#     print(actualIndex)
#     while actualIndex < len(array) - 1:
#         menorIndex = actualIndex
#         print("Menor",menorIndex)
#         for k in range(actualIndex + 1, len(array)):
#             if array[menorIndex] > array[k]:
#                 menorIndex = k
#         swap(actualIndex, menorIndex, array)
#         actualIndex = actualIndex + 1
#     return array

# def swap(k, i, array):
#     array[k], array[i] = array[i], array[k]

'#-----Time complexcity O(n^2)------------'
'#-----Space complexcity O(1)-------------'
def selectionSort(array):
    for k in range(len(array)-1):
        minpos = k
        print("K=======>",k)
        for i in range(k, len(array)):
            print("I",i)
            if array[i] < array[k]:
                #with swap function
                swap(k, i, array)
                #without swap function
                #array[i], array[k] = array[k], array[i]
            print(array)

def swap(a, b, c):
    temp = c[a]
    c[a] = c[b]
    c[b] = temp

array = [9, 1, 8, 2, 3, 5]
print(selectionSort(array))
