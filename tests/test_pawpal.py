
from pawpal_system import Pet, Task


def test_task_completion():
    task = Task(description="Feed Buddy")

    assert task.completed is False

    task.complete_task()

    assert task.completed is True


def test_task_addition():
    pet = Pet(name="Buddy", species="Dog", age=3)
    task = Task(description="Walk Buddy")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task