# Explicación De Conceptos Claves

Estructuras de Datos:

Listas: Se utilizan listas para almacenar los saldos de las cuentas, los saldos clasificados (bajos, medios, altos) y las deducciones por préstamo e impuestos.

Funciones:

Definición y uso de funciones: El código define cinco funciones con nombres descriptivos que realizan tareas específicas:
generar_saldos(): Crea una lista de 10 saldos aleatorios entre 1000 y 100000.
clasificar_saldos(saldos): Clasifica los saldos en tres categorías: bajos, medios y altos.
calcular_estadisticas(saldos): Calcula y muestra el saldo más alto, el más bajo, el promedio y la media geométrica.
generar_reporte(saldos): Genera un archivo CSV con información sobre cada cliente (saldo inicial, deducciones y saldo neto).
main(): Función principal que controla el flujo del programa y presenta el menú al usuario.
Parámetros y valores de retorno: Las funciones reciben parámetros (listas de saldos) y devuelven valores (listas, estadísticas, informes) según corresponda.
Modularidad: El código está organizado en funciones modulares que permiten una mejor comprensión y reutilización.
media_geométrica de un conjunto de datos, La función primero verifica que el conjunto de datos no esté vacío. Luego, multiplica todos los números del conjunto de datos y eleva el resultado a la potencia del número inverso de la cantidad de números del conjunto de datos. al final, la función devuelve la media geométrica.

Flujo de Control:

for: Se utilizan bucles for para:
Generar 10 saldos aleatorios.
Recorrer listas de saldos.
Escribir datos en un archivo CSV.
Sentencias if-elif-else: Se utilizan sentencias if-elif-else para controlar el flujo del programa en función de las opciones seleccionadas por el usuario en el menú principal.

Manipulación de Datos:

Generación de números aleatorios: Se utiliza la función random.randint() para generar números aleatorios para los saldos, deducciones por préstamo e impuestos.
Cálculo de estadísticas: Se calculan el saldo más alto, el más bajo, el promedio y la media geométrica de los saldos.
