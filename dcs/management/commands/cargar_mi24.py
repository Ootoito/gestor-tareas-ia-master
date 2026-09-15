from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS, VersionMisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del Mi-24 Hind."

    GORIACHI = [
        (1, "Misión 1", 'https://mega.nz/file/f7h0lKgQ#j5evRj3etzobsFWFEqP3BcdJcD9-drpO7Hel2brjeQw'),
        (2, "Misión 2", 'https://mega.nz/file/LnIQiTjC#UCTS_7j3iCp1E6ttCyi5F3qXc12Tzb4QUEqcSUVUrlA'),
        (3, "Misión 3", 'https://mega.nz/file/X74jAbCT#7Oj055IaCuu3CY8TZWNj8E_QgJxTWHImEvHksGoBTuE'),
        (4, "Misión 4", 'https://mega.nz/file/zyhyEI6C#XSkkE5uJ42z-59MGyTtcZlaLsxMiPULFAbt1_02A78s'),
        (5, "Misión 5", 'https://mega.nz/file/2zYAUazb#HWbh936WAQyAU2DSfoO3hIIQnBAJlDjfCEiqKWFLF48'),
        (6, "Misión 6", 'https://mega.nz/file/6rIRXIiT#WBn9qRVIU2DmnqgnobDAu-rZiefgQ1CXWFo3eVG6OPU'),
        (7, "Misión 7", 'https://mega.nz/file/yyxzTJ5a#UxiOIi2ZRLyx3eCb55ACKTfaUfVdQaAGQ6EHUfoS948'),
        (8, "Misión 8", 'https://mega.nz/file/irhkjZ5J#CuKGUpySLgb3wopRtIDQnLNkeTolaEVNosW36eJKXwc'),
        (9, "Misión 9", 'https://mega.nz/file/HzIyDDoI#__CrPk33P-CpGZ_k9a1ZxGsvOijDmrCm221oEw9t3T4'),
        (10, "Misión 10", 'https://mega.nz/file/33oEzaxL#J0tqawrz_jme_D3gkw_hHgaqx402nFkS54iPB8VbCSc'),
        (11, "Misión 11", 'https://mega.nz/file/63xkUYrA#aD8A4NK-lTLSY727oQgZjAzrP37dis8p9kvFPPeBbPs'),
        (12, "Misión 12", 'https://mega.nz/file/D7oDAQ6T#n9YDlzLOoBfIA4vCvZys38_uAinxGc5qSnpg5ynjs8Q'),
        (13, "Misión 13", 'https://mega.nz/file/2vJUnYpS#vc5sfiXyRUJAOgBiJjrACC2jnQ2qiCiUUBX83EKPUWA'),
        (14, "Misión 14", 'https://mega.nz/file/fiZwnQJY#2Ane_NntWYxVy7LtXfaS6ckL7JvpwetGXpD1MbPHyaw'),
        (15, "Misión 15", 'https://mega.nz/file/OzgkXbTK#EioycSYAgi5cQFmbV4UxaoabdpNMRxByR6Me5edDC4U'),
    ]

    SIRIA = [
        (1, "Misión 1", 'https://mega.nz/file/7y5ASbgK#2VaVn5ZMSwsrkMWLCJSzqMhCOlY0qpdCWLPsLvAZaCs'),
        (2, "Misión 2", 'https://mega.nz/file/TqxEGDKD#bRn5G7BzXSng1JegvfXC9eQKLZVv36Dg9m_edIFX7TI'),
        (3, "Misión 3", 'https://mega.nz/file/G3RDgKZT#w0k0yr2Fj1WUISj0MTZVGgvDZAs0bpVrLIAnn-_PiRI'),
        (4, "Misión 4", 'https://mega.nz/file/i7ZmRbrJ#On8-eQ9VQxahUBHKSZYN415_0zTCF1dP4chmmYpDRuk'),
        (5, "Misión 5", 'https://mega.nz/file/n6pQVRRS#316PTEIqVajPdD85RSgFlsJcqGSs4peykqMf-2pAhRM'),
        (6, "Misión 6", 'https://mega.nz/file/2n5ikJxa#yqn3DNQYOc63rS0quqkeKK7lOtDJhdC6VFZxsE6yrgI'),
        (7, "Misión 7", 'https://mega.nz/file/TnIWRbgS#Mp_sZqpiYv-PnJuhVX37sODjvEAarWJDJRNahY2PSkk'),
        (8, "Misión 8", 'https://mega.nz/file/Cy5mWKrC#6HKsfmhWjjQyindpEIURZrlmUtipyN3j6DRjBd5BGIc'),
        (9, "Misión 9", 'https://mega.nz/file/r6gB2IYa#oiLGwpR6-qeW7Y5dCKaV6gWhmIDnl2c7XCR6az7TN6Q'),
        (10, "Misión 10", 'https://mega.nz/file/mqoiUQwS#-JlXmNOhyP9BKfD7Q-9xC5A96nzcPxV7MmPKNP9q_r4'),
        (11, "Misión 11", 'https://mega.nz/file/erwzkZQB#-del4dxUVblw1XIo67sSrdf0ZrpS2yu576Yj0NmbT28'),
        (12, "Misión 12", 'https://mega.nz/file/anA2GJLL#DAbW0u03RqGvKje5d0q5cIlzdjvFeH4CW6svQwcZMMA'),
        (13, "Misión 13", 'https://mega.nz/file/yiBQxBbY#9REBQ6OgAB6p2RywB8Ai3PKVvDQUKUjs-jFvWpQwuos'),
        (14, "Misión 14", 'https://mega.nz/file/Gzp3WARI#aaxozs2JLnRNcpNqZgBngtXNqxI3RIi-Pl342TLuRBY'),
        (15, "Misión 15", 'https://mega.nz/file/j64XVSBY#9omUW3MPGQcP8hUqSyI_RXIu-jTo47Jcnw1qIIXpsRo'),
    ]

    SIRIA_MISION_15_ALTERNATIVA = 'https://mega.nz/file/nmoHEZSK#FhVZuVlvl7mzJs3iQ1zXcpNERXl-WARXZtJf91vVXL8'

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="mi-24-hind",
            defaults={
                "nombre": "Mi-24 Hind",
                "descripcion": "Campañas y escenarios para el helicóptero de ataque Hind",
                "imagen": "imagenes/mi24.jpg",
                "activo": True,
                "orden": 30,
            },
        )

        goriachi, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="goriachi-nevo",
            defaults={
                "titulo": "Goriachi Nevo",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el Mi-24 Hind — Operaciones en Europa del Este",
                "situacion": (
                    "La situación entre las exrepúblicas de Akichistan y Bokovia es tensa. "
                    "Bokovia se ha acercado en los últimos años al bando occidental, tratando "
                    "de caer en gracia a sus nuevos patrocinadores de la OTAN. Para ello su "
                    "ejército ha realizado maniobras conjuntas con países de la alianza y ha "
                    "declarado su intención de solicitar el acceso al bloque. Akichistan, sin "
                    "embargo, se ha mantenido fiel a su antiguo régimen y mantiene lazos "
                    "fuertes con Rusia, que ha desplegado fuerzas de paz en la frontera."
                ),
                "objetivo": (
                    "Completar una serie de misiones de escolta, ataque y transporte táctico "
                    "bajo presión enemiga y condiciones meteorológicas severas."
                ),
                "imagen": "imagenes/goriachinevo.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        siria, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="siria-en-llamas",
            defaults={
                "titulo": "Siria en llamas",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "Campaña para el Mi-24 Hind — Operaciones en Siria",
                "situacion": (
                    "Noviembre de 1985. Hemos llegado hace una semana a la frontera con Siria, "
                    "desde aquí partiremos hasta nuestros destinos, acompañaremos a un grupo de "
                    "helicopteros de transporte con infanteria y pertrechos. Llevan toda la "
                    "semana haciendo varios vuelos al día, parece que hay algo de prisa por "
                    "reforzar ciertos puntos, las noticias hablan de una posible insurrección "
                    "de grupos rebeldes radicales. Primera misión. Se supone que saldriamos a "
                    "las 7 de la mañana para evitar el calor, pero la arena, el calor, y en "
                    "general estas tierras barbaras no se llevan bien con nuestras maquinas. "
                    "Los mecanicos no terminan de dar el visto bueno de los aparatos. Finalmente "
                    "el comandante del grupo de escolta, bajo su responsabilidad, ha ordenado "
                    "que saldremos inmediatamente."
                ),
                "objetivo": (
                    "Completar una serie de misiones de escolta, ataque y transporte táctico."
                ),
                "imagen": "imagenes/mi24.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._sync(goriachi, self.GORIACHI)
        self._sync(siria, self.SIRIA)

        # El HTML histórico contiene dos descargas distintas etiquetadas ambas
        # como "Misión 15". No inventamos una misión 16: conservamos la segunda
        # como variante adicional de la misión 15.
        m15 = siria.misiones.get(numero=15)
        if self.SIRIA_MISION_15_ALTERNATIVA:
            VersionMisionDCS.objects.update_or_create(
                mision=m15,
                nombre="Versión alternativa",
                defaults={
                    "url_descarga": self.SIRIA_MISION_15_ALTERNATIVA,
                    "activo": True,
                    "orden": 1,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Mi-24 Hind cargado correctamente: 2 campañas, 30 misiones."
            )
        )

    def _sync(self, contenido, datos):
        numeros = []
        for numero, titulo, url in datos:
            numeros.append(numero)
            mision, _ = MisionDCS.objects.update_or_create(
                contenido=contenido,
                numero=numero,
                defaults={
                    "titulo": titulo,
                    "descripcion": "",
                    "url_descarga": url,
                    "activo": True,
                    "orden": numero,
                },
            )

            # En Goriachi no hay variantes. En Siria se añade después
            # únicamente la segunda descarga histórica de la misión 15.
            mision.versiones.all().delete()

        contenido.misiones.exclude(numero__in=numeros).delete()
