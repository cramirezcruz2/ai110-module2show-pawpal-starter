
from datetime import date, time, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


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


def test_tasks_are_sorted_by_time():
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog", age=3)
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    late_task = Task(
        description="Walk Buddy",
        time=time(10, 0),
        scheduled_date=date.today(),
    )
    early_task = Task(
        description="Feed Buddy",
        time=time(8, 0),
        scheduled_date=date.today(),
    )

    scheduler.add_task(pet, late_task)
    scheduler.add_task(pet, early_task)

    assert scheduler.sort_by_time() == [early_task, late_task]


def test_daily_task_creates_next_occurrence():
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog", age=3)
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    task = Task(
        description="Feed Buddy",
        time=time(8, 0),
        frequency="daily",
        scheduled_date=date.today(),
    )
    scheduler.add_task(pet, task)

    next_task = scheduler.mark_task_complete(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.scheduled_date == date.today() + timedelta(days=1)
    assert next_task.completed is False
    assert next_task in pet.tasks


def test_conflict_detection_finds_duplicate_times():
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog", age=3)
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    task1 = Task(
        description="Feed Buddy",
        time=time(8, 0),
        scheduled_date=date.today(),
    )
    task2 = Task(
        description="Give medicine",
        time=time(8, 0),
        scheduled_date=date.today(),
    )

    scheduler.add_task(pet, task1)
    scheduler.add_task(pet, task2)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]


def test_empty_schedule_returns_no_tasks():
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog", age=3)
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    assert scheduler.get_todays_tasks() == []
    assert scheduler.detect_conflicts() == []
