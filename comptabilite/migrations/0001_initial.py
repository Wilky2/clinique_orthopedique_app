# Generated by Django 4.1.7 on 2023-03-10 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarteAssurance',
            fields=[
                ('num_carte_assurance', models.AutoField(primary_key=True, serialize=False)),
                ('date_expiration', models.DateField()),
                ('num_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('num_paiement', models.AutoField(primary_key=True, serialize=False)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('montant', models.FloatField()),
                ('objet_paiement', models.CharField(max_length=50)),
                ('num_carte_assurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comptabilite.carteassurance')),
                ('num_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('num_visite', models.AutoField(primary_key=True, serialize=False)),
                ('date_visite', models.DateField(auto_now_add=True)),
                ('objectif_visite', models.CharField(max_length=255)),
                ('num_paiement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comptabilite.paiement')),
                ('num_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.patient')),
            ],
        ),
    ]
