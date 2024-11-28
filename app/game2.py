tasks = []


def display_menu():
    print("\n=== Трекер задач ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")


def show_tasks():
    if not tasks:
        print("Ваш список задач пуст!")
    else:
        print("\nСписок задач:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")


def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Введите номер задачи для удаления: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Задача '{removed_task}' удалена.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Введите корректный номер.")


def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-4): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Пожалуйста, выберите корректный пункт меню.")


if __name__ == "__main__":
    main()


