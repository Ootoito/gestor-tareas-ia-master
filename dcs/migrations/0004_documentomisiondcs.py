from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("dcs", "0003_versionmisiondcs")]
    operations = [
        migrations.CreateModel(
            name="DocumentoMisionDCS",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                ("descripcion", models.CharField(blank=True, max_length=500)),
                ("url_descarga", models.URLField(max_length=1000)),
                ("activo", models.BooleanField(default=True)),
                ("orden", models.PositiveIntegerField(default=0)),
                ("mision", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="documentos", to="dcs.misiondcs")),
            ],
            options={"ordering": ["orden", "id"], "verbose_name": "Documento de misión DCS", "verbose_name_plural": "Documentos de misiones DCS"},
        ),
    ]
