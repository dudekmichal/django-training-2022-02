# Generated by Django 4.0.2 on 2022-02-20 10:02

import competitor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0005_alter_guard_rank_alter_person_recruitment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[competitor.models.validate_3_digits_number]),
        ),
        migrations.AlterField(
            model_name='guard',
            name='rank',
            field=models.CharField(choices=[('C', 'Circle'), ('S', 'Square'), ('T', 'Triangle')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[competitor.models.validate_positive, competitor.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='person',
            name='debt',
            field=models.PositiveBigIntegerField(blank=True, validators=[competitor.models.validate_minimal_debt]),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=12, validators=[competitor.models.validate_phone_number_format]),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[competitor.models.validate_minimal_weight]),
        ),
        migrations.AlterField(
            model_name='suit',
            name='colour',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green')], default='R', max_length=1),
        ),
    ]