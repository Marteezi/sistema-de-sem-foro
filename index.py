from colorama import Fore
import time

vermelho = 0
verde = 0


while True:
    if vermelho < 20:
        vermelho += 1
        alerta = Fore.RED + "Não pode passar. {:02}".format(vermelho)
    elif verde < 30:
        verde += 1
        alerta = Fore.GREEN + "Pode passar. {:02}".format(verde)
    else:
        vermelho = 0
        verde = 0
    print("\r" + " " * 50 + "\r{}".format(alerta), end="")
    time.sleep(1)
