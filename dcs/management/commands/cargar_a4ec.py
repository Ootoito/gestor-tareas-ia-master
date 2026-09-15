from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del A-4E-C."

    MISIONES = [
        (1, 'https://mega.nz/file/WzpA2DCZ#hxKmaaNXbqlGaySDJYsMKSr__2vv80fk0nLU_iwRwj8'),
        (2, 'https://mega.nz/file/H2gjlRzI#590qpCmgSSFLuE7O1CzmfN11rqL6sSkbG7mb33-EcG4'),
        (3, 'https://mega.nz/file/Grw3jJCC#Svp73BEMohRoOZ7Jy-zU_7sXri2yYi1FfSJ20NVP1Bg'),
        (4, 'https://mega.nz/file/Sn5hhI4I#TdqmGyfID32lt16SCM86-JC6Z_pjfX77sj_nBHztsRA'),
        (5, 'https://mega.nz/file/z2xB2Kha#HLcOlqqMBHCDHSWclztdR-seIBGNEWk1rUVdJVaHzqo'),
        (6, 'https://mega.nz/file/zyIFnARJ#yIUNqS2YynOKiNErQiBKt2UiyJ_roZSZF6SFemfzwNM'),
        (7, 'https://mega.nz/file/uyw0TLRJ#U8AqSd9XsuN61Epz-8dPnOXvR1vnOxEGCV6mESTj1f0'),
    ]

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="a-4e-c",
            defaults={
                "nombre": "A-4E-C",
                "descripcion": "Campañas y misiones para el A-4E-C",
                "imagen": "imagenes/a4ec.jpg",
                "activo": True,
                "orden": 70,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="operacion-fragoneta",
            defaults={
                "titulo": "Operación Fragoneta",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el A-4E-C — Vietnam",
                "situacion": (
                    "Desplegados en Vietnam, a los mandos del A4E "
                    "realizaremos misionees de combate"
                ),
                "objetivo": "Briefings en las misiones.",
                "imagen": "imagenes/a4ec.jpg",
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
                "A-4E-C cargado correctamente: 1 campaña, 7 misiones."
            )
        )
