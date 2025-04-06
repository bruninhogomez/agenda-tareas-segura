import streamlit as st
import csv
import os

TAREAS_CSV = "tareas.csv"

# Cargar tareas
def cargar_tareas():
    if not os.path.exists(TAREAS_CSV):
        return []
    with open(TAREAS_CSV, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

# Guardar tareas
def guardar_tareas(tareas):
    with open(TAREAS_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(tareas)

# App web
def main():
    st.title("📝 Agenda Segura de Tareas")

    # Contraseña (muy básica para esta demo)
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        password = st.text_input("Introduce la contraseña:", type="password")
        if password == "1234":
            st.session_state.autenticado = True
            st.experimental_rerun()
        else:
            st.stop()

    tareas = cargar_tareas()

    # Ver tareas
    st.subheader("📋 Lista de Tareas")
    for i, tarea in enumerate(tareas):
        nombre, estado = tarea
        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            st.write(f"{nombre} {'✔️' if estado == 'hecha' else '❌'}")
        with col2:
            if st.button("Hecha", key=f"h{i}"):
                tareas[i][1] = "hecha"
                guardar_tareas(tareas)
                st.experimental_rerun()
        with col3:
            if st.button("🗑️", key=f"e{i}"):
                tareas.pop(i)
                guardar_tareas(tareas)
                st.experimental_rerun()

    # Añadir nueva tarea
    st.subheader("➕ Añadir Tarea")
    nueva_tarea = st.text_input("Escribe una nueva tarea:")
    if st.button("Añadir"):
        if nueva_tarea:
            tareas.append([nueva_tarea, "pendiente"])
            guardar_tareas(tareas)
            st.success("Tarea añadida.")
            st.experimental_rerun()

if __name__ == "__main__":
    main()
