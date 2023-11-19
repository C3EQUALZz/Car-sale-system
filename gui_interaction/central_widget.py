from PyQt6 import QtWidgets


class MyCentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)
        button1 = QtWidgets.QPushButton("Button 1", self)
        button2 = QtWidgets.QPushButton("Button 2", self)

        layout.addWidget(button1)
        layout.addWidget(button2)

        # Устанавливаем objectName для центрального виджета
        self.setObjectName("myCentralWidget")
