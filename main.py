from functions.get_sequence import get_sequence
from classes.fifo import Fifo
from classes.aging import Aging
import matplotlib.pyplot as plt



def run_algorithms_and_get_faults(frame_counts, sequence_references):
    fifo_faults = []
    aging_faults = []

    for frames in frame_counts:
        fifo = Fifo(frames_quantity=frames, pages_quantity=15, page_sequence=sequence_references)
        page_fault_fifo = fifo.run()
        fifo_faults.append(page_fault_fifo)

        agin = Aging(frames_quantity=frames, pages_quantity=15, page_sequence=sequence_references)
        page_fault_agin = agin.run()
        aging_faults.append(page_fault_agin)

    return fifo_faults, aging_faults


sequence_references = get_sequence(15, "output")
frame_counts = [2, 4, 6, 8, 10]

fifo_faults, aging_faults = run_algorithms_and_get_faults(frame_counts, sequence_references)

plt.figure(figsize=(10, 6))
plt.plot(frame_counts, fifo_faults, marker='o', linestyle='-', color='b', label='FIFO')
plt.plot(frame_counts, aging_faults, marker='o', linestyle='-', color='r', label='Aging')

plt.xlabel('Número de Molduras de Página')
plt.ylabel('Número de Faltas de Página')
plt.title('Faltas de Página vs Número de Molduras de Página')
plt.legend()
plt.grid(True)
plt.show()