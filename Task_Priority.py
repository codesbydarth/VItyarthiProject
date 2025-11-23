import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    name: str
    deadline: datetime.date
    importance: int
    effort: int
    dependencies: int
    score: float = 0.0

def get_valid_date(prompt: str) -> datetime.date:
    """Prompts user for a date until a valid format is entered."""
    while True:
        date_str = input(prompt).strip()
        try:
            day, month, year = map(int, date_str.split("-"))
            return datetime.date(year, month, day)
        except ValueError:
            print("Invalid format. Please use DD-MM-YYYY (e.g., 15-08-1947).")

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    """Prompts user for an integer within a specified range."""
    while True:
        try:
            val_input = input(prompt).strip()
            val = int(val_input)
            if min_val <= val <= max_val:
                return val
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def compute_priority(task: Task) -> float:
    """Computes a priority score between 0 and 1 based on task attributes."""
    today = datetime.date.today()
    days_left = (task.deadline - today).days
    
    # Clamp days_left: 
    # If overdue (negative), treat as 0 days left (max urgency).
    # If > 30 days, treat as 30 (min urgency for this factor).
    effective_days = max(0, min(days_left, 30))
    
    urgency = 1 - (effective_days / 30)
    importance_score = task.importance / 5
    # Clamp effort to max 480 minutes for normalization
    effort_score = 1 - (min(task.effort, 480) / 480)
    # Clamp dependencies to max 5
    dep_score = min(task.dependencies, 5) / 5

    # Weighted sum
    score = (0.4 * urgency +
             0.3 * importance_score +
             0.15 * effort_score +
             0.1 * dep_score)
    return score

def prioritize_tasks(task_list: List[Task]) -> List[Task]:
    """Calculates scores for all tasks and sorts them by priority."""
    for task in task_list:
        task.score = compute_priority(task)
    return sorted(task_list, key=lambda x: x.score, reverse=True)

def main():
    print("==========================================")
    print("         Task Priority Calculator         ")
    print("==========================================")
    
    tasks = []
    while True:
        try:
            num_tasks_input = input("Enter number of tasks: ").strip()
            if not num_tasks_input: continue
            n = int(num_tasks_input)
            if n > 0: break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(n):
        print(f"\n--- Task {i+1} ---")
        name = input("Task name: ").strip()
        if not name: name = f"Task {i+1}"
        
        deadline = get_valid_date("Enter deadline (DD-MM-YYYY): ")
        importance = get_valid_int("Importance (1-5): ", 1, 5)
        effort = get_valid_int("Effort in minutes (0-480): ", 0, 480)
        dependencies = get_valid_int("Dependencies count (0-5): ", 0, 5)

        task = Task(name, deadline, importance, effort, dependencies)
        tasks.append(task)

    result = prioritize_tasks(tasks)

    print("\n\n===== PRIORITIZED TASK LIST =====")
    # Header
    print(f"{'Rank':<5} | {'Task Name':<20} | {'Deadline':<12} | {'Imp':<3} | {'Score':<6}")
    print("-" * 60)
    
    for idx, t in enumerate(result, 1):
        print(f"{idx:<5} | {t.name[:20]:<20} | {t.deadline.strftime('%d-%m-%Y'):<12} | {t.importance:<3} | {t.score:.3f}")

if __name__ == "__main__":
    main()
