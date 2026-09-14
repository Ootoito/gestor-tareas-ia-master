from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga y sincroniza todo el contenido del Mirage F1"

    def handle(self, *args, **options):

        self.stdout.write("")
        self.stdout.write("===================================")
        self.stdout.write(" CARGA DE DATOS · MIRAGE F1")
        self.stdout.write("===================================")
        self.stdout.write("")

        # ============================================================
        # AERONAVE
        # ============================================================

        mirage, creado = Aeronave.objects.update_or_create(
            slug="mirage-f1",
            defaults={
                "nombre": "Mirage F1",
                "descripcion": (
                    "Misiones, campañas y cursos de entrenamiento "
                    "para el Mirage F1."
                ),
                "imagen": "imagenes/miragef1.png",
                "activo": True,
                "orden": 60,
            },
        )

        if creado:
            self.stdout.write(
                self.style.SUCCESS(
                    "Aeronave creada: Mirage F1"
                )
            )
        else:
            self.stdout.write(
                "Aeronave actualizada: Mirage F1"
            )

        # ============================================================
        # PUMA BLANCO
        # ============================================================

        puma_blanco, creado = ContenidoDCS.objects.update_or_create(
            aeronave=mirage,
            slug="puma-blanco",
            defaults={
                "titulo": "Puma Blanco",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Serie de misiones para el Mirage F1 "
                    "ambientada en el mapa del Cáucaso."
                ),
                "situacion": (
                    'Las tensiones entre Georgia, país donde estamos '
                    'estableciendo lazos de "amistad", y Rusia han '
                    "llegado a un punto muy elevado con la maniobra "
                    "arriesgada de Tiflis de atacar Osetia del Sur, "
                    "que cuenta con protección y tropas de "
                    "pacificación rusas.\n\n"
                    "Esperando una lenta respuesta de Rusia, esta ha "
                    "actuado rápida y ferozmente, avanzando y arrasando "
                    "las tropas que atacaban al sur de Osetia, que "
                    "ahora se encuentran en retirada.\n\n"
                    "La fuerza aérea rusa es muy superior, pero no "
                    "permitiremos que vuelen sin oposición sobre los "
                    "cielos de Georgia."
                ),
                "objetivo": (
                    "Completar una serie de misiones de escolta, "
                    "ataque y transporte táctico bajo presión enemiga."
                ),
                "imagen": "imagenes/miragef1.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Puma Blanco",
        )

        misiones_puma = [
            (
                1,
                "Misión 1",
                "https://mega.nz/file/b2IQEQTC#1vzmaCcfIKkxbv-zs0RwGryabzjbzJqJisVrWqeaNAw",
            ),
            (
                2,
                "Misión 2",
                "https://mega.nz/file/Ti5XhYDI#ubm_nwtclz5DfBvrM-jEveJFDWXPP9v99kzoJeP7J68",
            ),
            (
                3,
                "Misión 3",
                "https://mega.nz/file/ijx3nCLJ#oUayH-SVzJO8JNO3okG_pZt01pvnDZeb-e6Sj4yVpxM",
            ),
            (
                4,
                "Misión 4",
                "https://mega.nz/file/ayBwwY5T#KNJCWXUMEEkNzuMVM5G2LEGvNG8oIl9QDlIom5E2Flo",
            ),
            (
                5,
                "Misión 5",
                "https://mega.nz/file/TmIFBCra#nt45cxq9huGjWHlQnMS0Ms6ie5gRZFpKx6tYGsJgQ24",
            ),
            (
                6,
                "Misión 6",
                "https://mega.nz/file/jjQi1QzC#cl9I6gBFyLOVI2ZDm1lRZ96-PAKhovJpoQ-Nzi5WGLQ",
            ),
            (
                7,
                "Misión 7",
                "https://mega.nz/file/LzwDzaSR#iZRozFChw5ClJYbQkeHWEtJP__nAPFjy6gxM38CyXwk",
            ),
            (
                8,
                "Misión 8",
                "https://mega.nz/file/K3oGjJbT#VAW4e6Mf9NTnAxVKDlRemSidkemaPMqXNBjS2tbcBU8",
            ),
            (
                9,
                "Misión 9",
                "https://mega.nz/file/PnBwAbrA#1koeqKZaMsHUJAOOwrqaTZEonOepEAc0MtD7OU5Hc6Y",
            ),
        ]

        self._sincronizar_misiones(
            puma_blanco,
            misiones_puma,
        )

        # ============================================================
        # AMANECER CARMESÍ
        # ============================================================

        amanecer, creado = ContenidoDCS.objects.update_or_create(
            aeronave=mirage,
            slug="amanecer-carmesi",
            defaults={
                "titulo": "Amanecer Carmesí",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": (
                    "Serie de misiones para el Mirage F1 "
                    "ambientada en las Islas Marianas."
                ),
                "situacion": (
                    "Nuevo destino en las islas Marianas. Aquí estamos, "
                    "mi primer destino de combate. Estoy emocionado aunque "
                    "trato de disimularlo y parecer un eficiente piloto "
                    "de caza de la fuerza aérea, pero mis compañeros "
                    "veteranos hacen bromas y se ríen poniéndome apodos "
                    "infantiles. Todos habrán pasado por esto.\n\n"
                    "Tras llegar y presentarme al comandante me ha "
                    "explicado que la costumbre es realizar unos cuantos "
                    "vuelos de acondicionamiento a la zona, conocer las "
                    "zonas de patrulla, los puntos de notificación y toda "
                    "la teoría que rodea las operaciones en la base.\n\n"
                    "Este destino es el sueño de cualquier piloto recién "
                    "graduado: tranquilo, en unas islas paradisíacas y "
                    "con buen clima."
                ),
                "objetivo": (
                    "Misiones de adiestramiento para la "
                    "familiarización con el Mirage F1CE."
                ),
                "imagen": "imagenes/miragef1a.jpg",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 20,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Amanecer Carmesí",
        )

        misiones_amanecer = [
            (
                1,
                "Misión 1",
                "https://mega.nz/file/LugxnJoS#eac5Pxbt1VhgL36yicQp8PoQUW3jbysgl_PrsSrAYOI",
            ),
            (
                2,
                "Misión 2",
                "https://mega.nz/file/mrBChALZ#b40aYuNbxuaCGDLLSdDXTBh36hKx_9PTEqDQNfREoAU",
            ),
            (
                3,
                "Misión 3",
                "https://mega.nz/file/7n5QjCzb#eohycxxYpLTCw-E5Zl8X90AKQwfJLaRPIVlnU86LDBo",
            ),
            (
                4,
                "Misión 4",
                "https://mega.nz/file/jnRDTTZb#r4uWFnENETypMaZ5wsCH-mcf1VIS11yZQa-I1OZHYG8",
            ),
            (
                5,
                "Misión 5",
                "https://mega.nz/file/rjRmwLyR#VeW9FhV2dPLvcQk9FpLofx8Gvc7YQyGnl4g8eTEQNHA",
            ),
            (
                6,
                "Misión 6",
                "https://mega.nz/file/H7w3ASjB#deKS_2o09taC11M1qJQvkDGrYCJRuqC2E3-qC2_H0u4",
            ),
            (
                7,
                "Misión 7",
                "https://mega.nz/file/73BE0RTQ#1OdttrMV4_j9pEU5NYVcVYwtKpKr684zFgF4vV9FWc4",
            ),
            (
                8,
                "Misión 8",
                "https://mega.nz/file/v642jZrQ#cgewTo4DrCP_8CtWhY-e7tccPRcn2M3xEa7R3exVUHg",
            ),
            (
                9,
                "Misión 9",
                "https://mega.nz/file/PjhXxLID#6Bk1qUyHzVzZhNZJskEDxh8Tu-6pvhLE3ce2S7ClQMU",
            ),
        ]

        self._sincronizar_misiones(
            amanecer,
            misiones_amanecer,
        )

        # ============================================================
        # CURSO DEL MIRAGE F1
        #
        # Datos actualizados a partir de la versión más reciente
        # de miragef1course.html.
        # ============================================================

        curso, creado = ContenidoDCS.objects.update_or_create(
            aeronave=mirage,
            slug="curso-mirage-f1",
            defaults={
                "titulo": "Curso del Mirage F1",
                "tipo": ContenidoDCS.TIPO_CURSO,
                "descripcion": (
                    "Misiones de aprendizaje y repaso del Mirage F1 "
                    "en el mapa del Sinaí."
                ),
                "situacion": (
                    "Las FFAA españolas han sido desplegadas en una "
                    "misión internacional de entrenamiento en Egipto."
                ),
                "objetivo": (
                    "Misiones de adiestramiento para la "
                    "familiarización con el Mirage F1EE."
                ),
                "imagen": "imagenes/cursomiragef1_portada.png",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 30,
            },
        )

        self._mostrar_resultado_contenido(
            creado,
            "Curso del Mirage F1",
        )

        misiones_curso = [
            (
                1,
                "Puesta en marcha. Navegación Tacan.",
                "https://mega.nz/file/yrJ13K5Y#3sbTDCx4Si-c8PaTjua9cnHGBoQDWQLQi9cIA80wID0",
            ),
            (
                2,
                "Navegación Tacan-VOR.",
                "https://mega.nz/file/b6ZBUaSI#ua8XYwe87TXfcMkqV0tgP_QgMMycIJ7qRwITLUsiOuk",
            ),
            (
                3,
                "Navegación puntos de ruta Tacan-VOR.",
                "https://mega.nz/file/viJ21CyB#K26ir6XSzgT2nnxVKzTZsjz6_GV4a5J4stUC1KW-pFs",
            ),
            (
                4,
                "Navegación Tacan condiciones atmosféricas adversas.",
                "https://mega.nz/file/viJ21CyB#K26ir6XSzgT2nnxVKzTZsjz6_GV4a5J4stUC1KW-pFs",
            ),
            (
                5,
                "Navegación Tacan nocturna.",
                "https://mega.nz/file/SqRHCThB#pOJfkD8hCBVTJCrRXZMPqbt666pE8Nscs-KC5iOn56o",
            ),
            (
                6,
                "Ataque a tierra I. Cohetes y cañón.",
                "https://mega.nz/file/SqRHCThB#pOJfkD8hCBVTJCrRXZMPqbt666pE8Nscs-KC5iOn56o",
            ),
            (
                7,
                "Ataque a tierra II. Bombas convencionales",
                "https://mega.nz/file/LvowwYDY#Y60maG0uJLYroC05BMc12C1112tPH6Vo_EwQGW2EotU",
            ),
            (
                8,
                "Ataque a tierra III. Bombardeo en picado",
                "https://mega.nz/file/f7p1VJ5b#-TQBd4kDgWADClGemYeUTQ4jvOdpNOyjg_1w4Qavsr8",
            ),
            (
                9,
                "Ataque a tierra IV. Bombardeo a baja cota",
                "https://mega.nz/file/W3AWAaKS#bUz5wDyDbO94ui2lrfDZDRsW0hpWc-P8yDAUJAvIgLA",
            ),
            (
                10,
                "Reabastecimiento en vuelo.",
                "https://mega.nz/file/T2BRzBYJ#Oo5KAFneZc_eygCIHSnj4OeJ5YuKU8uaguB2mZN-wo8",
            ),
            (
                11,
                "Ataque a tierra V. BLU-107/B Durandal antipista",
                "https://mega.nz/file/zigyFTBS#8t40-i2rBVaeelwcRfmokvce8l5nycVnysrYiFfL3zo",
            ),
            (
                12,
                "Ataque a tierra VI. GBU-12 Guiado láser",
                "https://mega.nz/file/u2QGyACL#dDl0cZB9AIyR0pd3Mufyv-DHfrViKthBEzkOheaKeV0",
            ),
            (
                13,
                "Ataque a tierra VII. GBU-16 Guiado láser",
                "https://mega.nz/file/nq4RxASI#c0r_ZZJuuvV4jJFXiRYmgTFLZcFYdzXdywE568rkdfM",
            ),
            (
                14,
                "Introducción al radar. Localización e identificación de contactos.",
                "https://mega.nz/file/HyA3UL6I#FcM9tU-ipLX-LMmJ4ENdBLySYg3Z39wzqEjnNylW4ik",
            ),
            (
                15,
                "Radar II. Localización e identificación de contactos.",
                "https://mega.nz/file/rip01ZIJ#GBueWREfB4O93yVZLZCPpPvvdSEI7nPMtj8UP9GHAYc",
            ),
            (
                16,
                "Combate aire-aire I. Interceptación",
                "https://mega.nz/file/qrgkXJQI#Wezsuj-8ckAPgxcMUlMzLizDxibgg_e3-4t4Ld3T_QM",
            ),
        ]

        self._sincronizar_misiones(
            curso,
            misiones_curso,
        )

        # ============================================================
        # RESUMEN
        # ============================================================

        total_mirage = MisionDCS.objects.filter(
            contenido__aeronave=mirage,
        ).count()

        self.stdout.write("")
        self.stdout.write("-----------------------------------")
        self.stdout.write(
            self.style.SUCCESS(
                "Mirage F1 sincronizado correctamente."
            )
        )
        self.stdout.write("")

        self.stdout.write(
            "Contenidos Mirage F1: "
            f"{mirage.contenidos.count()}"
        )

        self.stdout.write(
            f"Misiones Mirage F1: {total_mirage}"
        )

        self.stdout.write("-----------------------------------")
        self.stdout.write("")

    def _sincronizar_misiones(
        self,
        contenido,
        misiones,
    ):
        creadas = 0
        actualizadas = 0

        numeros_validos = []

        for numero, titulo, url in misiones:

            numeros_validos.append(numero)

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

        # Elimina misiones antiguas que ya no existan
        # en la versión actual del contenido.
        eliminadas, _ = (
            MisionDCS.objects
            .filter(contenido=contenido)
            .exclude(numero__in=numeros_validos)
            .delete()
        )

        self.stdout.write(
            f"  {contenido.titulo}: "
            f"{creadas} creadas, "
            f"{actualizadas} actualizadas, "
            f"{eliminadas} eliminadas."
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