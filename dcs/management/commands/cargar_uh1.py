from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del UH-1H Huey."

    MISIONES = [
        (1, 'https://mega.nz/file/bvQlTLyZ#1bmox6-i6QsWRmVtSfybUEW_PkgfEm5hY0V1Gk8YO4g'),
        (2, 'https://mega.nz/file/36Q1gCIA#zY9hYGnxBy_dlnQ8FcEoFWXgeljpGvlubVX9JDjqCiA'),
        (3, 'https://mega.nz/file/Wr5j0LBK#NDn-1eXkH6v14hmf2E4cheLS6_LWzASeRwIo6YKVq5k'),
        (4, 'https://mega.nz/file/6igFFbpL#H5nzFmOHot5XZJI0BHQezaK2HXZjxjyEKB6pjjaju-g'),
        (5, 'https://mega.nz/file/2qgD1JCS#_VmArq-pZ5TvaQnIMfm-O8DYvfISjuwi6otAzpyGGq4'),
        (6, 'https://mega.nz/file/TyYlEKrI#8wVyFGPafEaWvirhp6ELmlNai0-XijTnAj88r7uBMyg'),
        (7, 'https://mega.nz/file/634VDTSQ#Bxp-V128xV6yvC57lnMKKcCOkQYO8hDGpPEN77h0h68'),
        (8, 'https://mega.nz/file/fi5jXDJC#V32_ZJZjeWRq9ipJo6WjpTlyM-0JXIJUvWGvzxTSx8Y'),
        (9, 'https://mega.nz/file/yiwUQRYI#xBoDq5D6prOMwvxpPuad-u5hhtXvwTDdPQd04p4Afrs'),
        (10, 'https://mega.nz/file/umZAGKxS#sGQEXsKAUyXn6yQ2SWoqlJQWpidgCjYdc242ASXK8EY'),
        (11, 'https://mega.nz/file/jnQQGQKT#m655VJ7j3Zw1hm0T3gvftr3FZ092sH-Qr9aU4RgUa5c'),
    ]

    MISIONES_MULTI = [
        (1, 'https://mega.nz/file/O6ACFbTa#y1slS6F7fzWj4sSU4xRV7JHa9Sn1w8pqkpBpVlEcT00'),
        (2, 'https://mega.nz/file/O7pVCZ7a#iznOKCqDZ-vPkPsU-sCe1xk_nuueCb54vrPTseyUmA0'),
        (3, 'https://mega.nz/file/iqwh3DJI#L64YgxGHvwo91MDjFCc44xssX_fcm1YidcB-PzOdFSY'),
        (4, 'https://mega.nz/file/W7BxzIhR#iSKbt234rjDJKYqbOFO2443xvHI4cjKu5wLmELOPZ6o'),
        (5, 'https://mega.nz/file/33YQBKDL#1JpvHILsVZdkxniHvylkmOMr7mzzufBnzrPzmVqwUmE'),
        (6, 'https://mega.nz/file/f2ZTkR5L#AYZZ1hxAm-EvQ8IrdzCMbvXBTwqGc6ONJ1RQHLhoybE'),
        (7, 'https://mega.nz/file/CmRGBKzD#skRm7DthizHAf8S3JyeBauTfXyobA1WObNbrtc3LBiM'),
        (8, 'https://mega.nz/file/fjRDGaBY#fazxvE7oOIHRuZPLuMKnziJAhmGzAurVGL7L1O5mPm0'),
        (9, 'https://mega.nz/file/bnAVFbwA#5cCGsntuuS9X5Uo7k9BEH8rmmSIJMnfCd3Yc-oceVJw'),
        (10, 'https://mega.nz/file/amp2mD7C#LVBqHvYwwiXjbVA57YOBpnRmuAOqYfqdKgni9PRpoqg'),
        (11, 'https://mega.nz/file/euhikZBA#32jwVIXvGry_j1fOCzHbA44NVGULgEY_I-ms6XzzDXg'),
    ]

    SITUACION = (
        "Desplegados en Akinostan, exrepublica sovietica donde los asesores "
        "españoles realizan una misión internacional"
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="uh-1h-huey",
            defaults={
                "nombre": "UH-1H Huey",
                "descripcion": "Campañas y misiones para el UH-1H Huey",
                "imagen": "imagenes/uh1.jpg",
                "activo": True,
                "orden": 80,
            },
        )

        individual, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="operacion-vmc",
            defaults={
                "titulo": "Operación VMC",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Campaña ficticia. Destacamento español de helicopteros "
                    "UH1 desplegados en el Caucaso en una misión internacional"
                ),
                "situacion": self.SITUACION,
                "objetivo": "Briefings en las misiones.",
                "imagen": "imagenes/uh1.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        multiplayer, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="operacion-vmc-multiplayer",
            defaults={
                "titulo": "Operación VMC MULTIPLAYER hasta 4 UH-1",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Campaña ficticia multiplayer para un grupo de hasta "
                    "4 UH-1 desplegados en el Cáucaso."
                ),
                "situacion": self.SITUACION,
                "objetivo": "Briefings en las misiones.",
                "imagen": "imagenes/uh1.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._sync(individual, self.MISIONES)
        self._sync(multiplayer, self.MISIONES_MULTI)

        self.stdout.write(
            self.style.SUCCESS(
                "UH-1H Huey cargado correctamente: "
                "2 campañas, 22 misiones (11 individual + 11 multiplayer)."
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
