from django.db import models

class InscricoesQuerySet(models.QuerySet):
    use_for_related_fildes = True

    def pago(self):
        return  self.filter(status_inscricao=True)