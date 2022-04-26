import csv


res = []
with open("rez.csv", 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        res.append(row)

school, c = map(int, input("School, class: ").split())

matching = []
for r in res:
    sch = int(r['login'][12:14])
    cl = int(r['login'][15:17])
    if sch == school and cl == c:
        matching.append(f"{' '.join(r['user_name'].split()[-2:])}, {r['Score']}")

print(*matching, sep='\n')