with open("input.txt", 'r') as f:
    file = f.read()

nums = list(map(int, file.split()))

pos = len(list(filter(lambda x: x > 0, nums)))
neg = len(list(filter(lambda x: x < 0, nums)))
zero = len(list(filter(lambda x: x == 0, nums)))
total = len(nums)

out = f"{total}\n1 {pos} -1 {neg} 0 {zero}"
with open("output.txt", 'w') as f:
    f.write(out)