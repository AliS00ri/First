
import random

pound = float(input("Enter fish weight in pounds: "))

kg = pound * 0.45359237

money = kg * 2

print(f"Weight in kilograms: {kg:.2f}")
print(f"U get: {money:.2f} dollars")

if money > 100:
    prize = random.choice(["hat", "hook", "bucket"])
    print("Your gift is :", prize)
