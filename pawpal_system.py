from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    tasks: list["Task"] = field(default_factory=list)

    def get_info(self) -> str:
        ...


@dataclass
class Task:
    description: str

    def complete_task(self) -> None:
        ...


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        ...


@dataclass
class Scheduler:
    tasks: list[Task] = field(default_factory=list)

    def schedule_tasks(self) -> None:
        ...