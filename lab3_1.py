import tkinter as tk
import math

class Function:
    def __init__(self, name):
        self.name = name

    def value(self, x):
        raise NotImplementedError("Метод value должен быть реализован в подклассе.")

    def derivative(self):
        raise NotImplementedError("Метод derivative должен быть реализован в подклассе.")

class Arctan(Function):
    def __init__(self):
        super().__init__("Arctan")

    def value(self, x):
        return math.atan(x)

    def derivative(self):
        return Derivative(self)

class Arccot(Function):
    def __init__(self):
        super().__init__("Arccot")

    def value(self, x):
        return math.atan(1/x) if x != 0 else float('inf')

    def derivative(self):
        return Derivative(self)

class Derivative:
    def __init__(self, function):
        self.function = function

    def value(self, x):
        if isinstance(self.function, Arctan):
            return 1 / (1 + x**2)
        elif isinstance(self.function, Arccot):
            return -1 / (1 + (1/x)**2) * (-1/x**2) if x != 0 else float('inf')
        else:
            raise ValueError("Неизвестная функция для производной.")

class FunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Функции и производные")

        self.arctan_func = Arctan()
        self.arccot_func = Arccot()

        self.label = tk.Label(root, text="Введите значение x:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.calculate_button = tk.Button(root, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            x_value = float(self.entry.get())
            arctan_value = self.arctan_func.value(x_value)
            arccot_value = self.arccot_func.value(x_value)

            arctan_derivative = self.arctan_func.derivative().value(x_value)
            arccot_derivative = self.arccot_func.derivative().value(x_value)

            result = (
                f"Arctan({x_value}) = {arctan_value}\n"
                f"Производная Arctan({x_value}) = {arctan_derivative}\n"
                f"Arccot({x_value}) = {arccot_value}\n"
                f"Производная Arccot({x_value}) = {arccot_derivative}"
            )
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionApp(root)
    root.mainloop()
