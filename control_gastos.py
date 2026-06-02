import json
import os

NOMBRE_ARCHIVO = "datos_gastos.json"

def mostrar_menu():
    print("\n--- CONTROL DE GASTOS PERSONALES ---")
    print("1. Agregar Ingreso")
    print("2. Agregar Gasto")
    print("3. Ver Historial de Movimientos")
    print("4. Ver Saldo Actual")
    print("5. Salir")

def solicitar_monto_valido(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            monto = float(entrada)
            if monto <= 0:
                print("❌ El monto debe ser mayor a cero. Intenta de nuevo.")
                continue
            return monto
        except ValueError:
            print("❌ Por favor, ingresa solo números (ej: 1500 o 350.50).\n")

def cargar_datos():
    """Lee el archivo JSON al iniciar. Si no existe, devuelve valores vacíos."""
    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos.get("movimientos", []), datos.get("saldo", 0.0)
        except json.JSONDecodeError:
            print("⚠ Archivo de datos dañado. Iniciando con saldo en cero.")
    return [], 0.0

def guardar_datos(movimientos, saldo):
    """Guarda los movimientos y el saldo en el archivo JSON."""
    datos = {"movimientos": movimientos, "saldo": saldo}
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def ejecutar_sistema():
    # Cargamos lo que estaba guardado antes
    movimientos, saldo = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            print("\n--- AGREGAR INGRESO ---")
            monto = solicitar_monto_valido("Monto del ingreso: $")
            descripcion = input("Descripción: ")
            saldo += monto
            movimientos.append({"tipo": "Ingreso", "monto": monto, "descripcion": descripcion})
            guardar_datos(movimientos, saldo) # Guardado automático
            print(f"¡Ingreso de ${monto} registrado!")

        elif opcion == "2":
            print("\n--- AGREGAR GASTO ---")
            monto = solicitar_monto_valido("Monto del gasto: $")
            descripcion = input("Descripción: ")
            if monto <= saldo:
                saldo -= monto
                movimientos.append({"tipo": "Gasto", "monto": monto, "descripcion": descripcion})
                guardar_datos(movimientos, saldo) # Guardado automático
                print(f"¡Gasto de ${monto} registrado!")
            else:
                print(f"❌ Saldo insuficiente. Tu saldo es: ${saldo}")

        elif opcion == "3":
            print("\n--- HISTORIAL ---")
            if not movimientos:
                print("No hay movimientos registrados.")
            for mov in movimientos:
                print(f"[{mov['tipo']}] {mov['descripcion']}: ${mov['monto']}")

        elif opcion == "4":
            print(f"\n💰 Saldo actual: ${saldo}")

        elif opcion == "5":
            print("\n¡Datos guardados con éxito! Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    ejecutar_sistema()
