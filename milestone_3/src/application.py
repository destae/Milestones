"""Defines an Application Class"""
from abc import ABC, abstractmethod


class Application(ABC):
    """Abstract class"""

    def __init__(self, idx, kv):
        self.idx = idx
        self.kv = kv
        super().__init__()

    @abstractmethod
    def run_(self):
        pass

    def this_node(self):
        """Returns the id of this application"""
        return self.idx