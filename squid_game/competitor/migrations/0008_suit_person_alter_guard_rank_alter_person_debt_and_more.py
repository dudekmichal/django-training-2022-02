# Generated by Django 4.0.2 on 2022-02-20 15:47

import competitor.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0007_alter_guard_rank_alter_person_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suit',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitor.person'),
        ),
        migrations.AlterField(
            model_name='guard',
            name='rank',
            field=models.CharField(choices=[('C', 'Circle'), ('T', 'Triangle'), ('S', 'Square')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='debt',
            field=models.PositiveBigIntegerField(default=0, validators=[competitor.models.validate_minimal_debt]),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='Unknown', max_length=20, verbose_name='Nazwa gracza'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='profession',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(choices=[('A', 'Alive'), ('D', 'Dead')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='suit',
            name='colour',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green')], default='R', max_length=1),
        ),
    ]
