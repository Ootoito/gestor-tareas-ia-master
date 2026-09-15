from django.core.management.base import BaseCommand

from dcs.models import (
    Aeronave,
    ContenidoDCS,
    MisionDCS,
    VersionMisionDCS,
)


class Command(BaseCommand):
    help = "Carga el contenido histórico del MiG-29A Fulcrum."

    ENTRENAMIENTO = [
        {
            "numero": 1,
            "titulo": "Entrenamiento: seguimiento de ruta con evaluación de rendimiento",
            "descripcion": "Mapa: Germany (*)",
            "url": "https://mega.nz/file/XnY3HDYZ#WOJ7yVHXNYi3J5YAeXe7CZqGcEqf6fempd34cxcTsbk",
            "versiones": [
                ("Versión nocturna", "https://mega.nz/file/KzgSnRgK#MAXEGhQMu8rnxZeNAuUUeLlAWnj2ulndusP9-EjhznY"),
                ("Versión con mal tiempo", "https://mega.nz/file/CiJwTbhR#mq56GI--SvPtG3tGelCmYrjAmlqUPuK79C5exXXTHTk"),
            ],
        },
        {
            "numero": 2,
            "titulo": "Entrenamiento: seguimiento de ruta con evaluación (policía aérea)",
            "descripcion": "Mapa: Germany (*)",
            "url": "https://mega.nz/file/XqRgnTBZ#O5KVaD1va7FRMt4wZTKK5PWYVjoqcpEj5Hwy546Royk",
            "versiones": [
                ("Versión nocturna", "https://mega.nz/file/2jB00QoY#i01wUTB55PYcfssoZ0Nt-tPCZZ6SAt3-ni5aMqdnlok"),
                ("Versión con mal tiempo", "https://mega.nz/file/zvQjCRST#Ijp2T1TYI7QCWRj5B80wjT-hLJRFGoaZg7hdrxqQKf4"),
            ],
        },
        {
            "numero": 3,
            "titulo": "Entrenamiento: seguimiento de ruta e interceptación de avión enemigo (policía aérea, sin combate)",
            "descripcion": "Mapa: Germany (*)",
            "url": "https://mega.nz/file/qrJF0Tga#kECWdqmIkRIervq7W6HTNPG-OOPOI4ICV8ADM02d_lI",
            "versiones": [],
        },
        {
            "numero": 4,
            "titulo": "Misión de policía aérea. Siga el briefing. Debe ser capaz de formar con un aparato a corta distancia (<300 metros)",
            "descripcion": "Mapa: Germany (*)",
            "url": "https://mega.nz/file/Kv5j3QRD#t2BI0H9876D6SzHNRzqp6mwf9h9nzj3rfgDx-ZTe-wU",
            "versiones": [],
        },
        {
            "numero": 5,
            "titulo": "Misión de aterrizaje de precisión. Pista improvisada. RSBN y PRMG disponibles (no obligatorios)",
            "descripcion": "Mapa: Germany (*)",
            "url": "https://mega.nz/file/Kuwx2CBA#iNmR2Hcxe_DgIVqOlTS678hszz6hfGkK8Pk-uuHEO3E",
            "versiones": [
                ("Versión nocturna", "https://mega.nz/file/yvYUxa5Q#jAEMwqv9G8OWkSw5bYbYjT-PUu2IRYxig8Vdpw1b7jQ"),
            ],
        },
        {
            "numero": 6,
            "titulo": "Entrenamiento en el empleo del radar",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/GuYE0SzJ#zbpnyQqDriHpDgUS-MF6bLbao30_O5FcAMlb5l-IRBA",
            "versiones": [
                ("Versión nocturna", "https://mega.nz/file/nix2QL6A#XAEUZTh5rQtaq_6EUoolSlEfBLZrb3-lMkuLNgusPW4"),
            ],
        },
        {
            "numero": 7,
            "titulo": "Misión de combate. Interceptación de avión de reconocimiento sin escolta",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/n7h1zShL#GBKLRnIKpfqkgeUScmFoEASpCNZtkcJgJBjKJBOiOq4",
            "versiones": [
                ("Versión con escolta armada", "https://mega.nz/file/aqomnDZA#QiVnmGKJNMrXk743O3EyM5Z_eKk6eRNPigJBtV0KPho"),
            ],
        },
        {
            "numero": 8,
            "titulo": "Misión de patrulla armada. Defender barcos aliados",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/GjYT0CpS#5xwOeEP7Fs1RUwp7-ZoSEB_zhAZzlI2lcQtEfSR6y2E",
            "versiones": [
                ("Versión con escolta armada", "https://mega.nz/file/fqgAjbpZ#gg4YdCFvkMjaMhI6LVgcAz7OardIvKo4Nuk71lFw9qQ"),
            ],
        },
        {
            "numero": 9,
            "titulo": "Misión de patrulla armada. Defender barcos aliados",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/ruBTRCbJ#ERqsBAnfvznfDvLHLytm8iFkya3DkLMKvUQX6xbCAxk",
            "versiones": [
                ("Versión con escolta armada", "https://mega.nz/file/b7pmQbSI#gmfaqSF_y_rAW1sdlGPodszw09Un7OZMMt9MH33lh48"),
            ],
        },
        {
            "numero": 10,
            "titulo": "Misión de combate. Agitando el avispero",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/qyhgBYLK#d0n_z0IZdfyDWbllggG6ubU6YLNZIA3PxeVYzSb-K3M",
            "versiones": [],
        },
        {
            "numero": 11,
            "titulo": "Misión de combate. Agitando el avispero II. Escolta de bombarderos estratégicos Tu-95 “Oso”",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/6yI0HICY#as3bjgjnRClTue3U4ClrCJyeVWh76eVNKocEKpStWsok",
            "versiones": [],
        },
        {
            "numero": 12,
            "titulo": "Misión de combate. Empleo de armamento aire-tierra: bombas",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/LqYGXLCB#uFQE_WL93ChCwVGIfB7LWUeFLjq27jRoLCxJBZq8xlU",
            "versiones": [
                ("Versión con escolta armada", "https://mega.nz/file/K7wyVAZD#KRzSsjZs8nm-yE63t1RSh-v74DzpBEMGwrC6sGkTs04"),
            ],
        },
        {
            "numero": 13,
            "titulo": "Misión de combate. Ataque a base enemiga protegida (vuelo rasante entre valles)",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/G2A30LQR#hyQYpgXPPEVgPwni-Tq9kY4QHes6cCc45Dtszwi8ye4",
            "versiones": [
                ("Versión con escolta armada", "https://mega.nz/file/GyxAkRIQ#2zvUL6nDWSbHj_6h0paGSZ-yRadJ9AaKlZXU601zd1c"),
            ],
        },
        {
            "numero": 14,
            "titulo": "Misión de combate. Seguiremos a un grupo de Mig29A de la VVS en una misión de patrulla hasta la frontera rusa.",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/ni432Y7L#JfYRLyxTta6wt1XQmgMS2PGc5kkZbev7eqJYUQ-swfQ",
            "versiones": [],
        },
        {
            "numero": 15,
            "titulo": "Misión de combate. Nuestra misión consiste en escoltar a un grupo de MiG-23 en una misión de ataque a tierra.",
            "descripcion": "Mapa: Kola (*)",
            "url": "https://mega.nz/file/T3QGCazC#e4LpJKkAR-Wjdu4GLW9OQanfoLc9kyieltD2O7ZiKrg",
            "versiones": [],
        },
    ]

    CAMPANA = [
        (1, "Ataque a columna blindada etiope", "https://mega.nz/file/2iY0xQqJ#-k_iANzv9rhnehcBNMg6TAk_pvCsmvli7pfdKHZoJ7w"),
        (2, "Ataque a las unidades sobrevivientes del ataque anterior", "https://mega.nz/file/HuJC3LZS#4GCVXgpVQCnqrpFEq5cRpS_YiGD7mM8thHqelen3_Vo"),
        (3, "Dia de patrullas", "https://mega.nz/file/n6AETZqS#-mAd-s9-vL_SEnTPbBINsVRyX474vVSvGKYjBuUK37s"),
        (4, "Ataque a posición de artilleria", "https://mega.nz/file/f7olwBQa#3FZkHk1s_gq4JPkvZs-e4zjrkNXoY9bKOr2f8jZKxpc"),
        (5, "El enemigo ataca la capital", "https://mega.nz/file/L2olWAjT#rpK75ucKeH7k_k-bX4gGyTuGzo6mXTUgdouQWGwfxUc"),
        (6, "Emboscada nocturna", "https://mega.nz/file/ynRBSBAT#WpOSnxUlduo2oWo4ZRrAjrW9MNc_ZIBFIthBE5yDXXU"),
        (7, "Escolta armada", "https://mega.nz/file/aj5XGSRK#-6QdPIfXZ4-pl8b3GqmIsVlksWKO3eURLKQBYCMaTSM"),
        (8, "Ataque naval", "https://mega.nz/file/ivAA3L4Z#5CHaxteUJ8m_N3worAE2ezuiBj1vPyxQKVFW0BG226w"),
    ]

    SITUACION_ERITEA = (
        "Corre el año 1998 las fuerzas eriteas han declarado su independencia "
        "desde 1993 pero la via armada no habia sido una opcion, los ultimos "
        "acontecimientos ha precipitado la situacion y finalmente, los rebeldes "
        "eriteos han tomando bajo su mando gran parte del norte y el este de "
        "Etiopia quedando bajo su control toda la salida de este pais al mar "
        "rojo. Tras el golpe inicial, Etiopia ha movilizado sus fuerzas y trata "
        "de avanzar hacia el norte, donde los rebeldes eriteos se han hecho "
        "fuertes.."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="mig-29a-fulcrum",
            defaults={
                "nombre": "MiG-29A Fulcrum",
                "descripcion": "",
                "imagen": "imagenes/mig29a_thumb.jpg",
                "activo": True,
                "orden": 10,
            },
        )

        entrenamiento, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="misiones-entrenamiento",
            defaults={
                "titulo": "Misiones de entrenamiento",
                "tipo": ContenidoDCS.TIPO_MISIONES,
                "descripcion": "Mapa: Germany y Kola (*)",
                "situacion": "",
                "objetivo": "",
                "imagen": "imagenes/mig29aweb.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="campana-eritea-etiopia",
            defaults={
                "titulo": "Campaña de Eritea-Etiopia",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Mapa: Sinai (Mod Massun92-Humans)",
                "situacion": self.SITUACION_ERITEA,
                "objetivo": "Completar la campaña.",
                "imagen": "imagenes/mig29eritea.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._sincronizar_entrenamiento(entrenamiento)
        self._sincronizar_campana(campana)

        self.stdout.write(
            self.style.SUCCESS(
                "MiG-29A cargado correctamente: "
                "2 contenidos, 23 misiones."
            )
        )

    def _sincronizar_entrenamiento(self, contenido):
        numeros_validos = []

        for datos in self.ENTRENAMIENTO:
            numero = datos["numero"]
            numeros_validos.append(numero)

            mision, _ = MisionDCS.objects.update_or_create(
                contenido=contenido,
                numero=numero,
                defaults={
                    "titulo": datos["titulo"],
                    "descripcion": datos["descripcion"],
                    "url_descarga": datos["url"],
                    "activo": True,
                    "orden": numero,
                },
            )

            nombres_validos = []

            for orden, (nombre, url) in enumerate(
                datos["versiones"],
                start=1,
            ):
                nombres_validos.append(nombre)

                VersionMisionDCS.objects.update_or_create(
                    mision=mision,
                    nombre=nombre,
                    defaults={
                        "url_descarga": url,
                        "activo": True,
                        "orden": orden,
                    },
                )

            mision.versiones.exclude(
                nombre__in=nombres_validos
            ).delete()

        contenido.misiones.exclude(
            numero__in=numeros_validos
        ).delete()

    def _sincronizar_campana(self, contenido):
        numeros_validos = []

        for numero, titulo, url in self.CAMPANA:
            numeros_validos.append(numero)

            mision, _ = MisionDCS.objects.update_or_create(
                contenido=contenido,
                numero=numero,
                defaults={
                    "titulo": titulo,
                    "descripcion": "Mapa: Sinai (Mod Massun92-Humans)",
                    "url_descarga": url,
                    "activo": True,
                    "orden": numero,
                },
            )

            # Estas misiones históricas solo tienen versión estándar.
            mision.versiones.all().delete()

        contenido.misiones.exclude(
            numero__in=numeros_validos
        ).delete()
