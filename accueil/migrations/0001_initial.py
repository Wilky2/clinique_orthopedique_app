# Generated by Django 4.1.7 on 2023-03-10 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('num_patient', models.AutoField(primary_key=True, serialize=False)),
                ('nom_patient', models.CharField(max_length=20)),
                ('prenom_patient', models.CharField(max_length=20)),
                ('adresse_patient', models.CharField(max_length=255)),
                ('no_tel_patient', models.IntegerField()),
                ('date_naissance', models.DateField()),
                ('groupe_sanguin', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('num_responsable', models.AutoField(primary_key=True, serialize=False)),
                ('nom_responsable', models.CharField(max_length=20)),
                ('prenom_responsable', models.CharField(max_length=20)),
                ('adresse_responsable', models.CharField(max_length=255)),
                ('no_tel_responsable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Accompagner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.patient')),
                ('num_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.responsable')),
            ],
        ),
        migrations.AddConstraint(
            model_name='accompagner',
            constraint=models.UniqueConstraint(fields=('num_patient', 'num_responsable'), name='patient_responsable_unique'),
        ),
    ]