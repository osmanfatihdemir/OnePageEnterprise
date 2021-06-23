# Generated by Django 3.2.4 on 2021-06-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('Text', models.TextField(verbose_name='Metin')),
            ],
        ),
        migrations.CreateModel(
            name='Section2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('Text', models.TextField(verbose_name='Metin')),
            ],
        ),
        migrations.CreateModel(
            name='Section3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Text', models.TextField(verbose_name='Metin')),
            ],
        ),
        migrations.CreateModel(
            name='Section4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Text', models.TextField(verbose_name='Başlık')),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Görsel Açıklaması'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Slider Adı'),
        ),
    ]