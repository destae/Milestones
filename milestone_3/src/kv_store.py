
class Key:
    ## Creates a key class: main constructor
    def __init__(self, name: str, home: int):
        self.name = name
        self.home = home

    ## Sets the home value of the key
    def set_home(self, home: int):
        self.home = home
    
    ## Retrieves the home value of the key
    def get_home(self):
        return self.home

    ## Sets the name of the key, this a unique value
    def set_name(self, name: str):
        self.name = name

    ## Retrieves the name of the key
    def get_name(self):
        return self.name

class KeyValueStore:
    def __init__(self, home_node: int=-1):
        self.home_node = home_node
        self.key_store = {}

    def add_key_value(self, key: Key, value):
        if key.get_home() == self.home_node:
            self.key_store.update({key.get_name(), value})
            if key.get_name() in self.key_store:
                print("Error: Key already exists in the store, please rename")
        else:
            ## TODO: retrieve the home node of the given key: key.get_home
            ## TODO: send a request to the node running the KV store to contact the home node
            ## TODO: send the key value pair over serial to the home node
            ## TODO: place new key value there
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