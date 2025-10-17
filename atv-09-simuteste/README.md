
# Task Manager (Simulação e Teste)

Sistema simples de gerenciamento de tarefas para praticar **arquitetura em camadas** e **testes automatizados com pytest**.

## Funcionalidades
- Criar tarefas com título, descrição, prioridade e prazo
- Listar todas as tarefas
- Buscar tarefa por ID
- Atualizar status da tarefa
- Deletar tarefas

## Estrutura do Projeto
```
task_manager/
  __init__.py
  task.py
  storage.py
  repository.py
  service.py  # (Bônus)
tests/
  test_task.py
  test_repository.py
requirements.txt
README.md
```
## Como executar os testes
```bash
pytest -v
```
Cobertura (opcional):
```bash
pytest --cov=task_manager
```

## Exemplo de uso
```python
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository

storage = InMemoryStorage()
repo = TaskRepository(storage)

prazo = datetime.now() + timedelta(days=5)
task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
task.validar()

task_salva = repo.save(task)
print(f"ID: {task_salva.id}")

encontrada = repo.find_by_id(1)
print(f"Título: {encontrada.titulo}")
```
