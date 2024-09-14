from manim import *

# Функция для считывания функции из файла
def read_function_from_file(file_path):
    with open(file_path, 'r') as file:
        function_code = file.read().strip()
    return eval(f"lambda x: {function_code}")

class PlotFunction(Scene):
    def construct(self):
        # Создаем координатную плоскость
        plane = NumberPlane()
        self.add(plane)

        # Читаем функцию из файла
        func = read_function_from_file('rendering_queue.txt')

        # Создаем график функции
        graph = plane.plot(lambda x: func(x), color=BLUE)

        # Добавляем график на сцену
        self.add(graph)
        self.wait(2)


