from functions.get_sequence import get_sequence
from classes.fifo import Fifo
from classes.aging import Aging


sequence_references = get_sequence(5, "output")


fifo = Fifo(frames_quantity=2, pages_quantity=5, page_sequence=sequence_references)
page_fault_fifo = fifo.run()

agin = Aging(frames_quantity=2, pages_quantity=5, page_sequence=sequence_references)
page_fault_agin = agin.run()

print("PAGES_FAULT_FIFO:", page_fault_fifo)
print("PAGES_FAULT_AGING:", page_fault_agin)
