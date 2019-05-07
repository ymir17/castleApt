# Generated by Django 2.2.1 on 2019-05-07 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropImages',
            fields=[
                ('imgId', models.AutoField(primary_key=True, serialize=False)),
                ('propImgUrl', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zipCode', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('size', models.FloatField()),
                ('price', models.FloatField()),
                ('imgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PropImages')),
                ('realtId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Realtors')),
            ],
        ),
    ]