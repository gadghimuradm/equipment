# Generated by Django 4.2 on 2023-05-02 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Наименование')),
                ('mask', models.CharField(max_length=32, verbose_name='Маска серийного номера')),
            ],
            options={
                'verbose_name': 'тип оборудования',
                'verbose_name_plural': 'типы оборудования',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=32, verbose_name='Серийный номер')),
                ('note', models.TextField(blank=True, default='', verbose_name='Примечание')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='api.equipmenttype', verbose_name='Тип оборудования')),
            ],
            options={
                'verbose_name': 'оборудование',
                'verbose_name_plural': 'оборудование',
            },
        ),
    ]
