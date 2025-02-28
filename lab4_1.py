import tkinter as tk
from tkinter import messagebox, simpledialog
import csv

class Teacher:
    def __init__(self, name, department, position):
        self.name = name
        self.department = department
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.department}, {self.position}"

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher_name):
        self.teachers = [t for t in self.teachers if t.name != teacher_name]

    def get_teacher_count(self):
        return len(self.teachers)

    def __str__(self):
        return f"{self.name} (Преподаватели: {self.get_teacher_count()})"

class University:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            return True
        return False

    def add_teacher(self, department_name, teacher_name, position):
        if department_name in self.departments:
            teacher = Teacher(teacher_name, department_name, position)
            self.departments[department_name].add_teacher(teacher)
            return True
        return False

    def remove_teacher(self, department_name, teacher_name):
        if department_name in self.departments:
            self.departments[department_name].remove_teacher(teacher_name)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ФИО преподавателя", "Кафедра", "Должность"])
            for department in self.departments.values():
                for teacher in department.teachers:
                    writer.writerow([teacher.name, teacher.department, teacher.position])

    def load_from_csv(self, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовок
            for row in reader:
                teacher_name, department_name, position = row
                self.add_department(department_name)
                self.add_teacher(department_name, teacher_name, position)

class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление кафедрами и преподавателями")
        self.university = University()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.add_department_button = tk.Button(self.frame, text="Добавить кафедру", command=self.add_department)
        self.add_department_button.pack(fill=tk.X)

        self.add_teacher_button = tk.Button(self.frame, text="Добавить преподавателя", command=self.add_teacher)
        self.add_teacher_button.pack(fill=tk.X)

        self.remove_teacher_button = tk.Button(self.frame, text="Удалить преподавателя", command=self.remove_teacher)
        self.remove_teacher_button.pack(fill=tk.X)

        self.show_departments_button = tk.Button(self.frame, text="Показать кафедры", command=self.show_departments)
        self.show_departments_button.pack(fill=tk.X)

        self.save_button = tk.Button(self.frame, text="Сохранить в CSV", command=self.save_to_csv)
        self.save_button.pack(fill=tk.X)

        self.load_button = tk.Button(self.frame, text="Загрузить из CSV", command=self.load_from_csv)
        self.load_button.pack(fill=tk.X)

    def add_department(self):
        department_name = simpledialog.askstring("Добавить кафедру", "Введите название кафедры:")
        if department_name:
            if self.university.add_department(department_name):
                messagebox.showinfo("Успех", f"Кафедра '{department_name}' добавлена.")
            else:
                messagebox.showwarning("Ошибка", f"Кафедра '{department_name}' уже существует.")

    def add_teacher(self):
        department_name = simpledialog.askstring("Добавить преподавателя", "Введите название кафедры:")
        teacher_name = simpledialog.askstring("Добавить преподавателя", "Введите ФИО преподавателя:")
        position = simpledialog.askstring("Добавить преподавателя", "Введите должность преподавателя:")
        if department_name and teacher_name and position:
            if self.university.add_teacher(department_name, teacher_name, position):
                messagebox.showinfo("Успех", f"Преподаватель '{teacher_name}' добавлен в кафедру '{department_name}'.")
            else:
                messagebox.showwarning("Ошибка", f"Кафедра '{department_name}' не найдена.")

    def remove_teacher(self):
        department_name = simpledialog.askstring("Удалить преподавателя", "Введите название кафедры:")
        teacher_name = simpledialog.askstring("Удалить преподавателя", "Введите ФИО преподавателя для удаления:")
        if department_name and teacher_name:
            self.university.remove_teacher(department_name, teacher_name)
            messagebox.showinfo("Успех", f"Преподаватель '{teacher_name}' удален из кафедры '{department_name}'.")

    def show_departments(self):
        departments_info = "\n".join(str(department) for department in self.university.departments.values())
        if departments_info:
            messagebox.showinfo("Кафедры", departments_info)
        else:
            messagebox.showinfo("Кафедры", "Нет доступных кафедр.")

    def save_to_csv(self):
        filename = simpledialog.askstring("Сохранить в CSV", "Введите имя файла (например, data.csv):")
        if filename:
            self.university.save_to_csv(filename)
            messagebox.showinfo("Успех", f"Данные сохранены в '{filename}'.")

    def load_from_csv(self):
        filename = simpledialog.askstring("Загрузить из CSV", "Введите имя файла (например, data.csv):")
        if filename:
            self.university.load_from_csv(filename)
            messagebox.showinfo("Успех", f"Данные загружены из '{filename}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()
