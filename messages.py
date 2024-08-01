list = ['hi ,how are you?','im fine']
print(f"old list: {list}")   
updatedList =[]

def listPrint(list):
    while list:
        item = list.pop(0)
        updatedList.append(item)
   
        
        
listPrint(list[:])  
print(f"updated list: {updatedList}")      
print(f"old list: {list}")   