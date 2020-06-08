import sys
import cv2
import os.path 
import pathlib
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from UI import ProjectUI


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = ProjectUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.showvideo.setScene(self.showImage("kirito.jpg"))
        self.ui.loadfilebutton.clicked.connect(self.loadEvent)
        self.ui.scalelevel.sliderReleased.connect(self.debug)

    def debug(self):
        print("Starburststream")
        print(self.ui.savebutton.setVisible(False))

    def loadEvent(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.ui.showvideo.setScene(self.showImage(fileName))

    def showImage(self, path):
        if path.split("/")[0] == "C:":
            img = cv2.imread(os.path.relpath(path), cv2.IMREAD_UNCHANGED)
        else:
            # print(path)
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_height, img_width, gar = img.shape

        image_disp = QtGui.QImage(img, img_width, img_height, QtGui.QImage.Format_RGB888)

        pixMap = QtGui.QPixmap.fromImage(image_disp)
        item = QtWidgets.QGraphicsPixmapItem(pixMap)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        return scene

# need to read video
# how to display on GUI?
# final Merge

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()

# img = cv2.imread("kirito.jpg")
# cv2.imshow("", img)
# cv2.waitKey(0)\
# cv2.destroyAllWindows()

sys.exit(app.exec_())
