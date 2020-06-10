import sys
import cv2
import os.path 
import pathlib
import copy
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from UI import ProjectUI
from image_process_function import * 


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = ProjectUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = ''
        self.ori_data = ''
        self.fps = 0
        
        self.isGrey = False

        self.readImageFromPath("kirito.jpg")
        self.ori_data = copy.deepcopy(self.data)

        self.ui.showvideo.setScene(self.showImage(self.data[0]))
        self.ui.loadfilebutton.clicked.connect(self.loadEvent)
        self.ui.greylevelbutton.clicked.connect(self.setGrey)
        self.ui.Applybutton.clicked.connect(self.apply)


    def debug(self):
        print("Starburststream")
        print(self.ui.savebutton.setVisible(False))

    def apply(self):
        self.data = self.resizeImage()
        self.ui.showvideo.setScene(self.showImage(self.data[0]))

    def setGrey(self):
        if not self.isGrey:
            img = grey(self.data)
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
            self.isGrey = True
        else:
            self.data = copy.deepcopy(self.ori_data)
            self.data = self.resizeImage()
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
            self.isGrey = False

    def resizeImage(self):
        # decide text
        temp = cv2.cvtColor(self.data[0], cv2.COLOR_BGR2RGB)

        height, width , gar = self.data[0].shape

        # resize image
        temp_data = copy.deepcopy(self.data)
        img = size(temp_data, ((self.ui.heightlevel.value() / height) * 100), ((self.ui.widthlevel.value() / width) * 100))
        return img
        # self.ui.showvideo.setScene(self.showImage(img[0]))

    def loadEvent(self):
        self.isGrey = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.readImageFromPath(fileName)
            if len(self.data) == 1:
                self.ui.showvideo.setScene(self.showImage(self.data[0]))
            else:
                print("Video")

    def readImageFromPath(self, path):
        if path.split("/")[0] == "C:":
            if path.split("/")[-1].split('.')[1] == 'mp4':
                self.data, self.fps = get_video(os.path.relpath(path))
            else:
                self.data = get_image(os.path.relpath(path))
        else:
            self.data = get_image(path)
        self.ori_data = copy.deepcopy(self.data)
    def showImage(self, send_img):
        img = send_img
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
