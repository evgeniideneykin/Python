print("exercise_1")
time_s = abs(int(input('ввести время в секундах: ')))

if time_s < 60:
  out = str(time_s) + " сек"
elif time_s < 3600:
    out = str(time_s // 60) + " мин " + str(time_s % 60) + " сек"
elif time_s < 86400:
    out = str(time_s // 3600) + " час " + str((time_s % 3600) // 60) + " мин " + str(time_s % 60) + " сек"
else:
    out = str(time_s // 86400) + " дн " + str((time_s % 86400)//3600) + " час " + str((time_s // 60) % 60) + " мин " + str(time_s % 60) + " сек"
print(out)

print()
print("exercise_2")
numbers = [i**3 for i in range(0, 1000) if i % 2 == 1]
num = 0
for i in numbers:
  if sum(map(int,str(i))) % 7 ==0:
    num += i
print("сумма чисел = " + str(num))

numbers_17 = [i**3 + 17 for i in range(0, 1000) if i % 2 == 1]
num_17 = 0
for i in numbers_17:
  if sum(map(int,str(i))) % 7 ==0:
    num_17 += i
print("сумма чисел+17 = " + str(num_17))


print()
print("exercise_2*")
numbers = [i**3 for i in range(0, 1000) if i % 2 == 1]
num = 0
for i in numbers:
  if sum(map(int,str(i))) % 7 ==0:
    num += i
print("сумма чисел = " + str(num))

num_17 = 0
for i in numbers:
  if sum(map(int,str(i + 17))) % 7 ==0:
    num_17 += i + 17
print("сумма чисел+17 = " + str(num_17))

print()
print("exercise_3")
print()
lst = [i for i in range(0, 101)]
for num in lst:
  if num in (11, 12, 13, 14):
   txt = "процентов"
  elif num % 10 in (2 ,3 ,4):
    txt = "процента"
  elif num % 10 == 1:
    txt = "процент"
  else:
   txt = "процентов"
  print(str(num) + " " + txt)
