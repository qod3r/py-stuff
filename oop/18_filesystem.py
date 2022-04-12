class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content = ""
        
    def __str__(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_content(self):
        return self.content
    
    def add_content(self, content):
        self.content = content
        

# everything is a file
class Dir(File):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def get_content(self):
        return self.children
    
    def add_content(self, thing):
        self.children.append(thing)


class System:
    def __init__(self):
        self.root = Dir("", None)
        self.curr_dir = self.root
    
    def __lookup(self, target):
        for idx, file in enumerate(map(str, self.curr_dir.get_content())):
                if target == file:
                    return self.curr_dir.get_content()[idx]
    
    # print current path
    def pwd(self):
        print(f"/{self.curr_dir}")
    
    # print contents of current directory
    # group directories first
    def ls(self):
        if self.curr_dir.get_content() == []:
            print("empty")
        else:
            dir_arr = []
            file_arr = []
            for c in self.curr_dir.get_content():
                if type(c) is Dir:
                    dir_arr.append(c)
                elif type(c) is File:
                    file_arr.append(c)
            print(*dir_arr, sep=" ", end=" ")
            print(*file_arr, sep=" ", end="\n")
        
    # go to dir
    # no argument cd's into root dir
    # .  - current
    # .. - parent
    def cd(self, dir=""):
        if dir == ".":
            pass
        elif dir == "..":
            if self.curr_dir.get_parent() is not None:
                print(self.curr_dir.get_parent())
                self.curr_dir == self.curr_dir.get_parent()
        else:
            self.curr_dir = self.__lookup(dir)
    
    # create directory
    def mkdir(self, name):
        self.curr_dir.add_content(Dir(name, self.curr_dir))
    
    # print a file    
    def cat(self, target):
        print(f"{target}:\n\t{self.__lookup(target).get_content()}")
    
    # create file
    def touch(self, name):
        self.curr_dir.add_content(File(name, self.curr_dir))

    # delete
    def rm(self, file):
        pass
    
    # put string into file
    def echo_into(self, content, target):
        self.__lookup(target).add_content(content)


s = System()
s.pwd()
s.ls()
s.mkdir("dir1")
s.touch("bruh.txt")
s.mkdir("dir2")
s.ls()
s.echo_into("test 123", "bruh.txt")
s.cat("bruh.txt")

s.cd("dir1")
s.mkdir("dir1-1")
s.ls()
s.cd("..")
s.pwd()