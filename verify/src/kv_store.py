from verify.src import utils

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

    '''
    Adds a new key to the key value store.
    If the key value store home node does not align with the home node of the store, it sends a request to the right key value store to add the pair.
    '''
    def add_key_value(self, key: Key, value):
        self.key_store.update({key.get_name(): value})

    '''
    Removes the specified key from the store. 
    If the home node of the key does not match this node, a request is sent to the home node to remove the key in question.
    '''
    def remove_key_value(self, key: Key):
        self.key_store.pop(key.get_name())

    '''
    Updates the home node of this key value store
    '''
    def update_home_node(self, home_node):
        self.home_node = home_node
    
    '''
    Retrieves the value associated with the given key. 
    If the given Key's home node is not this node, the system sends a message to the home node of the key to retrieve the value
    '''
    def get_value(self, key: Key):
        return self.key_store.get(key.get_name())


    def wait_and_get(self, key: Key):
        if key.get_home() != self.home_node:
            #Request to proper node
            return None
        else:
            return self.get_value(key)

# Fixes a circular dependency
