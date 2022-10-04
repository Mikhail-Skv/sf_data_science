import numpy as np
number = np.random.randint(1, 101)

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданое число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    mark_begin = 1
    mark_end = 101

    while True:
        count+=1
        predict_number = mark_begin + (mark_end - mark_begin) // 2 
    
        if predict_number > number:
            mark_end = predict_number 
        
        elif predict_number < number:
            mark_begin = predict_number 
        else:
            
            break
    return(count)


def score_game(random_predict) -> int:
    """За какое число попыток в среднем за 100 подходов угадывает наш алгоритм

    Args:
        random_predict (int): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} раз')
    return(score)

if __name__ == '__main__':      # не будет запускаться если подключить как библиотеку
    #RUN
    score_game(random_predict) 
