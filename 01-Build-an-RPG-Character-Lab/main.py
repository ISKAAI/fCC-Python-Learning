full_dot = '●'
empty_dot = '○'
def dot(num,size):
    return str(num*full_dot+(size-num)*empty_dot)
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if name=='':
        return 'The character should have a name'
    if len(name)>10:
        return 'The character name is too long'
    if ' 'in name:
        return 'The character name should not contain spaces'
    states =[strength,intelligence,charisma]
    for state in states:
        if not isinstance(state,int):
            return 'All stats should be integers'
        if state <1:
            return 'All stats should be no less than 1'
        if state >4:
            return 'All stats should be no more than 4'
    if sum(states) !=7:
        return 'The character should start with 7 points'
    return f"{name}\nSTR {dot(strength,10)}\nINT {dot(intelligence,10)}\nCHA {dot(charisma,10)}"
print(create_character('ren', 4, 2, 1))

