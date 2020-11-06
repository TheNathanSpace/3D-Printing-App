import sys
import inspect

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from ui.main_ui import Ui_Printing
from change_screen import ChangeScreen
from ui.uses_ui import Ui_Uses
from ui.plastic_ui import Ui_Plastic


# Convert resource to .py:
# pyrcc5 C:\Users\wasab\Documents\images.qrc -o resource_rc.py

# Convert UI to .py:
# pyuic5 mydesign.ui -o mydesign.py


# pyinstaller -F --upx-dir "D:\Programs\upx-3.96-win64" -p "C:/Users/wasab/PycharmProjects/3D_printing_packager/venv27/Lib/site-packages" "main restart.spec"

# pyinstaller -n "main yeet" -i "3d printer icon 64.ico" --upx-dir "D:\Programs\upx-3.96-win64" --upx-exclude "vcruntime140.dll" --hidden-import "PyQt5" --hidden-import "QtWidgets" --clean main.py

# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

class MainWindow(QWidget):

    def __init__(self, change_screen):
        super(MainWindow, self).__init__()
        self.setStyleSheet(open("resources/stylesheet.css").read())

        self.ui = Ui_Printing(change_screen)
        self.ui.setupUi(self)

    def center(self):
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


class UsesWindow(QWidget):

    def __init__(self, change_screen):
        super(UsesWindow, self).__init__()
        self.setStyleSheet(open("resources/stylesheet.css").read())

        self.ui = Ui_Uses(change_screen)
        self.ui.setupUi(self)

    def center(self):
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def updateSelf(self, object):
        self.ui.updateSelf(object)


class PlasticWindow(QWidget):

    def __init__(self, change_screen):
        super(PlasticWindow, self).__init__()
        self.setStyleSheet(open("resources/stylesheet.css").read())

        self.ui = Ui_Plastic(change_screen)
        self.ui.setupUi(self)

    def center(self):
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def updateSelf(self, object):
        self.ui.updateSelf(object)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon(":/images/3d printer icon.png"))

    change_screen = ChangeScreen()

    main_window = MainWindow(change_screen)
    main_window.setWindowTitle("3D Printing")
    main_window.show()

    uses_window = UsesWindow(change_screen)
    uses_window.updateSelf(uses_window)
    uses_window.setWindowTitle("3D Printing - Uses")

    plastics_window = PlasticWindow(change_screen)
    plastics_window.updateSelf(plastics_window)
    plastics_window.setWindowTitle("3D Printing - Plastics")

    change_screen.update(main_window, uses_window, plastics_window)

    main_window.center()
    uses_window.center()
    plastics_window.center()

    sys.exit(app.exec())
