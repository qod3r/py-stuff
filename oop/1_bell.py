class BigBell:
    sounds = ["ding", "dong"]
    last_sound = 0
    
    def sound(self):
        print(self.sounds[self.last_sound])
        self.last_sound = not self.last_sound


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()