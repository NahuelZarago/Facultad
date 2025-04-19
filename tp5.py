def romano(n):
  letras= {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  
  end = 0
  before = 0
  
  for i in n:
    letritas = letras[i]
    if before and letritas > before:
        end += letritas - 2 * before
    else:
        end += letritas 
    before =  letritas
  
  return end

n = input('Ingrese un numero romano (mayusculas): ')
print ('Decimal: ', romano(n))
