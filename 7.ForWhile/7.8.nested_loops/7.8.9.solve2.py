# 10 * bull + 5 * cow + 0.5 * calf = 100
# bull + cow + calf = 100

for bull in range(1, 10):
    for cow in range(1, 20):
        for calf in range(1, 200):
            if 10 * bull + 5 * cow + 0.5 * calf == 100 and bull + cow + calf == 100:
                print(f'bull = {bull}, cow = {cow}, calf = {calf}')

