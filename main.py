
from datetime import date, time
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create an owner
    owner = Owner(name="Alex")

    # Create two pets
    buddy = Pet(name="Buddy", species="Dog", age=3)
    luna = Pet(name="Luna", species="Cat", age=2)

    # Add pets to the owner
    owner.add_pet(buddy)
    owner.add_pet(luna)

    # Create at least three tasks at different times
    task1 = Task(
        description="Feed Buddy",
        time=time(8, 0),
        frequency="daily",
        priority="high",
        scheduled_date=date.today()
    )

    task2 = Task(
        description="Walk Buddy",
        time=time(9, 30),
        frequency="daily",
        priority="medium",
        scheduled_date=date.today()
    )

    task3 = Task(
        description="Feed Luna",
        time=time(12, 0),
        frequency="daily",
        priority="high",
        scheduled_date=date.today()
    )

    # Assign tasks to pets through the scheduler
    scheduler = Scheduler(owner=owner)
    scheduler.add_task(buddy, task1)
    scheduler.add_task(buddy, task2)
    scheduler.add_task(luna, task3)

    # Print today's schedule
    print("Today's Schedule")
    print("================")

    tasks = scheduler.get_todays_tasks()

    if not tasks:
        print("No tasks scheduled for today.")
    else:
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(
                f"{task.time.strftime('%I:%M %p')} | "
                f"{task.description} | "
                f"Priority: {task.priority.title()} | "
                f"Status: {status}"
            )


if __name__ == "__main__":
    main()

    