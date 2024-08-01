current_users=["kela","deka","bora","baro","sam"]
caps_current_users=[]
for curr_user in current_users:
    caps_current_users.append(curr_user.upper())

new_users=["Kela","div","nim","baro","jaggy"]

for new_user in new_users:
    if new_user.upper() in caps_current_users:
        print(f"{new_user} will need new username")
    else:
        print(f"{new_user} username available")    