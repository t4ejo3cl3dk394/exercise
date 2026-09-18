tasks = []

def add_task(name):
    tasks.append(name)

def delete_task(name):
    # 依名稱在清單中搜尋，找不到時印出提示
    if name not in tasks:
        print(f"'{name}' not found, nothing to delete")
        return
    tasks.remove(name)

def show_tasks():
    # 注意：這裡標題故意改用 remaining
    print(f"=== To-Do List ({len(tasks)} remaining) ===")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def main():
    add_task("Learn Git")
    show_tasks()
    delete_task("Learn Git")
    show_tasks()
    delete_task("Not Exist")
    show_tasks()

if __name__ == "__main__":
    main()