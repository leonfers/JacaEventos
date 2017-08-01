import inspect
from enum import Enum


class EscolhaEnum(Enum):
    @classmethod

    def choices(cls):
        # pega todos os membros da classe
        membros = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filtra apenas pelas propriedades
        props = [m for m in membros if not (m[0][:2] == '__')]
        # formata para django tuplas
        escolha = tuple([(str(p[1].value), p[0]) for p in props])
        return escolha

    def name(self):
        """The name of the Enum member."""
        return self._name_

    def value(self):
        """The value of the Enum member."""
        return self._value_