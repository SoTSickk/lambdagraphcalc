import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QFont

class Lambda(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda")
        self.setGeometry(100, 100, 1280, 720)

        self.setStyleSheet("background-color: rgb(11, 11, 11);")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        hbox_layout = QHBoxLayout()
        main_layout.addLayout(hbox_layout)

        self.display = QLabel()
        self.display.setFixedSize(600, 240)
        self.display.setStyleSheet("color: white; background-color: rgb(0, 0, 0);")
        font = QFont("Segoe UI", 32)
        self.display.setFont(font)
        hbox_layout.addWidget(self.display)

        self.secondary_display = QLabel()
        self.secondary_display.setFixedSize(600, 240)
        self.secondary_display.setStyleSheet("color: white; background-color: rgb(0, 0, 0);")
        self.secondary_display.setFont(font)
        hbox_layout.addWidget(self.secondary_display)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)
        main_layout.addLayout(grid_layout)

        buttons = [
            ('add1', '1'), ('add2', '2'), ('add3', '3'),
            ('add4', '4'), ('add5', '5'), ('add6', '6'),
            ('add7', '7'), ('add8', '8'), ('add9', '9'),
            ('add0', '0'), ('plus', '+'), ('minus', '-'),
            ('times', '*'), ('division', '/'), ('equals', '='),
            ('addpoint', '.'), ('addx', 'x'), ('addy', 'y'),
            ('power', '^'), ('cancel', '<---')
        ]

        positions = [(i // 4, i % 4) for i in range(len(buttons))]

        for i, (name, text) in enumerate(buttons):
            button = QPushButton(text)
            button.setStyleSheet(f"background-color: rgb(47, 47, 47); color: white; font-size: 20pt;")
            button.setFixedSize(1280 // 4, 240 // 5)

            if name == 'cancel':
                button.clicked.connect(self.cancel_text)
            elif name == 'power':
                button.clicked.connect(lambda checked, t=text: self.add_text(t))
            else:
                button.clicked.connect(lambda checked, t=text: self.add_text(t))

            grid_layout.addWidget(button, *positions[i])

        render_button = QPushButton("Render")
        render_button.setStyleSheet("background-color: rgb(47, 47, 47); color: white; font-size: 20pt;")
        render_button.setFixedSize(300, 240 // 5)
        render_button.clicked.connect(self.render_text)

        main_layout.addWidget(render_button)

    def add_text(self, text):
        current_text = self.display.text()
        self.display.setText(current_text + text)

    def cancel_text(self):
        current_text = self.display.text()
        if current_text:
            new_text = current_text[:-1]
            self.display.setText(new_text)

    def render_text(self):
        with open("rendering_queue.txt", "w") as file:
            file.write(self.display.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Lambda()
    window.show()
    sys.exit(app.exec())
