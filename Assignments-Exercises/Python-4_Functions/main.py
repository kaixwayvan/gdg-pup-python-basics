def create_greeting(name):
    return f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

try:
    name = input("\nEnter your name: ")
    greet = create_greeting(name)
    print("\n"+greet)
except ValueError:
    print("Invalid input: Please enter a valid name.")