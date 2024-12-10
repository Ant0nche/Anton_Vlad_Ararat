import sqlite3

def setup_database():
    # Подключение к SQLite и создание файла базы данных, если он не существует
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # Создание таблицы users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role_id INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Проверка наличия данных в таблице
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # Если таблица пуста, добавляем тестовых пользователей
        cursor.executemany("""
            INSERT INTO users (first_name, last_name, login, password, role_id)
            VALUES (?, ?, ?, ?, ?)
        """, [
            ("Админ", "Админ", "admin", "admin", 1),
            ("Иван", "Иванов", "user1", "user1", 3),
            ("Модер", "Модеров", "moder", "moder", 2),
        ])
        print("Тестовые данные успешно добавлены.")
    else:
        print("Таблица 'users' уже содержит данные. Добавление пропущено.")

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print("База данных успешно создана и готова к использованию.")

if __name__ == "__main__":
    setup_database()
