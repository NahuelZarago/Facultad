def romano(n):
    letras = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not n:
        return 0
    if len(n) > 1 and letras[n[0]] < letras[n[1]]:
        return -letras[n[0]] + romano(n[1:])
    return letras[n[0]] + romano(n[1:])


print(romano('V'))     
print(romano('IV'))    
print(romano('IX'))    
print(romano('XIV'))   

