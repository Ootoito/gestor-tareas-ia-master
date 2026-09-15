from django.core.management.base import BaseCommand
from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del F/A-18C Hornet."

    ISLAND_SPEAR = [
        (1, 'https://mega.nz/file/ni4j1L4L#WaiiaAye5wFALghMPhgNr0m4nVB_Q7IVPlF9Za6GcW0'),
        (2, 'https://mega.nz/file/LjglgL6Z#YU8w9mhGtN0WBt8SJFvz2moN3mapwMmkXyPPtqsg2Zs'),
        (3, 'https://mega.nz/file/jvADkD6Q#YSRf6ZIzTTl5gqbS65Z1iz9dNLByiRnUg8KsbfhI6bo'),
        (4, 'https://mega.nz/file/LqxEgAiD#fuWqVIVGVdTSBTzS_9pS2Tm97akAWpLiOvCvQJ9gNpM'),
        (5, 'https://mega.nz/file/LvhlnZpL#MpiukGudbZ8uQGNxTKVXm0S4o7UDND_1dR7LVyP23Ps'),
        (6, 'https://mega.nz/file/C2Y1wKxb#UiEbD7PVhi9hGJnKms6xUsfO6MlyUPyR45uFp9USR7Y'),
        (7, 'https://mega.nz/file/rqAFiRLQ#XsH_runiFN2NgYQCdsm4lDFq0Edrp0Y2F0LUZXS2L_E'),
        (8, 'https://mega.nz/file/rjpRzAxQ#Jng1qLYw0Bq7L2LHXY7PV5jknbELvb5TJLbjce_QQVQ'),
        (9, 'https://mega.nz/file/mn5F0KJb#Dx8PxdzschwoYI91XuvQvVX9ySKk0nmJwY8KheGU2R0'),
        (10, 'https://mega.nz/file/zqAw3bDR#olLZfjZwve9BRMDDO5N5DoOgj_orXNphrZelpR7Fdk4'),
        (11, 'https://mega.nz/file/PjJQELIK#VEoG4-nP3kcAzEorkI_MUh9hDoNvEOsAqLJ_KwHOS3k'),
    ]

    ISLAND_SPEAR_MP = [
        (1, 'https://mega.nz/file/XiYWQCbQ#41lqYkWtYX6j8Mq7oOHB2eWPkzMgGYn8GGn3bMD0u08'),
        (2, 'https://mega.nz/file/z2BGkQrI#93cQvZ5lNdUmZgdYedA7dWIY1cnXYzVi8cutRRuqIGs'),
        (3, 'https://mega.nz/file/Kq5xhLzT#pHtzmFQcjPq7bIeeNa5KK0VKB9I_BICMfOtcrZMHI7A'),
        (4, 'https://mega.nz/file/i7R3AYDT#vql6dqHHmmC3SKetmDuvORPLVei0fi5ydgy-RnJfFQM'),
        (5, 'https://mega.nz/file/qvITiSSK#GvoFn1CJRQAwGpyLPgsqlQgGnPHxsAD5dC4Z5iOb_R8'),
        (6, 'https://mega.nz/file/Oqgi0DxB#LzON6Nr9Xjlg4r2_4grRirT0QdhV5Jm2XTTBbpS2BtU'),
        (7, 'https://mega.nz/file/nz53QYiJ#pjkNqgwaxmfPnZTml7yUh6TbTSo_fyDMCQx-noHB5T0'),
    ]

    # Enlaces generales existentes en la página histórica. El modelo actual
    # no dispone de campos de descarga/instrucciones a nivel de campaña, por
    # lo que no se fuerzan dentro de MisionDCS.
    CAMPANA_COMPLETA_URL = 'https://mega.nz/file/Kyh0wKKY#wE7HusMcho5ufcLf5JWUJIdKqNsmmJA4u8uqmXsMoZU'
    INSTRUCCIONES_URL = 'https://mega.nz/file/GvwCBZrY#gF_NDiDVWL1WxmskYEab72Vy-v4AENai44LfNLTd058'

    SITUACION = (
        "Un general rebelde, General Viktor Sokolov, ha liderado un golpe "
        "militar en Guam. Con apoyo de mercenarios y sistemas SAM de origen "
        "ruso, ha tomado el control del sur de la isla y amenaza el tráfico "
        "naval del Pacífico occidental."
    )

    OBJETIVO = (
        "Task Force 78, con un grupo de portaaviones para restaurar el "
        "control del archipiélago"
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="fa-18c-hornet",
            defaults={
                "nombre": "F/A-18C Hornet",
                "descripcion": "Campañas y misiones para el F/A-18C Hornet",
                "imagen": "imagenes/f18c_thumb.jpg",
                "activo": True,
                "orden": 40,
            },
        )

        individual, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="island-spear",
            defaults={
                "titulo": "Operation Island Spear",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el F/A-18C Hornet — Mapa Islas Marianas",
                "situacion": self.SITUACION,
                "objetivo": self.OBJETIVO,
                "imagen": "imagenes/DragonSpear1.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        multiplayer, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="island-spear-multiplayer",
            defaults={
                "titulo": "Island Spear Multiplayer (4 jugadores)",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para hasta 4 F/A-18C Hornet — Mapa Islas Marianas",
                "situacion": self.SITUACION + " Campaña de misiones para hasta 4 F18C en multiplayer",
                "objetivo": self.OBJETIVO,
                "imagen": "imagenes/DragonSpear1.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._sync(individual, self.ISLAND_SPEAR)
        self._sync(multiplayer, self.ISLAND_SPEAR_MP)

        self.stdout.write(
            self.style.SUCCESS(
                "F/A-18C Hornet cargado correctamente: "
                "2 campañas, 18 misiones (11 individual + 7 multiplayer)."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Nota: la descarga ZIP de la campaña completa y las instrucciones "
                "de instalación no se importan todavía porque el modelo actual "
                "no tiene enlaces a nivel de contenido."
            )
        )

    def _sync(self, contenido, datos):
        numeros = []
        for numero, url in datos:
            numeros.append(numero)
            mision, _ = MisionDCS.objects.update_or_create(
                contenido=contenido,
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

        contenido.misiones.exclude(numero__in=numeros).delete()
