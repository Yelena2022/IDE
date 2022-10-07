"""Игра угадай число"""
# Компьютер сам загадывает число (Тренировочный файл)

import numpy as np

def random_predict(number:int=1) -> int: # -> int: """+ Enter -для написания документации(какие аргументы мы принимаем и на выходе)
    """рандомно угадываем число
    
    Args:
        number (int, optinal): Загаданное число. Default to 1.
        
    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count +=1
        predict_number = np.random.randint(1,500) #Предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    return(count)

print(f'количество попыток: {random_predict(10)}')

def score_game(random_predict) ->int:
    """За какое количество попыток в среднем за 1000 подходов угадываем наш алгоритм
    
    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = [] # список для сохранения кол-ва попыток угадывания
    np.random.seed(1) #фиксируем Сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число {number} в среднем за:{score} попыток')
    return(score)


if __name__== '__main__':
    #RUN (запускаем)
    score_game(random_predict)