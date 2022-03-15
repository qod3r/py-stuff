def mirror(arr):
    arr += arr[::-1]

arr = [1, 2]
mirror(arr)
print(arr)
