from dataclasses import dataclass, field
from datetime import date, time as Time, timedelta


@dataclass
class Task:
    description: str
    time: Time = Time(9, 0)
    frequency: str = "daily"
    completed: bool = False
    priority: str = "medium"
    duration_minutes: int = 20
    scheduled_date: date = field(default_factory=date.today)

    def complete_task(self) -> None:
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def get_info(self) -> str:
        """Return a summary describing the pet."""
        return f"{self.name} ({self.species}), age {self.age}"

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's schedule."""
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        """Return a copy of the pet's tasks."""
        return list(self.tasks)


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's collection."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks assigned to the owner's pets."""
        return [
            task
            for pet in self.pets
            for task in pet.get_tasks()
        ]


@dataclass
class Scheduler:
    owner: Owner

    def add_task(self, pet: Pet, task: Task) -> None:
        """Assign a task to a pet belonging to this owner."""
        if not any(p is pet for p in self.owner.pets):
            raise ValueError(
                "Cannot add a task to a pet that does not belong to this owner."
            )
        pet.add_task(task)

    def sort_by_time(self, tasks: list[Task] | None = None) -> list[Task]:
        """Sort tasks by time, then by priority."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        tasks_to_sort = (
            self.owner.get_all_tasks() if tasks is None else tasks
        )

        return sorted(
            tasks_to_sort,
            key=lambda task: (
                task.time,
                priority_order.get(task.priority.lower(), 3),
            ),
        )

    def _sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Keep compatibility with the original sorting method."""
        return self.sort_by_time(tasks)

    def schedule_tasks(self) -> list[Task]:
        """Return all tasks in sorted order."""
        return self.sort_by_time()

    def filter_tasks(
        self,
        completed: bool | None = None,
        pet_name: str | None = None,
    ) -> list[Task]:
        """Filter tasks by completion status and/or pet name."""
        results = []

        for pet in self.owner.pets:
            if pet_name and pet.name.lower() != pet_name.lower():
                continue

            for task in pet.tasks:
                if completed is not None and task.completed != completed:
                    continue
                results.append(task)

        return self.sort_by_time(results)

    def get_tasks_by_pet(self, pet_name: str) -> list[Task]:
        """Return all tasks belonging to a pet by name."""
        return self.filter_tasks(pet_name=pet_name)

    def get_todays_tasks(self) -> list[Task]:
        """Return tasks due today based on their frequency."""
        today = date.today()
        todays_tasks = []

        for task in self.owner.get_all_tasks():
            if task.scheduled_date > today:
                continue

            frequency = task.frequency.lower()

            if frequency == "daily":
                todays_tasks.append(task)
            elif frequency == "weekly":
                if task.scheduled_date.weekday() == today.weekday():
                    todays_tasks.append(task)
            elif frequency == "monthly":
                if task.scheduled_date.day == today.day:
                    todays_tasks.append(task)
            elif frequency in ("once", "one-time", "one time"):
                if task.scheduled_date == today:
                    todays_tasks.append(task)
            elif task.scheduled_date == today:
                todays_tasks.append(task)

        return self.sort_by_time(todays_tasks)

    def get_pending_tasks(self) -> list[Task]:
        """Return today's tasks that are incomplete."""
        return self.filter_tasks(completed=False)

    def mark_task_complete(self, task: Task) -> Task | None:
        """Complete a task and create its next daily or weekly occurrence."""
        if task.completed:
            return None

        task.complete_task()

        # Find the pet that owns this task.
        for pet in self.owner.pets:
            if any(existing_task is task for existing_task in pet.tasks):
                frequency = task.frequency.lower()

                if frequency == "daily":
                    next_date = date.today() + timedelta(days=1)
                elif frequency == "weekly":
                    next_date = date.today() + timedelta(days=7)
                else:
                    return None

                next_task = Task(
                    description=task.description,
                    time=task.time,
                    frequency=task.frequency,
                    completed=False,
                    priority=task.priority,
                    duration_minutes=task.duration_minutes,
                    scheduled_date=next_date,
                )

                pet.add_task(next_task)
                return next_task

        raise ValueError("This task does not belong to one of the owner's pets.")

    def detect_conflicts(self) -> list[str]:
        """Warn about tasks scheduled for the same date and exact time."""
        tasks = self.owner.get_all_tasks()
        warnings = []

        for i, task_a in enumerate(tasks):
            if task_a.completed:
                continue

            for task_b in tasks[i + 1:]:
                if task_b.completed:
                    continue

                same_date = task_a.scheduled_date == task_b.scheduled_date
                same_time = task_a.time == task_b.time

                if same_date and same_time:
                    pet_a = next(
                        pet.name for pet in self.owner.pets
                        if any(t is task_a for t in pet.tasks)
                    )
                    pet_b = next(
                        pet.name for pet in self.owner.pets
                        if any(t is task_b for t in pet.tasks)
                    )

                    warnings.append(
                        f"Conflict: '{task_a.description}' for {pet_a} "
                        f"and '{task_b.description}' for {pet_b} are both "
                        f"scheduled for {task_a.scheduled_date} at "
                        f"{task_a.time.strftime('%I:%M %p')}."
                    )

        return warnings
