import csv
import os

def login():
    password = input("Introduce la contraseña para acceder a la agenda: ")
    if password != "1234":  # puedes cambiar la contraseña
        print("❌ Contraseña incorrecta.")
        exit()

if __name__ == "__main__":
    login()
    main()

TAREAS_CSV = "tareas.csv"

def cargar_tareas():
    tareas = []
    if os.path.exists(TAREAS_CSV):
        with open(TAREAS_CSV, newline='', encoding='utf-8') as f:
            lector = csv.reader(f)
            tareas = list(lector)
    return tareas

def guardar_tareas(tareas):
    with open(TAREAS_CSV, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerows(tareas)

def mostrar_menu():
    print("\nAGENDA SEGURA")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Marcar tarea como hecha")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            for i, tarea in enumerate(tareas):
                estado = "✔" if tarea[1] == "hecha" else "✘"
                print(f"{i + 1}. {tarea[0]} [{estado}]")
        elif opcion == "2":
            nombre = input("Escribe la nueva tarea: ")
            tareas.append([nombre, "pendiente"])
            guardar_tareas(tareas)
            print("✅ Tarea añadida.")
        elif opcion == "3":
            num = int(input("Número de la tarea hecha: ")) - 1
            if 0 <= num < len(tareas):
                tareas[num][1] = "hecha"
                guardar_tareas(tareas)
                print("✅ Tarea marcada como hecha.")
        elif opcion == "4":
            num = int(input("Número de la tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                tareas.pop(num)
                guardar_tareas(tareas)
                print("🗑️ Tarea eliminada.")
        elif opcion == "5":
            print("Hasta luego 👋")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()
