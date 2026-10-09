from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("praktiko", "0011_examen_respuestaexamen_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SesionDemo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("creada_en", models.DateTimeField(auto_now_add=True)),
                ("caduca_en", models.DateTimeField(db_index=True)),
                ("usuario", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="praktiko_sesion_demo", to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "Sesión de demostración", "verbose_name_plural": "Sesiones de demostración"},
        ),
    ]
