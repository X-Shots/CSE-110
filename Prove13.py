import math
def windChill(temp,speed):
    return 35.74 + (.6215 * temp) - (35.75 * math.pow(speed,.16)) + (.4275 * temp * math.pow(speed,.16))
def CtoF(num):
    return (num * (9/5)) + 32


temp = int(input("What is the temperature? "))
ans = input("Fahrenheit or Celsius (F/C)? ")
if ans.lower() == "c":
    temp = CtoF(temp)
num = 5
while num < 61:
    print(f"At temperature {temp:.1f}F, and wind speed {num} mph, the windchill is: {windChill(temp,num):.2f}F")
    num += 5
