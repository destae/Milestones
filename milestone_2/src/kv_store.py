from milestone_2.src.key import Key


class KeyValueStore:
    """Key value store that is the backbone of this application"""

    def __init__(self,home_node=None):
        self.home_node = home_node
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
