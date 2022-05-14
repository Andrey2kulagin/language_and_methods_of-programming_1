human_age = float(input("введите возраст человека в годах "))
if human_age<=0:
  raise Exception("странные данные, проверьте правильность") 
if human_age<=21:
  dog_age = human_age/10.5
  print(f"Возраст человека в собачьих годах равен: {round(dog_age,2)}")
else:
  dog_age = (human_age-21)/4+2
  print(f"Возраст человека в собачьих годах равен: {round(dog_age,2)}")
