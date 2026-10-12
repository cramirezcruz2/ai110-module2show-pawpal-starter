# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output
Today's Schedule
================
08:00 AM | Feed Buddy | Priority: High | Status: Pending
09:30 AM | Walk Buddy | Priority: Medium | Status: Pending
12:00 PM | Feed Luna | Priority: High | Status: Pending

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Cesar\ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 6 items                                                                                                                         

tests\test_pawpal.py ......                                                                                                         [100%]

=========================================================== 6 passed in 0.09s ============================================================

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---|---|---|
| Task sorting | `sort_by_time()` | Sorts tasks by time, using priority to break ties. |
| Filtering | `filter_tasks()`, `get_tasks_by_pet()` | Filters tasks by completion status or pet name. |
| Conflict detection | `detect_conflicts()` | Identifies incomplete tasks scheduled for the same date and exact time. |
| Recurring tasks | `mark_task_complete()` | Creates the next occurrence when a daily or weekly task is completed. |
| Daily schedule | `get_todays_tasks()` | Returns tasks due today based on their scheduled date and frequency. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Launch PawPal+ using Streamlit.
2. Enter the owner's information and add a pet, including its name, species, and age.
3. Add a care task such as feeding, walking, or giving medication. Set the time, duration, priority, and frequency.
4. Review today's schedule. Tasks are organized by time, and priority is used to break ties.
5. Check any conflict warnings to identify tasks that share the same date and time.
6. Mark a task complete and verify that the system creates the next occurrence for daily or weekly task.
