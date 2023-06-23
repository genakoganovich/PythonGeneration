articles = ['a', 'an', 'the']
print(f'Общее количество артиклей: {len(list(filter(lambda x: str(x).lower() in articles, input().split())))}')
