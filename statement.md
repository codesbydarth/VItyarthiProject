# Project Statement: Task Priority Calculator

## Problem Statement
In a busy work or academic environment, individuals often struggle to decide which tasks to tackle first. Subjective decision-making can lead to missed deadlines or focusing on low-impact activities. There is a need for an objective, data-driven tool to calculate task priority based on multiple factors like urgency and importance.

## Scope of the Project
The project involves developing a Command Line Interface (CLI) tool in Python. The tool will:
- Accept user input for multiple tasks.
- Validate input data (dates, integers).
- Compute a priority score using a weighted algorithm.
- Display a sorted list of tasks to help the user plan their work.
The scope is limited to a local, single-session execution without persistent database storage.

## Target Users
- **Students**: To manage assignments and study schedules.
- **Professionals**: To organize daily work tasks and meet project deadlines.
- **Freelancers**: To prioritize client deliverables based on effort and value.

## High-level Features
1.  **Task Input**: User-friendly prompts to collect task details (Name, Deadline, Importance, Effort, Dependencies).
2.  **Input Validation**: Robust error handling to ensure valid dates (DD-MM-YYYY) and numeric values are entered.
3.  **Priority Algorithm**: A smart scoring system that weighs urgency (40%), importance (30%), effort (15%), and dependencies (10%).
4.  **Ranked Output**: A clear, formatted table displaying tasks sorted from highest to lowest priority.
