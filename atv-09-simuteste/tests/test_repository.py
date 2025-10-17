
from datetime import datetime, timedelta

from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority


def make_task():
    return Task(None, "Teste", "Desc", Priority.BAIXA, datetime.now() + timedelta(days=1))


def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = make_task()
    resultado = repo.save(task)

    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, resultado)


def test_save_incrementa_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    t1 = repo.save(make_task())
    t2 = repo.save(make_task())

    assert t1.id == 1
    assert t2.id == 2
    assert mock_storage.add.call_count == 2


def test_find_by_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.find_by_id(42)
    mock_storage.get.assert_called_once_with(42)


def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    mock_storage.get_all.return_value = ["a", "b"]
    res = repo.find_all()
    assert res == ["a", "b"]
    mock_storage.get_all.assert_called_once()


def test_delete_chama_storage_delete(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.delete(3)
    mock_storage.delete.assert_called_once_with(3)
