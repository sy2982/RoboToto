import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from main import initialize_servos, home, moves
import board
import neopixel

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RoboToto")
        self.setGeometry(100, 100, 300, 200)

        self.servo = initialize_servos()

        layout = QVBoxLayout()

        self.home_button = QPushButton("Home", self)
        self.home_button.clicked.connect(self.home_action)
        layout.addWidget(self.home_button)

        self.move_button = QPushButton("Move", self)
        self.move_button.clicked.connect(self.move_action)
        layout.addWidget(self.move_button)
        
        self.rabbit_button = QPushButton("Rabbit", self)
        self.rabbit_button.clicked.connect(self.rabbit_action)
        layout.addWidget(self.rabbit_button)

        self.dance_button = QPushButton("Dance", self)
        self.dance_button.clicked.connect(self.dance_action)
        layout.addWidget(self.dance_button)

        self.wave_button = QPushButton("Wave", self)
        self.wave_button.clicked.connect(self.wave_action)
        layout.addWidget(self.wave_button)
        
        self.police_button = QPushButton("Police Chase", self)
        self.police_button.clicked.connect(self.police_action)
        layout.addWidget(self.police_button)

        self.setLayout(layout)

    def home_action(self):
        subprocess.Popen(['sudo', 'python3', 'LedHome.py'])
        home(self.servo)

    def move_action(self):
        moves(self.servo, "move")
        
    def rabbit_action(self):
        moves(self.servo, "rabbit")

    def dance_action(self):
        subprocess.Popen(['sudo', 'python3', 'LedDance.py'])
        moves(self.servo, "dance")

    def wave_action(self):
        moves(self.servo, "wave")
        
    def police_action(self):
        subprocess.Popen(['sudo', 'python3', 'LedPolice.py'])
        moves(self.servo, "rabbit")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec_())
