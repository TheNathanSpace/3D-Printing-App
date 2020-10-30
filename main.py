import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from ui.main_ui import Ui_Printing
from change_screen import ChangeScreen
from ui.uses_ui import Ui_Uses
from ui.plastic_ui import Ui_Plastic


# pyrcc5 C:\Users\wasab\Documents\images.qrc -o resource_rc.py
# pyuic5 mydesign.ui -o mydesign.py
# https://likegeeks.com/pyqt5-tutorial/#Install-PyQt5-designer

# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

class MainWindow(QtWidgets.QWidget):

    def __init__(self, change_screen):
        super(MainWindow, self).__init__()
        self.ui = Ui_Printing(change_screen)
        self.ui.setupUi(self)


class UsesWindow(QtWidgets.QWidget):

    def __init__(self, change_screen):
        super(UsesWindow, self).__init__()
        self.ui = Ui_Uses(change_screen)
        self.ui.setupUi(self)

    def updateSelf(self, object):
        self.ui.updateSelf(object)


class PlasticWindow(QtWidgets.QWidget):

    def __init__(self, change_screen):
        super(PlasticWindow, self).__init__()
        self.ui = Ui_Plastic(change_screen)
        self.ui.setupUi(self)

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

    sys.exit(app.exec())
