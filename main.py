import random
import csv

# Función para generar saldos aleatorios
def generar_saldos():
  saldos = []
  for _ in range(10):
    saldo = random.randint(1000, 100000)
    saldos.append(saldo)
  return saldos

# Función para clasificar saldos
def clasificar_saldos(saldos):
  saldos_bajos = [saldo for saldo in saldos if saldo <= 20000]
  saldos_medios = [saldo for saldo in saldos if 20001 <= saldo <= 50000]
  saldos_altos = [saldo for saldo in saldos if saldo > 50001]
  print("Saldos bajos:", saldos_bajos)
  print("Saldos medios:", saldos_medios)
  print("Saldos altos:", saldos_altos)