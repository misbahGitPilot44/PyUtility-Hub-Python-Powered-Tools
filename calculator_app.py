import streamlit as st
import math
import time
from datetime import datetime

# Set page configuration with Python-themed title and icon
st.set_page_config(
    page_title="🐍 PyUtility Hub – Python-Powered Tools",
    page_icon="🐍",
    layout="wide"
)

# Sidebar for navigation
st.sidebar.title("🐍 PyUtility Hub")
st.sidebar.markdown("Navigate Python-powered utilities:")
sections = ["Calculator", "To-Do List", "Clock/Timer", "Calendar", "Notes Pad", "Pomodoro Timer", "Habit Tracker", "Python Quiz", "Uplifting Rhythms", "AI Assistant"]
selected_section = st.sidebar.radio("Go to:", sections)

# Main title with Python emoji
st.title("🐍 PyUtility Hub – Python-Powered Tools")
st.markdown("Explore a suite of Python-driven utilities for productivity and learning.")


# Placeholder AI response function
def get_ai_response(user_input):
    # Simple rule-based responses (replace with API call later)
    if "hello" in user_input.lower() or "hi" in user_input.lower() or "goodmorning" in user_input.lower() or "Good Morning" in user_input.lower():
        return "Hello! How can I assist you today? 🐍"
    if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "see you later" in user_input.lower():
        return "Good Bye, See you soon buddy!!🐍"
    if "how are you" in user_input.lower() or "how are you doing" in user_input.lower():
        return "I'm doing great, thanks for asking! How about you? 😊"
    elif "help" in user_input.lower():
        return "I'm here to help! Try asking about calculators, timers, or Python tips."
    elif "what is python" in user_input.lower():
        return "Python is a versatile programming language known for its readability and simplicity. It's great for beginners and powerful enough for experts!"
    elif "features of app" in user_input.lower():
        return "Welcome to the PyUtility Hub, a Python-powered web application designed to boost your productivity and learning experience!\n. Built using Streamlit, this dashboard offers a variety of interactive utilities, all accessible through a user-friendly interface. Here’s a breakdown of what you can explore: \n\n1. **Calculator**: Perform basic arithmetic operations, including addition, subtraction, multiplication, division, square root, logarithm, and trigonometric functions like sine.\n2. **To-Do List**: Manage your tasks with an interactive to-do list that allows you to add, edit, and delete tasks.\n3. **Clock/Timer/Stopwatch**: Keep track of time with a live clock, set timers, and use a stopwatch for timing activities.\n4. **Calendar**: View and manage events in a calendar format.\n5. **Notes Pad**: Write and save notes with search functionality to find specific notes easily.\n6. **Pomodoro Timer**: Boost your productivity with a Pomodoro timer that alternates between work sessions and breaks.\n7. **Habit Tracker**: Track your daily or weekly habits and monitor your progress.\n8. **Python Quiz**: Test your Python knowledge with a quiz featuring multiple-choice questions.\n9. **Uplifting Rhythms**: Enjoy a curated playlist of uplifting music to keep you motivated.\n10. **AI Assistant**: Chat with an AI assistant for quick answers and assistance on various topics."
    elif "time" in user_input.lower():
        return f"The current time is {datetime.now().strftime('%H:%M:%S')} IST on {datetime.now().strftime('%B %d, %Y')}."
    else:
        return "I'm not sure how to respond to that yet. Try 'hello' or 'help' for now!"

