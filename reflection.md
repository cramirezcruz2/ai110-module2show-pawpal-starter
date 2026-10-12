# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design coninas four main classes: Owner, Pet, Task, and Scheduler. The owner class manages the owners's information and pets, the Pet class stores information about each of the pets, the Task class represents pet care activitie like feed or walking, and the Scheduler organizes task based on their time and priority.
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
 I prioritized time first so tasks appear in the correct order, then used priority to put high-priority tasks before lower-priority tasks scheduled at the same time. I also added filtering and conflMy scheduler considers task time, priority, completion status, frequency, and scheduled date.ict detection to help pet owners manage their tasks.

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
I did not accept every AI suggestion without checking it. I reviewed the code to make sure it matched my project and tested the scheduler to verify that tasks were sorted correctly and scheduling conflicts were detected.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
