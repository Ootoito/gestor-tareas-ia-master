from django.core.management.base import BaseCommand
from dcs.models import Aeronave, ContenidoDCS, MisionDCS, VersionMisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del Su-22M4 Fitter."

    ENTRENAMIENTO = [
        (1, 'Entrenamiento: seguimiento de ruta con evaluación de rendimiento', [('Descargar version diurna', 'https://mega.nz/file/D2hU0KxR#PLo0zM1vj7pQZObhUrMbT1ZYXkZMV4akZPzw8OhqFbQ'), ('Descargar version nocturna', 'https://mega.nz/file/7upAFQyQ#IfzKChF1n69aWG62rdPfFgBdueAIRxtrV-pkdgMeuys')]),
        (2, 'Entrenamiento: seguimiento de ruta con reconocimiento', [('Descargar', 'https://mega.nz/file/DqJl2LbJ#rlCqNbYyzfIuMKwQthEG9um_4ETE8qEEAboRFiHPlps')]),
        (3, 'Entrenamiento: Poligono de tiro con blancos blandos sin AAA (bombas y armas sin guiado)', [('Descargar', 'https://mega.nz/file/j2BWjSKQ#GNelxsU07JzadTUTRzA5t66GFmlFmbDL3ihEBxxrBu0')]),
        (4, 'Entrenamiento: Navegación y reconocimiento', [('Descargar', 'https://mega.nz/file/S3ZVxS5J#aevCF4Bm-ZatpCdgPUOEcvW9N2ne2CzhRKh0p83bhs8')]),
        (5, 'Entrenamiento: Poligono de tiro con blancos blandos sin AAA (cohetes no guiados)', [('Descargar', 'https://mega.nz/file/u3hUjTAa#kBIJXFHgQ43_Qec_mTIZ3RE1tSnkIy3ReeFr8JW_TsA')]),
        (6, 'Entrenamiento: Poligono de tiro con blancos blandos sin AAA (cohetes S25L guiados)', [('Descargar', 'https://mega.nz/file/23JxHRII#hHblRyKyN2UQVdGQS1c7ZrYR6JzDT2CcXjYDnYrjbtk')]),
        (7, 'Entrenamiento: Poligono de tiro con blancos blandos sin AAA (bombas de racimo columnas de vehiculos)', [('Descargar', 'https://mega.nz/file/23JxHRII#hHblRyKyN2UQVdGQS1c7ZrYR6JzDT2CcXjYDnYrjbtk')]),
        (8, 'Entrenamiento: SEAD. Mision para el entrenamiento del empleo de misiles antiradar Kh25UP y Kh58U', [('Descargar', 'https://mega.nz/file/Hvo1EaBI#fhXQdFjJziUQUGg957wqQksq5-hV_CZxiI_okjzmlEI')]),
    ]

    HAMA = [
        (1, 'Ataque a convoy que avanza hacia Hama.', [('Descargar .miz', 'https://mega.nz/file/u6YmHASY#h8tabR7G_a1PWEQoBy4Mck9HQiLmdUA0btlkyLltYzU')]),
        (2, 'Continuamos el ataque sobre convoy enemigo avanzando hacia Hama.', [('Descargar .miz', 'https://mega.nz/file/i6ZQFB5S#oTwBb9USNHMOiNDKdqAoo49MJqMzCvzn72dM1p4FVIQ')]),
        (3, 'La artilleria enemiga esta a distancia de tiro ¡Destruyalos!', [('Descargar .miz', 'https://mega.nz/file/nzYRXYTY#6Jb2P00aO9Kg569kByl0gssrJQpk9NBL0C68XP5oRG4')]),
        (4, 'Cortar la cabeza de la serpiente', [('Descargar .miz', 'https://mega.nz/file/qjQXHY6a#FBel-lo1XZ2tPo3PZTt-Zi30h9zoK3WeCfPkGCvE-mQ')]),
        (5, 'Columna de suministros', [('Descargar .miz', 'https://mega.nz/file/X6gk1K6K#WwZlyL76st0QqiEVVBUUgiQKkNl6evX2RaSxahngpjU')]),
        (6, 'Mision SEAD', [('Descargar .miz', 'https://mega.nz/file/WqIk3IhT#6T7LKeXfAEzAlwAXvI0rPS9ZUsaytG3kqSd2MTARz9E')]),
        (7, 'Mision CAS', [('Descargar .miz', 'https://mega.nz/file/G6RgCb7B#XSDzqw20lxtnsVcIT-UvU_2zNOjSddK0RQU9QwrFN8o')]),
        (8, 'Mision MARTILLO DE HIERRO', [('Descargar .miz', 'https://mega.nz/file/yjAC0ThL#j68Zp_7sDRBAvgUUc_Yh_kPdC5J0QiR4hvpg1BPq7UQ')]),
    ]

    def sincronizar(self, contenido, datos):
        numeros = []
        for numero, titulo, enlaces in datos:
            numeros.append(numero)

            # El primer enlace se conserva como descarga principal histórica.
            principal_nombre, principal_url = enlaces[0]
            mision, _ = MisionDCS.objects.update_or_create(
                contenido=contenido,
                numero=numero,
                defaults={
                    "titulo": titulo or f"Misión {numero}",
                    "descripcion": "",
                    "url_descarga": principal_url,
                    "activo": True,
                    "orden": numero,
                },
            )

            # Las variantes adicionales se almacenan como VersionMisionDCS.
            nombres_version = []
            for orden, (nombre, url) in enumerate(enlaces[1:], start=1):
                nombre = nombre.replace("Descargar ", "").strip()
                if not nombre:
                    nombre = f"Versión {orden + 1}"
                nombres_version.append(nombre)
                VersionMisionDCS.objects.update_or_create(
                    mision=mision,
                    nombre=nombre,
                    defaults={
                        "url_descarga": url,
                        "activo": True,
                        "orden": orden,
                    },
                )
            if nombres_version:
                mision.versiones.exclude(nombre__in=nombres_version).delete()
            else:
                mision.versiones.all().delete()

        contenido.misiones.exclude(numero__in=numeros).delete()

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="su-22m4",
            defaults={
                "nombre": "Su-22M4 Fitter",
                "descripcion": "Campañas y misiones para el Su-22M4 Fitter",
                "imagen": "imagenes/Su22M4.webp",
                "activo": True,
                "orden": 160,
            },
        )

        entrenamiento, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="misiones-entrenamiento",
            defaults={
                "titulo": "Misiones de entrenamiento",
                "tipo": ContenidoDCS.TIPO_MISIONES,
                "descripcion": "Entrenamiento del Su-22M4 Fitter — Mapa Germany",
                "situacion": "",
                "objetivo": "",
                "imagen": "imagenes/su22m4.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        hama, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="operacion-hama",
            defaults={
                "titulo": "Operación Hama",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el mod Su-22M4 Fitter — Mapa Siria",
                "situacion": (
                    "Junio 2015. Las fuerzas del ISIS avanzan inparables hacia "
                    "la ciudad siria de Hama. Apoyados por el ejercito de "
                    "liberación sirio, a su vez patrocinado por los "
                    "estadounidenses, los terroristas del ISIS han conseguido "
                    "avances al este de Siria. Ahora su ofensiva hacia la "
                    "historica ciudad de Hama parece imparable."
                ),
                "objetivo": (
                    "Completar una serie de misiones de ataque para el "
                    "Su22M4 sirio"
                ),
                "imagen": "imagenes/Su22Hama.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self.sincronizar(entrenamiento, self.ENTRENAMIENTO)
        self.sincronizar(hama, self.HAMA)

        self.stdout.write(self.style.SUCCESS(
            "Su-22M4 Fitter cargado correctamente: "
            "2 contenidos, 16 misiones (8 entrenamiento + 8 Operación Hama)."
        ))
