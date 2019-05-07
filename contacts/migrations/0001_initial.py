# Generated by Django 2.2.1 on 2019-05-07 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealtorImages',
            fields=[
                ('realtImgId', models.AutoField(primary_key=True, serialize=False)),
                ('realtImgUrl', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Realtors',
            fields=[
                ('realtId', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1024)),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.Accounts')),
                ('realtImgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.RealtorImages')),
            ],
        ),
    ]
