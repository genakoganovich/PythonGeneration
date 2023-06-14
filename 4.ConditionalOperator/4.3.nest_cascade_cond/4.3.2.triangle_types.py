count = len({input() for _ in range(3)})
print('Равносторонний' if count == 1 else 'Равнобедренный' if count == 2 else 'Разносторонний')
