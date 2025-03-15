# This program checks the age and categorizes the person into different age groups.
# It also demonstrates exception handling using try and except.

try :
    # Asking users' age
    age = int(input("Please enter your age: "))
    
    # Checking users' age category
    if age < 0 :
        # Raising an error if the input age is negative
        raise ValueError("Age cannot be negative.")
    elif age < 13 :
        print("You are categorized as: Child")  # If age is from 0 to 12
    elif age < 20 : 
        print("You are categorized as: Teenager")   # If age is from 13 to 19
    elif age < 60 :
        print("You are categorized as: Adult")  # If age is from 20 to 59
    else :
        print("You are categorized as: Senior") # If age is from 60 or above

except ValueError as e :
    # Handling invalid input (e.g., non-numeric value)
    print(f"Invalid input: {e}")



'''
try:
    # Input: Get age from the user
    user_input = int(input("Please enter your age: "))

    # Check the age category
    if user_input < 0:
        raise ValueError("Age cannot be negative.")
    elif user_input < 13:
        print("You are categorized as: Child")
    elif user_input < 20:
        print("You are categorized as: Teenager")
    elif user_input < 60:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")
        
except ValueError:
    print("Invalid input: Age cannot be a non-number.")
'''