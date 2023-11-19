import os
import sys

from PyQt6 import QtWidgets, QtGui

from .central_widget import MyCentralWidget


class MainFrame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainFrame")
        self._initialization_ui()
        self.setCentralWidget(MyCentralWidget())

    def _initialization_ui(self) -> None:
        self.setWindowTitle("Car Registration")
        self.setWindowIcon(QtGui.QIcon(self.path_to_icon("icons/icons8-app.svg")))
        self._set_geometry_app()

    @staticmethod
    def path_to_icon(path: str) -> str:
        # Получаем путь к текущему скрипту
        script_path = os.path.dirname(os.path.abspath(__file__))
        # Строим полный путь к иконке
        icon_path = os.path.join(script_path, path)
        return icon_path

    def _set_geometry_app(self) -> None:
        # Фиксированные размеры
        preferred_width, preferred_height = 850, 500

        # Получаем текущее разрешение экрана
        screen_resolution = QtGui.QGuiApplication.primaryScreen()

        # Определяем коэффициент масштабирования как минимальный из двух
        scale_factor = min(preferred_width, screen_resolution.availableGeometry().width()) / preferred_width

        # Устанавливаем новый размер окна
        self.setFixedSize(*map(lambda x: int(x * scale_factor), (preferred_width, preferred_height)))
        self._center()

    def _center(self) -> None:
        """
        Метод, который центрует положения появления окна при запуске.
        """
        # Здесь qr представляет собой прямоугольник, который определяет геометрию (размер и положение)
        # главного окна (вашего QMainWindow) до того, как оно отобразится на экране.
        # Этот прямоугольник инициализируется текущими размерами и позицией окна.
        qr = self.frameGeometry()
        # Здесь вы получаете геометрию текущего доступного экрана (часть экрана, доступная для приложения)
        # и затем находите центр этой геометрии. Это определяет центр экрана.
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        # Теперь мы перемещаем прямоугольник qr так, чтобы его центр совпадал с центром экрана,
        # который мы определили в шаге 2.
        qr.moveCenter(cp)
        # Затем мы перемещаем окно (self) так, чтобы его верхний левый угол находился в верхнем левом углу
        # прямоугольника qr. Таким образом, окно становится центрированным относительно экрана.
        self.move(qr.topLeft())

    def closeEvent(self, event) -> None:
        """
        Диалоговое окно, оно появляется, когда пользователь хочет закрыть приложение
        """
        res = QtWidgets.QMessageBox.question(
            self,
            "Выход",
            "Вы точно уверены, что хотите выйти?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if res == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()  # Игнорируем событие закрытия приложения
        else:
            sys.exit(0)
