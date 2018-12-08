# Generated by Django 2.0.4 on 2018-04-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_chamado', models.CharField(max_length=50)),
                ('protocolo', models.CharField(max_length=50)),
                ('date_entrada', models.DateField(verbose_name='Data de entrada')),
                ('date_saida', models.DateField(verbose_name='Data da baixa')),
                ('status_chamado', models.CharField(choices=[('ABERTO', 'ABERTO'), ('FECHADO', 'FECHADO'), ('PENDENTE', 'PENDENTE')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(choices=[('U1500', 'U1500'), ('U900', 'U900'),
                ('U2500', 'U2500'), ('U950', 'U950')], max_length=20)),
                ('estado', models.CharField(choices=[('Tela queimada', 'Tela queimada'), ('Mancha na tela', 'Mancha na tela'),
                ('Barulho no cooler', 'Barulho no cooler'), ('Não liga', 'Não liga'), ('Liga porém não apresenta imagem',
                 'Liga porém não apresenta imagem'), ('Lentidão no S.O HD com problemas', 'Lentidão no S.O - HD com problemas'),
                ('Botão ligar danificado', 'Botão ligar danificado'), ('Entrada RJ45 com folga', 'entrada RJ45 com folga'),
                ('Não reconhece usb', 'Não reconhece usb'), ('Porta usb com folga', 'Porta usb com folga'),
                ('Problema na entrada usb', 'Problema na entrada usb'), ('Tela quebrada', 'Tela quebrada')], max_length=20)),
                ('patrimonio', models.CharField(max_length=50)),
                ('num_serie', models.CharField(max_length=50)),
                ('ID_chamado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=20)),
                ('matricula', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='maquina',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tecnico'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Maquina'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tecnico'),
        ),
    ]
