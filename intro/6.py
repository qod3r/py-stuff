a = input()
max = 0
min = 10
Imax, Imin = 0, 0

arr = list(map(int, a))

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        Imax = i
    if arr[i] < min:
        min = arr[i]
        Imin = i

arr.pop(Imax)
arr.pop(Imin)

if (min + max)/2 == arr[0]:
    print("красиво")
else:
    print("некрасиво")