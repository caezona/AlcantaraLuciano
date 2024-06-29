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

# Función para calcular y mostrar estadísticas
def calcular_estadisticas(saldos):
  saldo_mas_alto = max(saldos)
  saldo_mas_bajo = min(saldos)
  saldo_promedio = sum(saldos) / len(saldos)

  # Cálculo de la media geométrica
  media_geometrica = 1
  for saldo in saldos:
    media_geometrica *= saldo
  media_geometrica = pow(media_geometrica, 1/len(saldos))

  print("Saldo más alto:", saldo_mas_alto)
  print("Saldo más bajo:", saldo_mas_bajo)
  print("Saldo promedio:", saldo_promedio)
  print("Media geométrica:", media_geometrica)

# Función para generar reporte de saldos
def generar_reporte(saldos):
  with open("reporte_saldos.csv", "w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Cliente", "Saldo Inicial", "Deduccion Prestamo", "Deduccion Impuestos", "Saldo Neto"])

    for i, saldo in enumerate(saldos):
      deduccion_prestamo = random.randint(1000, saldo // 2)  # Deduccion entre 1000 y la mitad del saldo
      deduccion_impuestos = random.randint(100, 500)  # Deduccion entre 100 y 500
      saldo_neto = saldo - deduccion_prestamo - deduccion_impuestos

      escritor.writerow([i + 1, saldo, deduccion_prestamo, deduccion_impuestos, saldo_neto])

# Función principal
def main():
  saldos = generar_saldos()

  while True:
    print("\nMenú Principal:")
    print("1. Clasificar saldos")
    print("2. Ver estadísticas")
    print("3. Generar reporte de saldos")
    print("4. Salir del programa")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
      clasificar_saldos(saldos)
    elif opcion == 2:
      calcular_estadisticas(saldos)
    elif opcion == 3:
      generar_reporte(saldos)
      print("Reporte generado en el archivo reporte_saldos.csv")
    elif opcion == 4:
      print("¡Muchas gracias por ocupar nuestra aplicación, esperemos que le haya ayudado analizar y gestionar sus datos!")
      break
    else:
      print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()