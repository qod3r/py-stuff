import csv


class Warehouse:
    
    def __init__(self):
        self.goods = {}
    
    def add(self):
        name = input("name: ")
        price = input("price: ")
        quant = input("quantity: ")
        self.goods[name] = f"{price},{quant}"

    def check(self):
        name = input("name: ")
        if name not in self.goods.keys():
            print("no such product")
            return
        print(self.goods[name])
        
    def view_all(self):
        for k in self.goods.keys():
            print(f"{k},{self.goods[k]}")
    
    def edit(self):
        name = input("name: ")
        if name not in self.goods.keys():
            print("no such product")
            return
        price = input("price: ")
        quant = input("quantity: ")
        self.goods[name] = f"{price},{quant}"
    
    def delete(self):
        name = input("name: ")
        if name not in self.goods.keys():
            print("no such product")
            return
        del self.goods[name]
        print(f"{name} deleted")
    
    def save(self):
        file = input("filename: ")
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            for i in self.goods.keys():
                writer.writerow([i, *self.goods[i].split(",")])

    def load(self):
        file = input("filename: ")
        with open(file, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                name, price, quant = row
                self.goods[name] = f"{price},{quant}"
                


w = Warehouse()

while True:
    print("[a] Add item\n"
          "[c] Check item\n"
          "[v] View all items\n"
          "[e] Edit item\n"
          "[d] Delete Item\n"
          "[s] Save to file\n"
          "[l] Load from file\n"
          "[x] Exit")
    choice = input()
    
    match choice:
        case "a":
            w.add()
        case "c":
            w.check()
        case "v":
            w.view_all()
        case "e":
            w.edit()
        case "d":
            w.delete()
        case "s":
            w.save()
        case "l":
            w.load()
        case "x":
            break
        case _:
            pass