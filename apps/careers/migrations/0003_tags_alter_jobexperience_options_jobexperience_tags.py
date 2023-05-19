# Generated by Django 4.1.7 on 2023-05-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_remove_certificate_file_certificate_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='jobexperience',
            options={'verbose_name': 'Tags profesional', 'verbose_name_plural': 'Tags profesionales'},
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='tags',
            field=models.ManyToManyField(to='careers.tags', verbose_name='Tags'),
        ),
    ]