from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del MiG-21Bis."

    MISIONES = [
        (1, 'https://mega.nz/file/H34jFaoR#nhgcPfa3zwCt8Wo-BX5mtai5Jb8znWHaUv1O83VuDh4'),
        (2, 'https://mega.nz/file/ijRSgJqL#CgKOer6j8Mo6N8zEKTJ44wdYnBJ5abZlgrF0vFRg1jc'),
        (3, 'https://mega.nz/file/XyZ0QKSD#0WONAbt89Gx-ICEnEvmNnOZ9SZP2VouowYTurly1j9g'),
        (4, 'https://mega.nz/file/uywAjTzR#eg5M5xLduI0HNu1aABqlbQckVF3lj31Q-72BdCW_iwE'),
        (5, 'https://mega.nz/file/umQRXC6K#d5kMrI7mJkQ2oFBRD7922cs05abKpWKeSHYeNCuWhD4'),
        (6, 'https://mega.nz/file/bz4QwY5L#cDBu4cNB_pKGRdYIzdCwAR_wxUNW9WtHNgj3U2PcxqA'),
        (7, 'https://mega.nz/file/avxkUDhQ#5eQhs9lO660xu8ucTczuy3PxsOo1l4ihe34IooE_ptI'),
        (8, 'https://mega.nz/file/v2xDmQ7Z#XvYGhdZ09Ct-wVELohE9SUKi-bN60hrG0cJbiGaIO5U'),
    ]

    # Se conserva literalmente la situación de la página de campaña histórica.
    # Ojo: no coincide con el resumen del índice mig21bis.html.
    SITUACION = (
        "Egipto 1965. Las relaciones con el, aún reciente estado de Israel, "
        "no son buenas. Los aviones de patrulla israelies continuamente violan "
        "el espacio aereo de la disputada zona de la peninsula del Sinai bajo "
        "el control del gobierno de Egipcio. Hemos sido deplegados cerca de la "
        "frontera con el estado de Israel en un intento de detener y hacer "
        "retroceder a las fuerzas israelies en la zona."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="mig-21bis",
            defaults={
                "nombre": "MiG-21Bis",
                "descripcion": (
                    "Campañas y misiones para este increíble aparato "
                    "de la era soviética"
                ),
                "imagen": "imagenes/Mig21bis.png",
                "activo": True,
                "orden": 120,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="eritea-vs-egipto",
            defaults={
                "titulo": "Eritea vs Egipto",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el MiG-21Bis — Mapa Sinaí",
                "situacion": self.SITUACION,
                "objetivo": (
                    "Completar todo tipo de misiones. Briefings en la propia "
                    "mision. CAMPAÑA INCOMPLETA"
                ),
                "imagen": "imagenes/Mig21bis.png",
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
                "MiG-21Bis cargado correctamente: "
                "1 campaña incompleta, 8 misiones."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Aviso histórico: el resumen de mig21bis.html describe "
                "Eritrea/Etiopía en 1998, pero la página de campaña "
                "mig21Eritea.html contiene Egipto/Israel en 1965. "
                "Se ha conservado la página de campaña sin corregirla."
            )
        )
