from django.db import models


class Periodo(models.Model):
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return self.data_inicio.__str__() + "para " + self.data_fim.__str__()


class Horario(models.Model):
    data = models.DateField("Data inicio", blank=True, null=False)
    hora_inicio = models.TimeField("Hora inicio" , blank=True, null = False)
    hora_fim = models.TimeField("Hora Fim", blank=True, null=False)

    class Meta:
        abstract = True
        verbose_name = 'Horario'
        verbose_name_plural = 'Horario'

    def __str__(self):
        return self.data.__str__() + " de  " + self.hora_inicio.__str__() + " para  " + self.hora_fim.__str__()

class HorarioAtividade(Horario):
    atividade = models.ForeignKey("core.Atividade" ,
                                  verbose_name="Atividade" ,
                                  related_name="Atividade" ,
                                  default="")
    class Meta:
        verbose_name = 'Horario_da_atividdade'
        verbose_name_plural = 'Horarios_da_ativiade '

class Endereco(models.Model):
    class Meta:
        verbose_name ="endereco"