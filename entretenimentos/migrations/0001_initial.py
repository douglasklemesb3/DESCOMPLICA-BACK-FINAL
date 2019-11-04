# Generated by Django 2.2.6 on 2019-11-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entretenimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=10)),
                ('idade', models.IntegerField()),
                ('dataNascimento', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=12)),
                ('sexo', models.CharField(choices=[('---', '---'), ('M', 'Masculino'), ('F', 'Feminino'), ('ND', 'Não Definido')], max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('numero_de_recidencia', models.CharField(max_length=255)),
                ('periodo', models.CharField(choices=[('---', '---'), ('M', 'Manha'), ('T', 'Tarde'), ('N', 'Noite')], max_length=255)),
            ],
        ),
    ]
