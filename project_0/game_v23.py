"""Игра: 'Угадай число'""" #3
#загадывает и угадывает машина. Решение с функцией

import numpy as np

def random_predict(number: int=np.random.randint(1, 101)) -> int:
    
    min = 1
    max = 100

    predict_number = int(np.random.randint(min, max + 1)) #машина начинает отгадывать число
    count = 0  #подсчет количества попыток на угадывание числа

    while predict_number != number:
        count += 1
    
        if predict_number > number:
            max = predict_number
            predict_number = (min + max) // 2
        
        elif predict_number < number:
            min = predict_number
            predict_number = (min + max) // 2
            
        else:
            break  #конец игры и выход из цикла
    #print(f"Машина угадала число! Это число = {number}, за {count} попыток.")
    return count

#print(random_predict(2))
def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(np.random.randint(1, 10)) # не фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100)) #загадали список рандомных чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Этот алгоритм угадывает загаданное число {number} в среднем за: {score} попытки.")

score_game(random_predict)