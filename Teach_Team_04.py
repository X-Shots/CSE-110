import math

print("\n Welcome to the velocity calculator. Please enter the following:")
m = float(input("\nMass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1/2) * p * A * C

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {math.sqrt(m * g / c) * (1 - math.exp((-1 * math.sqrt(m * g * c) / m) * t)):.3f} m/s")

print("\nWelcome to the Termianl Velocity Guesser!use this t")
term = round(math.sqrt(m * g / c),0)
guess = ""
while(guess != term):
    guess = input("\nEnter your guess!")
    if guess < term:
        
        print("Your guess is LOWER than the terminal velocity!")
        
    elif guess > term:
        print("Your guess is higher than the terminal velocity")
    elif guess == term:
        print("Coreect!")

print(f"The termainl velocity rounded to 10 decimals is {math.sqrt(m * g / c):.10f}")

    
    
    

