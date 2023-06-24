from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Motos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('Boleta', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.ForeignKey(on_delete=models.CASCADE, to='ventas.Usuario')),
                ('Producto', models.ManyToManyField(blank=True, related_name='Producto', to='ventas.Producto')),
            ],
        ),
<<<<<<< HEAD
    ]
=======
    ]
>>>>>>> egenau
