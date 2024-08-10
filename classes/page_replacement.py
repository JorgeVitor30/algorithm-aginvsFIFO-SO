from abc import ABC, abstractmethod


class PageReplacement(ABC):
    '''
    A base interface for Algorithms
    '''
    def __init__(self, frames_quantity: int, page_sequence: list, pages_quantity: int = 5, **kwargs) -> None:
        self.frames_quantity = frames_quantity
        self.pages_quantity = pages_quantity
        self.page_sequence = page_sequence
        self.missing_pages = 0

    @abstractmethod
    def replace_page():
        pass

    @abstractmethod
    def run():
        pass