import tkinter as tk
from tkinter import messagebox
import random
import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def generate_random_data(size, unique_values=False):
    if unique_values:
        num_unique = max(1, size // 10)
        unique_vals = random.sample(range(1, size + 1), num_unique)
        return [random.choice(unique_vals) for _ in range(size)]
    else:
        return [random.randint(1, 10000) for _ in range(size)]


def sort_and_display():
    try:
        size = int(size_entry.get())
        if size <= 0:
            raise ValueError("Размер должен быть положительным.")
        
        data_type = data_type_var.get()
        if data_type == "вводимый":
            input_data = input_data_entry.get()
            arr = list(map(int, input_data.split()))
            if len(arr) != size:
                raise ValueError("Количество элементов не соответствует заданному размеру.")
        else:
            unique_values = unique_values_var.get()
            arr = generate_random_data(size, unique_values)

        original_arr = arr.copy()
        
        # Измерение времени сортировки
        start_time = time.time()
        sorted_arr = shell_sort(arr.copy())
        end_time = time.time()
        
        elapsed_time = end_time - start_time

        if size <= 10:
            result_text = f"Исходный вектор: {original_arr}\nОтсортированный вектор: {sorted_arr}"
        else:
            result_text = f"Исходный вектор: {original_arr[:25]}... (всего {len(original_arr)})\n" \
                          f"Отсортированный вектор: {sorted_arr[:25]}... (всего {len(sorted_arr)})"

        result_label.config(text=result_text)
        time_label.config(text=f"Время сортировки: {elapsed_time:.6f} секунд")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

# Создание основного окна
root = tk.Tk()
root.title("Сортировка Шелла")

# Ввод размера вектора
size_label = tk.Label(root, text="Введите размер вектора:")
size_label.pack()
size_entry = tk.Entry(root)
size_entry.pack()

# Выбор типа данных
data_type_var = tk.StringVar(value="вводимый")
data_type_label = tk.Label(root, text="Выберите тип данных:")
data_type_label.pack()
input_radio = tk.Radiobutton(root, text="Вводимый", variable=data_type_var, value="вводимый")
input_radio.pack()
generated_radio = tk.Radiobutton(root, text="Сгенерированный", variable=data_type_var, value="сгенерированный")
generated_radio.pack()

# Ввод данных
input_data_label = tk.Label(root, text="Введите элементы вектора (через пробел):")
input_data_label.pack()
input_data_entry = tk.Entry(root)
input_data_entry.pack()

# Выбор уникальных значений
unique_values_var = tk.BooleanVar()
unique_values_check = tk.Checkbutton(root, text="Случайные данные с малым числом уникальных значений", variable=unique_values_var)
unique_values_check.pack()

# Кнопка сортировки
sort_button = tk.Button(root, text="Сортировать", command=sort_and_display)
sort_button.pack()

# Метка для вывода результата
result_label = tk.Label(root, text="")
result_label.pack()

# Метка для вывода времени сортировки
time_label = tk.Label(root, text="")
time_label.pack()

# Запуск основного цикла
root.mainloop()
