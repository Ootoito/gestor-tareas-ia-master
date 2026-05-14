import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

TAREAS_FILE = os.path.join(DATA_DIR, "tareas.json")
AMBITOS_FILE = os.path.join(DATA_DIR, "ambitos.json")
TECNICOS_FILE = os.path.join(DATA_DIR, "tecnicos.json")


def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(TAREAS_FILE):
        save_json(TAREAS_FILE, [])

    if not os.path.exists(AMBITOS_FILE):
        save_json(AMBITOS_FILE, ["Rehabilitacion", "Seflogic", "Sicoin", "Otros"])

    if not os.path.exists(TECNICOS_FILE):
        save_json(TECNICOS_FILE, ["Jose Ramón", "Diana"])


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_tareas():
    ensure_data_files()
    return load_json(TAREAS_FILE, [])


def save_tareas(tareas):
    save_json(TAREAS_FILE, tareas)


def get_ambitos():
    ensure_data_files()
    return load_json(AMBITOS_FILE, [])


def save_ambitos(items):
    save_json(AMBITOS_FILE, items)


def get_tecnicos():
    ensure_data_files()
    return load_json(TECNICOS_FILE, [])


def save_tecnicos(items):
    save_json(TECNICOS_FILE, items)


def next_tarea_id():
    tareas = get_tareas()
    if not tareas:
        return 1
    return max(t["id"] for t in tareas) + 1


def crear_tarea(titulo, descripcion, estado, ambito, tecnico):
    tareas = get_tareas()
    nueva = {
        "id": next_tarea_id(),
        "titulo": titulo.strip(),
        "descripcion": descripcion.strip(),
        "estado": estado.strip(),
        "ambito": ambito.strip(),
        "tecnico": tecnico.strip(),
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tareas.append(nueva)
    save_tareas(tareas)


def add_catalog_item(path_getter, path_saver, nuevo_valor):
    valor = nuevo_valor.strip()
    if not valor:
        return False, "Valor vacío"

    items = path_getter()
    if valor in items:
        return False, "Ya existe"

    items.append(valor)
    items.sort()
    path_saver(items)
    return True, "OK"