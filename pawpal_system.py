
from dataclasses import dataclass, field
from datetime import date, time as Time
import calendar


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
        """Return a summary string describing the pet."""
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
        """Return every task assigned to the owner's pets."""
        return [
            task
            for pet in self.pets
            for task in pet.get_tasks()
        ]


@dataclass
class Scheduler:
    owner: Owner

    def add_task(self, pet: Pet, task: Task) -> None:
        """Assign a task to a pet that belongs to the owner."""
        if not any(owned_pet is pet for owned_pet in self.owner.pets):
            raise ValueError(
                "Cannot add a task to a pet that does not belong to this owner."
            )
        pet.add_task(task)

    def _sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by time and priority for scheduling."""
        priority_order = {"high": 0, "medium": 1, "low": 2}

        return sorted(
            tasks,
            key=lambda task: (
                task.time,
                priority_order.get(task.priority.lower(), 3),
            ),
        )

    def schedule_tasks(self) -> list[Task]:
        """Return all tasks sorted into a schedule."""
        return self._sort_tasks(self.owner.get_all_tasks())

    def get_todays_tasks(self) -> list[Task]:
        """Return the tasks due today for the owner."""
        today = date.today()
        todays_tasks = []

        for task in self.owner.get_all_tasks():
            # Do not include tasks scheduled to begin in the future.
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
                # Unknown frequencies are treated as one-time tasks.
                todays_tasks.append(task)

        return self._sort_tasks(todays_tasks)

    def get_pending_tasks(self) -> list[Task]:
        """Return today's tasks that are still incomplete."""
        return [
            task
            for task in self.get_todays_tasks()
            if not task.completed
        ]