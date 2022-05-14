year_number = int(input("Введите номер года "))
condition_1 = year_number%400==0
condition_2 = year_number%100==0
condition_3 = year_number%4==0
flag = False
if condition_1:
  if condition_2==False:
    if condition_3:
      print("Весокосный год")
      flag = True
if flag==False:
  print("невесокосный год")