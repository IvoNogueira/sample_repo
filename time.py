import sys

x = int(input('Quantos graus? '))

def tempo(arg = None):
    if arg > 30:
        print('esta calor')
    elif arg < 10:
        print('esta frio')
    else:
        print('hoje está um bom dia')


tempo(x)

