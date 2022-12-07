from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget

app = QApplication([])
window = QWidget()
window.setFixedWidth(400)
window.setFixedHeight(600)
window.setWindowTitle("Система управління бібліотекою")
layout = QVBoxLayout()

art_alb = QLabel()
art_alb.setText("Перевірка")
layout.addWidget(art_alb, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)

window.show()
app.exec()
