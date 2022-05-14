letter = input("введите букву латинского алфавита ")
vowels_arr = ("a","e","i","o","u")
if letter == "y":
  print("Буква может быть и гласной и согласной")
if letter in vowels_arr:
  print("гласная")
else: print("согласная")