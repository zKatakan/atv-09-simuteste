
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


@dataclass
class Task:
    id: Optional[int]
    titulo: str
    descricao: str
    prioridade: Priority
    prazo: datetime
    status: Status = Status.PENDENTE

    def validar(self) -> None:
        # Título com 3+ caracteres (desconsiderando espaços nas pontas)
        if self.titulo is None or len(self.titulo.strip()) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres.")
        # Prazo não pode ser no passado
        agora = datetime.now()
        if self.prazo < agora:
            raise ValueError("Prazo não pode ser no passado.")
