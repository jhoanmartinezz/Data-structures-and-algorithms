'#-----Time complexcity O(n^2)------------'
'#-----Space complexcity O(1)-------------'


def insertionSort(array):
    for k in range(1,len(array)):
        i = k
        print("para ====>",array[i])
        print("first i=",i)
        while i > 0 and array[i] < array[i-1]:
            swap(i, array)
            i = i - 1
            print("i =", i)
    return array

def swap(i, array):
    temp = array[i-1]
    array[i-1] = array[i]
    array[i] = temp


a = [9,8,7,6,0,-5,4,-3,2,-1]
print(insertionSort(a))
