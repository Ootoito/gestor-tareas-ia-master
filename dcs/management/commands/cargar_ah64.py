from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del AH-64D Apache."

    MISIONES = [
        (1, 'https://mega.nz/file/v2YDHTYT#2XNg_Xn4Ud3gBjXzr1Q5JSmmRiJ6Q67ivJHoakpxHm0'),
        (2, 'https://mega.nz/file/LqxDXDTQ#R1HHHb0LszwshnIT9mUTsv_eUXlIjVo_ztMKyqRvC5Q'),
        (3, 'https://mega.nz/file/jnQgXRgA#m9QpeYHln8n3NooodW4Ny_5snCuWvPghC7_-Gnde3lc'),
        (4, 'https://mega.nz/file/L6BkDLgQ#ptyjtLnvEu1Vae4pTBvXbfHt8K-G4qgTR1zSS09cwUM'),
        (5, 'https://mega.nz/file/3jQE3AAQ#3hc4-0SQOoqvLPOSjafPRX3xYhk7T2_J9O6aTMd6jZY'),
        (6, 'https://mega.nz/file/C3IGkBiB#MVf0ZZVw3008cWRhXEAn_KcOjMKrqxn9QndJGTp_G9A'),
        (7, 'https://mega.nz/file/Gz4TDJqD#4IhKnmJsL-FpdyFd3iMP71BY_VFEi0y1LHnWt-BuFDs'),
        (8, 'https://mega.nz/file/XjghkTjZ#yZobrJ5LCutNLe1AhJQTbq1F93ZJ8SNOxhldmME9Kwg'),
        (9, 'https://mega.nz/file/evYHhYjQ#fILzhh3guJ4y8i0ZjtCuz6FYYn1_Tu4bH6DOSnKeSRw'),
        (10, 'https://mega.nz/file/PjREUAjJ#tx1oBXTYBaF99TG5QeMUa1WyAx2mHe-JAr8eNVqU9co'),
        (11, 'https://mega.nz/file/TuJhGYZR#K5u8n9jqbQ61zGKTMVoFHQww5r3nTYTJuUZ71rL9mUw'),
    ]

    SITUACION = (
        "Corre el año 2004, los primeros apaches modelo D se incorporan a las "
        "FFAA americanas. Como capitan y jefe de un grupo ha sido destinado a "
        "reemplazar a los AH1 Cobra de la marina desplazados en la base de "
        "Jirah en Siria. Su cometido es controlar el trafico insurgente "
        "vinculado con el terrorismo internacional que amenaza no solo EEUU "
        "sino el resto del mundo. Siria es uno de los principales escondites "
        "de terroristas y traficantes de armas, nuestra misión es evitar el "
        "trafico de armas y golpear al enemigo en cada oportunidad."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="ah-64d-apache",
            defaults={
                "nombre": "AH-64D Apache",
                "descripcion": "Campañas y misiones para el AH-64D Apache",
                "imagen": "imagenes/ah64.jpg",
                "activo": True,
                "orden": 100,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="apaches-en-siria",
            defaults={
                "titulo": "Apaches en Siria",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el AH-64D Apache — Mapa Siria",
                "situacion": self.SITUACION,
                "objetivo": (
                    "Completar todo tipo de misiones. "
                    "Briefings en la propia mision"
                ),
                "imagen": "imagenes/ah64.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        numeros = []
        for numero, url in self.MISIONES:
            numeros.append(numero)
            mision, _ = MisionDCS.objects.update_or_create(
                contenido=campana,
                numero=numero,
                defaults={
                    "titulo": f"Misión {numero}",
                    "descripcion": "",
                    "url_descarga": url,
                    "activo": True,
                    "orden": numero,
                },
            )
            mision.versiones.all().delete()

        campana.misiones.exclude(numero__in=numeros).delete()

        self.stdout.write(
            self.style.SUCCESS(
                "AH-64D Apache cargado correctamente: 1 campaña, 11 misiones."
            )
        )
