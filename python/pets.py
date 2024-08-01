pet1 = {'name': 'Buddy', 'breed': 'Golden Retriever', 'age': 3}
pet2 = {'name': 'Whiskers', 'breed': 'Persian', 'age': 2}
pet3 = {'name': 'Rocky', 'breed': 'Boxer', 'age': 1}

list = [pet1,pet2,pet3]

for pet in list:
    for k,v in pet.items():
        print(f"key {k} , value {v}")
    print("\n")