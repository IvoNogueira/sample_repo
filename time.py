import sys

x = input('Quantos graus? ')

def tempo(arg = None):
    if arg > 30:
        print('esta calor')
    else:
        print('hoje está um bom dia')


tempo(x)

