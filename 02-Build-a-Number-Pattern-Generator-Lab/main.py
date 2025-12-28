def number_pattern(n):
    num =''
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    if n<1:
        return 'Argument must be an integer greater than 0.'
    for i in range(n):
        num+=str(i+1)+' '
    num = num.strip()
    return num
