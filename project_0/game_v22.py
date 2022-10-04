"""Игра: "Угадай число""" #2

import numpy as np

min = 1
max  =  100

number = np.random.randint(min, max + 1) #машина загадывает число
count = 0  #подсчет количества попыток угадываний
while True:
    count  += 1
    X = int((min + max)/2)
    
    if mid > number:
        max = mid
        
    elif mid < number:
        min = mid
            
    else:
        print(f"Машина угадала число! Это число = {number}, за {count} попыток.")
        break  #конец игры и выход из цикла