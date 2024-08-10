from page_replacement import PageReplacement


class Fifo(PageReplacement):

    def __init__(self, frames_quantity: int, page_sequence: list, pages_quantity: int = 5) -> None:
        self.frames_quantity = frames_quantity
        self.pages_quantity = pages_quantity
        self.page_sequence = page_sequence
        self.page_fault = 0
        self.fifo = []


    def insert_fifo(self, page):
        if page in self.fifo:
            return
                
        if len(self.fifo) == self.frames_quantity:
            self.replace_page(page)
        else:
            self.page_fault += 1
            self.fifo.insert(0, page)


    def replace_page(self, page):
        self.fifo.pop()
        self.fifo.insert(0, page)
        self.page_fault += 1


    def save_results():
        pass


    def run(self):
        for page in self.page_sequence:
            self.insert_fifo(page)
        return self.page_fault
        


fifo = Fifo(frames_quantity=2, page_sequence=[0,1,1,2,3])
print(fifo.run())

