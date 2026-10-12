from datetime import date, time, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(name="Alex")
    buddy = Pet(name="Buddy", species="Dog", age=3)
    luna = Pet(name="Luna", species="Cat", age=2)

    owner.add_pet(buddy)
    owner.add_pet(luna)

    scheduler = Scheduler(owner=owner)
    today = date.today()

    task1 = Task(
        description="Feed Luna",
        time=time(12, 0),
        frequency="daily",
        priority="high",
        scheduled_date=today,
    )

    task2 = Task(
        description="Feed Buddy",
        time=time(8, 0),
        frequency="daily",
        priority="high",
        scheduled_date=today,
    )

    task3 = Task(
        description="Walk Buddy",
        time=time(9, 30),
        frequency="daily",
        priority="medium",
        scheduled_date=today,
    )

    task4 = Task(
        description="Give Luna medicine",
        time=time(12, 0),
        frequency="once",
        priority="high",
        scheduled_date=today,
    )

    scheduler.add_task(luna, task1)
    scheduler.add_task(buddy, task2)
    scheduler.add_task(buddy, task3)
    scheduler.add_task(luna, task4)

    print("\nTODAY'S SORTED SCHEDULE")
    print("=======================")

    for task in scheduler.get_todays_tasks():
        print(
            f"{task.time.strftime('%I:%M %p')} | "
            f"{task.description} | "
            f"Priority: {task.priority.title()}"
        )

    print("\nBUDDY'S TASKS")
    print("=============")

    for task in scheduler.get_tasks_by_pet("Buddy"):
        print(task.description)

    print("\nPENDING TASKS")
    print("=============")

    for task in scheduler.filter_tasks(completed=False):
        print(task.description)

    print("\nSCHEDULE CONFLICTS")
    print("==================")

    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts detected.")

    print("\nRECURRING TASK TEST")
    print("===================")

    next_task = scheduler.mark_task_complete(task2)

    print(f"Completed: {task2.description}")

    if next_task:
        print(f"Next occurrence: {next_task.description}")
        print(f"Next date: {next_task.scheduled_date}")
        print(f"Completed status: {next_task.completed}")

    print("\nCOMPLETED TASKS")
    print("===============")

    for task in scheduler.filter_tasks(completed=True):
        print(task.description)


if __name__ == "__main__":
    main()
