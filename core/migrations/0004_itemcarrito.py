from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_usuario_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemCarrito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.PositiveIntegerField(default=1)),
                ("agregado_en", models.DateTimeField(auto_now_add=True)),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.producto",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items_carrito",
                        to="core.usuario",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="itemcarrito",
            constraint=models.UniqueConstraint(
                fields=("usuario", "producto"),
                name="unique_producto_por_usuario_carrito",
            ),
        ),
    ]
