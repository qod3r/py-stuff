class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content = ""
        
    def __str__(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def _get_content(self):
        return self.content
    
    def _write(self, content):
        self.content = content
        

# everything is a file
class Dir(File):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def get_children(self):
        return self.children
    
    def add_child(self, thing):
        self.children.append(thing)


class System:
    def __init__(self):
        self.root = Dir("", None)
        self.curr_dir = self.root
    
    # print current path
    def pwd(self):
        print(f"/{self.curr_dir}")
    
    # print contents of current directory
    # group-directories-first=True
    def ls(self):
        if self.curr_dir.get_children() == []:
            print("empty")
        else:
            dir_arr = []
            file_arr= []
            for c in self.curr_dir.get_children():
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
            for idx, child_dir in enumerate(map(str, self.curr_dir.get_children())):
                if dir == child_dir:
                    self.curr_dir = self.curr_dir.get_children()[idx]
    
    # create directory
    def mkdir(self, name):
        self.curr_dir.add_child(Dir(name, self.curr_dir))
    
    # print a file    
    def cat(self, target):
        for idx, file in enumerate(map(str, self.curr_dir.get_children())):
                if target == file:
                    print(f"{target}:\n\t{self.curr_dir.get_children()[idx]._get_content()}")
    
    # create file
    def touch(self, name):
        self.curr_dir.add_child(File(name, self.curr_dir))

    # delete
    def rm(self, file):
        pass
    
    # put string into file
    def echo_into(self, content, target):
        for idx, file in enumerate(map(str, self.curr_dir.get_children())):
                if target == file:
                    self.curr_dir.get_children()[idx]._write(content)


s = System()
s.pwd()
s.ls()
s.mkdir("dir1")
s.touch("bruh.txt")
s.mkdir("dir2")
s.ls()
s.echo_into("test 123", "bruh.txt")
s.cat("bruh.txt")