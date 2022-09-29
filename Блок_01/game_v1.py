print('Hi')
import numpy as np
number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print('Число должно быть меньше    V')
        
    elif predict_number < number:
        print('Число должно быть больше    Л')
    else:
        print(f'Вы угадали! Это число = {number}, за {count} попыток')
        break
    