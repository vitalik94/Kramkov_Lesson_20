#ДЗ на понедельник (Ivanov_Lesson_20.py)
# Вы создаете БД для учета задач в команде разработки.
# Вам необходимо создать базу данных для хранения информации о задачах и их статусе.
# Каждая задача должна иметь уникальный идентификатор, название, описание и статус (выполнена или невыполнена).
#
# Напишите программу на языке Python, которая создает базу данных SQLite,
# добавляет в нее несколько задач и позволяет пользователю получать информацию о задачах.

import sqlite3
with sqlite3.connect('tasks_data.db') as conn:

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT,
    status TEXT)''')

    list_tasks = [('ознакомление', 'ознакомление с задачей, планировка, анализ', 'выполнено'),
    ('дизайн', 'проектирование интерфейса и структуры', 'выполнено'),
    ('декомпозиция', 'разбиение задачи на подзадачи', 'выполнено'),
    ('разработка', 'разработка и написание кода', 'выполнено'),
    ('тестирование', 'проверка задачи на ошибки', 'невыполнено'),
    ('релиз', 'релиз задачи', 'невыполнено'),
    ('мониторинг', 'оценка проделанной работы', 'невыполнено')]

    cursor.executemany('''INSERT INTO tasks(name, description, status) VALUES(?,?,?)''', list_tasks)
    conn.commit()

    cursor.execute('''SELECT * FROM tasks''')
    k = cursor.fetchall()
    print(k)

    cursor.execute('''SELECT * FROM tasks WHERE status='выполнено' ''')
    k = cursor.fetchall()
    print(k)

    cursor.execute('''SELECT * FROM tasks WHERE status='невыполнено' ''')
    k = cursor.fetchall()
    print(k)

    cursor.execute('''SELECT name, status FROM tasks''')
    k = cursor.fetchall()
    print(k)


