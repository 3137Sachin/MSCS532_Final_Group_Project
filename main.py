"""
Final Group Project
Bereket Gebremariam, Sachin Karki
Satish Penmatsa
2025 Fall - Algorithms and Data Structures (MSCS-532-M80) - Full Term
University of the Cumberland – Kentucky

This is the main class file which will consist of everything like the library, functions for insertion, deletion etc.
"""

import heapq

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
        self.heap = []  # Priority queue (min-heap)
        self.tasks = {}  # Hash table (dictionary) for task metadata

    def add_task(self, task_id, description, deadline, urgency):
        """Add a task to both priority queue and hash table."""
        if task_id in self.tasks:
            raise ValueError(f"Task ID {task_id} already exists")
        task = Task(task_id, description, deadline, urgency)
        # Add to hash table
        self.tasks[task_id] = task
        # Add to priority queue
        heapq.heappush(self.heap, (deadline, -urgency, task_id, description))

    def get_next_task(self):
        """Retrieve the highest-priority task."""
        if not self.heap:
            raise IndexError("Priority queue is empty")
        deadline, neg_urgency, task_id, description = self.heap[0]
        return self.tasks[task_id]  # Return task from hash table

    def complete_task(self):
        """Remove and return the highest-priority task."""
        if not self.heap:
            raise IndexError("Priority queue is empty")
        deadline, neg_urgency, task_id, description = heapq.heappop(self.heap)
        task = self.tasks.pop(task_id)  # Remove from hash table
        return task

    def find_task(self, task_id):
        """Retrieve task details by ID from hash table."""
        if task_id not in self.tasks:
            raise ValueError(f"Task ID {task_id} not found")
        return self.tasks[task_id]

    def is_empty(self):
        return len(self.heap) == 0

