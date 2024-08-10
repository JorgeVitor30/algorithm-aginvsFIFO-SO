from page_replacement import PageReplacement


class Aging(PageReplacement):

    def __init__(self, frames_quantity: int, page_sequence: list, pages_quantity: int = 5) -> None:
        self.frames_quantity = frames_quantity
        self.pages_quantity = pages_quantity
        self.page_sequence = page_sequence
        self.page_fault = 0
        self.age_counter = {i: 0b00000000 for i in range(pages_quantity)}
        self.frames = []
        self.page_fault = 0


    def replace_page(self, page):
        min = 255
        for frame in self.frames: # 0 e 1   {1: 160, 2: 64, 3: 0, 4: 0, 5: 0}
            if self.age_counter[frame] < min:
                min = self.age_counter[frame]
                sub = frame

        self.frames.remove(sub)
        self.age_counter[sub] = 0b00000000
        self.frames.append(page)


    def insert_aging(self, page):
        if page in self.frames:
            self.update_ticks(page)
            return
        
        if len(self.frames) == self.frames_quantity:
            self.replace_page(page)
            self.update_ticks(page)
            self.page_fault += 1
        else:
            self.frames.append(page)
            self.update_ticks(page)
            self.page_fault += 1


    
    def update_ticks(self, page):
        for key in self.age_counter.keys():
            if key == page:
                self.age_counter[key] = self.age_counter[key] >> 1
                self.age_counter[key] = self.age_counter[key] | 0b10000000
            else:
                self.age_counter[key] = self.age_counter[key] >> 1
        print(aging.age_counter)

    

    def run(self):
        for page in self.page_sequence:
            self.insert_aging(page)
        print(self.page_fault)


aging = Aging(frames_quantity=2, page_sequence=[0,1,0,0,2])
aging.run()
