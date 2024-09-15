import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl


class Lambda(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lambda")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: rgb(25, 25, 25);")
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        hbox_layout = QHBoxLayout()
        main_layout.addLayout(hbox_layout)
        self.display = QLabel()
        self.display.setFixedSize(600, 240)
        self.display.setStyleSheet("color: white; background-color: rgb(0, 0, 0); border-radius: 20px")
        font = QFont("Segoe UI", 32)
        self.display.setFont(font)
        hbox_layout.addWidget(self.display)
        self.video_widget = QVideoWidget()
        self.video_widget.setFixedSize(854, 480)
        self.video_widget.setStyleSheet("background-color: black;")
        hbox_layout.addWidget(self.video_widget)
        self.media_player = QMediaPlayer()
        audio_output = QAudioOutput()
        self.media_player.setAudioOutput(audio_output)
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setLoops(QMediaPlayer.Infinite)
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
            ('power', '**'), ('cancel', 'C')
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
        self.media_player.stop()
        with open("rendering_queue.txt", "w") as file:
            file.write(self.display.text())
        try:
            subprocess.run(["manim", "-ql", "anim_render.py", "rendering"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении рендеринга: {e}")
        with open("rendering_queue.txt", "w") as file:
            file.write("")
        video_url = QUrl.fromLocalFile("media/videos/anim_render/480p15/rendering.mp4")
        self.media_player.setSource(video_url)
        self.media_player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Lambda()
    window.show()
    sys.exit(app.exec())
