from django.db import models


class Tecnico(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=20, null=False)
    matricula = models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.nome

class Maquina(models.Model):
    ESTADO_CHOICES = (
        ("Tela queimada", "Tela queimada"),
        ("Mancha na tela", "Mancha na tela"),
        ("Barulho no cooler", "Barulho no cooler"),
        ("Não liga", "Não liga"),
        ("Liga porém não apresenta imagem", "Liga porém não apresenta imagem"),
        ('Lentidão no S.O HD com problemas', "Lentidão no S.O - HD com problemas"),
        ("Botão ligar danificado", "Botão ligar danificado"),
        ("Entrada RJ45 com folga", "entrada RJ45 com folga"),
        ("Não reconhece usb", "Não reconhece usb"),
        ("Porta usb com folga", "Porta usb com folga"),
        ("Problema na entrada usb", "Problema na entrada usb"),
        ("Tela quebrada", "Tela quebrada"),
    )
    MODELO_CHOICES = (
        ("U1500", "U1500"),
        ("U900", "U900"),
        ("U2500", "U2500"),
        ("U950", "U950"),
    )
    modelo = models.CharField(max_length=20, null=False, choices=MODELO_CHOICES)
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES)
    patrimonio = models.CharField(max_length=50, null=False)
    num_serie = models.CharField(max_length=50, null=False)
    ID_chamado = models.CharField(max_length=20, null=False)
    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_serie


class Chamado(models.Model):
    STATUS_CHAMADO_CHOICES = (
        ("ABERTO", "ABERTO"),
        ("FECHADO", "FECHADO"),
        ("PENDENTE", "PENDENTE"),
    )
    num_chamado = models.CharField(max_length=50, null=False)
    protocolo = models.CharField(max_length=50, null=False)
    date_entrada = models.DateField(null=False, verbose_name="Data de entrada")
    date_saida = models.DateField(null=True, verbose_name="Data da baixa")
    status_chamado = models.CharField(max_length=20, choices=STATUS_CHAMADO_CHOICES)
    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
    )
    maquina = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_chamado + " | " + self.status_chamado



