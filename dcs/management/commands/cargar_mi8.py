from django.core.management.base import BaseCommand

from dcs.models import Aeronave, ContenidoDCS, MisionDCS


class Command(BaseCommand):
    help = "Carga el contenido histórico del Mi-8 Hip."

    SITUACION = (
        "La pequeña república de Akichistan, situada en la frontera "
        "ruso-ucraniana, disputa desde su independencia una tensa relación "
        "con el gobierno de Kiev. Ucrania nunca ha reconocido la independencia "
        "de la población de Akichistan, de mayoría rusa, y por lo tanto ha "
        "bloqueado fuertemente su frontera, dejando como única salida económica "
        "y social del país las angostas y tortuosas carreteras de las montañas "
        "que le separan de Rusia.\n\n"
        "El presidente del país, Igor Bokerov, ha sido atacado cuando regresaba "
        "a la capital; sin embargo, y gracias a su destreza militar, ha "
        "conseguido salir indemne del ataque. Al parecer, los atacantes son "
        "militares descontentos con su política y que han iniciado un golpe de "
        "Estado justo después de conocer la noticia del fracaso del magnicidio.\n\n"
        "La frontera con Rusia ha sido completamente bloqueada por las fuerzas "
        "que apoyan a los sublevados, que se dirigen rápidamente hacia la "
        "capital tratando de impedir una respuesta de Bokerov.\n\n"
        "Un pequeño grupo de helicópteros de transporte y combate rusos, que "
        "llegaron esa misma noche —se sospecha que los servicios de inteligencia "
        "rusos conocían el posible ataque—, ha quedado aislado dentro de "
        "Akichistan en una base provisional utilizada para maniobras militares. "
        "Cuatro helicópteros de combate Kamov Ka-50 y cuatro Mi-8 de transporte "
        "han sido dispuestos por el gobierno ruso para apoyar a las fuerzas "
        "leales a Bokerov."
    )

    MISIONES = [
        (
            1,
            'Evacuación del personal “consular” ruso',
            'Evacuación urgente de personal diplomático ruso de la capital ante el intento de golpe de estado.',
            'https://mega.nz/file/67RVRLaT#-0tlH__WZ-xOYJD2UYOCaUXSQz8ChbUB0Oc2NWvsNRY',
        ),
        (
            2,
            'Búsqueda y destrucción de artillería enemiga',
            'Localiza y neutraliza las baterías Grad que bombardean la capital de Akichistan.',
            'https://mega.nz/file/GugTnSAT#pMwCj3vR0eBdvP6qr1R4amW2N7zZ9jsJGkDctuMmxuo',
        ),
        (
            3,
            'Reconquistando terreno a los sublevados',
            'Apoya el avance de las fuerzas leales recuperando posiciones estratégicas.',
            'https://mega.nz/file/6mQTjSgC#H6o3tE4-_F3SPVczsT5bF3xm8aaZratDnt-h0-HIwvU',
        ),
        (
            4,
            'Acorralando a los sublevados de la capital',
            'Coordina el cerco sobre las fuerzas rebeldes que aún resisten en la capital.',
            'https://mega.nz/file/zjhXTQbC#26C4hSIRpGQfACyuZUU_9emcG52t6eRdqMv_lqkxZSQ',
        ),
        (
            5,
            'Liberando la capital',
            'Operación final para recuperar el control total de la ciudad de Akichistán.',
            'https://mega.nz/file/O2ZlxYJY#spdcWVbEKjq8FuJna9cLzeuLd_VOuTEgMRFXqaTxSW4',
        ),
        (
            6,
            'Persiguiendo al enemigo en las montañas',
            'Apoya a las unidades que avanzan hacia las montañas para eliminar focos de resistencia.',
            'https://mega.nz/file/X2hQUAbJ#rmdcCv6HFRkPUfx4yg2G3f-jUKP7VUj4l8Wa-tYfwmo',
        ),
        (
            7,
            'Localizar y destruir asesores ucranianos',
            'Localiza a los asesores extranjeros que coordinan las acciones rebeldes.',
            'https://mega.nz/file/rno3XIKA#lABb2puyt_g1SObME3SA3YWCWSKiulVZg4JW_Jq6apk',
        ),
        (
            8,
            'Detener a los comandantes rebeldes',
            'Captura o neutraliza a los cabecillas sublevados para cortar la cadena de mando.',
            'https://mega.nz/file/X7QQ1bja#4loMfWFi69N65qlJhflUTDSPRf3mXWTn-Wsaxajmfyg',
        ),
        (
            9,
            'Regreso del presidente a la capital',
            'Última operación: escolta aérea y seguridad en el retorno de Igor Bokerov a la capital.',
            'https://mega.nz/file/qihxnCba#9kd-4561xSTB1AbeVo7wg9biCfFjxzAricnuWUrcXDs',
        ),
    ]

    def handle(self, *args, **options):
        aeronave, _ = Aeronave.objects.update_or_create(
            slug="mi-8-hip",
            defaults={
                "nombre": "Mi-8 Hip",
                "descripcion": "",
                "imagen": "imagenes/mi8_thumb.jpg",
                "activo": True,
                "orden": 20,
            },
        )

        campana, _ = ContenidoDCS.objects.update_or_create(
            aeronave=aeronave,
            slug="akichistan",
            defaults={
                "titulo": "Akichistan",
                "tipo": ContenidoDCS.TIPO_CAMPANA,
                "descripcion": "AKICHISTAN CRISIS",
                "situacion": self.SITUACION,
                "objetivo": "",
                "imagen": "",
                "estado": ContenidoDCS.ESTADO_PUBLICADO,
                "activo": True,
                "orden": 10,
            },
        )

        numeros_validos = []

        for numero, titulo, descripcion, url in self.MISIONES:
            numeros_validos.append(numero)

            mision, _ = MisionDCS.objects.update_or_create(
                contenido=campana,
                numero=numero,
                defaults={
                    "titulo": titulo,
                    "descripcion": descripcion,
                    "url_descarga": url,
                    "activo": True,
                    "orden": numero,
                },
            )

            # El HTML histórico de Akichistan solo contiene una
            # descarga estándar para cada misión.
            mision.versiones.all().delete()

        campana.misiones.exclude(numero__in=numeros_validos).delete()

        self.stdout.write(
            self.style.SUCCESS(
                "Mi-8 Hip cargado correctamente: "
                "1 campaña, 9 misiones."
            )
        )
