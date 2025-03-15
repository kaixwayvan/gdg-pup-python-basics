foods = ["ice cream", "pasta", "hash browns", "salad", "burrito bowl"]

for fave in foods:
    print(f"• {fave}")

try:
    num = int(input("\nEnter a positive countdown number: "))

    if num <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        while num > 0:
            print(num)
            num -= 1
        
        print("\nCountdown complete!")
except ValueError:
    print("Invalid input: Please enter a valid number.")