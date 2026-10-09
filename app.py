import streamlit as st
from datetime import date, time
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Keep owner and scheduler data between Streamlit reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(owner=st.session_state.owner)

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.title("🐾 PawPal+")
st.write("Plan and organize your pets' daily care tasks.")

# Owner information
owner_name = st.text_input("Owner name", value=owner.name)

if st.button("Update owner name"):
    owner.name = owner_name
    st.success("Owner name updated!")

st.divider()

# Add a pet
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

# Display pets
st.subheader("Your Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"🐾 **{pet.name}** — {pet.species}, age {pet.age}")
else:
    st.info("Add a pet before creating tasks.")

st.divider()

# Add a care task
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

# Generate today's schedule
st.subheader("Daily Schedule")

if st.button("Generate Schedule"):
    tasks = scheduler.get_todays_tasks()

    if tasks:
        for task in tasks:
            st.write(
                f"**{task.time.strftime('%I:%M %p')}** — "
                f"{task.description} | "
                f"Priority: {task.priority.title()} | "
                f"Duration: {task.duration_minutes} minutes | "
                f"Status: {'Completed' if task.completed else 'Pending'}"
            )
    else:
        st.info("No tasks scheduled for today.")

