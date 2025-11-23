# VItyarthiProject
# Task Priority Calculator

A Python CLI tool to help you prioritize your tasks based on urgency, importance, effort, and dependencies.

## Features
- **Smart Scoring**: Calculates a priority score (0-1) for each task.
- **Input Validation**: Robust handling of dates and numbers.
- **Formatted Output**: Displays a clean, sorted table of tasks.

## Usage
1. Run the script:
   ```bash
   python Task_Priority.py
   ```
2. Enter the number of tasks.
3. For each task, provide:
   - Name
   - Deadline (DD-MM-YYYY)
   - Importance (1-5)
   - Effort (minutes)
   - Dependency count

## How it Works
The priority score is a weighted sum of:
- **Urgency (40%)**: Based on days remaining.
- **Importance (30%)**: User-defined level (1-5).
- **Effort (15%)**: Lower effort gets a higher score.
- **Dependencies (10%)**: More dependencies slightly increase priority (critical path).
