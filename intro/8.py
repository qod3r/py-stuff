flag = True
height_max = 0
height_min = 0
eligible_count = 0

while flag:
    str = input()
    if str == "!":
        break
    h = int(str)
    
    if height_min == 0:
        height_min = h
    
    if h >= height_max:
        height_max = h
        
    if h <= height_min:
        height_min = h
    
    if h >= 150 and h <= 190:
        eligible_count += 1
        

print(eligible_count)
print(height_min, height_max)