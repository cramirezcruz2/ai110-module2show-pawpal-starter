
import streamlit as st
from datetime import date, time
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(owner=st.session_state.owner)

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.title("🐾 PawPal+")
st.write("Plan and organize your pets' daily care tasks.")

# --------------------------------------------------
# Update Owner Name
# --------------------------------------------------

owner_name = st.text_input("Owner name", value=owner.name)

if st.button("Update owner name"):
    owner.name = owner_name
    st.success("Owner name updated!")

st.divider()

# --------------------------------------------------
# Add a Pet
# --------------------------------------------------

st.subheader("Add a Pet")

with st.form("pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=100, value=1)
    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if pet_name.strip():
            pet = Pet(
                name=pet_name.strip(),
                species=species,
                age=int(age)
            )
            owner.add_pet(pet)
            st.success(f"{pet.name} was added!")
        else:
            st.error("Please enter a pet name.")

# --------------------------------------------------
# Display Pets
# --------------------------------------------------

st.subheader("Your Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"🐾 **{pet.name}** — {pet.species}, age {pet.age}")
else:
    st.info("Add a pet before creating tasks.")

st.divider()

# --------------------------------------------------
# Add a Care Task
# --------------------------------------------------

st.subheader("Add a Care Task")

if owner.pets:
    pet_names = [pet.name for pet in owner.pets]

    with st.form("task_form"):
        selected_name = st.selectbox("Choose a pet", pet_names)
        description = st.text_input("Task description", value="Morning walk")
        task_time = st.time_input("Task time", value=time(9, 0))
        frequency = st.selectbox(
            "Frequency", ["daily", "weekly", "once"]
        )
        priority = st.selectbox(
            "Priority", ["low", "medium", "high"], index=1
        )
        duration = st.number_input(
            "Duration (minutes)", min_value=1, max_value=240, value=20
        )
        scheduled_date = st.date_input("Scheduled date", value=date.today())

        add_task = st.form_submit_button("Add Task")

        if add_task:
            if description.strip():
                selected_pet = next(
                    pet for pet in owner.pets
                    if pet.name == selected_name
                )

                task = Task(
                    description=description.strip(),
                    time=task_time,
                    frequency=frequency,
                    priority=priority,
                    duration_minutes=int(duration),
                    scheduled_date=scheduled_date
                )

                scheduler.add_task(selected_pet, task)
                st.success(f"Task added for {selected_pet.name}!")
            else:
                st.error("Please enter a task description.")

st.divider()

# --------------------------------------------------
# Daily Schedule
# --------------------------------------------------

st.subheader("Daily Schedule")

tasks = scheduler.get_todays_tasks()

if tasks:
    for i, task in enumerate(tasks):
        st.write(
            f"**{task.time.strftime('%I:%M %p')}** — "
            f"{task.description} | "
            f"Priority: {task.priority.title()} | "
            f"Duration: {task.duration_minutes} minutes"
        )

        if task.completed:
            st.success("✅ Completed")
        else:
            st.warning("⏳ Pending")

            if st.button("Mark Complete", key=f"complete_{i}"):
                scheduler.mark_task_complete(task)
                st.rerun()
else:
    st.info("No tasks scheduled for today.")

st.divider()

# --------------------------------------------------
# Edit an Existing Task
# --------------------------------------------------

st.subheader("✏️ Edit a Task")

all_tasks = scheduler.schedule_tasks()

if not all_tasks:
    st.info("Add a task first before editing it.")
else:
    # Show the task description, pet, date, and time
    # so you can identify the task you want to edit.
    def task_label(task):
        pet_name = next(
            (
                pet.name
                for pet in owner.pets
                if any(existing is task for existing in pet.tasks)
            ),
            "Unknown pet"
        )

        return (
            f"{task.description} — {pet_name} — "
            f"{task.scheduled_date.strftime('%b %d, %Y')} "
            f"at {task.time.strftime('%I:%M %p')}"
        )

    selected_index = st.selectbox(
        "Select a task to edit",
        options=list(range(len(all_tasks))),
        format_func=lambda i: task_label(all_tasks[i]),
        key="edit_task_selection"
    )

    selected_task = all_tasks[selected_index]

    with st.form("edit_task_form"):
        edit_description = st.text_input(
            "Task description",
            value=selected_task.description
        )

        edit_date = st.date_input(
            "Scheduled date",
            value=selected_task.scheduled_date
        )

        edit_time = st.time_input(
            "Task time",
            value=selected_task.time
        )

        frequency_options = ["daily", "weekly", "once"]
        current_frequency = selected_task.frequency.lower()

        edit_frequency = st.selectbox(
            "Frequency",
            frequency_options,
            index=(
                frequency_options.index(current_frequency)
                if current_frequency in frequency_options
                else 0
            )
        )

        priority_options = ["low", "medium", "high"]
        current_priority = selected_task.priority.lower()

        edit_priority = st.selectbox(
            "Priority",
            priority_options,
            index=(
                priority_options.index(current_priority)
                if current_priority in priority_options
                else 1
            )
        )

        edit_duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=240,
            value=max(1, min(240, selected_task.duration_minutes))
        )

        save_changes = st.form_submit_button("Save Changes")

        if save_changes:
            if edit_description.strip():
                selected_task.description = edit_description.strip()
                selected_task.scheduled_date = edit_date
                selected_task.time = edit_time
                selected_task.frequency = edit_frequency
                selected_task.priority = edit_priority
                selected_task.duration_minutes = int(edit_duration)

                st.success("Task updated successfully!")
                st.rerun()
            else:
                st.error("Please enter a task description.")

st.divider()

# --------------------------------------------------
# Scheduling Conflict Warnings
# --------------------------------------------------

st.subheader("⚠️ Scheduling Conflicts")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for conflict in conflicts:
        st.warning(conflict)
else:
    st.success("No scheduling conflicts found!")
