import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont
from jarvis_worker import JarvisWorker

class OrbWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.radius = 90
        self.growing = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):
        if self.growing:
            self.radius += 1
            if self.radius >= 105:
                self.growing = False
        else:
            self.radius -= 1
            if self.radius <= 90:
                self.growing = True

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() // 2
        center_y = self.height() // 2

        # Outer Glow
        for i in range(10):
            alpha = 20 - (i * 2)

            painter.setBrush(
                QColor(0, 200, 255, max(alpha, 0))
            )

            painter.setPen(Qt.NoPen)

            painter.drawEllipse(
                center_x - (self.radius + i * 8),
                center_y - (self.radius + i * 8),
                (self.radius + i * 8) * 2,
                (self.radius + i * 8) * 2
            )

        # Main Circle
        painter.setBrush(QColor(0, 180, 255))
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            center_x - self.radius,
            center_y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        # Inner Circle
        painter.setBrush(QColor(5, 10, 20))

        painter.drawEllipse(
            center_x - self.radius + 20,
            center_y - self.radius + 20,
            (self.radius * 2) - 40,
            (self.radius * 2) - 40
        )


class JarvisUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS AI")
        self.setFixedSize(1000, 700)

        self.setStyleSheet("""
            background-color: #05070D;
        """)

        self.init_ui()

    def init_ui(self):

        self.title = QLabel("JARVIS", self)

        self.title.setGeometry(390, 20, 300, 60)

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setFont(QFont("Segoe UI", 26, QFont.Bold))

        self.title.setStyleSheet("""
            color: white;
        """)

        self.orb = OrbWidget()
        self.orb.setParent(self)

        self.orb.setGeometry(250, 120, 500, 350)

        self.status = QLabel("READY", self)

        self.status.setGeometry(300, 500, 400, 50)

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setFont(QFont("Segoe UI", 18, QFont.Bold))

        self.status.setStyleSheet("""
            color: #00D4FF;
        """)

        self.footer = QLabel(
            "AI Assistant Online",
            self
        )

        self.footer.setGeometry(350, 620, 300, 30)

        self.footer.setAlignment(Qt.AlignCenter)

        self.footer.setStyleSheet("""
            color: gray;
            font-size: 14px;
        """)
        self.worker = JarvisWorker()

        self.worker.statusChanged.connect(
            self.set_status
        )

        self.worker.responseGenerated.connect(
            self.show_response
        )

        self.worker.start()

    def set_status(self, text):
        self.status.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = JarvisUI()
    window.show()

    sys.exit(app.exec_())