from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del AV-8B Harrier."

    MISIONES = [
        (1, 'https://mega.nz/file/uzhnSC5T#JDCwiTcmbioVWa840vjVvFhHTuxp2mLVz6AbiIg0acs'),
        (2, 'https://mega.nz/file/f2Qi2QiL#BvtJU4gsP2zCkyYXh2y0BN06xlhICh66NVvUWta-Q_o'),
        (3, 'https://mega.nz/file/XqomSTzb#sJuhnOL8Ts3M5nOMGF-CJ1TZGUh3MtRXCAdaq8MDMig'),
        (4, 'https://mega.nz/file/yyAXyIbI#c2nQM3nWubQIGHdQP1HAgtGx0U9xMY8ZN9A4Ayzbhio'),
        (5, 'https://mega.nz/file/j2QUFDga#WXpmi8-ubescJUnqf8sUCTsU_ezUp2_BuepDgEpnVXE'),
        (6, 'https://mega.nz/file/7i41SDyD#YGmiMaHWGEO1jTiDztTjF2r_mauUBma3ArnChySWHK4'),
        (7, 'https://mega.nz/file/z6RjWYCJ#GyeZcsHVDzHkXDZe6icjjs8PGsIpI1Vnj8GFjymG55A'),
        (8, 'https://mega.nz/file/z2hTRC4b#b0JuCk3ZjvuQp3XEyOrZv58OtpRCP084yaMcDqTU-qI'),
        (9, 'https://mega.nz/file/3mYGBQhJ#i3yKyGL5ZYqQZSRtTjgpy_esZaJYHzMrTVg-Tn6vvv0'),
        (10, 'https://mega.nz/file/KzAjQT5I#4cxf0_DaQN5el05x_tf61BMpJHUXOdk0mosN_vP7QDc'),
    ]

    SITUACION = (
        "Operacion Zorro Blanco. Bokechistan ha invadidoTopovia, desde hace "
        "varios meses el presidente colabora con el estado britanico para "
        "mantener la paz en la zona. En coordinacion con fuerzas sublevadas "
        "del ejercio topovita han tomado en un primer golpe casi la totalidad "
        "de la isla, escapando el presidente y su grupo de gobierno en una "
        "arriesgada mision de evacuacion a primeras horas de hoy. El objetivo "
        "de la operacion Zorro Blanco, es restablecer en el gobierno al "
        "presidente elegido democraticamente y apoyar a las fuerzas que le "
        "son leales en la isla. El grupo de combate esta formado por varios "
        "barcos de apoyo asi como por los portaaviones ligeros Fe, Esperanza "
        "y Caridad y el portaaviones Vison."
    )

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="av-8b-harrier",
            defaults={
                "nombre": "AV-8B Harrier",
                "descripcion": "Campañas y misiones para el AV-8B Harrier",
                "imagen": "imagenes/harrier_thumb.jpg",
                "activo": True,
                "orden": 50,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="operacion-zorro-blanco",
            defaults={
                "titulo": "Operación Zorro Blanco",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el AV-8B Harrier",
                "situacion": self.SITUACION,
                "objetivo": "Completar todo tipo de misiones. Briefings en la propia mision",
                "imagen": "imagenes/harrier_thumb.jpg",
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
                "AV-8B Harrier cargado correctamente: 1 campaña, 10 misiones."
            )
        )
