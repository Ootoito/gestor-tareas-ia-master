from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga los datos iniciales de la sección DCS"

    def handle(self, *args, **options):

        self.stdout.write("")
        self.stdout.write("===================================")
        self.stdout.write(" CARGA INICIAL DE DATOS DCS")
        self.stdout.write("===================================")
        self.stdout.write("")

        # ============================================================
        # HANGAR
        # ============================================================

        aeronaves = [
            {
                "nombre": "MiG-29A Fulcrum",
                "slug": "mig-29a-fulcrum",
                "descripcion": (
                    "Misiones de entrenamiento para este magnífico "
                    "caza de la Guerra Fría."
                ),
                "imagen": "imagenes/mig29a_thumb.jpg",
                "orden": 10,
            },
            {
                "nombre": "Mi-8 Hip",
                "slug": "mi-8-hip",
                "descripcion": (
                    "Misiones de transporte, rescate y apoyo táctico "
                    "en distintos escenarios."
                ),
                "imagen": "imagenes/mi8_thumb.jpg",
                "orden": 20,
            },
            {
                "nombre": "Mi-24 Hind",
                "slug": "mi-24-hind",
                "descripcion": (
                    "Misiones de ataque, escolta y apoyo aéreo cercano "
                    "para el legendario Hind."
                ),
                "imagen": "imagenes/mi24.jpg",
                "orden": 30,
            },
            {
                "nombre": "F/A-18C Hornet",
                "slug": "fa-18c-hornet",
                "descripcion": (
                    "Misiones embarcadas, ataque al suelo "
                    "y operaciones combinadas."
                ),
                "imagen": "imagenes/f18c_thumb.jpg",
                "orden": 40,
            },
            {
                "nombre": "AV-8B Harrier",
                "slug": "av-8b-harrier",
                "descripcion": (
                    "Misiones de despegue vertical y operaciones CAS "
                    "sobre zonas costeras."
                ),
                "imagen": "imagenes/harrier_thumb.jpg",
                "orden": 50,
            },
            {
                "nombre": "Mirage F1",
                "slug": "mirage-f1",
                "descripcion": (
                    "Misiones, cursos de vuelo y operaciones "
                    "para el Mirage F1."
                ),
                "imagen": "imagenes/miragef1.png",
                "orden": 60,
            },
            {
                "nombre": "A-4E-C",
                "slug": "a-4e-c",
                "descripcion": (
                    "Misiones para el módulo comunitario A-4E-C."
                ),
                "imagen": "imagenes/a4ec.jpg",
                "orden": 70,
            },
            {
                "nombre": "UH-1H Huey",
                "slug": "uh-1h-huey",
                "descripcion": (
                    "Misiones para el UH-1H Huey."
                ),
                "imagen": "imagenes/uh1.jpg",
                "orden": 80,
            },
            {
                "nombre": "AJS 37 Viggen",
                "slug": "ajs-37-viggen",
                "descripcion": (
                    "Misiones para el AJS 37 Viggen."
                ),
                "imagen": "imagenes/asj37.jpg",
                "orden": 90,
            },
            {
                "nombre": "AH-64D Apache",
                "slug": "ah-64d-apache",
                "descripcion": (
                    "Misiones para el AH-64D Apache."
                ),
                "imagen": "imagenes/ah64.jpg",
                "orden": 100,
            },
            {
                "nombre": "MiG-19 Farmer",
                "slug": "mig-19-farmer",
                "descripcion": (
                    "Misiones para el MiG-19 Farmer."
                ),
                "imagen": "imagenes/mig19.jpg",
                "orden": 110,
            },
            {
                "nombre": "MiG-21Bis",
                "slug": "mig-21bis",
                "descripcion": (
                    "Misiones para el MiG-21Bis."
                ),
                "imagen": "imagenes/Mig21bis.png",
                "orden": 120,
            },
            {
                "nombre": "F-4E Phantom II",
                "slug": "f4e-phantom-ii",
                "descripcion": (
                    "Misiones, campañas y cursos de entrenamiento "
                    "para el F-4E Phantom II."
                ),
                "imagen": "imagenes/F4EPhantom.png",
                "orden": 130,
            },
            {
                "nombre": "C-130J",
                "slug": "c-130j",
                "descripcion": (
                    "Misiones para el C-130J."
                ),
                "imagen": "imagenes/C130J.png",
                "orden": 140,
            },
            {
                "nombre": "OH-6A",
                "slug": "oh-6a",
                "descripcion": (
                    "Misiones para el mod OH-6A."
                ),
                "imagen": "imagenes/oh-6a.png",
                "orden": 150,
            },
            {
                "nombre": "Su-22M4",
                "slug": "su-22m4",
                "descripcion": (
                    "Misiones para el mod Su-22M4."
                ),
                "imagen": "imagenes/su22m4.png",
                "orden": 160,
            },
        ]

        objetos_aeronave = {}

        for datos in aeronaves:

            slug = datos["slug"]

            aeronave, creado = Aeronave.objects.update_or_create(
                slug=slug,
                defaults={
                    "nombre": datos["nombre"],
                    "descripcion": datos["descripcion"],
                    "imagen": datos["imagen"],
                    "activo": True,
                    "orden": datos["orden"],
                },
            )

            objetos_aeronave[slug] = aeronave

            if creado:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Aeronave creada: {aeronave.nombre}"
                    )
                )
            else:
                self.stdout.write(
                    f"Aeronave actualizada: {aeronave.nombre}"
                )

        # ============================================================
        # F-4E PHANTOM II
        # ============================================================

        f4e = objetos_aeronave["f4e-phantom-ii"]

        # ============================================================
        # PHANTOM FLIGHT SCHOOL
        # ============================================================

        curso, creado = ContenidoDCS.objects.update_or_create(
            aeronave=f4e,
            slug="phantom-flight-school",
            defaults={
                "titulo": "Phantom Flight School",
                "tipo": ContenidoDCS.TIPO_CURSO,
                "descripcion": (
                    "Curso progresivo de entrenamiento para aprender "
                    "a volar y combatir con el F-4E Phantom II."
                ),
                "situacion": (
                    "Destinados en Alemania, iniciaremos un programa "
                    "de entrenamiento destinado a conocer y dominar "
                    "los principales sistemas del F-4E Phantom II."
                ),
                "objetivo": (
                    "Completar las misiones de entrenamiento en orden "
                    "progresivo. Los briefings detallados se encuentran "
                    "incluidos dentro de cada misión."
                ),
                "imagen": "imagenes/PhantomFlightSchool.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Phantom Flight School",
        )

        misiones_curso = [
            (
                1,
                "Puesta en marcha y vuelo simple",
                "https://mega.nz/file/6rgm2YRC#-R_HKkzqBV8Z6oXG4rSfmxAuTykKLB0vhdhBjs1RzSA",
            ),
            (
                2,
                "Vuelo siguiendo puntos de ruta",
                "https://mega.nz/file/rzBRma4L#zx5H-CGg-vyNpDL3U-bzN7zlukbdSxiDelacpyufGeo",
            ),
            (
                3,
                "Vuelo de navegación usando el sistema TACAN",
                "https://mega.nz/file/znwn1KAb#Le09iN6PUHTX3ayj4plTUFyJYRBkU-a6VCQwWVZGfn8",
            ),
            (
                4,
                "Navegación TACAN y aterrizaje de precisión",
                "https://mega.nz/file/q7onSDIY#n5iLhYkj8TtWq9FQO2II8Lpt0daFfR6_N25zarmKKpA",
            ),
            (
                5,
                "Traslado a Peenemünde con mal tiempo",
                "https://mega.nz/file/qrwjRQaL#DThECTo2jLsUOhh4qxcuDH7IqMzI3uwO0l3y4wfE4r0",
            ),
            (
                6,
                "Empleo de armamento: cohetes",
                "https://mega.nz/file/bnJDSYaB#UDRP3Rm2gh0fkiABFUmxpFoGpqrnzILlNEB0GjVMhnk",
            ),
            (
                7,
                "Bombas Mk-82 en modo Direct",
                "https://mega.nz/file/Oj5UkT5S#fgs-hcv7KWdNJC-yXNYebSdKIROQi-OYP-XKBOuVxUg",
            ),
            (
                8,
                "Bombas Mk-83 y Mk-84 en modo Direct",
                "https://mega.nz/file/a6JgFQCA#NpObpUU7MVrg0YV5GsrfDLWOiQSv7J5W1CCZ2_GsqaY",
            ),
            (
                9,
                "Bombas Mk-82 en modo DTOS",
                "https://mega.nz/file/Dj4nzYZB#HkuEA_5Zi7qgubHmGyDmGwB6b_dLLEKJqIOzWShXt3A",
            ),
            (
                10,
                "Bombas Mk-82 DL",
                "https://mega.nz/file/a75mTbyK#wMy2TBBaDqBQPjk1aM-58qgAKAyICb0FkMJ7KOYwq4I",
            ),
            (
                11,
                "Bombas Mk-82 SnakeEye",
                "https://mega.nz/file/vjR31ADI#V3Yg8kOT1LmQcqUjw7IcEdpKfLZ_8o6MmOXyZorQqjA",
            ),
            (
                12,
                "Bombas CBU en lanzamiento LOFT",
                "https://mega.nz/file/GmRDhIwI#4PeWbXqmGiH4P0jOcfOX27hOdmg6wRDkrzN9z8B90jg",
            ),
            (
                13,
                "AGM-65 Maverick",
                "https://mega.nz/file/Cv5VBQxC#EdDY4duPBKFZlq7ZgILvRGXgfubuPLZxPikhSfWl5eM",
            ),
            (
                14,
                "AGM-12 Bullpup",
                "https://mega.nz/file/frg20a4D#i_7PB5j5dg8DGaoz5OXH5iJyiYVyWuGQwZaZwa0mvDY",
            ),
            (
                15,
                "GBU-8 y AGM-62: guiado por TV",
                "https://mega.nz/file/PqoHVCbB#I0vI-h7NSL8x2wChYmsZLRg_Vurgg8HeX8t2mSycmHQ",
            ),
            (
                16,
                "GBU-10, GBU-12 y armamento guiado por láser",
                "https://mega.nz/file/bzQynLZY#gxkrxa0Fzj-uUJY0q5uoZnLQYMdctUX-84AvToYRLEA",
            ),
            (
                17,
                "Combate aire-aire: AIM-7 Sparrow",
                "https://mega.nz/file/724nWbYS#7-JB6PEJUbzj-Io1KChWpdSvZK7ze1uIaove5AwJBAk",
            ),
            (
                18,
                "Combate aire-aire: AIM-7 Sparrow",
                "https://mega.nz/file/DvhCiKzZ#u_2D9IwjSZIuzz0JOFHUNGonYwuqKOXIFbgqtf3x0N4",
            ),
        ]

        self._cargar_misiones(
            curso,
            misiones_curso,
        )

        # ============================================================
        # FUEGO EN EL ESTRECHO
        # ============================================================

        fuego, creado = ContenidoDCS.objects.update_or_create(
            aeronave=f4e,
            slug="fuego-en-el-estrecho",
            defaults={
                "titulo": "Fuego en el Estrecho",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Campaña de combate para el F-4E Phantom II "
                    "ambientada en el Golfo Pérsico."
                ),
                "situacion": (
                    "La tensión en el Golfo Pérsico es cada día más alta. "
                    "Irán está realizando movimientos agresivos contra "
                    "las monarquías árabes aliadas de Estados Unidos "
                    "y Occidente. Sus fuerzas han sido reforzadas con "
                    "sistemas antiaéreos rusos. Destinados en el 36th TFS "
                    "de la USAF, hemos sido desplegados en la zona a la "
                    "espera de los acontecimientos."
                ),
                "objetivo": (
                    "Completar diferentes tipos de misiones de combate. "
                    "Los briefings detallados se encuentran incluidos "
                    "dentro de cada misión."
                ),
                "imagen": "imagenes/fuegoenelestrecho.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Fuego en el Estrecho",
        )

        misiones_fuego = [
            (
                1,
                "Traslado a Kashab",
                "https://mega.nz/file/jiwykRyK#Ab6EuQPpxDi6Uxgv-4qsRfSi0dENRMvkQpwnqRIPO-o",
            ),
            (
                2,
                "Ataque a lanzadores Scud",
                "https://mega.nz/file/3zImFRrT#LXnep9OSBRNS9E5TY7XNgDk4rpTyQqf4HlVVb2UPuV0",
            ),
            (
                3,
                "Ataque a lanzadores Scud",
                "https://mega.nz/file/S7xBHAZY#tmeyr8fTpTRBp3CFSBiTasFe6m7BlgELkQNZMe6PJ-k",
            ),
            (
                4,
                "Interceptar convoy de transporte",
                "https://mega.nz/file/n6x33RCB#lQrU-I7qdAitgUQhqdFW3F6JqLttiVDqFzFV-Qfa59s",
            ),
            (
                5,
                "Apoyo aéreo cercano CAS",
                "https://mega.nz/file/XvZjRL6a#vjcA4WT5j0s66zb2I8uN4IbEJCp5gDX3aP5yhMGEP3A",
            ),
            (
                6,
                "Destruir tren de transporte en puerto enemigo",
                "https://mega.nz/file/D6Y0FBJI#rW-DxaFPCTAbnVfpFzi0nlzxFldgKukZA3LEnzGtW98",
            ),
            (
                7,
                "Ataque nocturno a tren de mercancías",
                "https://mega.nz/file/TuADlLAY#lUsY0nQcQeVVlaeWuBejdw_3f_0LOsv6p71HkYJ4tbY",
            ),
            (
                8,
                "Escolta al grupo Ghost en ataque a base enemiga",
                "https://mega.nz/file/yvJnjJ7K#VgJ_l0FtpECE5bqsG0rks-DJ12Zx6IcjT4f-vwFyrxE",
            ),
        ]

        self._cargar_misiones(
            fuego,
            misiones_fuego,
        )

        # ============================================================
        # PHANTOMS OVER MARIANAS
        # ============================================================

        marianas, creado = ContenidoDCS.objects.update_or_create(
            aeronave=f4e,
            slug="phantoms-over-marianas",
            defaults={
                "titulo": "Phantoms over Marianas",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Campaña para el F-4E Phantom II ambientada "
                    "en las Islas Marianas."
                ),
                "situacion": (
                    "Ha llegado el momento de devolver las islas al "
                    "norte del archipiélago al gobierno chino. Tras el "
                    "fin del acuerdo suscrito cien años atrás, las fuerzas "
                    "occidentales se retiran de Saipan y Tinian."
                ),
                "objetivo": (
                    "Completar todo tipo de misiones. "
                    "Los briefings detallados se encuentran incluidos "
                    "dentro de cada misión."
                ),
                "imagen": "imagenes/phantomsovermarianas.png",
                "estado": ContenidoDCS.ESTADO_DESARROLLO,
                "activo": True,
                "orden": 30,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Phantoms over Marianas",
        )

        misiones_marianas = [
            (
                1,
                "Misión 1",
                "https://mega.nz/file/fjBWDLoC#8NGE7PE3i27FEueLwVn4iS9Y2bAmgaSSeI1fENFHJTs",
            ),
            (
                2,
                "Misión 2",
                "https://mega.nz/file/3ugHRKgR#9DEzCeTg_vQGEjf1BgHvWtsCDmTgWGrswCMkyHv7h0Y",
            ),
            (
                3,
                "Misión 3",
                "https://mega.nz/file/jmZSia6T#ucmL6Gi4yWDAarhboHb0BqNUtCNvUfp8NN_mjDI37FI",
            ),
            (
                4,
                "Misión 4",
                "https://mega.nz/file/XmpWHARC#urkVZtpH8AdCcn756cDJ0eKx6DbRApYBjUSiXilIfKc",
            ),
            (
                5,
                "Misión 5",
                "https://mega.nz/file/6mggjTaI#RGzvZnxkusophb7KNqG9QqAC-eRhyPJ9CtvGzhvDjl4",
            ),
        ]

        self._cargar_misiones(
            marianas,
            misiones_marianas,
        )

        # ============================================================
        # RESUMEN
        # ============================================================

        self.stdout.write("")
        self.stdout.write("-----------------------------------")

        self.stdout.write(
            self.style.SUCCESS(
                "Carga DCS finalizada correctamente."
            )
        )

        self.stdout.write("")

        self.stdout.write(
            f"Aeronaves: {Aeronave.objects.count()}"
        )

        self.stdout.write(
            f"Contenidos: {ContenidoDCS.objects.count()}"
        )

        self.stdout.write(
            f"Misiones: {MisionDCS.objects.count()}"
        )

        self.stdout.write("-----------------------------------")
        self.stdout.write("")

    def _cargar_misiones(self, contenido, misiones):

        creadas = 0
        actualizadas = 0

        for numero, titulo, url in misiones:

            _, creado = MisionDCS.objects.update_or_create(
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

            if creado:
                creadas += 1
            else:
                actualizadas += 1

        self.stdout.write(
            f"  Misiones: {creadas} creadas, "
            f"{actualizadas} actualizadas."
        )

    def _mostrar_resultado_contenido(
        self,
        creado,
        titulo,
    ):

        if creado:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Contenido creado: {titulo}"
                )
            )
        else:
            self.stdout.write(
                f"Contenido actualizado: {titulo}"
            )