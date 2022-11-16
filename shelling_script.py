#py -m pip install numpy
import random
import matplotlib.pyplot as plt
import numpy as np

#region Константы
M = 15              # массив
BLUE, RED = 45, 45  # проценты цветов
HAPPY = 2           # порог клеток для "счастья"
ITERATIONS = 10000  # количество итераций
#endregion

#region Глобальные переменные
count_blue = round((M*M)*BLUE/100)
count_red = round((M*M)*RED/100)
count_none = M*M - (count_blue + count_blue)

colors = []
for i in range(count_blue):
  colors.append('blue')
for i in range(count_red):
  colors.append('red')
for i in range(count_none):
  colors.append('none')
random.shuffle(colors)

field = [['none' for i in range(M)] for i in range(M)]

iterations = 0
#endregion

def calculateIndexes(element, array):
  indexes = []
  for i in range(len(array)):
    for j in range(len(array)):
      if array[i][j] == element:
        indexes.append([i, j])
  return indexes

def ifHappy(array,i,j,HAPPY):
  count = 0

  for i in range(3):
    for j in range(3):
      ni = i + i - 1
      nj = j + j - 1
      if ni >= 0 and nj>=0 and ni < len(array) and nj < len(array) and not(i == ni and j == nj):
        if array[i][j] == array[ni][nj]: count += 1
      else:
        continue
  if count >= HAPPY:
    return True
  else:
    return False

def writeArray(myArray):
  plt.rcParams["figure.figsize"] = (5,5)
  data = np.myArray(field)

  x = np.arange(len(myArray))
  y = np.arange(len(myArray))

  x, y = np.meshgrid(x,y)

  plt.scatter(x,y,c=data[x,y], marker='s', s=400)
  plt.show()

def turnColorsToNumbers():
  for i in range(M):
    start = i*M
    end = (i+1)*M
    field[i] = colors[start:end]

  for i in range(M):
    for j in range(M):
      if field[i][j] == 'red':
        field[i][j] = 1
      elif field[i][j] == 'blue':
        field[i][j] = 2
      else:
        field[i][j] = 0

  countHappy = 0
  for i in range(M):
    for j in range(M):
      # Если точка не счастлива 
      if ifHappy(field,i,j,HAPPY):
        countHappy += 1
  print('Количество счастливых точек на старте: ', countHappy)
  writeArray(field)

def shellingStart():
  for step in range(ITERATIONS):
    for i in range(M):
      for j in range(M):
        # Если точка не счастлива 
        if not ifHappy(field,i,j,HAPPY):
          # Найти ей случайное место из пустых
          new_place = random.choice(calculateIndexes(0, field))
          new_place_i = new_place[0]
          new_place_j = new_place[1]
          # Поместить несчастную точку в случайное пустое место
          field[new_place_i][new_place_j], field[i][j] = field[i][j], field[new_place_i][new_place_j]
    iterations += 1
      
  # Количество счастливых в конце
  cnt_happy_end = 0
  for i in range(M):
    for j in range(M):
      # Если точка не счастлива 
      if ifHappy(field,i,j,HAPPY):
        cnt_happy_end += 1
  print('Количество счастливых точек в конце: ', cnt_happy_end)

  print('Количество шагов: ',iterations)
  print(field)

  writeArray(field)

turnColorsToNumbers()
shellingStart()