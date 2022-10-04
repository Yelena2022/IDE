"""Игра: "Угадай число""" #2

from re import X
import numpy as np

min = 1
max  =  100

number = np.random.randint(min, max + 1) #машина загадывает число
count = 0  #подсчет количества попыток угадываний
while True:
    count  += 1
    X = int((min + max)/2)
    
    if X > number:
        max = X
        
    elif X < number:
        min = X
            
    else:
        print(f"Машина угадала число! Это число = {number}, за {count} попыток.")
        break  #конец игры и выход из цикла