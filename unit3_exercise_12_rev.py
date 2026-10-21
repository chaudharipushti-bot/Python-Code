# 3.12 Combined DS Program
todo_list_value = []

def add_task_value(task_name_value, tags_set_value):
    task_value = {
        "task": task_name_value,
        "tags": set(tags_set_value)
    }
    todo_list_value.append(task_value)

def display_all_value():
    print("\n--- All To-Do Tasks ---")
    for idx_value, item_value in enumerate(todo_list_value, start=1):
        tags_str_value = ", ".join(item_value['tags'])
        print(f"{idx_value}. Task: {item_value['task']:<25} | Tags: [{tags_str_value}]")

def find_by_tag_value(search_tag_value):
    print(f"\n--- Tasks tagged with '{search_tag_value}' ---")
    matched_value = [t_value['task'] for t_value in todo_list_value if search_tag_value in t_value['tags']]
    if matched_value:
        for t_value in matched_value:
            print(f"  - {t_value}")
    else:
        print("  No tasks found for this tag.")


# Demonstration
add_task_value("Submit Assignment", {"college", "urgent"})
add_task_value("Buy Groceries", {"personal", "shopping"})
add_task_value("Prepare Presentation", {"college", "work"})

display_all_value()
find_by_tag_value("college")
find_by_tag_value("shopping")