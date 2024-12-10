import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel

# Функция для проверки логина и пароля
def authenticate_user():
    login = login_entry.get()
    password = password_entry.get()

    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect("app.db")
        cursor = conn.cursor()

        # Выполнение SQL-запроса для проверки логина и пароля
        cursor.execute("""
            SELECT first_name, last_name FROM users
            WHERE login = ? AND password = ?
        """, (login, password))
        user = cursor.fetchone()
        conn.close()

        # Если пользователь найден, приветствие
        if user:
            messagebox.showinfo("Успех", f"Добро пожаловать, {user[0]} {user[1]}!")
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")
    except Exception as e:
        messagebox.showerror("Ошибка базы данных", f"Ошибка: {str(e)}")

# Функция для добавления нового пользователя
def add_user_window():
    # Открытие нового окна
    add_window = Toplevel(root)
    add_window.title("Добавить пользователя")
    add_window.geometry("450x450")

    # Метки и поля ввода для нового пользователя
    Label(add_window, text="Имя:").pack(pady=5)
    first_name_entry = Entry(add_window)
    first_name_entry.pack(pady=5)

    Label(add_window, text="Фамилия:").pack(pady=5)
    last_name_entry = Entry(add_window)
    last_name_entry.pack(pady=5)

    Label(add_window, text="Логин:").pack(pady=5)
    login_entry = Entry(add_window)
    login_entry.pack(pady=5)

    Label(add_window, text="Пароль:").pack(pady=5)
    password_entry = Entry(add_window, show="*")
    password_entry.pack(pady=5)

    Label(add_window, text="Роль (ID):").pack(pady=5)
    role_id_entry = Entry(add_window)
    role_id_entry.pack(pady=5)

    # Функция для сохранения пользователя в базу данных
    def save_user():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        login = login_entry.get()
        password = password_entry.get()
        role_id = role_id_entry.get()

        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()

            # SQL-запрос для добавления нового пользователя
            cursor.execute("""
                INSERT INTO users (first_name, last_name, login, password, role_id)
                VALUES (?, ?, ?, ?, ?)
            """, (first_name, last_name, login, password, int(role_id)))
            conn.commit()
            conn.close()

            messagebox.showinfo("Успех", "Пользователь успешно добавлен!")
            add_window.destroy()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Ошибка", f"Ошибка добавления: {e}")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректное значение для поля 'Роль (ID)'")

    # Кнопка "Сохранить"
    Button(add_window, text="Сохранить", command=save_user).pack(pady=20)

# Создание основного окна
root = Tk()
root.title("Авторизация")
root.geometry("400x400")

# Метки и поля ввода
Label(root, text="Логин:").pack(pady=5)
login_entry = Entry(root)
login_entry.pack(pady=5)

Label(root, text="Пароль:").pack(pady=5)
password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

# Кнопка "Войти"
login_button = Button(root, text="Войти", command=authenticate_user)
login_button.pack(pady=20)

# Кнопка "Добавить пользователя"
add_user_button = Button(root, text="Добавить пользователя", command=add_user_window)
add_user_button.pack(pady=20)

# Запуск основного цикла приложения
root.mainloop()
