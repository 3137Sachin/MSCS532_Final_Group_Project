"""
Final Group Project
Bereket Gebremariam, Sachin Karki
Satish Penmatsa
2025 Fall - Algorithms and Data Structures (MSCS-532-M80) - Full Term
University of the Cumberland – Kentucky

This is the main class file which will consist of everything like the library, functions for insertion, deletion etc.
"""

class Task:
    def __init__(self, task_id, description, deadline, urgency):
        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.urgency = urgency

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Deadline: {self.deadline}, Urgency: {self.urgency}"

class TaskScheduler:
    def __init__(self):
        self.tasks = {}  # Hash table for tasks

    def add_task(self, task_id, description, deadline, urgency):
        """Add a task to the scheduler."""
        if task_id in self.tasks:
            raise ValueError(f"Task ID {task_id} already exists")
        task = Task(task_id, description, deadline, urgency)
        self.tasks[task_id] = task

    def get_next_task(self):
        """Return the highest-priority task based on earliest deadline and highest urgency."""
        if not self.tasks:
            raise IndexError("No tasks available")
        # Sort by deadline first, then urgency (descending)
        next_task = sorted(self.tasks.values(), key=lambda x: (x.deadline, -x.urgency))[0]
        return next_task

    def complete_task(self):
        """Remove and return the highest-priority task."""
        if not self.tasks:
            raise IndexError("No tasks available")
        next_task = self.get_next_task()
        del self.tasks[next_task.task_id]
        return next_task

    def find_task(self, task_id):
        """Retrieve a task by ID."""
        if task_id not in self.tasks:
            raise ValueError(f"Task ID {task_id} not found")
        return self.tasks[task_id]

    def is_empty(self):
        return len(self.tasks) == 0

