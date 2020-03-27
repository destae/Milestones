
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

class KeyValueStore:
    def __init__(self):
        self.home_node = -1 
        self.key_store = {}

    def add_key_value(self, key: Key, value):
        if key.get_home() == self.home_node:
            self.key_store.update({key.get_name(), value})
        else:
            print("Gotta find the home node!")

    def remove_key_value(self, key: Key):
        if key.get_home() == self.home_node:
            self.key_store.pop(key.get_name())
        else:
            print("Gotta skirt, not in the right place!")
    
    def update_home_node(self, home_node):
        self.home_node = home_node
    
    def get_value(self, key: Key):
        if key.get_home() == self.home_node:
            return self.key_store.get(key.get_name())
        else:
            print("Whoops...not my house!")

    def wait_and_get(self, key: Key):
        return self.get_value(key)