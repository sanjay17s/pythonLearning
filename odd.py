odd = []
for val in range(1,20,2):
    odd.append(val)
copy_odd = odd
odd.append(2)
copy_odd.append(78)
print(odd)
print(copy_odd)