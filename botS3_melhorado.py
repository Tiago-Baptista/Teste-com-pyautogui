import funcoes
from time import sleep
from random import randint
funcoes.browser()
for c in range(0, 10):
#fazer ataque
    funcoes.ataque()
#voltar ao contador
    funcoes.contador()
#esperar 4min a 5min
    x = randint(250, 300)
    sleep(x)
# abrir o browser
    funcoes.browser()
