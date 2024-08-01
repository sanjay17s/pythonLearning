name = input("Enter your superhero name: ")

print("THESE ARE THE FOLLOWING THINGS YOU CAN DO WITH YOUR NAME")
print("1. CHANGE IT TO UPPERCASE")
print("2. CHANGE IT TO LOWERCASE")
print("3. CHANGE IT TO TITLECASE")

option = int(input("CHOOSE YOUR OPTION (1/2/3): "))
print(option)

if option == 1 :
    print(name.upper())
elif option == "2" :
    print(name.lower())
elif option == "3" :
    print(name.title())
else:
    print("Invalid option. Please choose 1, 2, or 3.")
