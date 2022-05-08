import sys
import Demo

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Demo.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
