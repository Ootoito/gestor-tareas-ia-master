from pathlib import Path

INPUT_FILE = "tareas.txt"
OUTPUT_FILE = "migracion_gestor_tareas.sql"

SCHEMA = "db_admongral"
TABLA_TAREAS = f"{SCHEMA}.gestor_tareas_tbtareas"
TABLA_ESTADOS = f"{SCHEMA}.gestor_tareas_tbestados"
TABLA_AMBITOS = f"{SCHEMA}.gestor_tareas_tbambitos"
TABLA_TECNICOS = f"{SCHEMA}.gestor_tareas_tbtecnicos"
TABLA_GRUPOS = f"{SCHEMA}.gestor_tareas_tbgrupos"

GRUPO_POR_DEFECTO = "General"
PRIORIDAD_POR_DEFECTO = "Normal"


def sql_escape(value: str) -> str:
    if value is None:
        return ""
    return value.replace("'", "''").strip()


def canonical_estado(estado: str) -> str:
    e = (estado or "").strip().lower()

    mapping = {
        "pendiente": "Pendiente",
        "pte de hacer": "Pendiente",
        "pte. de hacer": "Pendiente",
        "pendiente de firma": "Pendiente de firma",
        "pte. de firma": "Pendiente de firma",
        "programada": "Programada",
        "urgente": "Urgente",
        "completada": "Completada",
        "hecho": "Completada",
    }

    return mapping.get(e, estado.strip() or "Pendiente")


def canonical_ambito(ambito: str) -> str:
    a = (ambito or "").strip().lower()

    mapping = {
        "rehabilitacion": "Rehabilitacion",
        "rehabilitación": "Rehabilitacion",
        "seflogic": "Seflogic",
        "sicoin": "Sicoin",
        "otros": "Otros",
        "otro": "Otros",
    }

    return mapping.get(a, ambito.strip() or "Otros")


def canonical_tecnico(tecnico: str) -> str:
    t = (tecnico or "").strip().lower()

    mapping = {
        "jose ramón": "Jose Ramón",
        "jose ramon": "Jose Ramón",
        "jclaher": "Jose Ramón",
        "diana": "Diana",
        "dmormarb": "Diana",
        "jose ramón / diana": "Jose Ramón / Diana",
        "jose ramon / diana": "Jose Ramón / Diana",
        "diana / jose ramón": "Jose Ramón / Diana",
        "diana / jose ramon": "Jose Ramón / Diana",
    }

    return mapping.get(t, tecnico.strip())


def parse_line(line: str):
    parts = line.rstrip("\n").split(";")

    if len(parts) < 7:
        return None

    try:
        tarea_id = int(parts[0].strip())
    except ValueError:
        return None

    fecha = parts[1].strip()
    estado = canonical_estado(parts[2].strip())
    ambito = canonical_ambito(parts[3].strip())
    tecnico = canonical_tecnico(parts[4].strip())
    titulo = parts[5].strip()
    descripcion = ";".join(parts[6:]).strip()

    return {
        "id": tarea_id,
        "fecha": fecha,
        "estado": estado,
        "ambito": ambito,
        "tecnico": tecnico,
        "titulo": titulo,
        "descripcion": descripcion,
    }


def build_insert(t):
    fecha = sql_escape(t["fecha"])
    estado = sql_escape(t["estado"])
    ambito = sql_escape(t["ambito"])
    tecnico = sql_escape(t["tecnico"])
    titulo = sql_escape(t["titulo"])
    descripcion = sql_escape(t["descripcion"])
    grupo = sql_escape(GRUPO_POR_DEFECTO)
    prioridad = sql_escape(PRIORIDAD_POR_DEFECTO)

    tecnico_sql = (
        f"(SELECT id_tecnico FROM {TABLA_TECNICOS} WHERE nombre = '{tecnico}')"
        if tecnico
        else "NULL"
    )

    return f"""INSERT INTO {TABLA_TAREAS} (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('{fecha}', 'DD/MM/YYYY'),
    (SELECT id_estado FROM {TABLA_ESTADOS} WHERE nombre = '{estado}'),
    '{prioridad}',
    (SELECT id_ambito FROM {TABLA_AMBITOS} WHERE nombre = '{ambito}'),
    {tecnico_sql},
    (SELECT id_grupo FROM {TABLA_GRUPOS} WHERE nombre = '{grupo}'),
    '{titulo}',
    '{descripcion}',
    TRUE
);"""


def main():
    input_path = Path(INPUT_FILE)
    output_path = Path(OUTPUT_FILE)

    if not input_path.exists():
        print(f"No existe el fichero de entrada: {input_path}")
        return

    tareas = []
    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tarea = parse_line(line)
            if tarea:
                tareas.append(tarea)

    sql_lines = []
    sql_lines.append("-- ===============================================")
    sql_lines.append("-- Migración de tareas.txt a PostgreSQL")
    sql_lines.append("-- ===============================================")
    sql_lines.append("BEGIN;")
    sql_lines.append("")

    for t in tareas:
        sql_lines.append(build_insert(t))
        sql_lines.append("")

    sql_lines.append("COMMIT;")
    sql_lines.append("")

    output_path.write_text("\n".join(sql_lines), encoding="utf-8")

    print(f"Tareas leídas: {len(tareas)}")
    print(f"SQL generado en: {output_path.resolve()}")


if __name__ == "__main__":
    main()