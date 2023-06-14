mixer = {'красный синий': 'фиолетовый',
         'желтый красный': 'оранжевый',
         'желтый синий': 'зеленый',
         'желтый желтый': 'желтый',
         'красный красный': 'красный',
         'синий синий': 'синий',
         }

color_pair = ' '.join(sorted([input() for _ in range(2)]))
print('ошибка цвета' if color_pair not in mixer else mixer[color_pair])