# Calculator
with st.container():
    st.markdown('<div id="Calculator">', unsafe_allow_html=True)
    st.subheader("📱 Calculator 🐍")
    with st.expander("Python Calculator"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            num1 = st.number_input("Enter first number", value=0.0, key="calc_num1")
        with col2:
            operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Log", "Sin"], key="calc_op")
        with col3:
            num2 = st.number_input("Enter second number", value=0.0, key="calc_num2") if operation not in ["Square Root", "Log", "Sin"] else 0.0

        def calculate(n1, n2, op):
            if op == "Add":
                return n1 + n2
            elif op == "Subtract":
                return n1 - n2
            elif op == "Multiply":
                return n1 * n2
            elif op == "Divide":
                if n2 == 0:
                    return "❌ Cannot divide by zero"
                return n1 / n2
            elif op == "Square Root":
                return math.sqrt(n1) if n1 >= 0 else "❌ Invalid input"
            elif op == "Log":
                return math.log(n1) if n1 > 0 else "❌ Invalid input"
            elif op == "Sin":
                return math.sin(math.radians(n1))

        if st.button("Calculate", key="calc"):
            if operation in ["Square Root", "Log", "Sin"]:
                result = calculate(num1, 0, operation)
            else:
                result = calculate(num1, num2, operation)
            st.success(f"Result: {result}")
    st.markdown('</div>', unsafe_allow_html=True)

# To-Do List
with st.container():
    st.markdown('<div id="To-Do List">', unsafe_allow_html=True)
    st.subheader("📝 To-Do List 🐍")
    with st.expander("Python To-Do List"):
        tasks = st.session_state.get("tasks", [])
        task_input = st.text_input("Add task", key="task_input")
        if st.button("Add Task", key="add_task"):
            if task_input:
                tasks.append({"task": task_input, "completed": False})
                st.session_state.tasks = tasks
        for i, task in enumerate(tasks):
            col1, col2, col3 = st.columns([4, 1, 1])
            with col1:
                task_text = st.checkbox(task["task"], key=f"task_{i}", value=task["completed"])
                if task_text != task["completed"]:
                    tasks[i]["completed"] = task_text
                    st.session_state.tasks = tasks
            with col2:
                if st.button("Edit", key=f"edit_{i}"):
                    new_task = st.text_input("Edit task", value=task["task"], key=f"edit_input_{i}")
                    if st.button("Save", key=f"save_{i}"):
                        tasks[i]["task"] = new_task
                        st.session_state.tasks = tasks
            with col3:
                if st.button("Delete", key=f"delete_{i}"):
                    tasks.pop(i)
                    st.session_state.tasks = tasks
    st.markdown('</div>', unsafe_allow_html=True)

# Clock/Timer/Stopwatch
with st.container():
    st.markdown('<div id="Clock/Timer">', unsafe_allow_html=True)
    st.subheader("⏰ Clock/Timer/Stopwatch 🐍")
    with st.expander("Python Time Tools"):
        # Live Clock
        clock = st.empty()
        clock.write(f"Current Time: {datetime.now().strftime('%H:%M:%S')} IST")

        # Timer
        if "timer_start" not in st.session_state:
            st.session_state.timer_start = time.time()
        if "timer_running" not in st.session_state:
            st.session_state.timer_running = True
        elapsed_time = time.time() - st.session_state.timer_start
        minutes, seconds = divmod(int(elapsed_time), 60)
        timer_display = st.empty()
        timer_display.write(f"Timer: {minutes:02d}:{seconds:02d}.{int(elapsed_time * 100 % 100):02d}")

        # Stopwatch
        if "stopwatch_start" not in st.session_state:
            st.session_state.stopwatch_start = None
        if "stopwatch_running" not in st.session_state:
            st.session_state.stopwatch_running = False
        if "stopwatch_laps" not in st.session_state:
            st.session_state.stopwatch_laps = []
        if "stopwatch_time" not in st.session_state:
            st.session_state.stopwatch_time = 0

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start/Resume" if not st.session_state.stopwatch_running else "Stop", key="stopwatch_toggle"):
                if not st.session_state.stopwatch_running:
                    if st.session_state.stopwatch_start is None:
                        st.session_state.stopwatch_start = time.time()
                    else:
                        st.session_state.stopwatch_start = time.time() - st.session_state.stopwatch_time
                    st.session_state.stopwatch_running = True
                else:
                    st.session_state.stopwatch_running = False
                    st.session_state.stopwatch_time = time.time() - st.session_state.stopwatch_start
        with col2:
            if st.button("Lap" if st.session_state.stopwatch_running else "Reset", key="stopwatch_lap"):
                if st.session_state.stopwatch_running:
                    lap_time = time.time() - st.session_state.stopwatch_start
                    st.session_state.stopwatch_laps.append(lap_time)
                else:
                    st.session_state.stopwatch_start = None
                    st.session_state.stopwatch_running = False
                    st.session_state.stopwatch_time = 0
                    st.session_state.stopwatch_laps = []

        if st.session_state.stopwatch_running:
            current_time = time.time() - st.session_state.stopwatch_start
        else:
            current_time = st.session_state.stopwatch_time
        minutes, seconds = divmod(int(current_time), 60)
        stopwatch_display = st.empty()
        stopwatch_display.write(f"Stopwatch: {minutes:02d}:{seconds:02d}.{int(current_time * 100 % 100):02d}")

        if st.session_state.stopwatch_laps:
            st.write("Lap times:")
            for i, lap in enumerate(st.session_state.stopwatch_laps):
                lap_minutes, lap_seconds = divmod(int(lap), 60)
                st.write(f"Lap {i+1}: {lap_minutes:02d}:{lap_seconds:02d}.{int(lap * 100 % 100):02d}")
    st.markdown('</div>', unsafe_allow_html=True)

# Calendar
with st.container():
    st.markdown('<div id="Calendar">', unsafe_allow_html=True)
    st.subheader("📅 Calendar 🐍")
    with st.expander("Python Calendar"):
        view = st.selectbox("View", ["Day", "Week", "Month"], key="calendar_view")
        today = datetime.now().date()
        st.write(f"Today: {today}")
        event = st.text_input("Add event", key="event_input")
        if st.button("Add Event", key="add_event"):
            if event:
                st.session_state.events = st.session_state.get("events", []) + [event]
        if "events" in st.session_state:
            st.write("Events:", st.session_state.events)
    st.markdown('</div>', unsafe_allow_html=True)

# Notes Pad
with st.container():
    st.markdown('<div id="Notes Pad">', unsafe_allow_html=True)
    st.subheader("📋 Notes Pad 🐍")
    with st.expander("Python Notes"):
        note = st.text_area("Enter note", key="note_input", height=200)
        if st.button("Save Note", key="save_note"):
            st.session_state.notes = st.session_state.get("notes", []) + [note]
        if "notes" in st.session_state:
            st.write("Saved Notes:", st.session_state.notes)
        search_term = st.text_input("Search notes", key="search_note")
        if search_term and "notes" in st.session_state:
            filtered_notes = [n for n in st.session_state.notes if search_term.lower() in n.lower()]
            st.write("Search Results:", filtered_notes if filtered_notes else "No matches found")
    st.markdown('</div>', unsafe_allow_html=True)

# Productivity Tools
st.header("🚀 Python Productivity Tools")

# Pomodoro Timer
with st.container():
    st.markdown('<div id="Pomodoro Timer">', unsafe_allow_html=True)
    st.subheader("🧠 Pomodoro Timer 🐍")
    with st.expander("Python Pomodoro"):
        st.write("Pomodoro Timer (25 minutes work, 5 minutes break)")
        if "pomodoro_start" not in st.session_state:
            st.session_state.pomodoro_start = None
        if "pomodoro_running" not in st.session_state:
            st.session_state.pomodoro_running = False
        if "pomodoro_mode" not in st.session_state:
            st.session_state.pomodoro_mode = "work"
        if "pomodoro_time" not in st.session_state:
            st.session_state.pomodoro_time = 25 * 60

        if st.session_state.pomodoro_running:
            elapsed_time = st.session_state.pomodoro_time - (time.time() - st.session_state.pomodoro_start)
            if elapsed_time <= 0:
                st.session_state.pomodoro_running = False
                st.session_state.pomodoro_mode = "break" if st.session_state.pomodoro_mode == "work" else "work"
                st.session_state.pomodoro_time = 5 * 60 if st.session_state.pomodoro_mode == "break" else 25 * 60
                st.warning(f"Time's up! Switch to {st.session_state.pomodoro_mode} mode.")
            minutes, seconds = divmod(int(elapsed_time), 60)
            st.write(f"Time remaining: {minutes:02d}:{seconds:02d}")
        else:
            minutes, seconds = divmod(st.session_state.pomodoro_time, 60)
            st.write(f"Time remaining: {minutes:02d}:{seconds:02d}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start" if not st.session_state.pomodoro_running else "Pause", key="pomodoro_toggle"):
                if not st.session_state.pomodoro_running:
                    if st.session_state.pomodoro_start is None:
                        st.session_state.pomodoro_start = time.time()
                    else:
                        st.session_state.pomodoro_start = time.time() - (st.session_state.pomodoro_time - (25 * 60 if st.session_state.pomodoro_mode == "work" else 5 * 60))
                    st.session_state.pomodoro_running = True
                else:
                    st.session_state.pomodoro_running = False
        with col2:
            if st.button("Reset", key="pomodoro_reset"):
                st.session_state.pomodoro_start = None
                st.session_state.pomodoro_running = False
                st.session_state.pomodoro_mode = "work"
                st.session_state.pomodoro_time = 25 * 60

        st.write("Relaxing Songs for Pomodoro Breaks:")
        st.write("[Song 1](https://youtu.be/rCSCPujLs14?si=CKuIH7L5c7XfZkDb)")
        st.write("[Song 2](https://youtu.be/_4kHxtiuML0?si=clHp0r_rkV6AxS3L)")
        st.write("[Song 3](https://youtu.be/qsEBaIMCKl4?si=CcQQa3eY8uosdlkF)")
    st.markdown('</div>', unsafe_allow_html=True)

# Habit Tracker
with st.container():
    st.markdown('<div id="Habit Tracker">', unsafe_allow_html=True)
    st.subheader("📊 Habit Tracker 🐍")
    with st.expander("Python Habit Tracker"):
        st.write("Track your habits daily or weekly")
        habits = st.session_state.get("habits", {})
        habit_name = st.text_input("Enter habit name", key="habit_name")
        if st.button("Add Habit", key="add_habit"):
            if habit_name and habit_name not in habits:
                habits[habit_name] = {"days": {}, "streak": 0}
                st.session_state.habits = habits

        today = datetime.now().date().isoformat()
        for habit, data in habits.items():
            st.write(f"**{habit}**")
            if st.button(f"Mark {habit} as done for today", key=f"mark_{habit}_{today}"):
                data["days"][today] = True
                streak = 0
                sorted_days = sorted(data["days"].keys(), reverse=True)
                for day in sorted_days:
                    if data["days"][day]:
                        streak += 1
                    else:
                        break
                data["streak"] = streak
                st.session_state.habits = habits
            st.write(f"Streak: {data['streak']} days")
            st.write("Days completed:", list(data["days"].keys()))

        if habits:
            st.write("Habit Streaks:")
            for habit, data in habits.items():
                st.write(f"{habit}: {data['streak']} days")
    st.markdown('</div>', unsafe_allow_html=True)

# Python Quiz
with st.container():
    st.markdown('<div id="Python Quiz">', unsafe_allow_html=True)
    st.subheader("🎓 Python Quiz 🐍")
    with st.expander("Test Your Python Skills"):
        st.write("✅ Instructions: Each question has one correct answer unless stated otherwise.")

        # Q1
        st.write("Q1. What will be the output of the following code?")
        st.code("x = [1, 2, 3]\ny = x\ny += [4, 5]\nprint(x)")
        q1_options = ["A. [1, 2, 3]", "B. [1, 2, 3, 4, 5]", "C. Error", "D. [4, 5]"]
        q1_answer = st.radio("Select your answer:", q1_options, key="q1")
        if q1_answer == "B. [1, 2, 3, 4, 5]":
            st.success("✅ Correct Answer: B")

        # Q2
        st.write("Q2. What does this decorator do?")
        st.code("def debug(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__}')\n        return func(*args, **kwargs)\n    return wrapper")
        q2_options = ["A. Adds a breakpoint to the function", "B. Logs the function name before calling it", "C. Times the function's execution", "D. Prevents function execution"]
        q2_answer = st.radio("Select your answer:", q2_options, key="q2")
        if q2_answer == "B. Logs the function name before calling it":
            st.success("✅ Correct Answer: B")

        # Q3
        st.write("Q3. What is the result of the following code?")
        st.code('print("".join(["a", "b", "c"]))')
        q3_options = ["A. a b c", "B. abc", "C. ['a', 'b', 'c']", "D. Error"]
        q3_answer = st.radio("Select your answer:", q3_options, key="q3")
        if q3_answer == "B. abc":
            st.success("✅ Correct Answer: B")

        # Q4
        st.write("Q4. Which of the following is not a valid way to create a generator in Python?")
        q4_options = ["A. Using yield in a function", "B. Using generator expressions", "C. Using range() function", "D. Using iter() on a list"]
        q4_answer = st.radio("Select your answer:", q4_options, key="q4")
        if q4_answer == "C. Using range() function":
            st.success("✅ Correct Answer: C (Note: range() returns a range object, not a generator.)")

        # Q5
        st.write("Q5. What will this code print?")
        st.code("a = [1, 2, 3]\nb = a\na = a + [4, 5]\nprint(b)")
        q5_options = ["A. [1, 2, 3, 4, 5]", "B. [1, 2, 3]", "C. [4, 5]", "D. Error"]
        q5_answer = st.radio("Select your answer:", q5_options, key="q5")
        if q5_answer == "B. [1, 2, 3]":
            st.success("✅ Correct Answer: B (Because a + [4, 5] creates a new object, doesn't mutate original b.)")

        # Q6
        st.write("Q6. What's the output of this set comprehension?")
        st.code("s = {i for i in range(5) if i % 2 == 0}\nprint(s)")
        q6_options = ["A. [0, 2, 4]", "B. {0, 2, 4}", "C. (0, 2, 4)", "D. 0 2 4"]
        q6_answer = st.radio("Select your answer:", q6_options, key="q6")
        if q6_answer == "B. {0, 2, 4}":
            st.success("✅ Correct Answer: B")

        # Q7
        st.write("Q7. What is the purpose of __slots__ in Python classes?")
        q7_options = ["A. Prevent inheritance", "B. Make class methods private", "C. Prevent dynamic attribute creation", "D. Improve readability"]
        q7_answer = st.radio("Select your answer:", q7_options, key="q7")
        if q7_answer == "C. Prevent dynamic attribute creation":
            st.success("✅ Correct Answer: C")

        # Q8
        st.write("Q8. How do you define a metaclass in Python?")
        q8_options = ["A. Subclass object", "B. Override __init__ method", "C. Subclass type", "D. Use @staticmethod"]
        q8_answer = st.radio("Select your answer:", q8_options, key="q8")
        if q8_answer == "C. Subclass type":
            st.success("✅ Correct Answer: C")

        # Q9
        st.write("Q9. What is the output of this function?")
        st.code("def func(a, L=[]):\n    L.append(a)\n    return L\n\nprint(func(1))\nprint(func(2))")
        q9_options = ["A. [1] and [2]", "B. [1, 2] and [1, 2]", "C. [1] and [1, 2]", "D. Error"]
        q9_answer = st.radio("Select your answer:", q9_options, key="q9")
        if q9_answer == "C. [1] and [1, 2]":
            st.success("✅ Correct Answer: C (Default mutable arguments retain changes across function calls.)")

        # Q10
        st.write("Q10. What will be the output of the following code?")
        st.code("x = [1, 2, 3]\ny = x[:]\nx[0] = 100\nprint(y[0])")
        q10_options = ["A. 1", "B. 100", "C. [100, 2, 3]", "D. Error"]
        q10_answer = st.radio("Select your answer:", q10_options, key="q10")
        if q10_answer == "A. 1":
            st.success("✅ Correct Answer: A (Slicing creates a shallow copy.)")
    st.markdown('</div>', unsafe_allow_html=True)

# Uplifting Rhythms
with st.container():
    st.markdown('<div id="Uplifting Rhythms">', unsafe_allow_html=True)
    st.subheader("🎶 Uplifting Rhythms 🐍")
    with st.expander("Python-Powered Playlist"):
        st.write("Boost your energy with these uplifting tracks:")
        st.write("[Music 1](https://youtu.be/l71aOtTJ1gE?si=UURaASDI6Ioh70QM)")
        st.write("[Music 2](https://youtu.be/bnqLzCsffwY?si=r_Jey8edanCV8gOi)")
        st.write("[Music 3](https://youtu.be/9oVnwTvXeh4?si=uMNp8j72-Z8yLSgw)")
    st.markdown('</div>', unsafe_allow_html=True)

# AI Assistant
with st.container():
    st.markdown('<div id="AI Assistant">', unsafe_allow_html=True)
    st.subheader("🤖 AI Assistant 🐍")
    with st.expander("Python AI Chat"):
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Handle user input
        if prompt := st.chat_input("Ask me anything..."):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Generate AI response
            response = get_ai_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response)
    st.markdown('</div>', unsafe_allow_html=True)

# Trigger scroll on section selection
if 'selected_section' not in st.session_state or st.session_state.selected_section != selected_section:
    st.session_state.selected_section = selected_section
    st.markdown(
        f"""
        <script>
            function scrollToSection(sectionId) {{
                const element = document.getElementById(sectionId);
                if (element) {{
                    element.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }}
            scrollToSection("{selected_section}");
        </script>
        """,
        unsafe_allow_html=True
    )
    st.rerun()
