import statistics as st

values = [int(x) for x in input()]
print('Число', 'интересное' if max(values) - min(values) == st.median(values) else 'неинтересное')