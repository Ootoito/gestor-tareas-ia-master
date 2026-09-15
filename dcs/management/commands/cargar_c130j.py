from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del C-130J."

    MISIONES = [
        (1, 'https://mega.nz/file/2qhlkKTZ#-ZZhAxZsWcY6fakscm8EKPBRCUaLVeFOw7bkUs0wTaM'),
        (2, 'https://mega.nz/file/Wig1xZzB#Cq6tqouX-BMbVG067dtpPlo0-SFaMl3bF63C5NlfWdo'),
        (3, 'https://mega.nz/file/jixWiCwZ#_wi8mImrqxkWYXhFzLCuCSkg0KxxXEfLLETJE8oBdzE'),
    ]

    SITUACION = (
        "Ha llegado el amargo momento de devolver las islas al norte del "
        "archipielago al gobierno chino. Tras el fin del acuerdo suscrito "
        "100 años atras, las fuerzas de occidentales se retiran de Saipan "
        "y Tinian, dejando el territorio en manos del gobierno chino."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="c-130j",
            defaults={
                "nombre": "C-130J",
                "descripcion": "Campañas y misiones para el C-130J",
                "imagen": "imagenes/C130J.png",
                "activo": True,
                "orden": 140,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="phantoms-over-marianas-adaptacion-c130j",
            defaults={
                "titulo": "Phantoms over Marianas adaptación C130J",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Adaptación de Phantoms over Marianas para el C-130J "
                    "— Mapa Islas Marianas"
                ),
                "situacion": self.SITUACION,
                "objetivo": (
                    "Completar todo tipo de misiones. Briefings en la propia "
                    "mision. CAMPAÑA INCOMPLETA"
                ),
                "imagen": "imagenes/C130J.png",
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
                "C-130J cargado correctamente: "
                "1 campaña incompleta, 3 misiones."
            )
        )
