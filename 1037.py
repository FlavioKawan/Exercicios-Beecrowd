valor = float(input())
if valor <= 25.0000 and valor >= 0 :
    print('Intervalo [0,25]')
    
elif valor >= 25.0001 and valor <= 50.0000000:
    print('Intervalo (25,50]')

elif valor >= 50.0000001 and valor <= 75.0000000:
    print('Intervalo (50,75]')
    
elif valor >= 75.0000001 and valor <= 100.0000000 :
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')