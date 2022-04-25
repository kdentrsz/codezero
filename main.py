try:
  num1 = int(input("число 1: "))
  num2 = int(input("число 2: "))
  final = num1/num2
  end = round(final)
  print(end)
except ZeroDivisionError:
  print("На 0 делить нельзя!")