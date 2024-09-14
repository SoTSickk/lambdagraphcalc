import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QFont

class Lambda(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda")
        self.setGeometry(100, 100, 1280, 720)

        # Устанавливаем цвет фона через setStyleSheet
        self.setStyleSheet("background-color: rgb(11, 11, 11);")

        # Основной layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Горизонтальный layout для двух QLabel
        hbox_layout = QHBoxLayout()
        main_layout.addLayout(hbox_layout)

        # QLabel для отображения введенного текста
        self.display = QLabel()
        self.display.setFixedSize(600, 240)  # Устанавливаем размер 600x240
        self.display.setStyleSheet("color: white; background-color: rgb(0, 0, 0);")  # Белый текст и черный фон
        font = QFont("Segoe UI", 32)  # Устанавливаем шрифт и его размер
        self.display.setFont(font)
        hbox_layout.addWidget(self.display)

        # Второй QLabel
        self.secondary_display = QLabel()
        self.secondary_display.setFixedSize(600, 240)  # Устанавливаем размер 600x240
        self.secondary_display.setStyleSheet("color: white; background-color: rgb(0, 0, 0);")  # Белый текст и черный фон
        self.secondary_display.setFont(font)
        hbox_layout.addWidget(self.secondary_display)

        # Сетка для кнопок
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Убираем отступы между кнопками
        main_layout.addLayout(grid_layout)

        # Список кнопок с их текстами
        buttons = [
            ('add1', '1'), ('add2', '2'), ('add3', '3'),
            ('add4', '4'), ('add5', '5'), ('add6', '6'),
            ('add7', '7'), ('add8', '8'), ('add9', '9'),
            ('add0', '0'), ('plus', '+'), ('minus', '-'),
            ('times', '*'), ('division', '/'), ('equals', '='),
            ('addpoint', '.'), ('addx', 'x'), ('addy', 'y'),
            ('power', '^'), ('cancel', 'C')
        ]

        # Позиции для размещения кнопок в сетке
        positions = [(i // 4, i % 4) for i in range(len(buttons))]

        # Создаем кнопки и добавляем их в сетку
        for i, (name, text) in enumerate(buttons):
            button = QPushButton(text)
            button.setStyleSheet(f"background-color: rgb(47, 47, 47); color: white; font-size: 20pt;")
            button.setFixedSize(1280 // 4, 240 // 5)  # Устанавливаем размер кнопок

            # Присоединяем обработчик клика для каждой кнопки
            if name == 'cancel':
                button.clicked.connect(self.cancel_text)  # Обработчик для кнопки отмены
            elif name == 'power':
                button.clicked.connect(lambda checked, t=text: self.add_text(t))  # Обработчик для кнопки возведения в степень
            else:
                button.clicked.connect(lambda checked, t=text: self.add_text(t))  # Обработчик для остальных кнопок

            grid_layout.addWidget(button, *positions[i])

        # Кнопка "Render"
        render_button = QPushButton("Render")
        render_button.setStyleSheet("background-color: rgb(47, 47, 47); color: white; font-size: 20pt;")
        render_button.setFixedSize(300, 240 // 5)
        render_button.clicked.connect(self.render_text)  # Присоединяем обработчик для кнопки Render

        main_layout.addWidget(render_button)  # Добавляем кнопку под сеткой кнопок

    def add_text(self, text):
        # Добавляем текст на QLabel
        current_text = self.display.text()
        self.display.setText(current_text + text)

    def cancel_text(self):
        # Удаляем один символ с конца текста
        current_text = self.display.text()
        if current_text:
            new_text = current_text[:-1]
            self.display.setText(new_text)

    def render_text(self):
        # Записываем текст из QLabel в файл
        with open("rendering_queue.txt", "w") as file:
            file.write(self.display.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Lambda()
    window.show()
    sys.exit(app.exec())
