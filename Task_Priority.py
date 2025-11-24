import datetime

class TodoItem:
    def __init__(self, title, date_obj, level, mins, deps):
        self.title = title
        self.due_date = date_obj
        self.level = level          # 1-5
        self.minutes = mins
        self.deps = deps
        self.total_score = 0

def ask_date(msg):
    # Keep asking until we get a real date
    while True:
        val = input(msg).strip()
        try:
            # user types DD/MM/YYYY
            parts = val.split('/')
            d = int(parts[0])
            m = int(parts[1])
            y = int(parts[2])
            return datetime.date(y, m, d)
        except:
            print("Error: Please type date as DD/MM/YYYY")

def ask_number(msg, bottom, top):
    while True:
        try:
            user_in = input(msg)
            num = int(user_in)
            if num >= bottom and num <= top:
                return num
            else:
                print(f"Number must be between {bottom} and {top}")
        except ValueError:
            print("That's not a number.")

def calculate_score(item):
    # 1. Urgency (How close is the deadline?)
    now = datetime.date.today()
    diff = (item.due_date - now).days
    
    # If it's already passed, it's super urgent
    if diff < 0:
        diff = 0
    # Cap it at 30 days out
    if diff > 30:
        diff = 30
        
    urgency_val = 1 - (diff / 30)

    # 2. Importance
    imp_val = item.level / 5

    # 3. Effort (Less effort = higher priority to clear list)
    # Cap at 8 hours (480 mins)
    m = item.minutes
    if m > 480:
        m = 480
    eff_val = 1 - (m / 480)

    # 4. Dependencies
    d = item.deps
    if d > 5:
        d = 5
    dep_val = d / 5

    # Combine them with weights
    final = (urgency_val * 0.40) + (imp_val * 0.30) + (eff_val * 0.15) + (dep_val * 0.15)
    return final

def main():
    print("--- Task Sorter ---")
    
    my_tasks = []
    
    while True:
        try:
            count_str = input("How many tasks do you have? ")
            count = int(count_str)
            if count > 0:
                break
        except:
            print("Just enter a positive number.")

    for i in range(count):
        print(f"\nDetails for Task #{i+1}")
        t_name = input("Name: ")
        if t_name == "":
            t_name = "Untitled"
            
        d_date = ask_date("Deadline (DD/MM/YYYY): ")
        imp = ask_number("Importance (1-5): ", 1, 5)
        eff = ask_number("Minutes needed (0-480): ", 0, 480)
        dep = ask_number("Dependencies (0-5): ", 0, 5)
        
        new_task = TodoItem(t_name, d_date, imp, eff, dep)
        # Calc score immediately
        new_task.total_score = calculate_score(new_task)
        my_tasks.append(new_task)

    # Sort the list based on score, highest first
    my_tasks.sort(key=lambda x: x.total_score, reverse=True)

    print("\n\nTODO LIST (Sorted)")
    print("-" * 50)
    print(f"{'#':<4} {'Task':<20} {'Date':<12} {'Score'}")
    print("-" * 50)

    for idx, t in enumerate(my_tasks):
        d_str = t.due_date.strftime("%d/%m/%Y")
        print(f"{idx+1:<4} {t.title:<20} {d_str:<12} {t.total_score:.2f}")

if __name__ == "__main__":
    main()
