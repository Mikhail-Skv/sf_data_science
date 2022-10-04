print('Hi')
import numpy as np
number = np.random.randint(1, 101)


def score_game() -> int:
    
    count = 0

    while True:
        count+=1
        predict_number = int(input("Угадай число от 1 до 100: "))
    
        if predict_number > number:
            print('Число должно быть меньше    V')
        
        elif predict_number < number:
            print('Число должно быть больше    ^')
        
        else:
            print(f'Вы угадали! Это число = {number}, за {count} попыток')
            break
    
    return(count)


if __name__ == '__main__':      # не будет запускаться если подключить как библиотеку
    #RUN
    score_game() 