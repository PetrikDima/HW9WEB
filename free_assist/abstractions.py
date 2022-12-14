from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def values(self):
        pass

    @abstractmethod
    def match_search_str(self, *args):
        pass
