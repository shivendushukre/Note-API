# Generated by Django 4.0 on 2022-01-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
