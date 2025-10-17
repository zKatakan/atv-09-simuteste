
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from .repository import TaskRepository
from .task import Priority, Status, Task


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def criar_tarefa(
        self,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
    ) -> Task:
        task = Task(id=None, titulo=titulo, descricao=descricao, prioridade=prioridade, prazo=prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> List[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Optional[Task]:
        tarefa = self.repository.find_by_id(id)
        if tarefa is None:
            return None
        tarefa.status = status
        # Em um repositório real, poderíamos persistir a mudança.
        # Aqui, como a referência está guardada no storage, já está atualizado.
        return tarefa
