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

class Observador(models.Model):

    observado = models.ForeignKey("utils.Observador" ,
                                  verbose_name = 'Observador' ,
                                  related_name = 'Observador' ,
                                  default="")


    def atualizar(self):
        return "sobrescreva"

class Notificador(Observador):

    class Meta:
        verbose_name = 'Notificador'
        verbose_name_plural = 'notificadores '

    def atualizar(self, msg):
        "enviar email para usuarios da atividade"
        return true

class Observado(models.Model):

    def addObservador(self, observador):
        observador.observado = self
        return true

    def removeObservador(self, observador):
        observador.observado = null
        return  true

    def notificar(self, msg):
        for observador in self.Observador:
            observador.atualizar(msg)

class MsgFactory():

    def gerar_msg_simples(self, atributo):
        msg = MsgSimples()
        msg.atual = String(atributo)
        return msg

    def gerar_msg_completa(self, atributo):
        msg = MsgCompleta()
        msg.atual = String(atributo)
        msg.data = datetime.now()
        return  msg




class MsgSimples(models.Model):
    atual = models.TextField(default="")
    def __str__(self):
        return "novo " + self.atual +"."


class MsgCompleta(MsgSimples):
    data = models.DateTimeField(null=False)
    anterior = models.TextField(default="")

    def __str__(self):
        return "Data :" + self.data + " Estado antigo :" + self.anterior + " Estado atual :" + self.atual +"."





