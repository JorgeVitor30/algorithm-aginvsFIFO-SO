from classes.page_replacement import PageReplacement


class Aging(PageReplacement):

    def __init__(self, frames_quantity: int, page_sequence: list, pages_quantity: int = 5) -> None:
        self.frames_quantity = frames_quantity
        self.pages_quantity = pages_quantity
        self.page_sequence = page_sequence
        self.page_fault = 0
        self.age_counter = {i: 0b00000000 for i in range(pages_quantity)}
        self.frames = []

    def replace_page(self, page):
        min_age = 255
        page_to_replace = None

        for frame in self.frames:
            if self.age_counter[frame] < min_age:
                min_age = self.age_counter[frame]
                page_to_replace = frame

        if page_to_replace is not None:
            self.frames.remove(page_to_replace)
            self.age_counter.pop(page_to_replace, None)
            self.frames.append(page)

            self.age_counter[page] = 0b00000000

    def insert_aging(self, page):
        if page in self.frames:
            self.update_ticks(page)
        else:
            if len(self.frames) == self.frames_quantity:
                self.replace_page(page)
            else:
                self.frames.append(page)
                self.age_counter[page] = 0b00000000 

            self.update_ticks(page)
            self.page_fault += 1

    def update_ticks(self, page):
        for key in self.age_counter.keys():
            if key == page:
                self.age_counter[key] = (self.age_counter[key] >> 1) | 0b10000000
            else:
                self.age_counter[key] = self.age_counter[key] >> 1

    def run(self):
        for page in self.page_sequence:
            self.insert_aging(page)
        return self.page_fault
