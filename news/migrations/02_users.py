from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("news", "01_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=200)),
            ],
        ),
    ]
