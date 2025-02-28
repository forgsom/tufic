import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def increase_pages(self):
        self.pages += 10
        return self.pages

    def decrease_price(self):
        if self.pages > 100:
            self.price /= 2
        return self.price

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Manager")

        self.book = Book("Пример книги", 95, 20.0)

        self.title_label = tk.Label(root, text="Название книги:")
        self.title_label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.insert(0, self.book.title)
        self.title_entry.pack()

        self.pages_label = tk.Label(root, text="Количество страниц:")
        self.pages_label.pack()

        self.pages_entry = tk.Entry(root)
        self.pages_entry.insert(0, self.book.pages)
        self.pages_entry.pack()

        self.price_label = tk.Label(root, text="Цена:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.insert(0, self.book.price)
        self.price_entry.pack()

        self.increase_button = tk.Button(root, text="Увеличить страницы на 10", command=self.increase_pages)
        self.increase_button.pack()

        self.decrease_button = tk.Button(root, text="Уменьшить цену", command=self.decrease_price)
        self.decrease_button.pack()

    def increase_pages(self):
        new_pages = self.book.increase_pages()
        self.pages_entry.delete(0, tk.END)
        self.pages_entry.insert(0, new_pages)
        messagebox.showinfo("Информация", f"Количество страниц увеличено до: {new_pages}")

    def decrease_price(self):
        new_price = self.book.decrease_price()
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, new_price)
        messagebox.showinfo("Информация", f"Цена изменена до: {new_price}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
