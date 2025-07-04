import random

def mutate(data: bytes, num_mutations: int = 5) -> bytes:
    data = bytearray(data)
    
    for _ in range(num_mutations):
        mutation_type = random.choice(['flip', 'insert', 'delete'])
        
        if mutation_type == 'flip' and len(data) > 0:
            idx = random.randint(0, len(data) - 1)
            data[idx] = random.randint(0, 255)
            
        elif mutation_type == 'insert':
            idx = random.randint(0, len(data))
            data.insert(idx, random.randint(0, 255))
            
        elif mutation_type == 'delete' and len(data) > 1:
            idx = random.randint(0, len(data) - 1)
            del data[idx]
            
    return bytes(data)