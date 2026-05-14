import csv
from django.db import connection

ID_GRUPO = 5
USUARIO_CREADOR = "pcovfue"
ID_AMBITO_FIJO = 11   # <-- PON AQUÍ EL id_ambito real que quieras usar para FECAM

def normalizar_tecnico(nombre):
    if not nombre:
        return None

    nombre = nombre.strip()

    if "Diana/Clara" in nombre:
        return "Diana"

    return nombre


def normalizar_fecha(fecha):
    if not fecha:
        return ""

    fecha = fecha.strip()
    partes = fecha.split("/")

    if len(partes) == 3 and len(partes[2]) == 2:
        return f"{partes[0]}/{partes[1]}/20{partes[2]}"

    return fecha


def buscar_id_estado(nombre_estado):
    sql = """
        SELECT id_estado
        FROM db_admongral.gestor_tareas_tbestados
        WHERE nombre = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [nombre_estado])
        row = cursor.fetchone()

    return row[0] if row else None


def buscar_id_tecnico(nombre_tecnico):
    if not nombre_tecnico:
        return None

    sql = """
        SELECT id_tecnico
        FROM db_admongral.gestor_tareas_tbtecnicos
        WHERE nombre = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [nombre_tecnico])
        row = cursor.fetchone()

    return row[0] if row else None


def importar_fecam(ruta_csv):
    if not ID_AMBITO_FIJO:
        print("❌ Debes indicar un ID_AMBITO_FIJO válido en gestortareas/import_fecam.py")
        return

    with open(ruta_csv, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            fecha = normalizar_fecha((row.get("fecha") or "").strip())
            estado = (row.get("estado") or "Pendiente").strip() or "Pendiente"
            prioridad = (row.get("prioridad") or "Normal").strip() or "Normal"
            tecnico_raw = (row.get("tecnico") or "").strip()
            titulo = normalizar_titulo((row.get("titulo") or "").strip())
            descripcion = (row.get("descripcion") or "").strip()
            usuario_asignado = (row.get("usuario_asignado") or "").strip()

            if not fecha or not titulo:
                print("❌ Saltada fila sin fecha o título:", row)
                continue

            tecnico = normalizar_tecnico(tecnico_raw)
            id_tecnico = buscar_id_tecnico(tecnico)
            id_estado = buscar_id_estado(estado)

            if not id_estado:
                print(f"❌ Estado no encontrado: {estado}. Fila saltada.")
                continue

            if tecnico and not id_tecnico:
                print(f"❌ Técnico no encontrado: {tecnico}. Fila saltada.")
                continue

            sql = """
                INSERT INTO db_admongral.gestor_tareas_tbtareas
                (
                    fecha,
                    id_estado,
                    prioridad,
                    id_ambito,
                    id_tecnico,
                    id_grupo,
                    titulo,
                    descripcion,
                    usuario_creador,
                    usuario_asignado,
                    activa
                )
                VALUES
                (
                    TO_DATE(%s, 'DD/MM/YYYY'),
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    TRUE
                )
            """

            with connection.cursor() as cursor:
                cursor.execute(sql, [
                    fecha,
                    id_estado,
                    prioridad,
                    ID_AMBITO_FIJO,
                    id_tecnico,
                    ID_GRUPO,
                    titulo,
                    descripcion,
                    USUARIO_CREADOR,
                    usuario_asignado if usuario_asignado else tecnico
                ])

            print(f"✔ Insertada: {titulo}")

def normalizar_titulo(titulo):
    if not titulo:
        return ""
    titulo = titulo.strip()
    if len(titulo) > 300:
        print(f"⚠️ Título recortado a 300 caracteres: {titulo[:80]}...")
        return titulo[:300]
    return titulo