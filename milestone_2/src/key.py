

class Key:
    def __init__(self, name: str, home: int):
        self.name = name
        self.home = home

    def set_home(self, home: int):
        self.home = home
    
    def get_home(self):
        return self.home

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name
