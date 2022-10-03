#Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) #загадываем число

#колличество попыток угадывания
count = 0

while True:
    count +=1
    
        print("Число должно быть меньше!")
        
    elif predict_number < number:
        print("Число должно быть больше!")
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла2                                        