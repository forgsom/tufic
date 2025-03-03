import tkinter as tk
from tkinter import colorchooser
import numpy as np
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, master):
        self.master = master
        master.title("График функции y = a * cos(bx) * exp(-cx)")

        self.label_a = tk.Label(master, text="Введите a:")
        self.label_a.pack()
        self.entry_a = tk.Entry(master)
        self.entry_a.pack()

        self.label_b = tk.Label(master, text="Введите b:")
        self.label_b.pack()
        self.entry_b = tk.Entry(master)
        self.entry_b.pack()

        self.label_c = tk.Label(master, text="Введите c:")
        self.label_c.pack()
        self.entry_c = tk.Entry(master)
        self.entry_c.pack()

        self.bg_color_button = tk.Button(master, text="Выбрать цвет фона", command=self.choose_bg_color)
        self.bg_color_button.pack()

        self.graph_color_button = tk.Button(master, text="Выбрать цвет графика", command=self.choose_graph_color)
        self.graph_color_button.pack()

        self.plot_button = tk.Button(master, text="Построить график", command=self.plot_graph)
        self.plot_button.pack()

        self.bg_color = "white"
        self.graph_color = "blue"

    def choose_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.bg_color = color

    def choose_graph_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.graph_color = color

    def plot_graph(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        x = np.linspace(-10, 10, 400)  # Увеличиваем диапазон x для лучшего отображения
        y = a * np.cos(b * x) * np.exp(-c * x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, color=self.graph_color)
        plt.xlim(-10, 10)
        plt.ylim(-1.5 * abs(a), 1.5 * abs(a))  # Устанавливаем пределы Y в зависимости от a
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.title("График функции y = a * cos(bx) * exp(-cx)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.gca().set_facecolor(self.bg_color)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
