# Generated by Django 2.2 on 2019-10-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_modelblog_url_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('correo', models.EmailField(default='', max_length=200)),
                ('mensaje', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
