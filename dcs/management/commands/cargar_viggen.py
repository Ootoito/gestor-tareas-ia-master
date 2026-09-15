from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del AJS 37 Viggen."

    MISIONES = [
        (1, 'https://mega.nz/file/mupw3QJa#oAxy9LJq9Em-FrPwBg3AjqRhl1wzGz7bVRZBSLhCkDw'),
        (2, 'https://mega.nz/file/26JxHRoB#VXJJ6PZxU6ED42T9IZNtUhO7h8rpodrBLsWc415oU2I'),
        (3, 'https://mega.nz/file/GuQHXJSS#vOo3LeX_iKtCwaaWrm_VVwE5y0n1cXcok2eg5e0nN_E'),
        (4, 'https://mega.nz/file/XuZUFCwb#wBot1zsMP_Gv0VOWUX_JbgJG62UbIkZv4Nus53wCOOs'),
        (5, 'https://mega.nz/file/n2ZlSITJ#eJcEyBPRfdVOaFcRMcL_PJWYRhliVomXgJQicMo2snQ'),
        (6, 'https://mega.nz/file/OyRznQDJ#9sRrbqPE488ussXq1M_aiZIYlVV8c9-rp9PJuEP-kUs'),
        (7, 'https://mega.nz/file/T6RDXLaY#ro063xSWVw0jNpmCWWBF1s0R8Hwm1mJ0TMlgt_bBkBw'),
        (8, 'https://mega.nz/file/S6pgRZQa#onHOhKD5dfZUUqa2Kb95mtBTlscSGecDrx6wFZ9GyC4'),
        (9, 'https://mega.nz/file/zzBRzYjQ#nWRcjK-99mmnzudm0baZx45o_yjbJhjmW12KSLqQe7Q'),
        (10, 'https://mega.nz/file/unJmXDCS#6D4Mvspi9kAc35Wrw-d6iMVC0xnGtHIVTlOiuX9eQ0k'),
        (11, 'https://mega.nz/file/7qIWRLaA#zrVYlJABTEFwyZsmrrgftoC1A5KhkneKdZjbGXWvbDk'),
        (12, 'https://mega.nz/file/CupjxDCJ#tSpyVeYvdEDUMBfY1ytuLh6F0Y75ZJ7WKpvv53BedOs'),
    ]

    SITUACION = (
        'Desde la base de Kiruna, al norte de Suecia operan en servicio '
        'conjunto con la fuerza aerea noruega el escuadron F10 Anhelholm '
        '"Los fantasmas". Este escuadron está especializado en misiones de '
        'reconocimiento y ataque de fuerzas navales enemigas que pudieran '
        'operar al norte de Noruega y Suecia, especialemente la flota rusa '
        'desplegada en Murskmansk.'
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="ajs-37-viggen",
            defaults={
                "nombre": "AJS 37 Viggen",
                "descripcion": (
                    "Campañas y misiones para este magnífico aparato "
                    "de la Guerra Fría"
                ),
                "imagen": "imagenes/asj37.jpg",
                "activo": True,
                "orden": 90,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="el-kraken",
            defaults={
                "titulo": "El Kraken",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el AJS 37 Viggen — Cáucaso",
                "situacion": self.SITUACION,
                "objetivo": (
                    "Completar todo tipo de misiones. "
                    "Briefings en la propia mision"
                ),
                "imagen": "imagenes/asj37kraken.jpg",
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
                "AJS 37 Viggen cargado correctamente: 1 campaña, 12 misiones."
            )
        )
