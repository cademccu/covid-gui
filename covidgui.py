from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys


# UI file containing gui information
ui_file = "design.ui"

Ui_MainWindow, QtBaseClasses = uic.loadUiType(ui_file)




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            self.setupUi(self)








# Main method
def main():
    main_window = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(main_window.exec_())


# Call to main method
if __name__ == "__main__":
    main()
