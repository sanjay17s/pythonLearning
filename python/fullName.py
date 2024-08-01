def name(firstname,lastname,middlname=''):
    if middlname:
        return {'Firstname':f"{firstname}",'Lastname':f'{lastname}','Middlname':f'{middlname}'}
    else:
        return {'Firstname':f"{firstname}",'Lastname':f'{lastname}'}

print(name('sanjay','s'))