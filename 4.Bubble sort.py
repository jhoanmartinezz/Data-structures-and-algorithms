'#Time complexcity = O(n^2)'
'#Space complexcity = O(n)'
def bubbleSort(array):
    for k in range(len(array)-1, 0, -1):
        print("K => ",k)
        for i in range(k):
            print("I=>",array[i]," | ",array[i+1])
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array

a = [4,9,6,8,2,5,3]
print(bubbleSort(a))
