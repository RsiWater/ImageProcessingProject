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

        self.initFilterBox()

        self.ui.showvideo.setScene(self.showImage(self.data[0]))
        self.ui.label_3.setText("Origin: "+ str(self.ori_data[0].shape[1]) + "x" +str(self.ori_data[0].shape[0]))
        self.ui.actionNew.triggered.connect(self.loadEvent)
        self.ui.loadfilebutton.clicked.connect(self.loadEvent)
        self.ui.greylevelbutton.clicked.connect(self.setGrey)
        self.ui.redLevel.sliderReleased.connect(self.setRLabel)
        self.ui.greenLevel.sliderReleased.connect(self.setGLabel)
        self.ui.blueLevel.sliderReleased.connect(self.setBLabel)
        self.ui.redLabel.valueChanged.connect(self.setRLevel)
        self.ui.greenLabel.valueChanged.connect(self.setGLevel)
        self.ui.blueLabel.valueChanged.connect(self.setBLevel)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.savebutton.clicked.connect(self.save)
        # self.ui.filterBox.currentIndexChanged.connect(self.modifyFilter)
        self.ui.Applybutton.clicked.connect(self.apply)


    def debug(self):
        print("Starburststream")
        print(self.ui.savebutton.setVisible(False))

    def initFilterBox(self):
        if True: # Image
            self.ui.filterBox.addItem("自訂義")
            self.ui.filterBox.addItem("鄉愁黃")
            self.ui.filterBox.addItem("共產紅")
            self.ui.filterBox.addItem("星爆藍")
            self.ui.filterBox.addItem("魅力紫")
            self.ui.filterBox.addItem("出軌綠")
            self.ui.filterBox.addItem("邊緣提取")
            self.ui.filterBox.addItem("邊緣增強")
            self.ui.filterBox.addItem("邊緣再增強")
            self.ui.filterBox.addItem("浮雕風")
        else: # Video
            pass

    def setRLabel(self):
        self.ui.redLabel.setValue(self.ui.redLevel.value() / 100)
    def setGLabel(self):
        self.ui.greenLabel.setValue(self.ui.greenLevel.value() / 100)
    def setBLabel(self):
        self.ui.blueLabel.setValue(self.ui.blueLevel.value() / 100)

    def setRLevel(self):
        self.ui.redLevel.setValue(int(self.ui.redLabel.value() * 100))
    def setGLevel(self):
        self.ui.greenLevel.setValue(int(self.ui.greenLabel.value() * 100))
    def setBLevel(self):
        self.ui.blueLevel.setValue(int(self.ui.blueLabel.value() * 100))

    def reset(self):
        self.data = copy.deepcopy(self.ori_data)
        self.ui.showvideo.setScene(self.showImage(self.ori_data[0]))

    def save(self):
        if True: # Image
            write_image("New.jpg", self.data)
        else:
            pass

    def apply(self):
        self.data = copy.deepcopy(self.ori_data)
        if self.ui.filterBox.currentText() == "自訂義":
            self.data = self.modifyColor()
        else:
            self.data = self.modifyFilter()
        self.data = self.resizeImage()
        self.ui.showvideo.setScene(self.showImage(self.data[0]))

    def modifyFilter(self):
        filterType = self.ui.filterBox.currentText()
        temp_data = copy.deepcopy(self.data)
        if filterType == "鄉愁黃":
            temp_data = color(temp_data, 0.005, 0.499, 0.888)
        elif filterType == "共產紅":
            temp_data = color(temp_data, 0.114, 0.114, 0.887)
        elif filterType == "星爆藍":
            temp_data = color(temp_data, 0.587, 0.299, 0.114)
        elif filterType == "魅力紫":
            temp_data = color(temp_data, 0.299, 0.114, 0.587)
        elif filterType == "出軌綠":
            temp_data = color(temp_data, 0.114, 0.587, 0.229)
        elif filterType == "邊緣提取":
            temp_data = findEdge(temp_data)
        elif filterType == "邊緣增強":
            temp_data = edgeEnhance(temp_data)
        elif filterType == "邊緣再增強":
            temp_data = edgeEnMore(temp_data)
        elif filterType == "浮雕風":
            temp_data = emboss(temp_data)

        return temp_data

    def setGrey(self):
        if not self.isGrey:
            img = grey(self.data)
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
            self.ui.greylevelbutton.setText("Grey Off")
            self.isGrey = True
        else:
            self.data = copy.deepcopy(self.ori_data)
            self.data = self.resizeImage()
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
            self.ui.greylevelbutton.setText("Grey On")
            self.isGrey = False

    def resizeImage(self):
        # temp = cv2.cvtColor(self.data[0], cv2.COLOR_BGR2RGB)

        height, width , gar = self.data[0].shape

        # resize image
        temp_data = copy.deepcopy(self.data)
        img = size(temp_data, ((self.ui.heightlevel.value() / height) * 100), ((self.ui.widthlevel.value() / width) * 100))
        return img

    def modifyColor(self):
        temp_data = copy.deepcopy(self.data)
        
        R_Value = self.ui.redLevel.value() / 100
        G_Value = self.ui.greenLevel.value() / 100
        B_Value = self.ui.blueLevel.value() / 100


        temp_data = color(temp_data, B_Value, G_Value, R_Value)
        return temp_data

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
