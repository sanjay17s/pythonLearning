guests = ["kalam sahab","vajpayee","nehru"]
#print(f"{guests[0]} was an inspiration for millions around india\n{guests[1]} is regarded as a great stateman\n{guests[-1]} is the 1st pm of our nation")
#print(f"{guests[-1]} sir wont be ale to  make it to the party, he has send his sincere apologies")
#print("We need a new guest")
guests.remove("nehru")
#new_guest = input("the new guest is: ")
#guests.append(new_guest)


#print("We have got a bigger hall for more guets,lets add more people to the list")
guests.append("mj")
guests.append("lata ji")
print(f"here is the original list {guests}")
print(f"here is the sorted list {sorted(guests,reverse=True)}")
print(f"here is the original list again {guests}")

