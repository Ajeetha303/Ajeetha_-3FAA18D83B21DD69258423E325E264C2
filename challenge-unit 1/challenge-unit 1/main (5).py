year=int(input("Enter the year:"))
if(year % 4==0 and year % 100!=0):
  print("The year is leap year")
elif(year %400==0):
  print("The year is leap year")
else:
  print('The is not leap year')
