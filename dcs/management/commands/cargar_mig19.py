from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del MiG-19 Farmer."

    MISIONES = [
        (1, 'https://mega.nz/file/DqggCb5I#kKV6AJY0xTLfiTtgFgQivFGgH1hPLRABIOtZQZTospo'),
        (2, 'https://mega.nz/file/zmgnlByT#DyB4qfWxsccrqqmGKTqPKB08e6iHb1XXqw5XJMgBzXo'),
    ]

    SITUACION = (
        "Egipto 1965. Las relaciones con el, aún reciente estado de Israel, "
        "no son buenas. Los aviones de patrulla israelies continuamente "
        "violan el espacio aereo de la disputada zona de la peninsula del "
        "Sinai bajo el control del gobierno de Egipcio. Hemos sido deplegados "
        "cerca de la frontera con el estado de Israel en un intento de detener "
        "y hacer retroceder a las fuerzas israelies en la zona."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="mig-19-farmer",
            defaults={
                "nombre": "MiG-19 Farmer",
                "descripcion": (
                    "Campañas y misiones para este increíble aparato "
                    "de la era soviética"
                ),
                "imagen": "imagenes/mig19.jpg",
                "activo": True,
                "orden": 110,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="halcones-del-sinai",
            defaults={
                "titulo": "Halcones del Sinaí",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el MiG-19 — Mapa Sinaí",
                "situacion": self.SITUACION,
                "objetivo": (
                    "Completar todo tipo de misiones. Briefings en la propia "
                    "mision. CAMPAÑA INCOMPLETA"
                ),
                "imagen": "imagenes/mig19.jpg",
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
                "MiG-19 Farmer cargado correctamente: "
                "1 campaña incompleta, 2 misiones."
            )
        )
