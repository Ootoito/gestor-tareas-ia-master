from django.core.management.base import BaseCommand
from dcs.models import Aeronave, ContenidoDCS, MisionDCS

class Command(BaseCommand):
    help = "Carga el contenido histórico del OH-6A."

    MISIONES = [
        (1, 'https://mega.nz/file/Lq5WTIDD#1MTpk0A5sf44ege3AZDft7JTWxYi_xhlgDAKjjH5rGs'),
        (2, 'https://mega.nz/file/7z41nZTa#wpQFLuBSA6mXXXn4vG_MDojiMSQOOVgS1ddnTVlHGDg'),
        (3, 'https://mega.nz/file/CrAjRKTI#qkb92jEg6LqCPbk0Z52F4X_8phWgc9ayzOnw26VKYVw'),
        (4, 'https://mega.nz/file/HrxW3RCL#08J6BU7xyDIB3YUU5vpPvVG7aqOYwWZ8tCkybr09S98'),
    ]

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="oh-6a",
            defaults={
                "nombre": "OH-6A",
                "descripcion": "Campañas y misiones para el mod OH-6A",
                "imagen": "imagenes/oh-6a.png",
                "activo": True,
                "orden": 150,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="viernes-negro",
            defaults={
                "titulo": "Viernes Negro",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Berlín, diciembre de 1985. Como piloto de un OH-6A "
                    "del grupo antiterrorista de la policía alemana."
                ),
                "situacion": (
                    "En el rol de un piloto del helicoptero OH-6A de la "
                    "policia antiterrorista alemana."
                ),
                "objetivo": "Completar todo tipo de misiones.",
                "imagen": "imagenes/opviernesnegro.jpg",
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

        self.stdout.write(self.style.SUCCESS(
            "OH-6A cargado correctamente: 1 campaña, 4 misiones."
        ))
        self.stdout.write(self.style.WARNING(
            "Nota histórica: la campaña requiere el mod OH-6A y las misiones "
            "incluyen la skin del GSG 9. Estos recursos adicionales no se "
            "importan aún porque ContenidoDCS no dispone de enlaces de recursos."
        ))
