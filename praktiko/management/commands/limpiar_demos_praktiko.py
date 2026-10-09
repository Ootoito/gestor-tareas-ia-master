"""Eliminar SOLO cuentas registradas explícitamente como demostraciones."""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from praktiko.models import SesionDemo


class Command(BaseCommand):
    help = "Borra las cuentas de demostración caducadas y sus datos asociados."

    def add_arguments(self, parser):
        parser.add_argument("--confirmar", action="store_true", help="Ejecuta el borrado; sin esta opción solo informa.")

    def handle(self, *args, **options):
        ids = list(SesionDemo.objects.filter(caduca_en__lte=timezone.now()).values_list("usuario_id", flat=True))
        self.stdout.write(f"Cuentas demo caducadas: {len(ids)}")
        if not options["confirmar"]:
            self.stdout.write("Simulación. Usa --confirmar para ejecutar.")
            return
        # No borrar si un usuario temporal ha obtenido privilegios administrativos.
        from django.contrib.auth import get_user_model
        User = get_user_model()
        with transaction.atomic():
            qs = User.objects.filter(pk__in=ids, is_staff=False, is_superuser=False)
            n = qs.count()
            qs.delete()
        self.stdout.write(self.style.SUCCESS(f"Cuentas eliminadas: {n}"))
