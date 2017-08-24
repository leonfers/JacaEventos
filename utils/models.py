from django.db import models
from localflavor.br.br_states import STATE_CHOICES

class Periodo(models.Model):
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return self.data_inicio.__str__() + " para " + self.data_fim.__str__()


class Endereco(models.Model):
    pais = models.TextField(blank=True, null=False)
    cidade = models.TextField(blank=True, null=False)
    bairro = models.TextField(blank=True, null=False)
    logradouro = models.TextField(blank=True, null=False)
    numero = models.TextField(blank=True, null=False)
    cep = models.TextField(blank=True, null=False)
    estado = models.TextField(blank=False,null=False)

    def __str__(self):
        return self.pais + '\n' + self.cidade + '\n' + self.bairro + '\n' + self.logradouro + '\n' + self.numero + '\n' + self.cep + '\n' + self.estado


class Horario(models.Model):
    # kasio permitiu data como null
    data = models.DateField("Data inicio", blank=True, null=True)
    hora_inicio = models.TimeField("Hora inicio" , blank=True, null = False)
    hora_fim = models.TimeField("Hora Fim", blank=True, null=False)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horario'

    def __str__(self):
        return self.hora_inicio.__str__() + "  para  " + self.hora_fim.__str__()

class HorarioAtividadeContinua(Horario):
    atividade = models.ForeignKey("core.AtividadeContinua" ,
                                  verbose_name="Atividade" ,
                                  related_name="Atividade" ,
                                  default="")
    class Meta:
        verbose_name = 'Horario_da_atividdade'
        verbose_name_plural = 'Horarios_da_ativiade '

