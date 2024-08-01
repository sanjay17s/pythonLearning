def fav(*names):
    return names

tuple = fav('rono','messi','kroos') 
tuple[0] = 'hjhj'   

def fav(name,age,**userinfo):
    for info in userinfo:
        print(info)

fav('sanjay','24','kayamkulam','690508')