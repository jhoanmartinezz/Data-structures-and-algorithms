'#-----Time complexcity O(n^2)------------'
'#-----Space complexcity O(n)-------------'

# def isPalindrome(string):
#     newString=""
#     for k in reversed(range(len(string))):
#         newString = newString + string[k]
#     return string == newString
# print(isPalindrome("aaat"))

'#-----Time complexcity O(n)------------'
'#-----Space complexcity O(n)-------------'
# def isPalindrome(string):
#     newString = []
#     for k in reversed(range(len(string))):
#         newString.append(string[k])
#         output = "".join(newString)
#     return string == output
# print(isPalindrome("ada"))

'#-----Time complexcity O(n)------------'
'#-----Space complexcity O(n)------------'
'#------Recursive function---------------'
# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)
#
# print(isPalindrome("ada"))

# def isPalindrome(string, i = 0):
#     j = len(string) - 1 - i
#     if i >= j:
#         return True
#     if string[i] != string[j]:
#         return False
#     return isPalindrome(string, i + 1)
#
# print(isPalindrome("adaz"))

'#-----Time complexcity O(n)------------'
'#-----Space complexcity O(1)------------'


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1
    return True


print(isPalindrome("adaiitrdxd"))
