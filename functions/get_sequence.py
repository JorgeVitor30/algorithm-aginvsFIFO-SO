import random

def get_sequence(page_quantity: int, file_name: str):
    pages = [i for i in range(page_quantity)]
    sequence = []

    for i in range (1000):
        sequence.append(random.choice(pages))
    
    with open(f"{file_name}.txt", "w") as arquivo:
        for page in sequence:
            arquivo.write(f"{page}\n")
