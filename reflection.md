# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

My initial UML design contained four main classes: Owner, Pet, Task, and Scheduler. The Owner class managed the owner's information and pets. The Pet class stored information about each pet, such as its name, species, and age. The Task class represented pet care activities, such as feeding and walking. The Scheduler organized tasks based on their time and priority.
- What classes did you include, and what responsibilities did you assign to each?

Owner
Attributes: name, pets, tasks
Methods: add_pet(), add_task()
Pet
Attributes: name, species, age
Methods: get_info()
Task
Attributes: description, pet, time, priority, completed
Methods: complete_task()
Scheduler
Attributes: tasks
Methods: add_task(), schedule_tasks(), get_today_tasks()

**b. Design changes**

- Did your design change during implementation?

Yes, my design changed during implementation. 
- If yes, describe at least one change and why you made it.

I added sorting, filtering, recurring tasks, and conflict detection to make the scheduler more useful and organized. These changes helped automate tasks and make it easier to manage pet care schedules.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

My scheduler considers task time, priority, completion status, frequency, and scheduled date.
- How did you decide which constraints mattered most?

 I prioritized time first so tasks appear in the correct order, then used priority to put high-priority tasks before lower-priority tasks scheduled at the same time. I also included filtering and conflict detection to help pet owners manage their schedules.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

My scheduler only detects tasks scheduled for the exact same date and time, so it does not detect overlapping task durations. 
- Why is that tradeoff reasonable for this scenario?

This tradeoff is reasonable because it keeps the code simple and easy to understand while still warning pet owners about basic scheduling conflicts.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI to help design my UML diagram, write Python code, fix errors, and improve my Streamlit UI.
- What kinds of prompts or questions were most helpful?

 The most helpful prompts were asking for code examples, explanations of how the scheduler works, and ways to test my classes.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I did not accept every AI suggestion without checking it. For example, I reviewed the suggested conflict detection code to make sure it matched my project requirements. I tested two tasks scheduled for the same date and time and verified that the scheduler returned a conflict warning. I also ran my automated tests to make sure the scheduler worked as expected.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

I tested task completion, adding tasks to pets, sorting tasks by time, creating the next occurrence of daily tasks, detecting scheduling conflicts, and handling an empty schedule.
- Why were these tests important?

These tests were important because they helped verify that the scheduler's main features worked correctly. All six automated tests passed, giving me confidence in the behaviors I tested.

**b. Confidence**

- How confident are you that your scheduler works correctly?

I am fairly confident that my scheduler works correctly for the behaviors I tested.
- What edge cases would you test next if you had more time?

If I had more time, I would test overlapping task durations, tasks scheduled for different dates, and weekly or monthly recurring tasks.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the scheduler organizes pet care tasks by time and identifies scheduling conflicts. I also successfully created automated tests to check important features.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the scheduler by handling overlapping tasks more accurately and adding more tests for different schedules and recurring tasks. I would also improve the Streamlit UI to make it easier to use.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that designing a system requires planning how classes work together, testing the code, and checking AI suggestions instead of accepting them without verification.