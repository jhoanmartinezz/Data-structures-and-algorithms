'# -------------------solucion iterativa-------------------------------------'
# '#Time complexity = O(n)'
# '#Space complexity = O(1)'
#
def getNthFib(n):
    if n == 2:
        return 1
    f0 = 0
    f1 = 1
    suma = 0
    contador = 2
    while contador < n:
        contador = contador + 1
        suma = f0 + f1
        f0 = f1
        f1 = suma
        print(suma)
    return suma

print(getNthFib(2))

# 1 => 0
# 2 => 1
# 3 => 1
# 4 => 2
# 5 => 3
# 6 => 5
# 7 => 8

"#-------------------solucion memorizacion o Hash Table-------------------"
"# Time complexity = O(n)"
"# Space complexity = O(n)"


# def getNthFib(n, memoize={1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
#         return memoize[n]
#
#
# print(getNthFib(9))
