# Generated by Django 4.1.7 on 2023-05-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_about_description_alter_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='whatsapp',
            field=models.URLField(default='', verbose_name='Whatsapp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion acerca de'),
        ),
    ]